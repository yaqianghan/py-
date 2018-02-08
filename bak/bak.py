#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : back.py


import os
import time

source = ['/home/hyq/projectPy']
target_dir = '/home/hyq/projectPy/bak'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print ('Successful backup')
else :
    print ('Backup Failed')

