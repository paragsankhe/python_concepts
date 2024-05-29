mystring = "abcd@#$%123ff33w##$$ff"
newstr = ""
for i in mystring:
    if i.isalpha():
        newstr = newstr + i
print(newstr)