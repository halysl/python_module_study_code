# -*- coding: utf-8 -*-

try:
    some_code()
# 这个将会捕获除了 SystemExit 、 KeyboardInterrupt 和 GeneratorExit 之外的所有异常。
except Exception as e:
    log('Reason:', e)      # Important!
# 如果你还想捕获这三个异常，将 Exception 改成 BaseException 即可。
except BaseException as e:
    log('Reason:', e)

