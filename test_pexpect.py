#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect

cmd = 'ls ta*'
process = pexpect.spawn('/bin/bash', ['-c', cmd])
index = process.expect(['test_celery.py', 'Pipfile'])
if index == 0:
    print('tasks')
elif index == 1:
    print('Pipfile')