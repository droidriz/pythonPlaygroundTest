n = int(input())
order=[]
s=[]
t=n
while(t > 0):
    ordr = int(input())-1
    if ordr>=n:
        print("Enter Less than given size")
    order.append(ordr)
    t = t-1

t=n
while(t > 0):
    s.append(input())
    t = t-1

lst = [None] * n

for i,j in zip(order,s):
    if i==s.index(j):
        lst[i]=j
    elif i+1 == len(j):
        lst[i]=j.upper()
    else:
        lst[i]=j.lower()
        
print(lst)
