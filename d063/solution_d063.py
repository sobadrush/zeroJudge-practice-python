num = int(input("Please input a nunmber:"))

if num != 1 or num != 0:
  print("Please input 1 or 0.")
else:
  print(1 if num == 0 else 0)