
import sys

# 建立一個字典來定義克制的關係
# 0: 石頭, 2: 剪刀, 5: 布
# 字典的 key 是對方的出拳，value 是我方能贏的出拳
WIN_AGAINST = {
    0: 5,  # 布 克 石頭
    2: 0,  # 石頭 克 剪刀
    5: 2   # 剪刀 克 布
}

def judge(brother_move, sister_move):
    """
    判斷哥哥的出拳結果
    回傳 "win", "lost", 或 "drew"
    """
    if brother_move == sister_move:
        return "drew"  # 平手
    if brother_move == WIN_AGAINST[sister_move]:
        return "win"   # 哥哥贏
    return "lost"      # 哥哥輸

def solve_all_cases():
    """
    讀取所有輸入，並處理所有測試案例
    """
    # 一次讀取所有輸入行
    lines = sys.stdin.readlines()
    if not lines:
        return

    line_idx = 0
    # 每次迴圈處理一個測試案例 (包含兩行)
    while line_idx < len(lines):
        try:
            # 讀取哥哥的初始出拳 F 和 回合數 N
            f_val, n_val = map(int, lines[line_idx].strip().split())
            line_idx += 1
            # 讀取妹妹的出拳序列
            sister_moves = list(map(int, lines[line_idx].strip().split()))
            line_idx += 1
        except (IOError, ValueError):
            # 處理空行或格式錯誤，提前結束
            break

        brother_move = f_val
        brother_history = []
        
        game_over = False
        # 依序進行 N 個回合
        for i in range(n_val):
            brother_history.append(brother_move)
            sister_move = sister_moves[i]
            
            result = judge(brother_move, sister_move)

            if result == "win":
                print(f"{brother_move} Won at round {i + 1}")
                game_over = True
                break
            
            if result == "lost":
                history_str = ' '.join(map(str, brother_history))
                print(f"{history_str} Lost at round {i + 1}")
                game_over = True
                break

            # 如果平手，決定下一回合的出拳策略
            if i > 0 and sister_move == sister_moves[i - 1]:
                # 策略2: 如果妹妹連續兩次出一樣的拳，哥哥就出能克制她的拳
                brother_move = WIN_AGAINST[sister_move]
            else:
                # 策略1: 哥哥模仿妹妹上一回合的出拳
                brother_move = sister_move
        
        if not game_over:
            # 如果所有回合都結束了還沒分出勝負，代表全部平手
            history_str = ' '.join(map(str, brother_history))
            print(f"{history_str} Drew at round {n_val}")

# 程式執行入口
if __name__ == "__main__":
    solve_all_cases()
