#作業一：請使用者輸入兩個數字，再請使用者輸入運算符號
print("【作業一】")
n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
op=input("請輸入運算:+,-,*,/")
if op=="*":
    print(n1*n2)
elif op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)

elif op=="/":
    print(n1/n2)
else:
    print("輸入錯誤")

#作業二 使用者輸入一個正整數，告訴他開平方的結果
print("【作業二】")
x=int(input("輸入一個正整數"))
n=1
while n*n<=x:
    n+=1
    if n*n<x:
        continue
    elif n*n==x:
        print(n)
        break
    else:
        print("無整數平方根")

#作業三 印出99乘法表 ex.1*1=1，1*2=2......
print("【作業三】")
n=1
while n<=9:
    for x in range(1,10):
        print(n,"*",x,"=",n*x)
    n+=1
