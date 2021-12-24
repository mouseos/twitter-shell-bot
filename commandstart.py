import sys
import subprocess
from subprocess import PIPE
args = sys.argv
id="@mouse_soft_y"
cmd = args[1]

delline = cmd.replace( '\n' , '' )
deluser = delline.replace(id+" ", '')
delshell= deluser.replace("シェル ", '')

proc = subprocess.run(delshell, shell=True, stdout=PIPE, stderr=PIPE, text=True)
date =  (proc.stdout) 
print(('実行結果: {}'.format(date)))

