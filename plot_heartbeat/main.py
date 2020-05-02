# 心拍データをファイルから読み取り，Matplotlibでグラフにプロット

import matplotlib.pyplot as plt
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

# 2分間隔のデータを生成
t = 0
data_plot = [[t], [data_org[1][1]]]
time = data_org[1][0]
for line in data_org[2:]:
    if (line[0].hour == time.hour) & (line[0].minute == time.minute + 2) & (line[0].second == time.second):
        t += 2
        time = line[0]
        data_plot[0].append(t)
        data_plot[1].append(line[1])

# グラフにプロット
plt.plot(data_plot[0], data_plot[1])
plt.title("Heartbeat")
plt.xlabel("Time t[min]")
plt.show()
