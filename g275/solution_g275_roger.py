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
  sentence1, sentence2 = pPoem[0], pPoem[1]
  if sentence1[1] == sentence2[1]: 
    return False
  if sentence1[3] == sentence2[3]: 
    return False
  if sentence1[5] == sentence2[5]: 
    return False
  return True

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
    if (not checkRuleA(sentence)): # 檢查規則 A (A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄)
      violation_rule.add("A")
      break
  
  if (not checkRuleB(pair_sentence)): # 檢查規則 B (A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄)
    violation_rule.add("B")
  
  if (not checkRuleC(pair_sentence)): # 檢查規則 C (上下相對：第一、二句的第二、四、六個字平仄必須不同)
    violation_rule.add("C")
  
  if violation_rule: # 不是空的 set, 才存
    violations.append(violation_rule)

if not violations:
  print("None")
else:
  for violation in violations:
    sorted_violation = sorted(violation)
    print(f"違反規則為：{''.join(sorted_violation)}")