#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T= int(sys.stdin.readline().strip())

lines = []
for c in range(T):
    lines.append(input())

print('\n'.join(lines))
