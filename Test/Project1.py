import random
a=1
b=100
c=[]
for i in range(b):
    r=random.randint(a,b)
    c.append(r)
print("Получившийся массив: ", c)
d=max(c)
print("Максимальное число в масиве: ", d)
#m=min(c)
#print("Минимальное число в масиве: ", m)