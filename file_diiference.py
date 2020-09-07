#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:01:21 2020

@author: nick
"""

import difflib
with open('linear_regression.py') as f1:
    f1_text = f1.read()
with open('linear_regressionv2.py') as f2:
    f2_text = f2.read()
# Find and print the diff:
for line in difflib.unified_diff(f1_text, f2_text, fromfile='file1', tofile='file2', lineterm=''):
    print(line)