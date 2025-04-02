mystring  = "abc def ghi"

mystrlist = mystring.split()
revmylist  = mystrlist[::-1]
print(revmylist)
newstr = ""
for i in revmylist:
    newstr  = newstr+" "+i[::-1]
print(newstr)