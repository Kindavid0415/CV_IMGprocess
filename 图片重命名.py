import os
import random
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\11"
    file_list = os.listdir(file_dir)
    cnt = 0
    for file in tqdm(file_list):
        cnt += 1
        name, _ = os.path.splitext(file)
        dst_name = str(cnt).zfill(5)
        img_path = os.path.join(file_dir, file)
        dst_img_path = os.path.join(file_dir, 'hat' + dst_name + '.jpg')
        os.rename(img_path, dst_img_path)