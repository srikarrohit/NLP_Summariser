import json
import sys
import os, sys

files=[]
files = os.listdir("../Dest_path/")
papers=[]
#files = ['paper1.tex_data.txt','paper3.tex_data.txt','paper4.tex_data.txt','paper6.tex_data.txt'
#         ,'paper11.tex_data.txt','paper12.tex_data.txt',
#         'paper13.tex_data.txt','paper14.tex_data.txt','paper15.tex_data.txt']
#files = ['1.paper.txt','3.paper.txt','4.paper.txt','6.paper.txt','12.paper.txt','13.paper.txt',
#         '14.paper.txt','15.paper.txt','16.paper.txt','17.paper.txt','18.paper.txt','19.paper.txt',
#         '20.paper.txt']

#file = sys.argv[1]
#for file in files:
train=open(file,'r+')

for line in train:
    line = line.replace("###FORMULA###","||FORMULA||")
    line = line.replace("###TABLE###","||TABLE||")
    line = line.replace("###FIGURE###","||FIGURE||")
    
    
    map=line.split('\t')
    paper=dict()
    paper['id']=map[0]
    paper['name']=map[1]
    try:
    	paper['info']=json.loads(map[2])
    except:
    	continue
    paper['sum']=map[3]
    if (len(paper['sum'])>=10):
    	papers.append(paper)


for paper in papers:
    #paper['sum']=paper['sum'].encode('utf-8')
    paper_data=""
    for key in paper['info']:
        if key == "Introduction" or key == "Conclusion":
       		for item in paper['info'][key]:
        			if isinstance(item,str):
        				paper_data+=item+" "
        			elif isinstance(item,str):
        				paper_data+=item+" "
        			elif isinstance(item,dict):
        				for innerKey in item:
        					for innerItem in item[innerKey]:
        						if (isinstance(innerItem,str)):
        							paper_data+=innerItem+" "
        						elif (isinstance(innerItem,str)):
        							paper_data+=innerItem+" "
        						elif isinstance(innerItem,dict):
        							for in_innerKey in innerItem:
        								for in_innerItem in innerItem[in_innerKey]:
        									if (isinstance(in_innerItem,str)):
        										paper_data+=in_innerItem+" "
        									elif (isinstance(in_innerItem,str)):
        										paper_data+=in_innerItem+" "

	
	#paper_data=paper_data.encode('utf-8')
    paper_data=paper_data.replace("\n"," ")
    data_input=open('./data-cat-all/sample/'+paper['id'],'w+')
    #data_model=open('./data_final/model/'+paper['id'],'w+')
    print(paper_data, file = data_input)
    #print(paper['sum'])
    #print(paper['sum'],file = data_model)
