import os

from flask import Flask, render_template, request

from nltk import word_tokenize, PorterStemmer, RegexpTokenizer
from nltk.corpus import stopwords

#nltk.download()
app = Flask(__name__)

ps = PorterStemmer()

app.config['SECRET_KEY'] = 'priyaxyz'


def CleaningProcess():
    path = "static/"
    dirs = os.listdir(path)
    # This would print all the files and directories
    for file in dirs:
        print(file)

        token = RegexpTokenizer(r'\w+')

        print("dirs >>>>>>>>>>>>>>> ", dirs)

        files = open("static/"+file, encoding="utf8")
        write_file_path = 'new/{}'.format(file)
        #Lines = files.readlines()
        #print(Lines)
        for a in files:
                a=a.lower()
                t1 = token.tokenize(a)
                filtered_words = [w for w in t1 if not w in stopwords.words('english')]
                a1 = " ".join(filtered_words)
                a = a1.replace("q1q1s1", "\n")

                writeFile = open(write_file_path, 'a', encoding="utf8")
                writeFile.write(a+ "\n")
                writeFile.close()
    files.close()





@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/SearchByWord", methods=['POST','GET'])
def SearchByWord():
             file_name=list()
             line_no=list()
             line_hv_wrd=list()
             word_pos=list()
             if request.method=='POST':
                 w=str(request.form['w'])
                 path="new/"
                 dirs=os.listdir(path)

                 for files in dirs:
                     file = open('new/{}'.format(files), encoding="utf8")

                     cntline = 0
                     for line in file:
                         cntline=cntline+1
                         if w in line:
                             wpos=0
                             woffset=line.strip().split(' ')
                             for offset in woffset:

                                 wpos = wpos + 1
                                 if offset==w:

                                     line_no.append(cntline)
                                     word_pos.append(wpos)
                                     line_hv_wrd.append(line)
                                     file_name.append(files.split('.')[0])
                                 else:
                                     continue
                     file.close()
                 allList=zip(file_name,line_hv_wrd,line_no,word_pos)
                 return render_template('SearchByWord.html', all_list=allList, word=w)

             else:
                 return render_template('SearchByWord.html')

@app.route("/SearchByCombination", methods=['POST','GET'])
def SearchByCombination():
             file_name=list()
             line_no=list()
             line_hv_wrd=list()

             if request.method=='POST':
                 c=str(request.form['c'])
                 path="static/"
                 dirs=os.listdir(path)

                 for files in dirs:
                     file=open("static/"+files,encoding="utf8")
                     print(files)
                     #print(file)
                     cntline = 0
                     for line in file:
                         cntline=cntline+1
                         if c in line:
                                     line_no.append(cntline)
                                     line_hv_wrd.append(line)
                                     file_name.append(files.split('.')[0])

                     file.close()
                 allList=zip(file_name,line_hv_wrd,line_no)
                 return render_template('SearchByCombination.html', all_list=allList, c=c)
             else:
                 return render_template('SearchByCombination.html')


if __name__ == '__main__':
    #CleaningProcess()
    app.run(debug=True,port=5001)