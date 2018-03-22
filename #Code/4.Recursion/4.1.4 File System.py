# 4.1.4 File System

import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total

#------------------------------ my main function ------------------------------
path = input('Please input the path\n')
print(disk_usage(path),' byte')