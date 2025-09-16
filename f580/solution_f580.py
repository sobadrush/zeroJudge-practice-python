m, n = map(int, input("請輸入 m (骰子個數), n(操作次數): ").split())
print(f"m = {m}, n = {n}")

handles = []
for t in range(n):
  perHandle = tuple(map(int, input("輸入 a (第幾顆骰子) , b (操作方式): ").split()))
  handles.append(perHandle)

print(f"handles = {handles}")

dices = [ [4, 1, 2] for ii in range(m) ] # m: 骰子個數
print(f"dices = {dices}")

for hd in handles:
  target_dice = hd[0] - 1 # 陣列 index 從 0 開始，故多減1
  target_handle = hd[1]
  if target_handle == -1: # 向前轉
    tmp_dice = dices[target_dice]
    dices[target_dice] = [ tmp_dice[1], 7 - tmp_dice[0], tmp_dice[2] ]
  elif target_handle == -2: # 向右轉
    dices[target_dice] = [ tmp_dice[0], 7 - tmp_dice[2], tmp_dice[1] ]
  else:
    target_handle_idx = target_handle - 1 # 陣列 index 從 0 開始，故多減1
    tmp = dices[target_dice]
    dices[target_dice] = dices[target_handle_idx]
    dices[target_handle_idx] = tmp

print(f"after handled dices = {dices}")