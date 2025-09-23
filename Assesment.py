s="XYZz"

rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]

chars=[]
for c in rev:
    chars.append(c)

for i in range(len(chars)):
    c=chars[i]
    code=ord(c)
    if 65<=code<=90:
        if code==90:
            chars[i]="A"
        else:
            chars[i]=chr(code+1)

    elif 97 <=code <=122:
        if code ==122:
            chars[i]='a'
        else:
            chars[i]=chr(code+1)
    else:
        chars[i]=chr(code+1)

result=""
for ch in chars:
    result=result+ch
print(result)
