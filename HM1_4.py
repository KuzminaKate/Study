#-----4 ЗАДАЧА-----

import random       # задание ф-и 
c=random.randint(1, 6)   # первая игральная кость
d=random.randint(1, 6)   # вторя игральная кость
print("Первая кость: ",c)
print("Вторая кость: ",d)
x=c+d
print("Сумма: ",x)
if x== 7 or x==11:
    print("Вы победили!")
    p1=6/36
    p2=2/36
    print("Вероятность:",round(p1+p2,2))
else:
    if x==2 or x==3 or x==12:
        print("Вы проиграли!")
    else:
        while True:
            c = random.randint(1, 6)
            d = random.randint(1, 6)
            print("Первая кость: ",c)
            print("Вторая кость: ",d)
            x = c + d
            print("Сумма: ",x)
            if x== 7:
                print("Вы победили!")
                p1 = 6 / 36
                print("Вероятность:", round(p1,2))
                break
            if x==4 or x==5 or x==6 or x==8 or x==9 or x==12:
                print("Вы проиграли!")
                break