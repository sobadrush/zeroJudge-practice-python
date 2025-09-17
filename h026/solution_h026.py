brotherFist = int(input("輸入哥哥第一輪要出的拳 F (0指石頭，2指剪刀，5指布)："))

nn = int(input("妹妹準備的數量 N: "))

rule = [ 2, 0, 5 ] # 0指石頭，2指剪刀，5指布

def judgeFun(bFist, sFist):
  if bFist == 2: # 剪刀
    if sFist == 2:
      return "drew"
    elif sFist == 0: # 石頭
      return "lost"
    else: # 布
      return "win"
  elif bFist == 0: # 石頭
    if sFist == 0:
      return "drew"
    elif sFist == 5: # 布
      return "lost"
    else: # 剪刀
      return "win"
  elif bFist == 5: # 布
    if sFist == 5:
      return "drew"
    elif sFist == 2: # 剪刀
      return "lost"
    else: # 石頭
      return "win"

while True:
  sisterFist = list(map(int, input("輸入妹妹準備出的拳：").split()))
  if len(sisterFist) != nn:
    print(f"請輸入 {nn} 個妹妹出的拳！")
    continue
  
  # 依序走訪妹妹出的拳
  sisterHistory = []
  brotherHistory = [brotherFist]
  for idx, sisF in enumerate(sisterFist):
    result = judgeFun(brotherFist, sisF)
    if result == 'win':
      print(f"{brotherFist}: Won at round {idx + 1}")
      break
    if result == 'drew':
      sisterHistory.append(sisF)
      if idx >= 1 and (sisterHistory[idx - 1] == sisF):
        if sisterHistory[idx - 1] == 0:
          brotherFist = 5
        if sisterHistory[idx - 1] == 2:
          brotherFist = 0
        if sisterHistory[idx - 1] == 5:
          brotherFist = 2
      else:
        brotherFist = sisF
      if idx != (len(sisterFist) - 1):
        brotherHistory.append(brotherFist)
      continue
    if result == 'lost':
      print(f"{brotherHistory}: Lost at round {idx + 1}")
      break
    
  print(f"{brotherHistory}: Drew at round {idx + 1}")

  break