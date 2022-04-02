#!/usr/bin/env python3

for _ in range(int(input())):
    print(sorted(list(map(int ,input().split())), reverse=True)[2])
