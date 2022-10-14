import sys,os
import codecs

import json

# input: [name].txt ,output: [name].json
# input: [folder] => folder/*.txt , output: *.json
if len(sys.argv)==2:
    input_file = sys.argv[1]
else:
    input_file = 'mindmap'
#else:
#    input_file='./mindmap/nodejs.txt'

colors = ['#fff','#e3aba7','#e82ad2','#0fbdff','#e3aba7','#d41dea','#01a6d5','#97d9c7','#eb6a68','#412ffc']
#colors = ['#5B8FF9', '#F6BD16', '#5AD8A6', '#945FB9', '#E86452', '#6DC8EC', '#FF99C3', '#1E9493', '#FF9845', '#5D7092'];
new_colors=[]
for _ in range(10):
    new_colors+=colors
colors=new_colors

last_id=''
def txt2json(file):    
    result_json=None
    filename=os.path.basename(file)
    title=os.path.splitext(filename)[0]
    global last_id
    #print('txt2json:%s'%file)
    with codecs.open(file,'r','utf-8') as f:
        lines = f.readlines()
        #sqrt_lines = math.sqrt(len(lines))        
        expand_limit = 4
        if len(lines)>128:
            expand_limit=1
        if len(lines)>64:
            expand_limit=2
        if len(lines)<32:
            expand_limit = 4
 
        last_tab_parent = dict()    
        result_json={
            'id':'root',
            'isroot':True,
            'title':title,
            'collapsed':False,
        }
        last_tab_parent[-1]=result_json
        for index,line in enumerate(lines):
            if len(line.strip())==0:
                continue
            line = line.rstrip()
            line = line.replace('    ',"\t")
            offset = line.count('\t')
            color = colors[offset]
            id='line_%d'%index
            parent_obj=last_tab_parent[offset-1]
            if 'children' not in parent_obj:
                parent_obj['children']=[]
            node_obj={
                "id":id,"title":line.strip(),"background-color":color,"collapsed":offset>=expand_limit
            }
            last_tab_parent[offset]=node_obj
            parent_obj['children'].append(node_obj)

    to_file=os.path.splitext(file)[0]+'.g6.json'
    print('write to:%s'%to_file)
    with codecs.open(to_file,'w','utf-8-sig') as f:
        json.dump(result_json,f,indent=4)

if os.path.isdir(input_file):    
    for root,dirs,files in os.walk(input_file):        
        for file in files:
            if file.endswith('.txt'):
                try:
                    txt2json(os.path.join(root,file))
                except Exception as ex:
                    print(file,'last_id',last_id,ex)
elif os.path.isfile(input_file):
    txt2json(input_file)
else:
    print('file not found..')