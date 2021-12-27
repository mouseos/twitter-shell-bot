import sys
import re
import subprocess
from subprocess import PIPE
args = sys.argv
id = "@mouse_soft_y"
cmd = args[1]


def truncate(str, num_bytes, encoding='utf-8'):
    while len(str.encode(encoding)) > num_bytes:
        str = str[:-1]
    return str
    
    
deluser = cmd.replace(id, '')
delshell = deluser.replace("シェル", '')

proc = subprocess.run(("timeout 5 fakechroot fakeroot chroot ./rootfs /bin/bash -c " + re.escape(delshell) ), shell=True, stdout=PIPE, stderr=PIPE, text=True)
date =  (proc.stdout) 
result = (('実行結果: {}'.format(date)))

print(truncate(result, 235))
