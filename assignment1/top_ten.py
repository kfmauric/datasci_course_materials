import sys
import json
import uu


import sys
import json
import uu


def dprint(dstr):
    debug_flag = 0
    if (debug_flag):
        print(dstr)


def hw(tweet_fp):
    htag_scores = {}
    for line in tweet_fp:
        dprint(line)
        dprint(type(line))
        json_line = json.loads(line)
        #json_line = json_line.encode('ascii', 'ignore')
        if ('entities' in json_line):
            #print(json_line['entities'])
            if ('hashtags' in json_line['entities']):
                if json_line['entities']['hashtags']:
                    #print(json_line['entities']['hashtags'])
                    for elem in json_line['entities']['hashtags']:
                        temp=dict(elem)
                        #print temp['text'].encode('ascii', 'ignore')
                        if temp not in htag_scores.keys():
                            htag_scores[temp['text']]=1
                        #print new_scores
                        else:
                            htag_scores[temp['test']] += 1
    for word in htag_scores.keys():
        print word.encode('ascii', errors='replace'),
        print htag_scores[word]
        #else: dprint('no text')
        #print(line_score)


def lines(fp):
    print(str(len(fp.readlines())))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
