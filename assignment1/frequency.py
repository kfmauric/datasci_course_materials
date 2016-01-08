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


def hw(tweetfile):
    new_scores = {}

    for line in tweetfile:
        line_score = 0
        dprint(line)
        dprint(type(line))
        json_line = json.loads(line)
        #json_line = json_line.encode('ascii', 'ignore')
        dprint(json_line)
        if ('text' in json_line):
            dprint(json_line['text'].encode('ascii', 'ignore'))
            #for word in json_line['text'].split((' ')):
            #    dprint(word.encode('ascii', 'ignore'))
            #    dprint('--------------------')
            #    if(word in scores.keys()):
            #        line_score = line_score + scores[word]

            for word in json_line['text'].split((' ')):
                dprint(word.encode('ascii', 'ignore'))
                dprint('--------------------')
                if word not in new_scores.keys():
                    new_scores[word] = 1
                    #print new_scores
                else:
                    new_scores[word] += 1
    total = 0
    for word in new_scores.keys():
        total += new_scores[word]
    for word in new_scores.keys():
        print word.encode('ascii', errors='replace'),
        print float(new_scores[word])/total
        #else: dprint('no text')
        #print(line_score)


def lines(fp):
    print(str(len(fp.readlines())))

def main():
    sent_file = open(sys.argv[1])
    hw(sent_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
