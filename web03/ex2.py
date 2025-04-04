import sys

print("my name is {}".format(sys.argv[0]))
if len(sys.argv) > 1:
    print("first arg is: '{}' and last arg is '{}'".format(
        sys.argv[1], sys.argv[-1]))
else:
    print("No arguments")