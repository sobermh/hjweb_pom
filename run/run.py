"""
@author:maohui
@time:2022/6/9 14:18
"""

import unittest
import HTMLTestRunner

suite=unittest.defaultTestLoader.discover('../case/','*.py')

file=open('../log/hjweb_test_result.html',mode='wb')
runner=HTMLTestRunner.HTMLTestRunner(file,title="官网自动化测试报告",description="IDC",tester="毛辉")

runner.run(suite)
file.close()
