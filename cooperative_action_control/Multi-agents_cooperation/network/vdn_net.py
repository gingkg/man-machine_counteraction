#! /user/bin/env python
# -*- coding: utf-8 -*-
"""
@author: gingkg
@contact: sby2015666@163.com
@software: PyCharm
@project: man-machine_counteraction
@file: vdn_net.py
@date: 2021-07-01 15:43
@desc: 
"""

import torch.nn as nn
import torch


class VDNNet(nn.Module):
    def __init__(self):
        super(VDNNet, self).__init__()

    def forward(self, q_values):
        return torch.sum(q_values, dim=2, keepdim=True)
