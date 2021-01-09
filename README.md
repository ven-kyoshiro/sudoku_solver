# sudoku_solver
数独ソルバー書いた方が早いのでは？と誰もが思うやつ

## 動作環境
- 標準ライブラリで動くはず
- python 3.6.6

## 使い方
- solve_random.py内部の
```
 62     ini_ans =[
 63         [X,X,X,8,4,5,X,X,X],
 64         [X,X,9,X,X,X,1,X,X],
 65         [X,3,X,X,X,9,X,2,X],
 66         [4,X,7,X,X,X,X,X,3],
 67         [5,X,X,X,1,X,X,X,4],
 68         [2,X,X,X,X,X,9,X,5],
 69         [X,8,X,3,X,X,X,6,X],
 70         [X,X,6,X,X,X,7,X,X],
 71         [X,X,X,5,2,6,X,X,X]
 72     ]
 ```
 箇所を編集して実行．
 > python solve_random.py
 以下のように結果が表示されます
 ```
 (c366) kyoshiro@MB ~/works/sudoku_solver$python solve_random.py
[random search] trial:0 result:cannot_continue
[random search] trial:1 result:dead
[random search] trial:2 result:goal
[[1, 7, 2, 8, 4, 5, 3, 9, 6],
 [6, 5, 9, 2, 3, 7, 1, 4, 8],
 [8, 3, 4, 1, 6, 9, 5, 2, 7],
 [4, 1, 7, 9, 5, 2, 6, 8, 3],
 [5, 9, 8, 6, 1, 3, 2, 7, 4],
 [2, 6, 3, 7, 8, 4, 9, 1, 5],
 [9, 8, 5, 3, 7, 1, 4, 6, 2],
 [3, 2, 6, 4, 9, 8, 7, 5, 1],
 [7, 4, 1, 5, 2, 6, 8, 3, 9]]
 ```

