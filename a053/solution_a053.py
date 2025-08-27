nn = int(input("請輸入題數:"))

if nn < 0 or nn > 100:
  raise ValueError("輸入題數超出範圍 (0~100)")

score = 0
if nn >= 0 and nn <= 10:
  question_score = 6
  score = nn * question_score
elif nn >= 11 and nn <= 20:
  question_score = 2
  score = 60 + question_score * (nn - 10)
elif nn >= 21 and nn <= 40:
  question_score = 1
  score = 60 + 20 + question_score * (nn - 20)
elif nn >= 40:
  score = 100
  
print(f"答對題數 {nn}，分數為: {score}")