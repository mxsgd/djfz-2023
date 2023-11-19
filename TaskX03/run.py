import sys

for line in sys.stdin:
    print(str(len(line)-1) + ' ' + line, end='')
