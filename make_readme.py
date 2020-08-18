#!/usr/bin/python3

def write_header(line):
    sl = line.split(">")
    s0 = sl[1]
    h = s0.split("<")
    header = h[0]
    header = "# " + header + "\n"
    return header

def get_desc(line):
    remove = ["<p>", "</p>", "\n"]
    replace = ["<code>", "</code>"]
    new = line

    for string in remove:
        new = new.replace(string, '')
    for string in replace:
        new = new.replace(string, "```")
    return(new)

files = []
descs = []
dc = 0

with open("webpage.txt") as wp:
    for line in wp:
        if "<h1" in line:
            header = write_header(line)
        elif "Task Body" in line:
            next_line = wp.readline()
            description = get_desc(next_line)
            descs.append(description)
        elif "File:" in line:
            file_name = line[24:-13]
            files.append(file_name)

readme = open('NEW_README.md', 'w')



readme.write(header + "\n")
readme.write("This is a repository containing assignments for Holberton School.\n\n")
readme.write("|FILES| DESCRIPTIONS|\n")
readme.write("|---|---|\n")

for f in files:
    string = "|{}|{}|\n".format(f, descs[dc])
    readme.write(string)
    dc += 1
readme.write("\n")
readme.close()