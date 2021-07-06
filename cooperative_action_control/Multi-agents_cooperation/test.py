#! /user/bin/env python
# -*- coding: utf-8 -*-
"""
@author: gingkg
@contact: sby2015666@163.com
@software: PyCharm
@project: man-machine_counteraction
@file: test.py
@date: 2021-07-06 13:20
@desc: 测试用文件
"""

import numpy as np
import matplotlib.pyplot as plt


win_rates = list(range(0, 100, 1))
episode_rewards = list(range(0, 100, 1))
evaluate_cycle = 5000


def PLT(num):
    plt.figure()
    plt.ylim([0, 105])
    plt.cla()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    plt.subplot(2, 1, 1)
    plt.plot(range(len(win_rates)), win_rates)
    plt.xlabel('step*{}'.format(evaluate_cycle))
    plt.ylabel('win_rates')

    plt.subplot(2, 1, 2)
    plt.plot(range(len(episode_rewards)), episode_rewards)
    plt.xlabel('step*{}'.format(evaluate_cycle))
    plt.ylabel('episode_rewards')

    plt.savefig('test/plt_{}.png'.format(num), format='png')
    np.save('test/win_rates_{}'.format(num), win_rates)
    np.save('test/episode_rewards_{}'.format(num), episode_rewards)
    plt.close()


if __name__ == '__main__':
    PLT(2)




