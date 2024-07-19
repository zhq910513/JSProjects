# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: 图片解混淆.py
@time: 2024/7/12 15:19
"""

from io import BytesIO

from PIL import Image


# 还原图片   适用于原 JS 代码会生成解密图片顺序
def reduction_image(_arr, _img):
    """
    用于将图片还原
    :param _arr: 图片的序列号数组
    :param _img: 背景图片
    :return: new img: 还原的背景图片
    """
    new_img = Image.new("RGB", (400, 200))

    for index in range(len(_arr)):
        c = _arr[index] * 12
        g = _img.crop((c, 0, c + 12, 200))
        new_x = index * 12
        new_img.paste(g, (new_x, 0))

    new_img.paste(_img.crop((384, 0, 400, 200)), (384, 0))

    output_buffer = BytesIO()
    new_img.save("new_bg.png")
    new_img.save(output_buffer, format="JPEG")

    image_binary = output_buffer.getvalue()
    return image_binary
