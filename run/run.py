"""
@author:maohui
@time:2022/6/9 14:18
"""

import unittest
import HTMLTestRunner1
from HwTestReport import HTMLTestReport

suite=unittest.defaultTestLoader.discover('../case/','case_08_index.py')
# suite=unittest.defaultTestLoader.discover('../case/','case_01_search.py')

file=open('../report/hjweb_test_result.html', mode='wb')
runner=HTMLTestReport(file,title="自动化测试报告",description="汇健官网自动化测试，涵盖前后端及交互",tester='IDC毛辉')
# runner=HTMLTestRunner1.HTMLTestRunner(file,title="自动化测试报告",description="官网自动化测试报告")

runner.run(suite)
file.close()
