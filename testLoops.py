# email=["ftsud@nj.com","something@gmail.com",'whyso@serious.com']
# for  item in email:# 3 lines of code
#     if 'gmail' in item:
#         print (item)
# print(*[item for item in email if 'nj' in item]) # one line of code
# print(email)
# ##########################################################
# # l=[]*5
# # for i in range(5):
# #     l.append(int(input("num : ")))
# # print(*[l[i]+l[i+1] for i in range(4)] , sep="\n" )
# # print(*[l[i]+l[i+1] for i in range(4)] , sep="\t" )

pwd=''
while(pwd!='taopypy'):
    pwd=input("Enter pwd =  ")
    if(pwd=='taopypy'):
        print("Logged in!")
        login()
    else:
        print("try again!")

def login():
    i=1
    while(i!=4):
        i=int(input("1: Home    2: MyProfile    3:ContactUs     4: Quit"))
        if(i==1):
        if(i==2):
        if(i==3):
        if(i<1 and i>4):
            print("Wrong/Invalid input. Try again!")
