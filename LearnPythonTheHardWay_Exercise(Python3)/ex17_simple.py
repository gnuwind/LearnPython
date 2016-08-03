from sys import argv

# This is a simplified edition of ex17.py
open(argv[2], "w").write(open(argv[1]).read())

