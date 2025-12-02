def factorial(_nn):
  if _nn == 0 or _nn == 1:
    return 1
  
  result = 1
  
  while _nn != 1:
    result = result * _nn
    _nn -= 1
    
  return result

if __name__ == '__main__':
  nn = int(input(f"輸入 n 階乘："))
  print(f"{nn} 階乘, 計算結果: {factorial(nn)}")