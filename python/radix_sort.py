# 基數排序法
"""
基數排序法 (Radix Sort)屬於 非比較性 的演算法，
是利用資料裡的值的某些特性來作為排序的依據，而非是用比較的方式。

一樣有份資料要做排序：
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

在排序前，有兩種排序方式可以參考。
MSD(Most Significant Digit)    從最低有效鍵值開始排序（最小位數排到大）
LSD(Least Significant Digit)   從最高有效鍵值開始排序（最大位數排到小）

以LSD為例:
(1) 先分個位數
    0   1   2   3   4   5   6   7   8   9
  100      92  23  34  55  66  67  78  89
               23          96      78  29
                           96      88  79

  data = [100, 92, 23, 23, 34 55, 66, 96, 96, 67, 78, 78, 88, 89, 29, 79]

(2) 再分十位數
    0   1   2   3   4   5   6   7   8   9   
   100      23  34      55  66  78  88  92
            23              67  78  89  96
            29                  79      96
    
  data = [100, 23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96]

(3) 再分百位數 (沒有就補0)
    0   1   2   3   4   5   6   7   8   9   
    023 100
    023
    029
    034
    ...
   data = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

... 以此類推

如果位數更多的話，就要重複做以上動作到最高位。
LSD 是從鍵值的最邊開始，所以適合位數小的資料來做排序。
MSD 則相反，從最左邊，也就是最高位數來開始排序。
如果位數很多的話，其實 MSD 會來得更有效率一些。

程式時間複雜度：Ｏ(kN)，k 取決於位元的位數
"""

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

# Radix sort
def radix_sort(data):
    length = len(data)
    count = max(data) # 資料裡最大的數值

    # 用最大數來判斷最大位數
    digit = 1
    while count > 9:
        count /= 10
        digit += 1

    tmp = []
    cur = 0
    for i in range(length):    # 資料的大小會決定桶子的數量，會是一個二維陣列
        tmp.append([0] * length)
    order = [0] * length       # 游標行，用來將資料放到同一位數但不同列的桶子

    if digit <= 9:
        '''use LSD(Least significant digit) method '''
        exp = 1 
        while exp <= max(data):
            for i in range(length):
                lsd = int(data[i]/exp) % 10  # 將資料用10來取個位數的餘數
                tmp[lsd][order[lsd]] = data[i]
                order[lsd] += 1
            for i in range(length):
                # 如果這個位數的桶子在此行有資料，就丟到同一個位數，但下一列的位置
                if order[i] != 0:
                    for j in range(order[i]):
                        data[cur] = tmp[i][j]
                        cur += 1
                # 將游標行的資料歸零
                order[i] = 0
            exp *= 10
            cur = 0
        print(data)
        
radix_sort(data)