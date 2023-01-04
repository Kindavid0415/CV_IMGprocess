import os
import cv2
import shutil
from lxml import etree
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\SF6barometer"
    save_dir = os.path.join(file_dir, 'rewrite')
    cnt = {}
    shutil.rmtree(save_dir, ignore_errors=True)
    os.mkdir(save_dir)
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list, desc='提取标签图片'):
        if file.endswith('.jpg'):
            img_path = os.path.join(file_dir, file)
            xml_path = img_path.replace('.jpg', '.xml')
            if os.path.exists(xml_path):
                img = cv2.imread(img_path)
                save_img = img
                save_img_path = os.path.join(save_dir, file)
                cv2.imwrite(save_img_path, save_img)


