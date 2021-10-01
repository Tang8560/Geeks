# 桶子演算法
"""
桶子排序法 (Bucket Sort) 想法很簡單，其實就是準備幾個桶子，將要排序的資料分類丟至指定的桶子中，
再依序將桶子裡的東西取出。有點類似資源回收的概念啦～

O(M + N)
"""
# 題目: 將資料 (分數) 由小到達排序
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

# 結果: data = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

def bucket_sort(data):
    # 1. 生成桶子
    # Suppose max score = 100
    max_score = 100
    bucket = []
    for i in range(max_score + 1):
        bucket.append(0)

    # 2. 依序將資料放入桶子
    for j in data:
        bucket[j] = bucket[j] + 1
    print(bucket)

    # 讀取桶子的資料
    index = 0
    for k in range(len(bucket)):
        if bucket[k] != 0:
            for _ in range(bucket[k]):
                data[index] = k
                index += 1
    print(data)
bucket_sort(data)

