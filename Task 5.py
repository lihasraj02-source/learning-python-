import os


fh="samplefile.txt"
if os.path.exists(fh):
    c=open(fh,'rt')
    content=c.read()
    print(content)

else:
    print("this file does not exist. ")

