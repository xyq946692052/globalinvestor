import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import base64
import io
from PIL import Image

# 在template 显示则应写成:  <img src="data:image/png;base64,{{ graphic|safe }}">
def draw_graph(xdata, ydata, title=None):
    xdatas = np.array(xdata)
    ydatas = np.array(ydata)

    # 以下两个顺序不能乱
    fig, ax = plt.subplots(figsize=(5, 5))  # 画布尺寸
    plt.plot(xdatas, ydatas)
    plt.xticks(rotation=20)  # 设置X轴文本倾斜角度
    if title:
        plt.title(title)  # 标题

    ax.xaxis.set_major_locator(ticker.AutoLocator())  # 划分X轴刻度间隔

    # for x, y in zip(mymonth, power): # 显示折线点数据
    #     plt.text(x, y+0.05, '%.0f' % y, ha='center', va='bottom', fontsize=8)

    canvas = fig.canvas
    buf, size = canvas.print_to_buffer()
    image = Image.frombuffer('RGBA', size, buf, 'raw', 'RGBA', 0, 1)
    buffer = io.BytesIO()
    image.save(buffer, 'PNG')
    graphic = buffer.getvalue()
    graphic = base64.b64encode(graphic)
    buffer.close()
    return str(graphic)[2:-1]
