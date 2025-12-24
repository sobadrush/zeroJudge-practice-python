#include <iostream>
#include <vector>
using namespace std;



// K: 字串長度
// Q: 操作次數
// R: 取出最後二維陣列的第 R 行
int main() {
  int K, Q, R;
  cin >> K >> Q >> R;

  char inputStr[K];
  for(int i = 0; i < K; i++) {
    cin >> inputStr[i];
  }

  // 🐞print array
  // for(int i = 0; i < K; i++) {
  //   cout << inputStr[i];
  // }

  // 輸入操作
  int operate[Q][K];
  for(int i = 0; i < Q; i++) {
    for(int j = 0; j < K; j++) {
      cin >> operate[i][j];
    }
  }

  // 🐞print array
  // for(int i = 0; i < Q; i++) {
  //   for(int j = 0; j < K; j++) {
  //     cout << arr[i][j] << " ";
  //   }
  //   cout << endl;
  // }

  char ans[Q][K];

  // 執行排列
  for(int i = 0; i < Q; i++) {
    for(int j = 0; j < K; j++) {
      ans[i][ operate[i][j] - 1 ] = inputStr[j];
    }
    
    // 修改原陣列，下一次迭代時使用
    for (int gg = 0; gg < K; gg++) {
      inputStr[gg] = ans[i][gg];
    }
  }


  // 🐞print array
  for(int i = 0; i < Q; i++) {
    for(int j = 0; j < K; j++) {
      cout << ans[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}


// 4 3 4
// abac
// 4 1 3 2   b c  a a
// 1 2 3 4   b c  a a 
// 2 3 4 1   a b  c a

