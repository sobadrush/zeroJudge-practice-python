n = int(input("請輸入團體中人數 n :"))
friends = list(map(int, input().split()))
visited = set()
groupNumber = 0

for i in range(n):
    if i not in visited:
        groupNumber += 1 # 小團體 +1
        cur = i
        while cur not in visited: # 檢查直到 cur 走訪的值已存在 visited 中，即代表已完成朋友圈
            visited.add(cur)
            cur = friends[cur]

print(f"小團體數：{groupNumber}")


# 0 1 2 3 4 5 6 7 8 9
# 4 7 2 9 6 0 8 1 5 3