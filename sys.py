import sys
try:
 print("my name is = " , sys.argv[1]) 
except IndexError:
 print ("too few argument")
else:
 print("too many argument")