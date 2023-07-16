#!/usr/bin/env python3

# Script pre-processing markdown
# Known commands:
# @(-- --) -- Comment
# @(include xxx)  -- Include verbatim target document
# @(dd xxx)  -- Create data dictionary
# @(dt xxx)  -- Create data table
# @(var ABC value) / @( ... $ABC ... ) -- macro substitutes variables

import re
import glob
import argparse
import sys
import os
import json
import io
from typing import IO

RE_COMMAND = re.compile("(.*)(?!\\\\)[$@]\\((.*?)(\\s+(.*?))?\\)(.*)")
RE_COMMENT = re.compile("[@$]\\(--")
RE_VARIABLE = re.compile("[$]([a-zA-Z0-9._-]+)")

def message(what):
	pass
	#print(what)


class Entry:
	def __init__(self, type:str, title:str):
		self.buffer = io.StringIO()
		self.type = type
		self.title = title
		self.reference = self.make_reference(title)
		self.break_line = False
		
	def make_reference(self, title: str) -> str:	
		return title.strip().lower().replace(" ","-").replace("--","-")
	
	def write(self, data:str):
		# Filter out blanks
		data = data.strip(" ")
		
		# Skip multiple newlines and newlines on top of items.
		if data == "\n": 
			self.break_line = True
			return
		elif data == "":
			return
		
		if self.break_line:
			self.break_line = False
			self.buffer.write("\n")

		self.buffer.write(data)

	def dump(self, fout:IO[str]) -> bool:
		data = self.buffer.getvalue()
		fout.write(data)
		return data.endswith("\n\n")
		
	def size(self):
		return self.buffer.tell()
	
	def is_empty_text(self):
		return self.type == "text" and self.size() == 0

	def is_inline(self):
		return self.type in ["placeholder"]

