# ファイル名などに日本語があるとエラーになります。
# 画像のピクセルごとにBlue(RGBのB)の数値0-255をcsvファイルに出力する。

import os

import cv2
import numpy

img_name = "format_butterfly_half.png"  # 画像ファイルの名前
csv_name = "butterfly_half.csv"  # csvファイルの名前

bgr_array = cv2.imread(img_name)

data = numpy.array(bgr_array[:, :, 1])
# ここでは[:, :, 0]の部分が0なのでBlueの値(0～255)が出力される。
# [:, :, 1]ならGreen、[:, :, 2]ならRedの数値が出力される。

numpy.savetxt(csv_name, data, fmt="%.0f", delimiter=",")
