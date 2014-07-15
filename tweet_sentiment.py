import sys
import json;


def hw():
    print 'Hello, world!'

def lines(fp):
    length = len(fp.readlines())
    print str(length)
    return length
    
def TweetsScore(tf, sf):
    
    sentiment = readSentFile(sf)
    line = open(tf).readlines()
    for l in line:
        tweets = json.loads(l)
        if ("entities" in tweets):
            if (tweets.get("lang")=="en"):
               ''' print ("language="+tweets.get("lang"))
                print (tweets.get("text"))'''
            text_score = ScoreSentiment(tweets.get("text"), sentiment)
            tweets["score"] = text_score
            if (text_score!=0):
                #print (tweets.get("text")," with Sentiment score =",tweets.get("score"))
                print tweets.get("score")
                
                
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


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    TweetsScore(sys.argv[2], sys.argv[1])

if __name__ == '__main__':
    main()

        
