from flask import Flask,request,send_from_directory
import os
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
    
def home():

    teststr="hello! Mr Barath Nithish you are a, \"fuc.ker\" bastard "
    li=list(teststr.split())
    print(li)
    li2=[]
    string=''
    for i in li:
        li3=[]
        for j in i:
            if j.isalpha():
               j=j.lower()
               print(j,sep=' ')
               li3.append(j)
        li3="".join(li3)
        li2.append(li3)
    print(li2)
    sentence=" ".join(li2)
    badwords=[]

    with open('D:/python/Words.txt','r',encoding="utf8") as file:
   
        for line in file:
       
            # reading each word        
            for word in line.split():   
                badwords.append(word) 
        result=[word for word in sentence if word in badwords]
    return " ".join(result)

    
    
    
if __name__ == '__main__':
    app.run(debug=True)
