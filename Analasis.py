import DbPy as DB


raw_weath_ok = pullByWeather("OK")# all ok weather #find({"weatherSent" : "OK"})

raw_weath_good = pullByWeather("GOOD")# all good weather

raw_weath_bad = pullByWeather("BAD")#all bad weather

weath_ok_pos = [] # contains the positive tweets created during OK weather
weath_ok_neg = [] # contains the negative tweets created during OK weather
weath_ok_neu = [] # contains the neutral tweets created during OK weather
weath_ok_posneu = [] # contains the positive leaning neutral tweets created during OK weather
weath_ok_negneu = [] # contains the negative leaning neutral tweets created during OK weather

for i in raw_weath_ok:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_ok_neg.add(i)
    
    else if i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_ok_pos.add(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > '0.25':
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_ok_negneu.add(i)
        else if i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > '0.25':
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_ok_posneu.add(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_ok_neu.add(i)


weath_good_pos = [] # contains the positive tweets created during GOOD weather
weath_good_neg = [] # contains the negative tweets created during GOOD weather
weath_good_neu = [] # contains the neutral tweets created during GOOD weather
weath_good_posneu = [] # contains the positive leaning neutral tweets created during GOOD weather
weath_good_negneu = [] # contains the negative leaning neutral tweets created during GOOD weather

for i in raw_weath_good:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_good_neg.add(i)
    
    else if i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_good_pos.add(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > '0.25':
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_good_negneu.add(i)
        else if i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > '0.25':
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_good_posneu.add(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_good_neu.add(i)  


weath_bad_pos = [] # contains the positive tweets created during GOOD weather
weath_bad_neg = [] # contains the negative tweets created during GOOD weather
weath_bad_neu = [] # contains the neutral tweets created during GOOD weather
weath_bad_posneu = [] # contains the positive leaning neutral tweets created during GOOD weather
weath_bad_negneu = [] # contains the negative leaning neutral tweets created during GOOD weather

for i in raw_weath_bad:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_bad_neg.add(i)
    
    else if i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_bad_pos.add(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > '0.25':
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_bad_negneu.add(i)
        else if i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > '0.25':
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_bad_posneu.add(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_bad_neu.add(i) 

print("********OK************** \\
    \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \\
    Pos Neutral length: {3} \n Neg Neutral length: {4}" \ 
    .format(len(weath_ok_pos), len(weath_ok_neg), len(weath_ok_neu), len(weath_ok_posneu), len(weath_ok_negneu)))
    
print("\n ************************************* \n")

print("********GOOD************** \\
    \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \\
    Pos Neutral length: {3} \n Neg Neutral length: {4}" \ 
    .format(len(weath_good_pos), len(weath_good_neg), len(weath_good_neu), len(weath_good_posneu), len(weath_good_negneu)))

print("********BAD************** \\
    \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \\
    Pos Neutral length: {3} \n Neg Neutral length: {4}" \ 
    .format(len(weath_bad_pos), len(weath_bad_neg), len(weath_bad_neu), len(weath_bad_posneu), len(weath_bad_negneu)))
#weath_ok = (raw_weath_ok.find({"tweetSent" : ""}))
# set of 5 sets, each set corresponding to pos, neu, neg, posNeu, negNeu

