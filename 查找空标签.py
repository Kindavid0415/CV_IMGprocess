import os
import xml.etree.ElementTree as ET
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\tt"
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list, desc='剔除空标签'):
        if file.endswith('.xml'):
            xml_path = os.path.join(file_dir, file)
            try:
                doc = ET.parse(xml_path)
                root = doc.getroot()
                sub_all = root.findall('.//object')
                if sub_all == []:
                    os.remove(xml_path)
                    print('%s空标签' % xml_path)
            except Exception as e:
                os.remove(xml_path)
                print('%s文件有问题' % xml_path)
