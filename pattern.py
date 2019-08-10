#!/usr/bin/env python3
import  os
import time


os.system("git init")

with open('pattern') as f:
    lines = f.read().replace('.', '0').replace('#', '9').split('\n')
    arr = [[int(c) for c in line] for line in lines if line]

arrx = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))][::-1]

now = time.time()

for i, x in enumerate(arrx):
    for j, y in enumerate(x):
        for yy in range(y):
            tx = now -  24*3600 * (i*7+j) - yy
            os.system(f"""
echo . >> file
git add .
git commit -m "test $i"
GIT_COMMITTER_DATE="`date --date=@{tx} `"
git commit --amend --no-edit --date "`date --date=@{tx}`"
""")
            

os.system("""
git remote add origin git@github.com:iamvee/mahmood.git
git push -u origin master
""")    
