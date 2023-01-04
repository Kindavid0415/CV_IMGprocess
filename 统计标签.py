import os
import xml.etree.ElementTree as ET
from tqdm import tqdm


if __name__ == '__main__':
    label_static = {}
    file_dir = r"C:\Users\kindavid\Desktop\tt\normal"
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list, desc='统计标签'):
        if file.endswith('.xml'):
            xml_path = os.path.join(file_dir, file)
            try:
                doc = ET.parse(xml_path)
                root = doc.getroot()
                sub_all = root.findall('.//object')
                for sub in sub_all:
                    name = str(sub.find('name').text)
                    if name == 'abnormal':
                        print(file)
                    if name in label_static.keys():
                        label_static[name] += 1
                    else:
                        label_static[name] = 1
            except Exception as e:
                print('%s标签文件有问题' % xml_path)
    print(label_static)
