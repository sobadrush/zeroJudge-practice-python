while True:
  
  inpVal = list(map(int, input("請輸入整數 a , b :").split(" ")))
  aa = inpVal[0]
  bb = inpVal[1]
  
  if aa > bb:
    print("a 不可大於 b，請重新輸入：")
    continue
  
  if aa == 0 or bb == 0:
    print("a, b 不可等於 0, 請重新輸入：")
    continue
  
  gcd = 1
  for i in range(aa, 0, -1):
    if (aa % i == 0) and (bb % i == 0):
      gcd = i
      break
    
  print(f"最大公因數 = {gcd}")
  break