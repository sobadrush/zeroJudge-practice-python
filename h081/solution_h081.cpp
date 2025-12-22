#include <iostream>

using namespace std;

// n: 預計觀察幾個股價
// D: Difference 表示預期的獲利(價差)
int main() {
  int n, D;
  cin >> n >> D;

  // 輸入跳動的股價
  if (n <= 0) {
    cout << 0 << endl;
    return 0;
  }

  // 用動態陣列（array）避免固定長度導致越界
  // int* ticks = new int[n];
  int ticks[n];
  for (int i = 0; i < n; i++) {
    cin >> ticks[i];
  }

  int profit = 0; // 獲利
  bool holding = true; // 一開始用 ticks[0] 買入
  int buy_price = ticks[0];
  int expect_price = buy_price + D; // 目標賣出價
  int last_sold = 0; // 前一次賣出的價格

  for (int i = 1; i < n; i++) {
    if (holding) { // 手中有股票
      if (ticks[i] >= expect_price) {
        profit += (ticks[i] - buy_price);
        last_sold = ticks[i];
        holding = false;
      }
    } else { // 未持有股票
      if (ticks[i] <= (last_sold - D)) {
        buy_price = ticks[i];
        expect_price = buy_price + D; // 計算目標賣出價
        holding = true;
      }
    }
  }

  // delete[] ticks; // 使用動態陣列才需要刪除
  cout << profit << endl;
  return 0;
}