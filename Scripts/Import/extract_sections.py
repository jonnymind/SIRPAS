import os
import re

RE_TITLE = re.compile("^\\s*(#+)\\s*([^#]*?)\\s*#*$")
level = 0
paths = ['doc']
current_out = open("docs", "w")
with open("sirpas-direct.md", "r") as fin:
	for line in fin:
		match = RE_TITLE.match(line)
		if match:
			depth = len(match.group(1))
			title = match.group(2)
			filename = title
			valid_end = filename.find('(')
			if valid_end > 0:
				filename = filename[0:valid_end].strip()
			filename = filename.replace(" ", "_")
			filename = filename.replace("/", "_")
			
			if len(paths) > depth:
				paths = paths[0:depth]
			else:
				while len(paths) < depth:
					paths.append('structure')

			current_out.close()
			path = "/".join(paths)
			os.makedirs(path, exist_ok=True)
			paths.append(filename)
			current_out = open("/".join(paths) + ".md", "w")
			current_out.write(match.group(1) + " " + title + "\n")
		else:
			current_out.write(line)
	
current_out.close()