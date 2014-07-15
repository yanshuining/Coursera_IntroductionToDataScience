import sys
import json

def frequency (tf):
    f = open(tf)
    line = f.readlines();
    frequency = {};
    term_count = 0;
    for l in line:
        tweets = json.loads(l);
        if ("entities" in tweets):
            text = tweets.get("text");
            words = text.split(" ");
            for w in words:
                if(w.lower() not in frequency):
                    frequency[w.lower()] = 1;
                else:
                    frequency[w.lower()] = frequency.get(w.lower())+1
                term_count = term_count + 1;
    for f in frequency:
        frequency[f] = float(frequency.get(f))/float(term_count);
        print f+"\t"+str(frequency.get(f));
    
    #print "term_count="+str(term_count)
    
    
def main():
    tweet_file = open(sys.argv[1])
    frequency(sys.argv[1])

if __name__ == '__main__':
    main()