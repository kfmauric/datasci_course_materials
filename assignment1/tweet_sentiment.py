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
                if(word in scores.keys() and word != ""):
                    line_score = line_score + scores[word]
        else: dprint('no text')
        print(line_score)


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
