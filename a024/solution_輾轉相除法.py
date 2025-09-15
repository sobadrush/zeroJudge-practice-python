while True:
  
  inpVal = list(map(int, input("請輸入整數 a , b :").split(" ")))
  aa = inpVal[0]
  bb = inpVal[1]
  
  if aa > bb:
    print("a 不可大於 b，請重新輸入：")
    continue
  
  if aa == 0:
    print("a 不可等於 0, 請重新輸入：")
    continue
  if bb == 0:
    print("b 不可等於 0, 請重新輸入：")
    continue
  
  gcd = 1
  while aa != 0:
    tmp = bb % aa
    if tmp == 0:
      break
    bb = aa
    aa = tmp
    
  gcd = aa
  print(f"最大公因數 = {gcd}")
  break