import os
from tqdm import tqdm


if __name__ == '__main__':
    imgs_dir = r"C:\Users\kindavid\Desktop\tt"
    imgs_list = os.listdir(imgs_dir)
    for file in tqdm(imgs_list, desc='删除多余文件'):
        if file.endswith('.jpg'):
            name, _ = os.path.splitext(file)
            xml_path = os.path.join(imgs_dir, name+'.xml')
            if os.path.exists(xml_path):
                continue
            else:
                img_path = os.path.join(imgs_dir, file)
                os.remove(img_path)
                print('已删除%s' % img_path)
        elif file.endswith('.xml'):
            name, _ = os.path.splitext(file)
            img_path = os.path.join(imgs_dir, name + '.jpg')
            if os.path.exists(img_path):
                continue
            else:
                xml_path = os.path.join(imgs_dir, file)
                os.remove(xml_path)
                print('已删除%s' % xml_path)
        else:
            file_path = os.path.join(imgs_dir, file)
            os.remove(file_path)
            print('已删除%s' % file_path)
