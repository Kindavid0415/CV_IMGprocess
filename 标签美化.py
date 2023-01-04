from lxml import etree
import os
import cv2
from tqdm import tqdm


def xml_simplify(img_path, xml_path):
    all_labels = []
    doc = etree.parse(xml_path)
    root = doc.getroot()
    # 1.提取目标框
    sub_all = root.findall('.//object')
    for sub in sub_all:
        label = {}
        label['name'] = str(sub.find('name').text)
        bndbox = sub.find('bndbox')
        label['xmin'] = str(bndbox.find('xmin').text)
        label['ymin'] = str(bndbox.find('ymin').text)
        label['xmax'] = str(bndbox.find('xmax').text)
        label['ymax'] = str(bndbox.find('ymax').text)
        all_labels.append(label)
    # 2.重写标签
    root = etree.Element('annotation')
    # filename
    filename = etree.SubElement(root, 'filename')
    filename.text = os.path.basename(img_path)
    # size
    size = etree.SubElement(root, 'size')
    img = cv2.imread(img_path)
    h, w, d = img.shape
    height = etree.SubElement(size, 'height')
    width = etree.SubElement(size, 'width')
    depth = etree.SubElement(size, 'depth')
    height.text = str(h)
    width.text = str(w)
    depth.text = str(d)
    # object
    for label in all_labels:
        object = etree.SubElement(root, 'object')
        name = etree.SubElement(object, 'name')
        name.text = label['name']
        bndbox = etree.SubElement(object, 'bndbox')
        xmin = etree.SubElement(bndbox, 'xmin')
        xmin.text = label['xmin']
        ymin = etree.SubElement(bndbox, 'ymin')
        ymin.text = label['ymin']
        xmax = etree.SubElement(bndbox, 'xmax')
        xmax.text = label['xmax']
        ymax = etree.SubElement(bndbox, 'ymax')
        ymax.text = label['ymax']
    # 3.写入文件
    doc = etree.ElementTree(root)
    doc.write(xml_path, pretty_print=True, encoding='utf-8')


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\SF6barometer\normal"
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list, desc='xml文件美化'):
        if file.endswith('.xml'):
            xml_path = os.path.join(file_dir, file)
            img_path = xml_path.replace('.xml', '.jpg')
            if os.path.exists(img_path):
                xml_simplify(img_path, xml_path)

