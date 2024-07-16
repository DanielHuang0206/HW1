import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# 設置隨機種子以確保結果可重現
np.random.seed(0)

# 用於存儲統計結果的列表
data = []

for i in range(10):
    # 生成隨機的三通道影像
    images = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)

    # 轉換為灰階並計算統計數據
    gray_images = np.mean(images, axis=2).astype(np.uint8)

    # 計算統計數據
    max_values = np.max(gray_images)
    min_values = np.min(gray_images)
    mean_values = np.mean(gray_images)
    std_values = np.std(gray_images)

    j=i+1
    plt.figure(figsize=(6, 6))
    plt.imshow(gray_images, cmap='gray')
    plt.title(f"Gray Image")
    plt.axis('off')
    plt.show()

    # 保存統計數據到列表
    data.append({
        "Image": j,
        "Max": max_values,
        "Min": min_values,
        "Mean": mean_values,
        "Std Dev": std_values
    })



# 將統計數據轉換為 DataFrame
df = pd.DataFrame(data)

# 獲取桌面路徑
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 組合檔案路徑
file_path = os.path.join(desktop_path, 'gray_image_data.xlsx')

# 儲存為 xlsx 文件
df.to_excel(file_path, index=False)
print(f"File saved to {file_path}")
