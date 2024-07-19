# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: 滑动轨迹.py
@time: 2024/7/12 21:52
"""
import random


# 轨迹规则定义:[[x,y,time],[],[],[]...]
# 一个随机列表长度范围为 30~60
# 第一个数组的 x 值必须为 0
# y 值允许在 -5 和 5 之间波动
# time 值必须从 0 开始
# 但是最后一个数组的x值必须等于 ditance
# y 值的波动范围允许在 -2~2 之间
# 每增加一个列表耗时增加范围为 80~120 之间的随机整数
def generate_track(distance):
    """
    :param distance: 缺口距离
    :return track: 轨迹列表
    """
    track = []
    length = random.randint(30, 60)

    current_x, current_y, current_time = 0, random.randint(-5, 5), 0
    track.append([current_x, current_y, current_time])

    for i in range(1, length - 1):
        remaining_distance = distance - current_x
        max_increment = min(remaining_distance, 20)  # 确保不会超出目标距离
        increment_x = random.randint(1, max_increment)
        current_x += increment_x
        current_y = random.randint(-5, 5)
        current_time += random.randint(80, 120)
        track.append([current_x, current_y, current_time])

        if current_x >= distance:
            break

    current_x = distance
    current_y = random.randint(-2, 2)
    current_time += random.randint(80, 120)
    track.append([current_x, current_y, current_time])

    return track

