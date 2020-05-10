import shutil
import sys,os
import codecs

ref_path = r'mindmap/english/龍飛虎/16.txt'
to_path = r'mindmap/english/龍飛虎'
for i in range(17,70):
    target_file = os.path.join(to_path,'%02d.txt'%i)
    print(ref_path,'->',target_file)
    shutil.copy(ref_path,target_file)
