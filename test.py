import pandas as pd

l=[['Pepsi', 1, 65], ['Tomato', 1, 50], ['Tomato', 1, 50], ['Coffee', 1, 500], ['Coffee', 1, 500], ['Coffee', 1, 500], ['Coffee', 1, 500], ['Coffee', 1, 500]]
w=dict()
b=[]
upd_list = list()
temp=list()

for i in l:
    if i not in upd_list:
        upd_list.append(i)
    else:
        for w in upd_list:
            if w==i:
                w[1]+=1
l[0][1]=3
print(upd_list)


    
for i in upd_list:
    i.append(i[1]*i[2])

print(upd_list)
    
df=pd.DataFrame(upd_list,columns=['Items','Quantity','Price','Total'])

df.index+=1

print(df)

