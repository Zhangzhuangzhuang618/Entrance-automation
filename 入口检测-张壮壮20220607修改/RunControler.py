import time
import os

case_list = ['index_top',
             'index_bottom',
             'index_classify',
             'roomsidebar',
             ]

for case in case_list:
    print('执行用例：' + case)
    cmd = 'python ' + r"C:\Users\janelin\PycharmProjects\uientrance\case" + '\\' + str(case) + '.py'
    os.system(cmd)
    print(case + '执行完成')
    time.sleep(5)
