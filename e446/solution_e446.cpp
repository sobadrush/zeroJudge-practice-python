#include <iostream>
using namespace std;

int N, ans[15];
bool visited[15];

void solve(int p) {

  if (p > N) {
    for (int i = 1; i <= N; i++) {
      cout << ans[i] << " ";
    }
    cout << "\n";
    return;
  }

  for (int i = 1; i <= N; i++) {
    if (visited[i]) {
      continue;
    }
    visited[i] = true;
    ans[p] = i;
    solve(p + 1);
    visited[i] = false; // # 回朔(Backtracking) ... 撤銷選擇
  }
}

int main() {
  cout << "Please Enter N: " << endl;
  cin >> N;
  solve(1);
  return 0;
}