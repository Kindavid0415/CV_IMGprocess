import os
import cv2
import shutil
from lxml import etree
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\20221115aqm6kimg"
    save_dir = os.path.join(file_dir, 'labels')
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
                doc = etree.parse(xml_path)
                root = doc.getroot()
                sub_all = root.findall('.//object')
                for sub in sub_all:
                    pre_dsc = sub.find('name').text
                    if pre_dsc in cnt.keys():
                        cnt[pre_dsc] += 1
                    else:
                        cnt[pre_dsc] = 1
                    bndbox = sub.find('bndbox')
                    xmin = int(bndbox.find('xmin').text)
                    ymin = int(bndbox.find('ymin').text)
                    xmax = int(bndbox.find('xmax').text)
                    ymax = int(bndbox.find('ymax').text)
                    save_img = img[ymin:ymax, xmin:xmax]
                    save_img_path = os.path.join(save_dir, pre_dsc + '_' + img_path[-8:-4]+'_'+str(cnt[pre_dsc]) + '.jpg')
                    cv2.imwrite(save_img_path, save_img)


