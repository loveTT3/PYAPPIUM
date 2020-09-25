'''
测试自定义模块的导入
'''


# 自定义模块被其他模块导入时，其中可执行语句会立即执行

import test
import time

test.main()
# python中提供一种