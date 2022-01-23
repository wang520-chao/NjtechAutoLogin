from sys import path
from os.path import dirname
path.append(dirname(__file__))
# from os import getcwd
# path.append(getcwd())

# 导入UI依赖的资源文件
import resource_rc

# 导入Windows界面类
from win_adh_login import WinFeedback, WinGiveReward, WinUpdateDialog