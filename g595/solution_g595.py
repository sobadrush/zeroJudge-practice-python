n = int(input("輸入圍籬數量："))

rods = list(map(int, input("輸入圍籬高度: ").split()))

print(f"rods = {rods}")

sum_of_fixed_rod = 0
for i in range(n):
  if i == 0 and rods[i] == 0: # 左側
    sum_of_fixed_rod += rods[i + 1]
    continue
  if i == (n - 1) and rods[i] == 0: # 右側
    sum_of_fixed_rod += rods[i - 1]
    continue
  if rods[i] == 0:
    sum_of_fixed_rod += min(rods[i - 1], rods[i + 1])

print(f"sum_of_fixed_rod = {sum_of_fixed_rod}")