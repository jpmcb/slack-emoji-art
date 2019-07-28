import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 script.py my-file-name.txt")

data = ''
by_grayskull = ''

with open(sys.argv[1], 'r') as file:
    data = file.read()

for char in data:
    if char == '\n':
        by_grayskull+='\n'
    elif char == '#':
        by_grayskull+=':he-man:'
    else:
        by_grayskull+=':curseyouheman:'

print(by_grayskull)
