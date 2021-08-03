s = input()
s=s.lower()
p = ""
for x in s:
  if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='y'):
    pass
  else:
    p = p + "." + x
print(p)