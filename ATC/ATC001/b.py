class UnionFind:

    # 初期化処理
    # 素集合の配列とランクの配列を用意
    # 0 <= (queryの対象となる頂点を表す番号) <= N - 1
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
    
    # 親を探すメソッド
    # 入力された値とその値のインデックスの要素を比較
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # ポインタ的な発想
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    # 結合するメソッド
    def unite(self, x, y):
        # 親を探す
        x = self.find(x)
        y = self.find(y)
        # 親が同じなら特に何もしない
        if x == y:
            return
        # rankに差がある時
        # rankの大き方に小さい方を結合する
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            # ランクが同じ時、上でxはyの親になったので
            if self.parent[x] == self.parent[y]:
                self.rank[x] += 1
    
    # 同じ親かすなはち同じカテゴリかを判定する
    def same(self, x, y):
        return self.find(x) == self.find(y)


N, Q = map(int, input().split()) # 頂点数とqueryの数

unionFind = UnionFind(N)
for _ in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        # 結合
        unionFind.unite(A, B)
    else:
        # 判定
        if unionFind.same(A, B):
            print('Yes')
        else:
            print('No')
