import os
import cv2
import xml.etree.ElementTree as ET
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\wangw\Desktop\hat2"
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list, desc='缩小图片数据'):
        if file.endswith('jpg'):
            img_path = os.path.join(file_dir, file)
            img_kb = os.path.getsize(img_path) / 1024
            if img_kb > 300:
                img = cv2.imread(img_path)
                h = img.shape[0]
                w = img.shape[1]
                if min(h, w) > 1080:
                    ratio = max(1080/h, 1080/w)
                    if ratio < 1:
                        h_new = int(ratio * h)
                        w_new = int(ratio * w)
                        img = cv2.resize(img, (w_new, h_new))
                        cv2.imwrite(img_path, img)

                        name, _ = os.path.splitext(file)
                        xml_path = os.path.join(file_dir, name + '.xml')
                        doc = ET.parse(xml_path)
                        root = doc.getroot()
                        size = root.find('size')
                        size.find('height').text = str(h_new)
                        size.find('width').text = str(w_new)
                        doc.write(xml_path)
                        sub_all = root.findall('.//object')
                        for sub in sub_all:
                            bndbox = sub.find('bndbox')
                            xmin = int(bndbox.find('xmin').text)
                            ymin = int(bndbox.find('ymin').text)
                            xmax = int(bndbox.find('xmax').text)
                            ymax = int(bndbox.find('ymax').text)
                            xmin_new = str(int(ratio * xmin))
                            ymin_new = str(int(ratio * ymin))
                            xmax_new = str(int(ratio * xmax))
                            ymax_new = str(int(ratio * ymax))
                            bndbox.find('xmin').text = xmin_new
                            bndbox.find('ymin').text = ymin_new
                            bndbox.find('xmax').text = xmax_new
                            bndbox.find('ymax').text = ymax_new
                            doc.write(xml_path)




