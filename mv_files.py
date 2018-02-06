import shutil
import glob
import os

src = '/home/nil/Desktop/TruthMask/'
dst = '/home/nil/Desktop/Masks/'
a=2304

if not os.path.exists(dst):
    os.makedirs(dst)

for (subdirs, algo, images) in os.walk(src):
    if not subdirs.startswith('.'):
        for subdir in os.walk(subdirs):
            print subdir
            for img in images:
                if not img.startswith('.'):
                    old_file = os.path.join(src,subdir[0],img)
                    print('Old:   ' + old_file)
                    new_file = os.path.join(dst, str(a)+'.png')
                    print ('New:   ' + new_file)
                    shutil.move(old_file,new_file)
                    a+=1