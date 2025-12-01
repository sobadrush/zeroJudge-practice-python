
def func(nn):
  
  # [終止條件] 如果剩一位數，回傳
  if nn < 10:
    return nn
  
  # 如果還有大於一位數，計算每個 10進位 數字的總和
  sum = 0
  while nn > 0:
    sum = sum + (nn % 10)
    nn = nn // 10
  print(sum)
  return func(sum)

if __name__ == '__main__':
  nn = 1234567892
  ans = func(nn)
  print(f"ans = {ans}")