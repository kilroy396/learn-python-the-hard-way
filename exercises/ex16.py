from sys import argv

# files have a few methods:
#   close - closes the files
#   read - reads the contents of the files
#   readline - reads just one line of a text files
#   truncate - empties the file
#   write('stuff') - writes "stuff" to the file
#   seek(0) - Move the read/write location to the beginning of the file

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do what that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# opening the file for writing by default truncates the file
# making the following steps redundant

# print("Truncating the file.  Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()