import os
import shutil
import torch
from tqdm import tqdm
from torchvision import transforms
from torchvision.io import read_image
from torchvision.io.image import ImageReadMode
from torchvision.utils import save_image


def image_enhancement(src_dir, dst_dir, number):
    shutil.rmtree(dst_dir, ignore_errors=True)
    os.mkdir(dst_dir)
    src_list = os.listdir(src_dir)
    bright_value = torch.rand(1).item() * 0.5
    contrast_value = torch.rand(1).item() * 0.5
    saturation_value = torch.rand(1).item() * 0.5
    hue_value = torch.rand(1).item() * 0.5
    trans = transforms.Compose(
        [
            # transforms.RandomHorizontalFlip(0.5),
            # transforms.RandomVerticalFlip(0.5),
            # transforms.RandomRotation(45),
            transforms.RandomAffine(degrees=45, scale=(1, 2), shear=45),
            transforms.ColorJitter(brightness=bright_value, contrast=contrast_value,
                                   saturation=saturation_value)  #, hue=hue_value)
        ]
    )
    for src_file in tqdm(src_list, desc='图像增强'):
        if src_file.endswith('.jpg'):
            src_path = os.path.join(src_dir, src_file)
            src_img = read_image(src_path, mode=ImageReadMode.RGB)
            for i in range(number):
                src_name, _ = os.path.splitext(src_file)
                dst_name = src_name + '_' + str(i)
                dst_file = dst_name + '.jpg'
                dst_path = os.path.join(dst_dir, dst_file)

                dst_img = trans(src_img)
                dst_img = torch.div(dst_img, 255)
                save_image(dst_img, dst_path)
    print('完成图像增强')


if __name__ == '__main__':
    image_enhancement(r"C:\Users\kindavid\Desktop\tt\abnormal",\
                      r"C:\Users\kindavid\Desktop\tt\abnormal\enhancement", 5)
