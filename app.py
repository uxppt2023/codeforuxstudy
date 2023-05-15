def do_something(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(do_something([1,2,3,3,3,3,4,5])) 
print ("Hello World")
