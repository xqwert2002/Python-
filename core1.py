def list(n1,n2):
    print(n1*n2)
    return n1*n2

def cal(n1,n2,op):
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