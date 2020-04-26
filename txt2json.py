import sys,os
import codecs
import json

# input: [name].txt ,output: [name].json
# input: [folder] => folder/*.txt , output: *.json
if len(sys.argv)==2:
    input_file = sys.argv[1]
#else:
#    input_file='./mindmap/nodejs.txt'

colors = ['#fff','#3333ff','#33ff33','#ff3333','#6633ff','#33ff66','#ff6633','#9933ff','#33ff99','#ff6699']

def txt2json(file):    
    print('txt2json:%s'%file)
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
                if offset >2:                    
                    json_list.append({"id":id,"parentid":last_tab_parent[offset-1],"topic":line.strip(),"background-color":color,"expanded":False})
                else:
                    json_list.append({"id":id,"parentid":last_tab_parent[offset-1],"topic":line.strip(),"background-color":color})
    to_file=os.path.splitext(file)[0]+'.json'
    print('write to:%s'%to_file)
    with codecs.open(to_file,'w','utf-8') as f:
        json.dump(json_list,f,indent=4)

if os.path.isdir(input_file):    
    for root,dirs,files in os.walk(input_file):        
        for file in files:
            if file.endswith('.txt'):
                txt2json(os.path.join(root,file))
elif os.path.isfile(input_file):
    txt2json(input_file)
else:
    print('file not found..')