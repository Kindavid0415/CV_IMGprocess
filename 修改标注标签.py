import xml.etree.ElementTree as ET
import os
from tqdm import tqdm
from PIL import Image


def change_one_xml(xml_path, dst_path, file_name, src_labels, dst_labels):
    # 打开xml文档
    doc = ET.parse(xml_path)
    root = doc.getroot()
    # 1.修改文件名
    # 2.修改路径
    # 3.修改尺寸
    # 4.修改difficult
    # 5.删除object
    sub_all = root.findall('.//object')
    for sub in sub_all:
        deleted = str(sub.find('name').text)
        if deleted not in src_labels:
            if deleted not in dst_labels:
                root.remove(sub)
                doc.write(dst_path)
    # 6.修改标签
    sub_all = root.findall('.//object/name')
    for sub in sub_all:
        if deleted in src_labels:
            idx = src_labels.index(sub.text)
            sub.text = dst_labels[idx]
            doc.write(dst_path)


if __name__ == '__main__':
    src_labels = ['0', '1']
    # dst_labels = ['No helmet', 'Standard wear', 'Irregular wear']
    dst_labels = ['abnormal', 'normal']

    xml_dir = r"C:\Users\kindavid\Desktop\SF6barometer"
    dst_dir = r"C:\Users\kindavid\Desktop\SF6barometer"
    xml_list = os.listdir(xml_dir)
    for xml in tqdm(xml_list):
        if xml.endswith('.xml'):
            xml_name, _ = os.path.splitext(xml)
            file_name = xml_name + '.jpg'
            xml_path = os.path.join(xml_dir, xml)
            dst_path = os.path.join(dst_dir, xml)
            change_one_xml(xml_path, dst_path, file_name, src_labels, dst_labels)

