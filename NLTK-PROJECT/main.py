#making the necessary imports
from flask import Flask,render_template,request
import nltk
import re
import heapq

    
#some helping functions
#------------------------------------------------------------------------------
def clean_the_text(unclean_text):
    unclean_text = re.sub(r'\[[0-9]*\]',' ',unclean_text)
    unclean_text = re.sub(r'\s+',' ',unclean_text)
    clean_text = unclean_text.lower()
    clean_text = re.sub(r'\W',' ',clean_text)
    clean_text = re.sub(r'\d',' ',clean_text)
    clean_text = re.sub(r'\s+',' ',clean_text)
    return clean_text

def generate_word2count(ct,sp):
    word2count = {}
    for word in nltk.word_tokenize(ct):
        if word not in sp:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1
    for key in word2count.keys():
        word2count[key] = word2count[key]/max(word2count.values())
    return word2count

def score_sentences(s,w):
    sent2score = {}
    for sentence in s:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in w.keys():
                if len(sentence.split(' ')) < 25:
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = w[word]
                    else:
                        sent2score[sentence] += w[word]
    return sent2score

def do_everything(text):    
    #take in the paragraph for summarizing
    sents = nltk.sent_tokenize(text)
    #calling the preprocessing function 
    clean_text = clean_the_text(text)
    stop_words = nltk.corpus.stopwords.words('english')
    #creating word2count table
    word2count = {}
    word2count = generate_word2count(clean_text,stop_words) 
    #give score to the sentences    
    sent2score = {}
    sent2score = score_sentences(sents,word2count)
    #summarize the text according to scored sentences and print the result
    #first approach: using average score
    average_score = sum(list(sent2score.values()))/len(list(sent2score.values()))
    best_sentences2 = heapq.nlargest(4, sent2score, key=sent2score.get)
    #for i in list(sent2score.keys()):
        #if sent2score[i] >= average_score:
            #best_sentences2.append(i)
    return best_sentences2
#------------------------------------------------------------------------------


app = Flask(__name__)
@app.route("/")
def show_main_page():
    return render_template('main.html')
@app.route("/action",methods=["POST","GET"])
def summarize():
    x = request.form["t1"]
    print(x)
    lis = []
    lis = do_everything(x)
    summary = lis[0]
    for i in range(1,len(lis)):
        summary += lis[i]
    return render_template('main.html',summary=summary)

if __name__ == '__main__':
   app.run()
    
#second approach: using heapq
best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)
print('---------------------------------------------------------')
for sentence in best_sentences2:
    print(sentence)
                    
