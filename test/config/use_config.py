import argparse
import copy
import os
import os.path as osp
import sys
sys.path.append(os.pardir)

from mmmcv.utils import Config

cfg = Config.fromfile('config_a.py')
print(cfg)