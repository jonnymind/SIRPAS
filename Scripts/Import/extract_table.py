
def write_table(fin, fout):
	for line in fin:
		if line.strip():
			fout.write(line.replace("**", ""))
		else:
			fout.write(line)
			return

count = 0
with open("sirpas.md", "r") as fin:
	for line in fin:
		if "--+--" in line:
			count += 1
			with open("tables/table{:03}.md".format(count), "w") as fout:
				fout.write(line)
				write_table(fin, fout)
				