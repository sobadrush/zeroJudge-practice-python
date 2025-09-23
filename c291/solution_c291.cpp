#include <set>
#include <iostream>
using namespace std;

// 0 1 2 3 4 5 6 7 8 9
// 4 7 2 9 6 0 8 1 5 3

int main(){
  
  cout << "請輸入 N: ";
  int nn;
  cin >> nn;

  cout << "輸入好友編號(空格隔開)：";

  int friends[nn];

  for(int i = 0; i < nn ; i++) {
    cin >> friends[i];
  }

  int groupNum = 0;
  set<int> visited;
  for (int j = 0; j < nn; j++) {
    if(visited.count(j) < 1) {
      groupNum++;
      
      int cur = j;

      while (1){
        if(visited.count(cur) > 0) {
          break;
        }
        visited.insert(cur);
        cur = friends[cur];
      }
      
    }
  }

  cout << "小團體數：" << groupNum << endl;
  return 0;
}