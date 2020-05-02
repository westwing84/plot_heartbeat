# 心拍データをファイルから読み取り，Matplotlibでグラフにプロット

import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime

# ファイルから心拍データを読み込む
filename = "hb_data.csv"
with open(filename) as file:
    reader = csv.reader(file)
    data_org = [row for row in reader]

# 時間表記をdatetimeオブジェクトに変換
i = 1
for line in data_org[1:]:
    data_org[i][0] = datetime.datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S.%f")
    data_org[i][1] = int(line[1])
    i += 1

# グラフにプロットするデータを生成
time = 0
data_plot = [[[time], [data_org[1][1]]]]
init_time = 3600 * data_org[1][0].hour + 60 * data_org[1][0].minute + data_org[1][0].second + 0.000001 * float(data_org[1][0].microsecond)
i = 0
for line in data_org[2:]:
    nowtime = 3600 * line[0].hour + 60 * line[0].minute + line[0].second + 0.000001 * float(line[0].microsecond)
    time = nowtime - init_time
    if int(time) / (i + 1) == 120:  # 2分(=120秒)ごとに区切る
        i += 1
        data_plot.append([[time], [line[1]]])
    else:
        data_plot[i][0].append(time)
        data_plot[i][1].append(line[1])

# グラフにプロット
for j in range(i):
    plt.figure(j)
    plt.plot(data_plot[j][0], data_plot[j][1])
    plt.title("Heartbeat")
    plt.xlabel("Time t[s]")

plt.show()

