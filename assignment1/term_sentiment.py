import sys
import json
import uu


import sys
import json
import uu

#def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
#    enc = file.encoding
#    if enc == 'UTF-8':
#        print(*objects, sep=sep, end=end, file=file)
#    else:
#        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
#        print(*map(f, objects), sep=sep, end=end, file=file)

def dprint(dstr):
    debug_flag = 0
    if (debug_flag):
        print(dstr)


def hw():
    afinnfile = open(sys.argv[1])
    dprint('Hello, world!')
    scores = {} # initialize an empty dictionary
    new_scores = {}
    for line in afinnfile:
        dprint(line)
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    dprint(scores.items()) # Print every (term, score) pair in the dictionary

    tweetfile = open(sys.argv[2])
    for line in tweetfile:
        line_score = 0
        dprint(line)
        dprint(type(line))
        json_line = json.loads(line)
        #json_line = json_line.encode('ascii', 'ignore')
        dprint(json_line)
        if ('text' in json_line):
            dprint(json_line['text'].encode('ascii', 'ignore'))
            for word in json_line['text'].split((' ')):
                dprint(word.encode('ascii', 'ignore'))
                dprint('--------------------')
                if(word in scores.keys()):
                    line_score = line_score + scores[word]

            for word in json_line['text'].split((' ')):
                dprint(word.encode('ascii', 'ignore'))
                dprint('--------------------')
                if(word not in scores.keys()):
                    if word not in new_scores.keys():
                        new_scores[word] = {'pos':0, 'neg':0}
                    if line_score >0:
                        new_scores[word]['pos'] += 1
                        #print word.encode('ascii','ignore'),
                        #print line_score,
                        #print new_scores[word]
                    elif line_score < 0:
                        new_scores[word]['neg'] += 1
                        #print word.encode('ascii','ignore'),
                        #print line_score,
                        #print new_scores[word]
                    #else:
                        #print word.encode('ascii', 'ignore'),
                        #print new_scores[word]
    for word in new_scores.keys():
        if new_scores[word]['pos'] > new_scores[word]['neg']:
            sign = 1
            #mag = new_scores[word][pos]/(new_scores[word]['neg']+1)
        elif new_scores[word]['pos'] < new_scores[word]['neg']:
            sign =-1
        else: sign = 0
        print word.encode('ascii', 'ignore'),
        print sign
        #else: dprint('no text')
        #print(line_score)


def lines(fp):
    print(str(len(fp.readlines())))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
