#include <iostream>
using namespace std;



// K: 字串長度
// Q: 操作次數
// R: 取出最後二維陣列的第 R 行
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int K, Q, R;
  cin >> K >> Q >> R;

  const int MAXN = 20;
  char inputStr[MAXN + 1];
  char nextStr[MAXN + 1];
  cin >> inputStr;

  int operate[MAXN][MAXN];
  for(int i = 0; i < Q; i++) {
    for(int j = 0; j < K; j++) {
      cin >> operate[i][j];
    }
  }

  char ans[MAXN][MAXN];

  // 執行排列
  for(int i = 0; i < Q; i++) {
    for(int j = 0; j < K; j++) {
      nextStr[ operate[i][j] - 1 ] = inputStr[j]; // 根據操作陣列重新排列字串
    }
    
    for (int col = 0; col < K; col++) {
      ans[i][col] = nextStr[col]; // 儲存當前操作結果到 ans 陣列
      inputStr[col] = nextStr[col]; // 更新 inputStr 為 nextStr，進行下一次操作
    }
  }


  // 🐞print array
  for(int row = 0; row < R; row++) {
    for(int col = 0; col < Q; col++) {
      cout << ans[col][row];
    }
    cout << '\n';
  }

  return 0;
}


// 4 3 4
// abac
// 4 1 3 2   b c  a a
// 1 2 3 4   b c  a a 
// 2 3 4 1   a b  c a

