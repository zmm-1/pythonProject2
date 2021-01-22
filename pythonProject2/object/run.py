import pytest,os,multiprocessing

from datetime import datetime
ts=datetime.now().strftime('%Y,%m,%d-%H-%M-%S')#获取当前时间
# pytest.main(['-v','-s','--alluredir=allureout'])#生成测试数据
# os.system('allure generate allureout -o ./report/Pad_{}'.format(ts))#生成html页面的测试报告
listdir=os.listdir('D:/pythonProject2/object/test_cases')
def run(i):
    pytest.main(['-s','--alluredir=allureout','D:/pythonProject2/object/test_cases/{}'.format(i)])


if __name__ == "__main__":
    # 设置进程池
    pool = multiprocessing.Pool(processes=4)
    # 提供数据

    for i in listdir:
        if 'test' in i:
            pool.apply_async(run, (i,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    # start_time = datetime.now()
    # print(f"进程开始了~~~~~~~{start_time}~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    # end_time = datetime.now()
    # print(f"所有进程结束~~~~~~~~~~{end_time}~~~~~~~~~~")
    # print(f"运行所有case总耗时：{end_time - start_time}")
    os.system('allure generate allureout -o ./report/Pad_{}'.format(ts))  # 生成html页面的测试报告

