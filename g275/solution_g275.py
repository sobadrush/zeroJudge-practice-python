# zeroJudge g275. 1. 七言對聯
# 題目：檢查七言對聯是否符合平仄規則

import sys

def check_couplet(first, second):
    violations = []
    
    # 檢查長度
    if len(first) != 7 or len(second) != 7:
        return "Invalid input"
    
    # 檢查只包含平仄標記
    if not all(c in [' ', ' '] for c in first + second):
        return "Invalid input"
    
    # 規則 A: 二四不同二六同
    # 第一句
    if not (first[1] != first[3] and first[1] == first[5]):
        violations.append('A')
    # 第二句
    if not (second[1] != second[3] and second[1] == second[5]):
        violations.append('A')
    
    # 規則 B: 仄起平收
    if first[6] != ' ':  # 第一句結尾仄聲
        violations.append('B')
    if second[6] != ' ':  # 第二句結尾平聲
        violations.append('B')
    
    # 規則 C: 上下相對
    for i in [1, 3, 5]:  # 第2,4,6字
        if first[i] == second[i]:
            violations.append('C')
            break
    
    # 輸出結果
    if violations:
        return ','.join(sorted(set(violations)))
    else:
        return 'None'

while True:
    try:
        first = input().strip()
        if first == '0':
            break
        second = input().strip()
        result = check_couplet(first, second)
        print(result)
    except EOFError:
        break