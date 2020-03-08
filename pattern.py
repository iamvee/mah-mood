#!/usr/bin/env python3
import  os
import time
import datetime


coef = 20
username = "iamvee"
repo = "mah-mood"
 
MILLISECONDS_PER_DAY = 24*3600
PATTERN = """
..9...................99...........................
..9...................99...........................
..9...................99...........................
..9.999......9999.9...99...........................
..99..99....99...9.................................
..99...99...99...99...99...........................
..99...99....9999.99..99...........................
"""


def transpose(pattern):
    lines = pattern.replace('.', '0').split('\n')
    arr = [[int(c) for c in line] for line in lines if line]

    a, b = len(arr), len(arr[0])
    arrx = [[arr[i][j] for i in range(a)] for j in range(b)]
    arrx = arrx[::-1]
    return arrx


def time_offset_gen(i, j, coef_index, weekday):
    days = j - weekday + 1
    return MILLISECONDS_PER_DAY * (i * 7 - days) - coef_index


def do_commit(i, j, k, now, weekday):
    tx = now -  time_offset_gen(i, j, k, weekday)
    os.system(f"echo {tx} > file") 
    os.system(f"git add . ")
    os.system(f"git commit -m 'test $i'" )
    os.system(f"GIT_COMMITTER_DATE='`date --date=@{tx}`'")
    os.system(f"git commit --amend --no-edit --date '`date --date=@{tx}`'")


if __name__ == '__main__':
    os.system("git init")
    now = time.time()
    weekday = datetime.datetime.now().weekday()
    remote = f"git@github.com:{username}/{repo}.git"

    for i, x in enumerate(arrx):
        for j, y in enumerate(x):
            for k in range(coef * y):
                do_commit(i, j, k, now, weekday)
            

    os.system(f"git remote add origin {remote} && git push -u origin master")    
