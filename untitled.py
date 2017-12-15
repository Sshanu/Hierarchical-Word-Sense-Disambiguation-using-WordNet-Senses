from bs4 import BeautifulSoup
import pickle

with open('./dataset/SemCor+OMSTI/semcor+omsti.data.xml', 'r') as f:
    soup = BeautifulSoup(f, 'xml')
    
train = []
count = 0
for sentence in soup.find_all('sentence'):
    count+=1
    print(count)
    temp_sent = []
    temp_sent.append(sentence.get('id'))
    
    string = sentence.text.strip('\n').split('\n')
    temp_sent.append(string)
    
    list_ = sentence.contents
    id_list = []
    lemma_list = []
    pos_list = []
    for i in range(1,len(list_),2):
        id_list.append(list_[i].get('id'))
        lemma_list.append(list_[i].get('lemma'))
        pos_list.append(list_[i].get('pos'))
    temp_sent.extend([id_list, lemma_list, pos_list])
    train.append(temp_sent)
    
with open('one_million', 'wb') as f:
    pickle.dump(train, f)

del train,soup