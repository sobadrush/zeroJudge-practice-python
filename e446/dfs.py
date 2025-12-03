# 定義一個深度優先搜尋 (DFS) 函式，用於生成列表的所有排列組合。
# 參數:
#   nums: 原始數字列表，每次遞迴會移除已選的數字。
#   path: 目前已形成的排列組合路徑。
def dfs(nums, path):
    # 基本情況 (Base Case): 如果 nums 列表為空，表示所有數字都已選擇完畢，
    # 形成了一個完整的排列組合。
    if not nums:
        # 印出這個排列組合。
        print(path)
        return

    # 遞迴情況 (Recursive Case): 遍歷 nums 列表中的每一個數字。
    for i in range(len(nums)):
        # 遞迴呼叫 dfs 函式：
        # 1. nums[:i] + nums[i+1:]: 創建一個新的列表，排除了當前選中的數字 nums[i]。
        #    這確保了每個數字在一個排列組合中只會被使用一次。
        # 2. path + [nums[i]]: 將當前選中的數字 nums[i] 加入到目前的排列組合路徑中。
        dfs(nums[:i] + nums[i+1:], path + [nums[i]])

# 初始呼叫 dfs 函式，以列表 [1, 2, 3] 開始生成其所有排列組合，
# 初始路徑為空列表 []。
dfs([1, 2, 3], [])
