#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:12:06 2019

@author: subhendugn
"""

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

""" :type : pyboto3.s3 """
# s3. -> will give you autocomplete for s3 methods in pycharm

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


