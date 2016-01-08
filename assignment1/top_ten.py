import sys
import json
import uu


def dprint(dstr):
    debug_flag = 0
    if (debug_flag):
        print(dstr)


def hw(sent_fp, tweet_fp):
    dprint('Hello, world!')
    scores = {} # initialize an empty dictionary
    for line in sent_fp:
        dprint(line)
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    dprint(scores.items()) # Print every (term, score) pair in the dictionary


    for line in tweet_fp:
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
        print
        print(line_score)


def lines(fp):
    print(str(len(fp.readlines())))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()