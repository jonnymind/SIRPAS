#!/usr/bin/env python3

# Script pre-processing markdown
# Known commands:
# $(-- --) -- Comment
# $(include xxx)  -- Include verbatim target document
# $(dd xxx)  -- Create data dictionary
# $(dt xxx)  -- Create data table

import re
import glob
import argparse
import sys
import os
import json

RE_COMMAND = re.compile("(.*)(?!\\\\)\\$\\((.*?)\\s+(.*?)\\)(.*)")

def message(what):
	pass
	#print(what)

class Processor:
	def __init__(self, fout):
		message(f"Creating processor to {fout}")
		self.basepath = None
		self.fout = fout
		self.fin = None
		self.line = 0
		self.current = None
		self.current_stack = []
		self.line_stack = []

	def process_comment(self, line):
		pos = line.find("--)")
		while pos < 0:
			line = self.fin.readline()
			self.line += 1
			if not line:
				return
			pos = line.find("--)")
		if pos >= 0:
			self.fout.write(line[pos+3:])

	def process_command(self, cmd, params):
		if cmd == "include":
			origin = os.path.abspath(os.path.dirname(self.current))
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
			cmt = line.find("$(--")
			if cmt >= 0:
				self.fout.write(line[0:cmt])
				self.process_comment(line[cmt:])
				continue

			# Process commands
			rcmd = RE_COMMAND.match(line)
			if rcmd:
				pre, cmd, params, post = rcmd.group(1), rcmd.group(2), rcmd.group(3), rcmd.group(4)
				self.fout.write(pre)
				self.process_command(cmd, params)
				self.fout.write(post)
			else:
				self.fout.write(line)
		self.fout.write("\n")
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
				self.fout.write("|")
				for word in line:
					self.fout.write("-" * (len(str(word))+2) +"|")
				self.fout.write("\n")
			self.fout.write( "| " + " | ".join(map(lambda x:str(x), line)) + " |\n")

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
					self.fout.write(line)
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

	def print_error(self, message):
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
	proc = Processor(fout)
	proc.process(fin)
