
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


r=requests.get("https://pagalworld.org/")
soup=BeautifulSoup(r.content, "html.parser")


# In[4]:


latestupdates = soup.find_all("li",{"class":"tnned"})


# In[5]:


print("LATEST UPDATES\n-----------------")
for c,albums in enumerate(latestupdates):
    print(c,albums.find("h3").text,sep="\t")


# In[6]:


ch = int(input("Enter the number of album  : "))
print("You Have chosen : {} {}".format(ch, latestupdates[ch].find("h3").text))


# In[7]:


dlpage=requests.get(latestupdates[ch].find("a")["href"])
soupdl=BeautifulSoup(dlpage.content, "html.parser")


# In[12]:


print(latestupdates[ch].find("h3").text+"\n----------------")
ziplinks = soupdl.find_all("a",{"class":"dbutton"})
songlinks = soupdl.find_all("div",{"class":"listbox"})
songlinks[0].find("a")["href"]


# In[ ]:


c=0
for zipfile in ziplinks:
    print(c,zipfile.find("span").text,sep="\t")
    c+=1
for songfile in songlinks:
    print(c,songfile.find("h2").text,sep="\t")
    c+=1


# In[ ]:


ch=int(input("Select a file to download : "))
if(ch==0 or ch==1):
    location= input("Enter Directory : ")
    with open(location+"\\"+str(ziplinks[ch]["title"])+".zip",'wb') as f:
        obj = requests.get(ziplinks[ch]["href"])
        f.write(obj.content)
else:
    songdlpage=requests.get("https://pagalworld.org"+songlinks[(ch-2)].find("a")["href"])
    soupdl =BeautifulSoup(songdlpage.content,"html.parser")
    songdllinks=soupdl.find_all("a",{"class":"dbutton"})
    for c,link in enumerate(songdllinks):
        print(c,link.find("span").text,sep="\t")
    ch=int(input("Choose a file : "))
    location= input("Enter Direcotory : ")
    with open(location+"\\"+str(songdllinks[ch]["title"])+".mp3",'wb') as f:
        obj = requests.get(songdllinks[ch]["href"])
        f.write(obj.content)
