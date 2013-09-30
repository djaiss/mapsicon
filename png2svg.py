import os
import subprocess

convert = 'convert -flatten 1024.png 1024.pnm'
potrace = 'potrace -s -o vector.svg 1024.pnm'

top_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and d != '.git']

for d in top_dirs:

    sub_dirs = [s for s in os.listdir(d) if os.path.isdir(os.path.join(d, s))]

    for sub_dir in sub_dirs:
        path = os.path.join(d, sub_dir)
        subprocess.call(
            "cd {}; {}; {};".format(path, convert, potrace),
            shell=True
        )
