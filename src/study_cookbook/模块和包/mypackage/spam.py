# -*- coding: utf-8 -*-

import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
print(data)
