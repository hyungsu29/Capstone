import os
import sys

site=sys.argv[1]

os.system('python3 aaa.py '+site)
os.system('python3 bbb.py')
os.system('R CMD BATCH ccc.r')
os.system('python3 ddd.py '+site)
os.system('python3 getpredict.py '+site+' 1 1')
