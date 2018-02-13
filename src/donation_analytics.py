import sys

# read itcont.txt
file = open('/Users/vickie/Downloads/indiv16/itcont.txt', 'r')
file.close
lines = []
lines = file.readlines()

print(len(lines))