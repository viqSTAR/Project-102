import shutil
import os

from_dir = 'C:/Users/vikas/OneDrive/Desktop/Pro102/Mover.py'
to_dir = 'C:/Users/vikas/OneDrive/Desktop/Pro102/Move'
file_name = 'New Text Document.txt'

src = os.path.join(from_dir, file_name)
dst = os.path.join(to_dir, file_name)

shutil.move(src, dst)
