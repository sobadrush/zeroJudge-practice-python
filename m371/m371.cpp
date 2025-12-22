#include <iostream>
using namespace std;

int n, m;
int ind[50][50]; // 根據題目範圍宣告陣列大小

int main() {
    // 讀取輸入
    if (!(cin >> n >> m)) return 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> ind[i][j];
        }
    }

    long score = 0;
    bool changed = true;

    // 外層循環：只要這輪有消掉東西，下一輪就可能產生新的消除路徑
    while (changed) {
        changed = false;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 如果已經被消除了，或是值為 0 (若題目有 0)，跳過
                if (ind[i][j] == -1) continue;

                int target = ind[i][j];
                bool found = false; // 標記目前這格是否已配對消除

                // 1. 向下檢查 (垂直方向)
                for (int k = i + 1; k < n; k++) {
                    if (ind[k][j] == -1) continue; // 空位不擋路，繼續往下看
                    if (ind[k][j] == target) {     // 找到成對
                        score += target;
                        ind[i][j] = -1;
                        ind[k][j] = -1;
                        changed = true;
                        found = true;
                    }
                    break; // 無論是找到還是撞到別的數字，都必須停止這方向的掃描
                }

                // 2. 如果向下沒消成，再向右檢查 (水平方向)
                if (!found) {
                    for (int k = j + 1; k < m; k++) {
                        if (ind[i][k] == -1) continue;
                        if (ind[i][k] == target) {
                            score += target;
                            ind[i][j] = -1;
                            ind[i][k] = -1;
                            changed = true;
                            found = true;
                        }
                        break; // 撞到數字或成功消除，都停止掃描
                    }
                }
            }
        }
    }

    cout << score << endl;
    return 0;
}