class Processor:
	def __init__(self):
		message(f"Creating processor to {fout}")
		self.basepath = None
		self.fin = None
		self.line = 0
		self.current = None
		self.current_stack = []
		self.line_stack = []
		self.variables = {}
		self.pending_entries_by_type = {}
		self.pending_entries = {}
		self.entries = []
		self.reference_entries = {}
		self.current_entry = None
		self.create_entry("placeholder", "@Start")

	def create_entry(self, type_of_entry: str, title: str) -> Entry:
		new_entry = Entry(type_of_entry, title)
		self.add_entry(new_entry)
		return new_entry
	
	def add_entry(self, new_entry: Entry) -> None:
		self.append_entry(new_entry)
		self.reference_entries[new_entry.reference] = new_entry
		self.current_entry = new_entry
		self.on_new_entry(new_entry)

	def append_entry(self, new_entry: Entry) -> None:
		# remove empty text entries
		if self.entries and self.entries[-1].is_empty_text():
			del self.entries[-1]
		self.entries.append(new_entry)

	def on_new_entry(self, entry: Entry):
		lambda_action = self.pending_entries_by_type.pop(entry.type, None)
		if lambda_action:
			self.pending_entries.pop(entry.reference, None)
			lambda_action[1](entry)
		lambda_action = self.pending_entries.pop(entry.reference, None)
		if lambda_action:
			lambda_action[1](entry)
		

	def process_titles(self, title:str):
		for type_of_entry, prefix in [
				("chapter", "# "), 
				("para", "## "),
				("sub", "### ")]:

			if title.startswith(prefix):
				title = title[len(prefix):].strip()
				new_entry = self.create_entry(type_of_entry, title)

	def process_comment(self, line):
		pos = line.find("--)")
		while pos < 0:
			line = self.fin.readline()
			self.line += 1
			if not line:
				return
			pos = line.find("--)")
		if pos >= 0:
			self.current_entry.write(line[pos+3:])

	def is_line_command(self, cmd:str):
		return cmd in ['include', 'dd', 'dt']
	
	def store_variable(self, vardef:str):
		varname = vardef.split(' ')[0]
		varvalue = vardef[len(varname)+1:].strip()
		message(f"Defining {varname} = {varvalue}")
		self.variables[varname] = varvalue
		
	def expand_variable(self, varname:str): 
		if varname not in self.variables:
			self.print_error("Unknown variable '{varname}'")
			return "UNKNOWN_VARIABLE"
		else:
			return self.variables[varname]
		
	def expand_variables(self, params:str):
		match = RE_VARIABLE.search(params)
		while match:
			message(f"Found variable {match.group(1)}")
			params = params[0:match.start] + self.expand_variable(match.group(1)) + params[match.end:]
		return params

	def process_command(self, cmd:str, params: str):
		if params:
			params = self.expand_variables(params)
		
		if cmd == "include":
			origin = os.path.abspath(os.path.dirname(self.current))
			params = params.strip()
			try:
				tgt = (self.basepath + params) if params.startswith("/")\
											 else os.path.join(origin, params)
				self.process(tgt)
			except IOError as error:
				self.print_error("Failed include {} - {}".format(
								tgt, error))
		elif cmd == "dd":
			self.process_dd(params)
		elif cmd == "dt":
			self.process_dt(params)
		elif cmd == "var":
			self.store_variable(params)
		elif cmd == "next":
			self.process_next(params)
		elif cmd.startswith("$"):
			self.current_entry.write(self.expand_variable(cmd[1:]))
		else:
			self.print_error("Unknown command: {}".format(cmd))

	def process(self, src):
		flist = glob.glob(src)
		if not flist:
			self.print_error("Invalid path {}".format(src))
			return
		flist.sort()
		if len(flist) > 1:
			for fin2 in flist:
				self.process(fin2)
				return
		elif len(flist) == 0:
			return
		src = flist[0]
		if os.path.isdir(src):
			src = src + "/main.md"
		with open(src, "r") as fin:
			self.process_file(src, fin)

	def process_file(self, src, fin):
		message(f"Processing file {src}")
		self.push_current(src)
		self.fin = fin
		self.line = 0
		for line in fin:
			self.line += 1

			# strip comments
			cmt = RE_COMMENT.search(line)
			if cmt:
				self.current_entry.write(line[0:cmt.start(0)])
				self.process_comment(line[cmt.start(0):])
				continue
			
			# proecess titles
			if line.startswith("#"):
				self.process_titles(line)
				# don't break, there could still be a command.
			
			# Process commands
			rcmd = RE_COMMAND.match(line)
			if rcmd:
				pre, cmd, params, post = rcmd.group(1), rcmd.group(2), rcmd.group(4), rcmd.group(5)
				# Avoid stray characters if we're doing a line commaand.
				if self.is_line_command(cmd):
					pre = post = ""
				self.current_entry.write(pre)
				self.process_command(cmd, params)
				self.current_entry.write(post+"\n")
			else:
				self.current_entry.write(line)
		self.current_entry.write("\n")
		self.pop_current()

	def pop_current(self):
		if len(self.current_stack):
			self.current = self.current_stack.pop()
			self.line = self.line_stack.pop()

	def push_current(self, current_file):
		if not self.basepath:
			self.basepath = os.path.abspath(os.path.dirname(current_file))
			message(f"Base directory f{self.basepath}")
		self.current_stack.append(self.current)
		self.line_stack.append(self.line)
		self.current = current_file

	def process_dt(self, params):
		table = self.get_json()
		self.write_table(table)

	def write_table(self, table, hidden_fields=False):
		if not table:
			return
		header = 0
		for line in table:
			if line[0] and line[0][0] == '*':
				if not hidden_fields:
					continue
				line[0] = line[0][1:]
			header += 1
			# skip creating a header separator if provided
			if header == 2 and "--" not in line[0]:
				self.current_entry.write("|")
				for word in line:
					self.current_entry.write("-" * (len(str(word))+2) +"|")
				self.current_entry.write("\n")
			self.current_entry.write( "| " + " | ".join(map(lambda x:str(x), line)) + " |\n")

	def process_dd(self, params):
		ddict = self.get_json()
		if ddict is None:
			self.print_error("Invalid DD entry: {}".format(self.get_json()))
			return
		table = [[" ", " "]]
		for key in sorted(ddict):
			table.append([key[4:], ddict[key]])
		self.write_table(table)

	def get_json(self):
		opener, closer, level = None, None, 0
		content = ""
		linecount = 0
		for line in self.fin:
			if not opener:
				if not line.strip():
					return None
				opener = line.strip()[0]
				if opener == '[':
					closer = ']'
				elif opener == '{':
					closer = '}'
				else:
					self.current_entry.write(line)
					return None

			level += line.count(opener) - line.count(closer)
			content += line if opener == "[" else \
						  line.replace('"', '"{0:03d}.'.format(linecount), 1)
			linecount += 1
			if level <= 0:
				self.line += linecount
				try:
					return json.loads(content)
				except json.decoder.JSONDecodeError as error:
					self.print_error(error)
					return None
	
	def process_next(self, waiting_for:str):
		pending_entry = Entry("placeholder", f"Next {waiting_for}")
		self.append_entry(pending_entry)
		self.create_entry("text", "")
		self.pending_entries_by_type[waiting_for] = (pending_entry, 
			lambda ref_entry: self.apply_next(ref_entry, pending_entry))
		
	def apply_next(self, ref_entry:Entry, target_entry:Entry):
		target_entry.write(ref_entry.reference)

	def commit(self, output: IO[str]):
		self.check_undefined()
		previous_inline = True
		for entry in self.entries:
			if not previous_inline and not entry.is_inline():
				output.write("\n")
			well_terminated = entry.dump(output)
			previous_inline = well_terminated or entry.is_inline()

	def check_undefined(self):
		for entry, func in list(self.pending_entries.values()) \
					+ list(self.pending_entries_by_type.values()):
			self.print_error(f"Undefined entry {entry.title}")
			entry.write(f"NOT FOUND {entry.reference}")


	def print_error(self, message:str):
		sys.stderr.write("ERROR: {}({}): {}\n".format(
							  self.current, self.line, message))



################################################################
# Main
################################################################

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('sources', metavar="SOURCE", action='append')
arg_parser.add_argument('-o', dest="output", metavar="FILE", help="Output here")
opts = arg_parser.parse_args()

if opts.output:
	fout = open(opts.output, "w")
else:
	fout = sys.stdout

for fin in opts.sources:
	proc = Processor()
	proc.process(fin)
	proc.commit(fout)
