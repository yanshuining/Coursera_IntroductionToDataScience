import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

                
def ScoreSentiment(text, sentiment):
    words = text.split(" ")
    sent_score=0
    for w in words:
        if (w.lower() in sentiment):
            score = sentiment.get(w.lower())
        else:
            score = 0
        sent_score+=score
    return sent_score
            
            
def readSentFile(sf):
    afinnfile = open(sf);
    scores = {} #initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t") #the file is tab-delimited.
	scores[term] = int(score) #convert the score to an integer
    #print scores.items();
    return scores;



def TermScore(tf, sf):
    sentiment = readSentFile(sf);
    line = open(tf).readlines();
    term_score={};
    
    for l in line:
        tweets = json.loads(l);
        if ("entities" in tweets):
            text_score = ScoreSentiment(tweets.get("text"), sentiment)
            tweets["score"] = text_score;
            '''if (text_score!=0):
                print (tweets.get("text")," with Sentiment score =",tweets.get("score"))
            else:
                print (tweets.get("text"), ":",tweets.get("score"));'''
            if (text_score!=0):
                UpdateTermScore(tweets.get("text"), sentiment, text_score, term_score);   
    for t in term_score:
        score = float(term_score.get(t)[0])/float(term_score.get(t)[1])
        term_score.get(t).append(score)
        print t + " " + str(term_score.get(t)[2]) #+ " " + str(term_score.get(t)[1])
        

def UpdateTermScore(line, sentiment, text_score, term_score):
    words = line.split(" ");
    for w in words:
        if (w.lower() not in sentiment):
            if(w.lower() not in term_score):
                term = [text_score, 1]
                #print term
                term_score[w.lower()] = term;
                #print term_score.get(w.lower())
            else:
                term = term_score.get(w.lower())
                #print term_score.get(w.lower())
                term = [term[0]+text_score, term[1]+1]
                term_score[w.lower()] = term
                
               

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    TermScore(sys.argv[2], sys.argv[1])

if __name__ == '__main__':
    main()
