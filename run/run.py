"""
@author:maohui
@time:2022/6/9 14:18
"""
import sys

sys.path.append('E:\PycharmProjects\hjweb_pom')
import unittest
import HTMLTestRunner1
from HwTestReport import HTMLTestReport
import BeautifulReport


# suite=unittest.defaultTestLoader.discover('../case/','*')
# # for case in suite:
# #     print(case)
#     # suite=unittest.defaultTestLoader.discover('../case/','case_01_search.py')
# file=open('../report/hjweb_test_result.html', mode='wb')
# runner=HTMLTestReport(file,title="自动化测试报告",description="汇健官网自动化测试，涵盖前后端及交互",tester='IDC毛辉')
# # runner=HTMLTestRunner1.HTMLTestRunner(file,title="自动化测试报告",description="官网自动化测试报告")
# runner.run(suite)
# file.close()

if __name__=='__main__':
    suite = unittest.defaultTestLoader.discover('../case', '*')
    # for case in suite:
    #     print(case)
    # suite=unittest.defaultTestLoader.discover('../case/','case_01_search.py')
    file = open('../report/hjweb_test_result.html', mode='wb')
    runner = HTMLTestReport(file, title="自动化测试报告", description="汇健官网自动化测试，涵盖前后端及交互", tester='IDC毛辉')
    # runner=HTMLTestRunner1.HTMLTestRunner(file,title="自动化测试报告",description="官网自动化测试报告")
    runner.run(suite)
    file.close()
    unittest.main()


# # 创建一个测试套件
# suite = unittest.defaultTestLoader.discover('../case/','*')
# # 将测试用例加载到测试套件中
# runner = BeautifulReport.BeautifulReport(suite)
# runner.report(filename='hjweb_test_result.html',description='汇健官网自动化测试，涵盖前后端及交互',log_path='.',report_dir='../report')

