import json
import requests
import csv
def list_positions(company, skils, pos_type):
    url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json?orderBy="company"&equalTo="'+company+'"'
    print(url)
    response = requests.get(url)
    query_result = json.loads(json.dumps(response.json()))
    #print(query_result)
    position_skills_type = []
    for i in query_result:
        val = query_result[i]
        position_skills_type.append([val['skills'], val['position'], val['type']])
    print(position_skills_type[0])
    
    #filter by type:
    postion_skills = []
    for i in position_skills_type:
        if(i[2] == pos_type):
            postion_skills.append([i[0], i[1]])
    print(postion_skills[0])
    user_skils = skils.split(';')
    min_required = int(len(user_skils) * 0.8)
    position_res = []
    for i in postion_skills:
        jd_skils = i[0].split(';')
        count = 0
        for j in jd_skils:
            if j in user_skils:
                count += 1
        if(count >= min_required):
            position_res.append(i[1])
    print(position_res)

    #     position_skils.append([i['skills'], i['type'], i['position']])
    # print(position_skils[0])
    # x = json.loads(json.dumps(response.json()))
    # print(x)

    # final_list = []
     
    # term_arr = term.split(" ")
    # for i in term_arr:
    #     url = 'https://assignment-1-c008d.firebaseio.com/index/'+i+'.json'
    #     #print(url)
    #     response = requests.get(url)
    #     x = json.loads(json.dumps(response.json()))
    #     #print(x)
    #     if(x):
    #         final_list.extend(x)
    # final_set = list(set(final_list))
    # final_set = map(int, final_set)
    # print(final_set)

#list_positions('Cisco','software;management;data;security;design;product', 'Full Time')

def list_skills_words(company, pos_type, csv_file):

    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        res = list(reader)
    #print(res)
    link = ""
    for row in res:
        #print(row)
        if(row[1]==company and row[2]== pos_type):
            link = row[3]
    #print(link)
    url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json?orderBy="company"&equalTo="'+company+'"'
    #print(url)
    response = requests.get(url)
    query_result = json.loads(json.dumps(response.json()))
    #print(query_result)
    skills_words_link = []
    for i in query_result:
        val = query_result[i]
        if(val['position']==pos_type):
            print(val)
            skills_words_link.append([val['skills'], val['frequentWords'], link])
    print(skills_words_link)
    

list_skills_words('Cisco','Sr. Software Kernel Security Engineer', 'companies_shreyasi.csv')