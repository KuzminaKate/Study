#-----2 ЗАДАЧА-----

import calendar
import time     # ДЛЯ ПРОВЕРКИ Y И M
f=True
while (f==True):
    y=input("Введите год: ")
    m=input("Введите месяц: ")
    try:
        y1=time.strptime(y,'%Y')
        m2=time.strptime(m,'%m')
        c=calendar.TextCalendar(calendar.SUNDAY)
        a=c.formatmonth(int(y), int(m))
        print(a)
    except ValueError:
        print("Неверный формат ввода (ГГГГ-год, ММ-месяц)!")
        t=input("Ввести дату ещё раз? \n 'yes'-ввести дату, любые другие символы выход из программы: ")
        if t=="yes":
            y = input("Введите год: ")
            m = input("Введите месяц: ")
            try:
                y1 = time.strptime(y, '%Y')
                m2 = time.strptime(m, '%m')
                c = calendar.TextCalendar(calendar.SUNDAY)
                a = c.formatmonth(int(y), int(m))
                print(a)
            except ValueError:
                print("Неверный формат ввода (ГГГГ-год, ММ-месяц)!")
        else:
            break
    t = input("Ввести дату ещё раз? \n 'yes'-ввести дату, любые другие символы выход из программы: ")
    if t!="yes":
        break