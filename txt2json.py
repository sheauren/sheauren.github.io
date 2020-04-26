import sys,os
import codecs
import json

# input: [name].txt ,output: [name].json
# input: [folder] => folder/*.txt , output: *.json
if len(sys.argv)==2:
    input_file = sys.argv[1]

def txt2json(file):    
    print('txt2json:%s'%file)
    with codecs.open(file,'r','utf-8') as f:
        lines = f.readlines()
        json_list =[]
        last_tab_parent = dict()    
        for index,line in enumerate(lines):
            offset = line.count('\t')
            #print('[%d]offset:%d'%(index,offset))
            if offset == 0:
                last_tab_parent[0] = "root"
                json_list.append({"id":"root","isroot":True,"topic":line.strip()})
            else:
                id = "line_%d"%index
                last_tab_parent[offset]=id
                json_list.append({"id":id,"parentid":last_tab_parent[offset-1],"topic":line.strip()})
        #print('json_list',json_list)
    
    with codecs.open(os.path.splitext(file)[0]+'.json','w','utf-8') as f:
        json.dump(json_list,f,indent=4)

if os.path.isdir(input_file):
    for root,dirs,files in os.walk(input_file):
        for file in files:
            txt2json(os.path.join(root,file))
elif os.path.isfile(input_file):
    txt2json(input_file)
