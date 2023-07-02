import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# 下載並解壓縮資料集
zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True)
csv_path, _ = os.path.splitext(zip_path)

# 讀取資料集並處理
df = pd.read_csv(csv_path)
# 切片 [start:stop:step]，從索引為 5 的記錄開始，每隔 6 個記錄選擇一個
df = df[5::6]

# 將 'Date Time' 轉換為日期時間格式並從資料框中移除
date_time = pd.to_datetime(df.pop('Date Time'), format='%d.%m.%Y %H:%M:%S')

# 顯示資料框的內容
print(df)
