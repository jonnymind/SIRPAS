#!/usr/bin/env python3

# Script pre-processing markdown
# Known commands:
# $(-- --) -- Comment
# $(include xxx)  -- Include verbatim target document

import re
import glob
import argparse
import sys
import os

RE_COMMAND = re.compile("(.*)(?!\\\\)\\$\\((.*?)\\s+(.*?)\\)(.*)")

def print_error(message):
	sys.stderr.write(message+"\n")

def process_comment(fin, fout, line):
	pos = line.find("--)")
	while pos < 0:
		line = fin.readline()
		if not line:
			return
		pos = line.find("--)")
	if pos >= 0:
		fout.write(line[pos+3:])
		
def process_command(basepath, cmd, params, origin, fout):
	if cmd == "include":
		try:
			tgt = basepath+params if params.startswith("/") else os.path.join(origin, params)
			process(basepath, fout, tgt)
		except IOError as error:
			print_error("Include command: ERROR OPENING {}\n:{}".format(tgt, error))
	else:
		print_error("Unknown command: {}".format(cmd))

def process(basepath, fout, src):
	origin = os.path.abspath(os.path.dirname(src))
	flist = glob.glob(src)
	if not flist:
		print_error("CANNOT FIND {}".format(src))
		return
	flist.sort()
	if len(flist) > 1:
		for fin2 in flist:
		   process(basepath, fout, fin2)
		return
	elif len(flist) == 0:
		return
	src = flist[0]
	
	with open(src, "r") as fin:
		for line in fin:
			# strip comments			
			cmt = line.find("$(--")
			if cmt >= 0:
				fout.write(line[0:cmt])
				process_comment(fin,fout,line[cmt:])
				continue
			
			# Process commands
			rcmd = RE_COMMAND.match(line)
			if rcmd:
				pre, cmd, params, post = rcmd.group(1), rcmd.group(2), rcmd.group(3), rcmd.group(4)
				fout.write(pre)
				process_command(basepath, cmd, params, origin, fout)
				fout.write(post)
			else:
				fout.write(line)
		fout.write("\n")


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
	base = os.path.abspath(os.path.dirname(fin))
	process(base, fout, fin)
		
	
