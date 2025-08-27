inputStr = input("輸入 a, b 及預期結果：")

inpStrings = inputStr.split(" ")
aa = bool(int(inpStrings[0]))
bb = bool(int(inpStrings[1]))
cc = bool(int(inpStrings[2]))

print(f"aa = {aa}, bb = {bb}, cc = {cc}")

ans = []

if (aa and bb) == cc:
  ans.append("AND")

if (aa or bb) == cc:
  ans.append("OR")
  
if (aa != bb) == cc:
  ans.append("XOR")

print(ans if len(ans) > 0 else "IMPOSSIBLE")