from sys import argv, exit

if len(argv) != 2:
    print("Missing commandline argument")
    exit(1)
else:
    print(f"Hello, {argv[1]}")
    exit(0)

