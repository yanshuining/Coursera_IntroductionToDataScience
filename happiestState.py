import sys
import json


def TweetsScore(line, sentiment):
    tweets = json.loads(line)
    text_score=0
    if ("entities" in tweets):
        if (tweets.get("lang")=="en"):
            ''' print ("language="+tweets.get("lang"))
            print (tweets.get("text"))'''
        text_score = ScoreSentiment(tweets.get("text"), sentiment)
        tweets["score"] = text_score
        '''if (text_score!=0):
            print (tweets.get("text")," with Sentiment score =",tweets.get("score"))
            print tweets.get("score")'''
    return text_score          
                
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
    scores = {} #initialize an empty dictionary
    for line in sf:
        term, score = line.split("\t") #the file is tab-delimited.
	scores[term] = int(score) #convert the score to an integer
    #print scores.items();
    return scores;


def GetStateName(line):
    tweets = json.loads(line);
    state_name="N/A"
    if ("text" in tweets):
        if(tweets.get("lang")=="en"):
            text = tweets.get("text")
            
        if ("place" in tweets):
            if(tweets.get("place")!=None):
                place = tweets.get("place")
                if ("country_code" in place and place.get("country_code")!=None):
                    country = place.get("country_code")     
                    #print country
                if ("place_type" in place and place.get("place_type")!=None):
                    place_type = place.get("place_type")  
                    #print place_type      
                if ("city" in place and place.get("city")!=None):
                    city = place.get("city")    
                    # print city 
                if ("full_name" in place and place.get("full_name")!=None):   
                    place_full_name = place.get("full_name")
                    #print place_full_name 
                if (place_full_name!=None and country=="US"):
                    state = place_full_name.split(",")
                    state[1]=state[1][1:]     
                    
                    if (state[1]=="USA"):           
                        state_name = Abbreviations(state[0])
                    else:
                        state_name = state[1]
                    #print "state_name="+state_name
    return state_name
        
      

def happiestState(tweetFile, sentiFile):
    tf = open(tweetFile);
    sentiFile = open(sentiFile)    
    sentiment = readSentFile(sentiFile)
    lines = tf.readlines();
    #print Abbreviations("Florida")
    maxScore = -9999;
    maxScore_state = "";
    
    for l in lines:
        tweets = json.loads(l)
        if ("text" in tweets and "place" in tweets):
            score = TweetsScore(l, sentiment)
            state = GetStateName(l)
            
            if (state!="N/A" and score is not None):
                #print state
                #print score
                if (score>=maxScore):
                    #print tweets.get("text"),tweets.get("place")
                    maxScore = score
                    maxScore_state = state
    
    '''print "maxScore_state", maxScore_state
    print "maxScore", maxScore'''
    print maxScore_state," ", maxScore
                  
                        
def Abbreviations(state_full_name):    
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    
    return states.keys()[states.values().index(state_full_name)]
            
def main():
    happiestState(sys.argv[2], sys.argv[1])
    
    #tweet = "C:\Users\wwang\Google Drive\Coursera-DataScienctTool\output.txt"
    #senti = "C:\Users\wwang\Google Drive\Coursera-DataScienctTool\AFINN-111.txt"
    #happiestState(tweet, senti)
    
if __name__=="__main__":
    main()