from flask import Flask, render_template,request, redirect, url_for
import json
import random
import requests
import os
app = Flask(__name__)



@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/searchJobs')
def hello_world():
    print("Request arguments: ", request.args)
    request_args = request.args
    print("Printed after being converted to dict: ", request_args)
    company = request_args["company_par"]
    pos_type = request_args["pos_type_par"]
    skils = request_args["skills_par"]
    # print "compant name: ", company
    # print "pos type: ", pos_type
    # print "skils: ", skils
    #company, skils, pos_type = 'Cisco','software;management;data;security;design;product', 'Full Time'

    url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json?orderBy="company"&equalTo="'+company+'"'
    #url = 'https://skillsmatch-820bf.firebaseio.com/companies.json?orderBy="company"&equalTo="'+company+'"'
    print(url)
    response = requests.get(url)
    query_result = json.loads(json.dumps(response.json()))
    #print(query_result)
    position_skills_type = []
    for i in query_result:
        val = query_result[i]
        position_skills_type.append([val['skills'], val['position'], val['type']])
    d = {}
    if(len(position_skills_type )== 0):
        d['jobs'] = ['No jobs found mactching your skills!! Please try another company']
        res = json.dumps(d)
        return res
    print(position_skills_type[0])
    
    #filter by type:
    postion_skills = []
    for i in position_skills_type:
        if(i[2] == pos_type):
            postion_skills.append([i[0], i[1]])
    print(postion_skills[0])
    user_skils = list(map(lambda x: x.lower(), skils.split(';')))
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
    # res = ' '.join(position_res)
    d = {}
    d['jobs'] = position_res
    res = json.dumps(d)
    return res


    

@app.route('/redirectToNewPage')
def render_second_page():
    # #print("dhhfhhh")
    print("Request arguments: ", request.args)
    request_args = request.args
    print("Printed after being converted to dict: ", request_args)
    company = request_args["company_par"]
    position = request_args["position_par"]
    # print "compant name: ", company
    # print "pos type: ", position 
    # # print "skils: ", skils
    #print("dd")
    url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json?orderBy="company"&equalTo="'+company+'"'
    print(url)
    response = requests.get(url)
    query_result = json.loads(json.dumps(response.json()))
    print(query_result)
    skills_words = []
    for i in query_result:
        #print(query_result[i])
        val = query_result[i]
        if(val['position'] == position):
            skills_words.append([val['frequentWords'], val['type'], val['skills'], val['url'], val['pdfURL']])

    
    # if(len( skills_words) == 0):
    #     skills_words = ['experience;product;collaboration;innovation;solutions','Full Time','Design;Java;Python;DevOps;Management']
    print("Values: ", skills_words)
    type_pos = 'Full Time'
    type_pos = skills_words[0][1]
    skills_vals = skills_words[0][2].split(';')
    link = skills_words[0][3]
    pdf_link = skills_words[0][4]
    print('skill_vals: ', skills_vals)
    random.shuffle(skills_vals)
    skill1 = 'System Design'
    skill2 = 'Java'
    skill3 = 'Python'
    skill4 = 'DevOps'
    skill5 = 'Management'
    if(len(skills_vals) >= 5):
        skill1 = skills_vals[0]
        skill2 = skills_vals[1]
        skill3 = skills_vals[2]
        skill4 = skills_vals[3]
        skill5 = skills_vals[4]
    elif(len(skills_vals) == 4):
        skill1 = skills_vals[0]
        skill2 = skills_vals[1]
        skill3 = skills_vals[2]
        skill4 = skills_vals[3]
    elif(len(skills_vals) == 3):
        skill1 = skills_vals[0]
        skill2 = skills_vals[1]
        skill3 = skills_vals[2]
    elif(len(skills_vals) == 2):
        skill1 = skills_vals[0]
        skill2 = skills_vals[1]
    elif(len(skills_vals) == 1):
        skill1 = skills_vals[0]
    if(skill1 == 'learning' or skill1 == 'machine'):
        skill1 = 'Machine Learning'
    if(skill2 == 'learning' or skill2 == 'machine'):
        skill2 = 'Machine Learning'
    if(skill3 == 'learning' or skill2 == 'machine'):
        skill3 = 'Machine Learning'
    if(skill4 == 'learning' or skill4 == 'machine'):
        skill4 = 'Machine Learning'
    if(skill5 == 'learning' or skill5 == 'machine'):
        skill5 = 'Machine Learning'
        
        

    freq_vals = skills_words[0][0].split(';')
    freq_temp_vals = ['experience', 'product', 'collaboration', 'innovation', 'solutions', 'design', 'simplicity', 'development']
    random.shuffle(freq_temp_vals)
    freq_temp_vals = freq_temp_vals[:5]
    freq1 = freq_temp_vals[0]
    freq2 = freq_temp_vals[1]
    freq3 = freq_temp_vals[2]
    freq4 = freq_temp_vals[3]
    freq5 = freq_temp_vals[4]

    if(len(freq_vals) == 5):
        freq1 = freq_vals[0]
        freq2 = freq_vals[1]
        freq3 = freq_vals[2]
        freq4 = freq_vals[3]
        freq5 = freq_vals[4]
    elif(len(freq_vals) == 4):
        freq1 = freq_vals[0]
        freq2 = freq_vals[1]
        freq3 = freq_vals[2]
        freq4 = freq_vals[3]
    elif(len(freq_vals) == 3):
        freq1 = freq_vals[0]
        freq2 = freq_vals[1]
        freq3 = freq_vals[2]
    elif(len(freq_vals) == 2):
        freq1 = freq_vals[0]
        freq2 = freq_vals[1]
    else:
        freq1 = freq_vals[0]






    return render_template('jobs.html', company=company, position=position, type_pos = type_pos, skill1=skill1, 
    skill2=skill2, skill3=skill3, skill4=skill4, skill5=skill5, word1=freq1, word2 = freq2, word3=freq3, word4=freq4, word5=freq5, link=link, pdfLink=pdf_link)
    #return "hejehh"
    
if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000)) 
   app.run(host='0.0.0.0', port=port, debug=True)  