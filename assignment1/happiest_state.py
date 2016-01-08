import sys
import json
import uu


def dprint(dstr):
    debug_flag = 0
    if (debug_flag):
        print(dstr)


def hw(sent_fp, tweet_fp):
    #dprint('Hello, world!')
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

    states_count = {}
    inv_state = {v: k for k, v in states.items()}
    #print inv_state
    state_scores = {}
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
        # json_line = json_line.encode('ascii', 'ignore')
        dprint(json_line)
        if ('text' in json_line):
            dprint(json_line['text'].encode('ascii', 'ignore'))
            for word in json_line['text'].split(' '):
                dprint(word.encode('ascii', 'ignore'))
                dprint('--------------------')
                if (word in scores.keys()):
                    line_score = line_score + scores[word]
        else: dprint('no text')
        if ('place' in json_line):
           if (json_line['place']):
               if(json_line['place']['country_code']=="US"):
                    # print json_line['place']['full_name']
                    a,b = json_line['place']['full_name'].split(',')
                    # print a
                    # print b
                    if (b.lstrip(' ') == 'USA'):
                        cur_state = inv_state[a]
                     #   print cur_state,
                     #   print 'foo'
                    elif b.lstrip(' ') in states.keys():
                        cur_state = b.lstrip(' ')
                      #  print cur_state,
                      #  print 'boo'
                    else:
                        cur_state = 'null'
                       # print cur_state,
                       # print 'roo'
                    if cur_state in state_scores.keys():
                        state_scores[cur_state]['score'] += line_score
                        state_scores[cur_state]['tweets'] += 1
                    else:
                        state_scores[cur_state] = {'score':line_score, 'tweets':1}
    max_score=0
    max_state='null'
    for state in state_scores.keys():
        cur_score = float(state_scores[state]['score'])/state_scores[state]['tweets']
        if max_score <= cur_score:
            max_score = cur_score
            max_state = state
    print max_state,
    print max_score




def lines(fp):
    print(str(len(fp.readlines())))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()