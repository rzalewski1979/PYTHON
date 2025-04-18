import os
import subprocess

lista=os.listdir()
print(lista)
x=subprocess.run(['ls','-1','|','wc','-l'])
print(x)
