# 1-1.把九九乘法表包裝成函式，可做n1*n2乘法
import core1 as c1
c1.list(5,9)

import lib.core2 as c2
c2.list(6,6)

# 1-2.把四則運算包裝成函式
# 1-3.將以上函式包裝在你自己的模組和封包中，並在主程式成功使用
import core1 as c1
c1.cal(4,5,"*")

import lib.core2 as c2
c2.cal(10,5,"/")


# 2.使用系統內建的模組random產生1~100的函數(可以參照官網random的解釋文件)
import random
print(random.randint(1,100))