#!/usr/bin/env python3

x,y,w,h = map(int, input().split(' '))
print(min(w - x, x, y, h -y))
