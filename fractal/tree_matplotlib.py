import matplotlib.pyplot as plt
import numpy as np

def draw_tree(ax, n, line, angle=20):
    if n > 0:
        # 描画する線の座標を計算
        x0, y0 = line[-1]  # 前の線の終点が新たな線の始点
        x1, y1 = x0 + (n * np.cos(np.radians(angle))), y0 + (n * np.sin(np.radians(angle)))  # 線の終点を計算
        ax.plot([x0, x1], [y0, y1], color='k', lw=n)  # 線を描画

        # 次の線を描画
        draw_tree(ax, n-1, [[x0, y0], [x1, y1]], angle - 20)  # 左側の枝
        draw_tree(ax, n-1, [[x0, y0], [x1, y1]], angle + 20)  # 右側の枝

fig, ax = plt.subplots()
draw_tree(ax, 10, [[0, 0], [0, 1]], angle=90)  # angle=90で上方向へ描画開始
plt.show()
