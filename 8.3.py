import sys
import os
for i in range(1,len(sys.argv),2):
    os.chdir(sys.argv[i])
    F = open(sys.argv[i+1])
    F = F.read()
    print(F)