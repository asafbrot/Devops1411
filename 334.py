my_file = open("read_my_contents.txt")

for line in my_file.readlines():
    print(line, end='')

my_other_file = open("moshe.txt", "w")
my_other_file.write("hey hey\n")

# "w" - defines file as "Write" - means he create the file as blank and put whatever you want in it
# - if not mentioned - default is read



