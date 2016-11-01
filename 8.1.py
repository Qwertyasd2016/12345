import sys
for i in range(1, len(sys.argv)):
    if len(str(sys.argv[i])) % 3 == 0:
        print(sys.argv[i])

