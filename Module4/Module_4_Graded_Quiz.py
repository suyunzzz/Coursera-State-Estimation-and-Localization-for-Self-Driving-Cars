#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 11:26
# @Author  : Su Yunzheng
# @Email   : suyun_zheng@163.com
# @File    : Module_4_Graded_Quiz.py
# @Description:

import  numpy as np

def h_ver(angle1,angle2,distance):
    '''
    :param angle1: 纵向角
    :param angle2:横向角
    :param distance:距离
    :return:x,y,z 三维世界中的坐标
    '''
    x = distance*np.cos(np.deg2rad(angle2))*np.cos(np.deg2rad(angle1))
    y = distance*np.sin(np.deg2rad(angle2))*np.cos(np.deg2rad(angle1))
    z = distance*np.sin(np.deg2rad(angle1))

    return x,y,z


if __name__ == '__main__':
    x,y,z = h_ver(5,10,4)
    print("x:{}, y:{}, z:{}".format(x,y,z))