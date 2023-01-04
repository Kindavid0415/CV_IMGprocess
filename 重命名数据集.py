import os
import random
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\tt\abnormal\enhancement"
    file_list = os.listdir(file_dir)
    random.shuffle(file_list)
    cnt = 0
    for file in tqdm(file_list):
        if file.endswith('.xml'):
            cnt += 1
            name, _ = os.path.splitext(file)
            dst_name = str(cnt).zfill(4)
            img_path = os.path.join(file_dir, file)
            dst_img_path = os.path.join(file_dir, 'abnormal2_'+dst_name + '.xml')
            os.rename(img_path, dst_img_path)

