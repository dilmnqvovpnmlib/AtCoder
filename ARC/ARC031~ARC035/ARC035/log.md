# 問題
* [ ] A
* [ ] B
* [ ] C
* [ ] D

# 要約
### A 高橋くんと回文
```text
一部が不明な文字列が与えられる。
この文字列が回文でありうるかを判定する。
```

### B アットコーダー王国のコンテスト事情
```text
ある問題を解くのにかかる時間が与えられる。各問題を解くのにかかった時間だけペナルティーが生じる。
このとき、ペナルティーの最小値とそのような解き方の場合の数を求める。
```

# 考察
### A 高橋くんと回文
- そんなに難しくはなかったけど、ちょっとだけ詰まった。

- 文字の半分の長さに関してインデックスを先頭と末尾から調査していくとう発想がすぐ出来たのは良かった。

- 別解(自分の書いてるコードをド・モルガンで表現し直した感じ)

```python
s = input()
ans = 'YES'
for i, j in zip(s, reversed(s)):
    if i != j and i !='*' and j != '*':
        ans = 'NO'
        break
print(ans)
```

### B アットコーダー王国のコンテスト事情
- 簡単やった。

- 昇順に標準入力をソートした配列の累積和の合計と適宜場合の数を求めるのみ。

# 参考
- [Pythonで階乗を計算](https://note.nkmk.me/python-math-factorial-permutations-combinations/)

```python
import math

print(math.factorial(5)) # 120
```
