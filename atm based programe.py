amount = int (input("enter amount")) -100

tk = amount // 2000
amount = amount - tk * 2000

fh  = amount // 500
amount = amount - fh * 500

oh = amount // 100

print (" 100 notes ",oh+1)
print (" 500 notes",fh)
print (" 2000 notes",tk)
