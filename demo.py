from flask import Flask,request,send_from_directory
import os
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])

def home():
    #print()
    from nltk.tokenize import word_tokenize
    from nltk.tokenize import RegexpTokenizer
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
    tokenized_text=word_tokenize(teststr)
    
    '''modified_token_list=str([word for word in tokenized_para if not word in to_be_removed])
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    punctuated_para = tokenizer.tokenize(modified_token_list)
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    to_be_removed = set(stopwords.words('english'))
    tokenized_para=str(word_tokenize(teststr))'''


    teststr = " ".join(tokenized_text)
    import nltk
    nltk.download('punkt')

    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    punctuated_para = tokenizer.tokenize(teststr)
    #teststr= " ".join(punctuated_para)

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    to_be_removed = set(stopwords.words('english'))
    modified_token_list=[word for word in punctuated_para if not word in to_be_removed]



    from nltk.stem import WordNetLemmatizer
    lemmatizer=WordNetLemmatizer()

    lemmatized_words = [lemmatizer.lemmatize(i) for i in modified_token_list] 

    badwords=[]

    with open('D:/python/Words.txt','r',encoding="utf8") as file:
   
        for line in file:
       
            # reading each word        
            for word in line.split():   
                badwords.append(word) 
        result=[word for word in lemmatized_words if word in badwords]
    return " hello mega"

    
    
    
if __name__ == '__main__':
    app.run(debug=True)
