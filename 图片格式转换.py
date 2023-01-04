import os
from PIL import Image
from tqdm import tqdm


if __name__ == '__main__':
    file_dir = r"C:\Users\kindavid\Desktop\11"
    file_list = os.listdir(file_dir)
    for file in tqdm(file_list):
        if file.endswith('.jpeg'):
            jpeg_path = os.path.join(file_dir, file)
            img = Image.open(jpeg_path)
            img.save(jpeg_path.replace('.jpeg', '.jpg'), "JPEG", quality=80, optimize=True, progressive=True)
            os.remove(jpeg_path)
        if file.endswith('.png'):
            png_path = os.path.join(file_dir, file)
            img = Image.open(png_path)
            img = img.convert('RGB')
            img.save(png_path.replace('.png', '.jpg'), quality=95)
            os.remove(png_path)
        if file.endswith('.webp'):
            webp_path = os.path.join(file_dir, file)
            img = Image.open(webp_path)
            img.load()
            img = img.convert('RGB')
            img.save(webp_path.replace('.webp', '.jpg'), 'JPEG')
            os.remove(webp_path)
