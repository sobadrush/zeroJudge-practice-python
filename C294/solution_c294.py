
# 判斷三角形函式
def defineTriangle(inputEdges):
  # 輸入
  edges = list(map(int, inputEdges.split()))
  edges.sort()
  print(f"輸入的邊長為 {edges}")

  aa = edges[0]
  bb = edges[1]
  cc = edges[2]

  if aa + bb <= cc:
    print("三線段無法構成三角形!")
  elif (aa * aa) + (bb * bb) < (cc*cc):
    print("三線段構成鈍角三角形(Obtuse triangle)")
  elif (aa * aa) + (bb * bb) == (cc*cc):
    print("三線段構成直角三角形(Right triangle)")
  elif (aa * aa) + (bb * bb) > (cc*cc):
    print("三線段構成銳角三角形(Acute triangle)")

if __name__ == '__main__':
  edges = input("請輸入三正整數，並以空白分隔: ")
  defineTriangle(edges)