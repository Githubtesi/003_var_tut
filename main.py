# ----------------------------
# 008 変数の宣言
# type
# https://docs.python.org/ja/3/library/functions.html#type
# ----------------------------

# 型の宣言は不要
num = 1
name = 'Mike'
is_ok = True

# 型の確認
print(num, type(num))
print(name, type(name))
print(name, type(name))

# ほかの型に代入をした場合
# intの型にstrをいれる→strの型になる
num = name
print("{} : {} = {}".format(type(num), "num", num))

# 型変換
name = '1'
new_num = int(name)
print("{} : {} = {}".format(type(new_num), "new_num", new_num))

# 型の宣言
# 記述はあっても意味がない。。。
# だたし、クラスの場合はメソッドが紐づけられるのでfuncの引数に書くのは有効
num: int = 1

# 先頭に数字を入れるとSyntaxErrorが発生する
# 1num=1 SyntaxError
