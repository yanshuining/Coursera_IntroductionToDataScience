import sys
import json
import operator

def topTenHashTags(tFile):
    tweetFile = open(tFile)
    lines = tweetFile.readlines()
    hashtags = {};
    entities={};
    tags_frequency = {};
    for l in lines:
        tweets = json.loads(l)
        if ("entities" in tweets):
            entities = tweets.get("entities")
            if("hashtags" in entities):
                hashtags=entities.get("hashtags")
                
        if (len(hashtags)>0):
            #print hashtags
            for h in hashtags:
                tag_text = h.get("text")
                tag_indices = h.get("indices")
                if (tag_text in tags_frequency):
                    tags_frequency[tag_text]=int(tags_frequency.get(tag_text))+1;
                else:
                    tags_frequency[tag_text]=1;
    sorted_tags = sorted(tags_frequency.iteritems(), key=operator.itemgetter(1), reverse=True)
    top_10 = 0;
    for t in sorted_tags:
        if top_10<10:
            #frequency=sorted_tags[t]
            #print type(frequency)
            print t[0]+" "+str(t[1])
        top_10=top_10+1

def main():
    topTenHashTags(sys.argv[1])
    
    
if __name__=="__main__":
    main()