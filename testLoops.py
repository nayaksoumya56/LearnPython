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
def login():
    i='1'
    while(i!='4'):
        i=input("\n1: Home    2: MyProfile    3:ContactUs     4: LogOut\n")
        if(i=='1'):
            print("\n------------\nWelcome to Home!\n")
        else:
            if(i=='2'):
                print("\n-------------\nMyProfile\n")
                print("Name: xyz\nID: 123\nProject: Python")
            else:
                if(i=='3'):
                    print("\n-------------\nthanks for support!\nPh: +1-123-123123\nemail:support@123.co\n")
                else:
                    if(i=='4'):
                        print("\nLogging out!\n")
                    else:
                        print("\nWrong/Invalid input. Try again!\n")

pwd=''
while(pwd!='taopypy'):
    pwd=input("Enter pwd =  ")
    if(pwd=='taopypy'):
        print("Logged in!")
        login()
    else:
        print("try again!")
print("----EXIT----")
