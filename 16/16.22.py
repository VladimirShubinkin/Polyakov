'''
def F( n ):
  print('*')
  if n >= 1:
    print('*')
    F(n-1)
    F(n-2)
    print('*')
F(35)
'''

def F(n):
    global count
    count += 1
    if n >= 1:
        count += 1
        F(n - 1)
        F(n - 2)
        count += 1


count = 0
F(35)
print(count)
