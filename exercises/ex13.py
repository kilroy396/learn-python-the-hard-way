from sys import argv
# read the WYSS section for how to run this

# if argv list length != 4 then
#    error message - argv[0] requires ....
# else
#    <test inputs>
#    <program>

#print("argument count:", len(argv))
if len(argv) != 4:
    print(f"{argv[0]} requires 3 paramenteres")
else:
    #script, first, second, third, fourth = argv
    script, first, second, third = argv
    #script, first  = argv

    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your thid variable is:", third)

print("Goodbye")