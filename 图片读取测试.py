import cv2
import os
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\Helmet_1500"
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list, desc='图片读取测试'):
        if file.endswith('.jpg'):
            img_path = os.path.join(file_dir, file)
            try:
                img = cv2.imread(img_path)
            except Exception as e:
                print(img_path)