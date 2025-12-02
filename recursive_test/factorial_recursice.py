
def factorial(_nn):
  if _nn == 1 or _nn == 0:
    return 1
  return _nn * factorial(_nn - 1)

if __name__ == '__main__':
  nn = int(input(f"輸入 n 階乘："))
  print(f"{nn} 階乘, 計算結果: {factorial(nn)}")