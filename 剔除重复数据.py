import os, time, hashlib
from tqdm import tqdm


def getmd5(file):
    if not os.path.isfile(file):
        return
    fd = open(file, 'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()


if __name__ == "__main__":
    all_imgs = []
    same_imgs = []

    start = time.time()
    imgs_dir = r"C:\Users\kindavid\Desktop\self"

    imgs_list = os.listdir(imgs_dir)
    for file in tqdm(imgs_list, desc='提取md5'):
        if file.endswith('.jpg'):
            file_path = os.path.join(imgs_dir, file)
            md5sum = getmd5(file_path)
            all_imgs.append({'path': file_path, 'md5sum': md5sum})

    # 根据MD5值比较
    for img1 in tqdm(all_imgs, desc='对比md5'):
        file1_path = img1['path']
        file1_md5sum = img1['md5sum']
        for img2 in all_imgs:
            file2_path = img2['path']
            file2_md5sum = img2['md5sum']
            if img1 != img2:
                if file1_md5sum == file2_md5sum:
                    same_imgs.append({'img1': file1_path, 'img2': file2_path})
    for i, img_pair in enumerate(same_imgs):
        print('第%d相同图片对：' % i)
        print(img_pair['img1'])
        print(img_pair['img2'])
        try:
            os.remove(img_pair['img1'])
            print('已删除%s' % img_pair['img1'])
        except Exception as e:
            print('%s不存在' % img_pair['img1'])


