# A basic program to make a summary of a body of text. Paragraph, essay etc.
# Not a very advanced script. This is my first summarizing algorithm.
class Summary:
    def run(self,text):
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize, sent_tokenize
        from nltk.stem import PorterStemmer



        #text = input("Enter some text : ")

        words = word_tokenize(text)
        sentences = sent_tokenize(text)
        #print (words)
        #print (sentences)

        stop_words = set(stopwords.words("english"))
        stop_words.add(".")
        stop_words.add(",")
        stop_words.add("!")
        stop_words.add("?")
        stop_words.add("I")
        for i in range(0,10):
            stop_words.add(str(i))


        ps = PorterStemmer()
        filteredwords = list()
        for word in words:
            if word not in stop_words:
                filteredwords.append(ps.stem(word))
                

        #print(filteredwords)
        word_freq={}

        for word in filteredwords:
            word = word.lower()
            if word in word_freq:
               # print ("Check : "+ word)
                word_freq[word] +=1
            else:
                word_freq[word] = 1
                
        #print(word_freq.keys())
        #print(word_freq.values())

        sentence_score={}

        for sentence in sentences:
            for word in word_freq.keys():
                if word in sentence.lower():
                    if sentence in sentence_score.keys():
                        sentence_score[sentence]+=1
                    else:
                        sentence_score[sentence]=1

        #print(sentence_score)

        sum_total = 0
        for sentence in sentences:
            sum_total += sentence_score[sentence]

        #print("Sum total : " + str(sum_total))

        average_score = int(sum_total/len(sentence_score))
        #print("Average = "+str(average_score))

        summary = ""
        #change the value have more fun!
        for sentence in sentences:
            if sentence in sentence_score.keys() and sentence_score[sentence] > 1.25 * average_score:
                summary += "<br>* "+sentence
    
        return (summary)
