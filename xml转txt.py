import shutil
import xml.etree.ElementTree as ET
import os
import random
from tqdm import tqdm


def convert_label(xml_file_path, txt_file_path):
    def convert_box(size, box):
        dw, dh = 1. / size[0], 1. / size[1]
        x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, \
                     box[1] - box[0], box[3] - box[2]
        return x * dw, y * dh, w * dw, h * dh

    in_file = open(xml_file_path)
    out_file = open(txt_file_path, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    names = ['aqm_wpd', 'aqm_zqpd', 'aqm_wzqpd']
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls in names:
            xmlbox = obj.find('bndbox')
            bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ('xmin', 'xmax', 'ymin', 'ymax')])
            cls_id = names.index(cls)  # class id
            out_file.write(" ".join([str(a) for a in (cls_id, *bb)]) + '\n')
    out_file.close()


if __name__ == '__main__':
    # 1.path
    root_dir = r"C:\Users\kindavid\Desktop\2022118_aqm_xml\2022118_aqm_xml"
    txts_dir = os.path.join(root_dir, 'Labels')
    imgs_dir = os.path.join(root_dir, 'Imgs')
    # 2.dir
    shutil.rmtree(imgs_dir, ignore_errors=True)
    shutil.rmtree(txts_dir, ignore_errors=True)
    os.mkdir(imgs_dir)
    os.mkdir(txts_dir)
    # 3.convert xml to txt
    imgs_list = os.listdir(root_dir)
    for img_file in tqdm(imgs_list, desc='convert xml to txt'):
        if img_file.endswith('.jpg'):
            name, _ = os.path.splitext(img_file)
            txt_file = name + '.txt'
            xml_file = name + '.xml'
            xml_path = os.path.join(root_dir, xml_file)
            txt_path = os.path.join(txts_dir, txt_file)
            convert_label(xml_path, txt_path)
            src_img_path = os.path.join(root_dir, img_file)
            dst_img_path = os.path.join(imgs_dir, img_file)
            shutil.copyfile(src_img_path, dst_img_path)

