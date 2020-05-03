import sys,os
import codecs
import math
import json

file='./json_list.txt'

def txt2html(file):    
    print('txt2html:%s'%file)
    with codecs.open(file,'r','utf-8') as f:
        lines = f.readlines()        
        json_list =[]
        last_tab_parent = dict()    
        for index,line in enumerate(lines):
            line = line.rstrip()
            line = line.replace('    ',"\t")
            offset = line.count('\t')
            color = colors[offset]
            if offset == 0:
                last_tab_parent[0] = "root"
                json_list.append({"id":"root","isroot":True,"topic":line.strip()})
            else:
                id = "line_%d"%index
                last_tab_parent[offset]=id
                if offset >expand_limit:                    
                    json_list.append({"id":id,"parentid":last_tab_parent[offset-1],"topic":line.strip(),"background-color":color,"expanded":False})
                else:
                    json_list.append({"id":id,"parentid":last_tab_parent[offset-1],"topic":line.strip(),"background-color":color})
    to_file=os.path.splitext(file)[0]+'.json'
    print('write to:%s'%to_file)
    with codecs.open(to_file,'w','utf-8') as f:
        json.dump(json_list,f,indent=4)

txt2html(file)