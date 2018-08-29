email=["ftsud@nj.com","something@gmail.com",'whyso@serious.com']
for  item in email:# 3 lines of code
    if 'gmail' in item:
        print (item)
print(*[item for item in email if 'nj' in item]) # one line of code
print(email)
##########################################################
l=[]*5
for i in range(5):
    l.append(int(input("num : ")))
print(*[l[i]+l[i+1] for i in range(4)] , sep="\n" )
print(*[l[i]+l[i+1] for i in range(4)] , sep="\t" )
