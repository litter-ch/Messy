# 导入 sys 模块 (Python内置模块)
import sys

# 修改递归的默认限制
sys.setrecursionlimit(500)

# 递归的最大深度
limit = sys.getrecursionlimit()
print(f'{limit=}')

