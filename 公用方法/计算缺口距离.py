# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: 计算缺口距离.py
@time: 2024/7/11 19:04
"""
# 适用版本 jsv 5.1.49   version 0.1.75

import cv2
import numpy as np


# 计算缺口距离
# 适用于下载的滑块图高度不等与背景图高度
def calculate_distance_model_1(bg_img_path, slider_img_path):
    """
    :param bg_img_path: 背景图路径
    :param slider_img_path: 滑块图路径
    :return: 缺口距离
    """
    # 读取背景图和滑块图
    bg_img = cv2.imread(bg_img_path, cv2.IMREAD_COLOR)
    slider_img = cv2.imread(slider_img_path, cv2.IMREAD_COLOR)

    if bg_img is None or slider_img is None:
        raise ValueError("One or both image paths are incorrect or the images could not be read.")

    # 转换为灰度图像
    bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    slider_gray = cv2.cvtColor(slider_img, cv2.COLOR_BGR2GRAY)

    # 去噪声（双边滤波）
    bg_gray = cv2.bilateralFilter(bg_gray, 9, 75, 75)
    slider_gray = cv2.bilateralFilter(slider_gray, 9, 75, 75)

    # 边缘检测（Canny）
    bg_edges = cv2.Canny(bg_gray, 50, 150)
    slider_edges = cv2.Canny(slider_gray, 50, 150)

    # 多尺度模板匹配
    best_match = None
    best_val = -1
    best_scale = 1.0
    for scale in np.linspace(0.8, 1.2, 20):
        # 调整滑块图像大小
        resized_slider = cv2.resize(slider_edges, (0, 0), fx=scale, fy=scale)
        result = cv2.matchTemplate(bg_edges, resized_slider, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > best_val:
            best_val = max_val
            best_match = max_loc
            best_scale = scale

    top_left = best_match
    slider_height, slider_width = (int(slider_gray.shape[0] * best_scale), int(slider_gray.shape[1] * best_scale))

    # 计算缺口距离（滑块的左上角 x 坐标）
    gap_distance = top_left[0]

    # 在背景图上绘制匹配区域矩形（可选）
    bottom_right = (top_left[0] + slider_width, top_left[1] + slider_height)
    cv2.rectangle(bg_img, top_left, bottom_right, (0, 0, 255), 2)

    # 显示结果图像（可选）
    cv2.imshow('Background Image with Gap', bg_img)
    cv2.imshow('Slider Image', slider_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("滑块缺口距离：", gap_distance)

    return gap_distance


# 适用于下载的滑块图高度等与背景图高度
def calculate_distance_model_2(bg_img_path, slider_img_path):
    """
    :param bg_img_path: 背景图路径
    :param slider_img_path: 滑块图路径
    :return: 缺口距离
    """
    # 读取图像
    bg_img = cv2.imread(bg_img_path)
    slider_img = cv2.imread(slider_img_path)

    # 确保图像加载成功
    if bg_img is None or slider_img is None:
        raise ValueError("One or both images could not be loaded.")

    # 转换为灰度图像
    gray_a = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(slider_img, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配方法找到最佳匹配位置
    result = cv2.matchTemplate(gray_a, gray_b, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # 返回最佳匹配位置的 x 轴坐标
    best_match_x = max_loc[0]

    # 在背景图上绘制匹配区域矩形
    slider_height, slider_width = slider_img.shape[:2]
    top_left = max_loc
    bottom_right = (top_left[0] + slider_width, top_left[1] + slider_height)
    cv2.rectangle(bg_img, top_left, bottom_right, (0, 0, 255), 2)

    # 显示结果图像
    cv2.imshow('Background Image with Gap', bg_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("滑块缺口距离：", best_match_x)

    return best_match_x