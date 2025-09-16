# 檢查是否違反規則 A
# True: 符合規則
# False: 違反規則
def checkRuleA(pLine):
  return (pLine[1] != pLine[3]) and (pLine[1] == pLine[5])

# 檢查是否違反規則 B
# True: 符合規則
# False: 違反規則
def checkRuleB(pPoem):
  return (pPoem[0][-1] == 1) and (pPoem[1][-1] == 0)

# 檢查是否違反規則 C
# True: 符合規則
# False: 違反規則
def checkRuleC(pPoem):
  result = True # 預設符合規則
  for sentence in pPoem:
    if(sentence[1] == sentence[3]):
      result = False
      break
    elif(sentence[3] == sentence[5]):
      result = False
      break
  return result

n = int(input("請輸入 n (1 <= n <= 30): "))

seven_word_poem = []
for i in range(2 * n):
  line = list(map(int, input(f"輸入平仄聲七言對聯{i + 1}: ").split()))
  seven_word_poem.append(line)


violations = [] # 違反的規則
for i in range(0, len(seven_word_poem), 2):
  violation_rule = set() # 每兩句違反的規則
  pair_sentence = [ seven_word_poem[i], seven_word_poem[i + 1] ]
  
  for sentence in pair_sentence:
    if (not checkRuleA(sentence)): # 檢查規則 A
      violation_rule.add("A")
      break
  
  if (not checkRuleB(pair_sentence)): # 檢查規則 B
    violation_rule.add("B")
  
  if (not checkRuleC(pair_sentence)): # 檢查規則 C
    violation_rule.add("C")
  
  if violation_rule: # 不是空的 set, 才存
    violations.append(violation_rule)

if not violations:
  print("None")
else:
  print(f"violations = {violations}")