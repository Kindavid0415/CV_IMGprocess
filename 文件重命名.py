import os
import random
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\tt\abnormal"
    file_list = os.listdir(file_dir)
    random.shuffle(file_list)
    cnt = 0
    for file in tqdm(file_list):
        if file.endswith('.jpg'):
            cnt += 1
            name, _ = os.path.splitext(file)
            dst_name = str(cnt).zfill(4)
            img_path = os.path.join(file_dir, file)
            xml_path = os.path.join(file_dir, name + '.xml')
            dst_img_path = os.path.join(file_dir, 'abnormal2'+dst_name + '.jpg')
            dst_xml_path = os.path.join(file_dir, 'abnormal2'+dst_name + '.xml')
            if os.path.exists(xml_path):
                os.rename(img_path, dst_img_path)
                os.rename(xml_path, dst_xml_path)
