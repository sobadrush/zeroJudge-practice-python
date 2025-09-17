import math, sys


nn = int(input("請輸入會會經過幾個巴士站？"))

all_coord_x = []
all_coord_y = []
for i in range(nn):
  xx, yy = map(int, input("輸入巴士站座標：").strip().split())
  all_coord_x.append(xx)
  all_coord_y.append(yy)

print(all_coord_x)
print(all_coord_y)

max_distance = 0
min_distance = sys.maxsize # 先設為系統最大值
for i in range(1, nn): # 從1開始
  distance = abs(all_coord_x[i] - all_coord_x[i-1]) \
            + abs(all_coord_y[i] - all_coord_y[i-1]) # 計算曼哈頓距離
  if distance > max_distance:
    max_distance = distance
  if distance < min_distance:
    min_distance = distance
    
print(f"最大值/最小值： {max_distance} {min_distance}")