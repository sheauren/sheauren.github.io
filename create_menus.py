import os
import json

target_path = './mindmap'
parent_node=dict()
parent_node[target_path]=[]
root_count=0
folder_count=0
leaf_count=0

for root,dirs,files in os.walk(target_path):
    for dirname in dirs:
        if root==target_path:
            root_count+=1 
            key=f'root-{root_count}'                  
        else:
            folder_count+=1
            key=f'folder-{folder_count}'
        dir_path = os.path.join(root,dirname)
        dirobj={
            'title':dirname,
            'key':key,
            'children':[],
            'selectable':False,
            'isLeaf':False
        }
        parent_node[dir_path]=dirobj['children']
        parent_node[root].append(dirobj)

for root,dirs,files in os.walk(target_path):
    for file in files:
        if not file.endswith('.g6.json'):
            continue
        leaf_count+=1
        title=os.path.splitext(os.path.basename(file))[0].replace('.g6','')
        data=os.path.join(root,file).replace('\\','/',10)
        parent_node[root].append({
            'title':title,
            'key':f'leaf-{leaf_count}',
            'data':data,
            'selectable':True,
            'isLeaf':True,
            'nav':data.replace(target_path+'/','').replace('.g6.json','').split('/')
        })

with open('menu.json','w',encoding='utf-8-sig') as f:
    json.dump(parent_node[target_path],f,indent=4)