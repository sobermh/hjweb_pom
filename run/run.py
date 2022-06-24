"""
@author:maohui
@time:2022/6/9 14:18
"""

import unittest
import HTMLTestRunner
from HTMLTestRunner_PY3 import HTMLTestRunner

suite=unittest.defaultTestLoader.discover('../case/','*.py')

file=open('../report/hjweb_test_result.html', mode='wb')
runner=HTMLTestRunner(file,title="官网自动化测试报告",description="IDC毛辉")

runner.run(suite)
file.close()
