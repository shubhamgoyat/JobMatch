import json

import requests

def retrive():
    company = 'Cisco'
    
    url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json?orderBy="company"&equalTo="'+company+'"'
    print(url)
    response = requests.get(url)
    query_result = json.loads(json.dumps(response.json()))
    #print(query_result)
    skills_words = []
    for i in query_result:
        #print(query_result[i])
        val = query_result[i]
        if(val['position'] == 'Software Engineer -C Programming/Multithreading'):
            skills_words.append([val['frequentWords'], val['type'], val['skills']])
    print(skills_words)
    return skills_words

retrive()