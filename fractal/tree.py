import turtle

def draw_fractal_tree(t, branch_length, shorten_by, angle):
    if branch_length < 3:
        return
    else:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        draw_fractal_tree(t, new_length, shorten_by, angle)

        t.right(angle * 2)
        draw_fractal_tree(t, new_length, shorten_by, angle)

        t.left(angle)
        t.backward(branch_length)

# タートル（描画ツール）の初期化
t = turtle.Turtle()
win = turtle.Screen()

# タートルの速度を設定
t.speed(10)

# 描画の開始位置を設定
t.left(90)  # 最初に左に90度回転して、上向きに
t.up()
t.backward(100)  # タートルの位置を少し下げる
t.down()

# フラクタルの木を描く
draw_fractal_tree(t, branch_length=100, shorten_by=15, angle=20)

# 画面が閉じられるまで待つ
win.exitonclick()
