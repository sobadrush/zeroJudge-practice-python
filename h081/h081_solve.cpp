#include <iostream>

using namespace std;

// n: 預計觀察幾個股價
// D: Difference 表示預期的獲利(價差)
int main() {
  int n, D;
  cout << "請輸入正整數 n , D" << endl;
  cin >> n >> D;

  // 輸入跳動的股價
  int ticks[5];
  for(int i = 0; i < n ; i++) {
    cin >> ticks[i];
  }

  int profit = 0; // 獲利
  int my_stock = ticks[0]; // 初次購買的股價
  int expect_price = my_stock + D; // 預期獲利
  int last_sold = 0; // 前一次賣出的價格
  for(int i = 1; i < n; i++) {
    if (my_stock > 0) { // 手中有股票
      if(ticks[i] > expect_price) {
        my_stock = 0; // 表示未持有股票
        profit += ticks[i] - my_stock;
      }
    } else { // 未持有股票
      if(ticks[i] <= (last_sold - D)) {
        my_stock = ticks[i]; // 買入股票
      }
    }
  }

  return 0;
}