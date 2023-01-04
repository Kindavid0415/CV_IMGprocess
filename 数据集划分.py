import os
import random
import shutil
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\4.第四阶段材料\1101预赛\数据集\官方数据集\Helmet_1500"
    train_ratio = 80
    train_dir = os.path.join(file_dir, '../train')
    val_dir = os.path.join(file_dir, '../val')
    shutil.rmtree(train_dir, ignore_errors=True)
    shutil.rmtree(val_dir, ignore_errors=True)
    os.mkdir(train_dir)
    os.mkdir(val_dir)
    file_list = os.listdir(file_dir)
    random.shuffle(file_list)
    for file in tqdm(file_list):
        if file.endswith('.jpg'):
            img_path = os.path.join(file_dir, file)
            xml_path = img_path.replace('.jpg', '.xml')
            if os.path.exists(xml_path):
                if random.randint(1, 100) < train_ratio:
                    train_img_path = os.path.join(train_dir, file)
                    train_xml_path = train_img_path.replace('.jpg', '.xml')
                    shutil.copyfile(img_path, train_img_path)
                    shutil.copyfile(xml_path, train_xml_path)
                else:
                    val_img_path = os.path.join(val_dir, file)
                    val_xml_path = val_img_path.replace('.jpg', '.xml')
                    shutil.copyfile(img_path, val_img_path)
                    shutil.copyfile(xml_path, val_xml_path)
