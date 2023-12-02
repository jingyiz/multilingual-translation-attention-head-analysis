import sys
def mread(file):
    return open(file,'r',encoding='UTF8').readlines()             
ls=mread(sys.argv[1])
lt=mread(sys.argv[2])
lv=mread(sys.argv[3])
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def mplot(dict,tt,d):
    sns.set()
    df = pd.DataFrame(dict, index =tt)
    ax = sns.heatmap(df,xticklabels=True,yticklabels=True)
    plt.savefig(d+'.png')    
    plt.clf()
def mmax3(vv,tt,ss,dict):
    toks=vv.strip().replace('[','').replace(']','').replace(',','').split(' ')
    if len(toks)!=len(tt):exit(1)    
    for i in range(len(toks)):
        toks[i]=float(toks[i])
    dict[ss]=toks                  
def mprint(ss,tt,att, idx,d):
    ones=att[idx].split('], [')   
    gates=att[idx+1].strip().replace('[','').replace(']','').replace(',','').split(' ') 
    if len(gates)!=8:exit(1)
    k=-1
    for i in range(8):
        dict={}
        for j in range(len(ss)):
            k+=1
            if float(gates[i])!=0:    mmax3(ones[k],tt,ss[j],dict)           
        if float(gates[i])!=0:mplot(dict,tt,d+str(i))    
kkk=0
for i in range(len(ls)):
   src=['bos']+ls[i].strip().split(' ')+['eos']
   for j in range(len(src)):src[j]=src[j]+'_'+str(j)   
   tgt=['bos']+lt[i].strip().split(' ')
   for j in range(len(tgt)):tgt[j]=tgt[j]+'_'+str(j)
   for j in range(6):       
       if i==398:mprint(src,src,lv, kkk,'sslayer'+str(j))
       kkk+=2
   for j in range(6):       
       if i==398:mprint(tgt,tgt,lv, kkk,'ttlayer'+str(j))
       kkk+=2      
       if i==398:mprint(tgt,src,lv, kkk,'tslayer'+str(j))
       kkk+=2
