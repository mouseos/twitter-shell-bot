import sys
import subprocess
from subprocess import PIPE
args = sys.argv
#自身のidを入れてね
id = "@yourid"
cmd = args[1]


def truncate(str, num_bytes, encoding='utf-8'):
    while len(str.encode(encoding)) > num_bytes:
        str = str[:-1]
    return str
    
    
deluser = cmd.replace(id, '')
delshell = deluser.replace("シェル", '')

proc = subprocess.run(delshell, shell=True, stdout=PIPE, stderr=PIPE, text=True)
date =  (proc.stdout) 
result = (('実行結果: {}'.format(date)))

print(truncate(result, 235))
