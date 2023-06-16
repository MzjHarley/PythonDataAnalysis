import jieba

print("----------------精确模式-----------------------")
sentence = '这是一件有意义的事情'
wordlist = jieba.cut(sentence) # return object
wordlist2 = jieba.lcut(sentence) #retuan word list
print(wordlist,"\n",wordlist2,"\n",list(wordlist))
print("---------------------------------------------")

print("----------------全模式模式-----------------------")
sentence = '这是一件有意义的事情'
wordlist = jieba.cut(sentence,cut_all=True) # return object
wordlist2 = jieba.lcut(sentence,cut_all=True) #retuan word list
print(wordlist,"\n",wordlist2,"\n",list(wordlist))
print("-----------------------------------------------")

print("----------------搜索引擎模式-----------------------")
sentence = '这是一件有意义的事情'
wordlist = jieba.cut_for_search(sentence) # return object
print(list(wordlist))
print("-----------------------------------------------")