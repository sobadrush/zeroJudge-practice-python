def sol():
  nowClock = input("輸入現在時間：")

  timeStrings = nowClock.split(" ")
  if len(timeStrings) > 2 or len(timeStrings) <= 0:
    print("時間格式錯誤！")

  targetTimeNumber = int("".join(timeStrings))

  if targetTimeNumber >= 730 and targetTimeNumber <= 1700:
    print("At school")
  else:
    print("Off School")
  
if __name__ == '__main__':
  while True:
    sol()