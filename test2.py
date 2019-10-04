l=[['Pepsi', 1, 65], ['Tomato', 1, 50], ['Tomato', 1, 50], ['Coffee', 1, 500], ['Coffee', 1, 500], ['Coffee', 1, 500], ['Coffee', 1, 500], ['Coffee', 1, 500]]
count=0
upd_list=[]
for i in l:
    a=i[0]
    for z in l:
        if a==z[0]:
            count+=1
    i[1]=count
    count=0

for i in l:
    if i not in upd_list:
        upd_list.append(i)


        

print(upd_list)