### 因數查詢

import pyinputplus as pypi

def get_factor(n:int)->None:
    print(f"{n}的因數: ",end='')
    for i in range(1,n+1):
        u:int = n%i
        if u==0:
            print(i ,end=' ')

    print()


mun:int = pypi.inputInt("請輸入查詢數值: ",min=1)
print(mun)
get_factor(mun)
print("程式結束")