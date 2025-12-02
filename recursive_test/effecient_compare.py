import time

"""_summary_
  計算階乘：迴圈版本
"""
def factorial_loop(_nn):
  if _nn == 0 or _nn == 1:
    return 1
  
  result = 1
  
  while _nn != 1:
    result = result * _nn
    _nn -= 1
    
  return result

"""_summary_
  計算階乘：遞迴版本
"""
def factorial_recurive(_nn):
  if _nn == 1 or _nn == 0:
    return 1
  return _nn * factorial_recurive(_nn - 1)


if __name__ == '__main__':
  print("比較迴圈與遞迴計算階乘的效率")
  nn = int(input(f"輸入 n 階乘："))

  # 使用高解析度計時器並將結果轉換為毫秒
  start = time.perf_counter()
  result_loop = factorial_loop(nn)
  elapsed_loop_ms = (time.perf_counter() - start) * 1000
  print(f"迴圈計算 {nn} 階乘, 計算結果: {result_loop}, 花費時間: {elapsed_loop_ms:.3f} 毫秒")
  
  start = time.perf_counter()
  result_recursive = factorial_recurive(nn)
  elapsed_recursive_ms = (time.perf_counter() - start) * 1000
  print(f"遞迴計算 {nn} 階乘, 計算結果: {result_recursive}, 花費時間: {elapsed_recursive_ms:.3f} 毫秒")