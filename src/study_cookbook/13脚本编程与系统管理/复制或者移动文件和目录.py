# -*- coding: utf-8 -*-

import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

# 复制目录中的符号链接而不是 符号链接指向的文件
shutil.copytree(src, dst, symlinks=True)

# 通过忽略函数忽略部分file
def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))
