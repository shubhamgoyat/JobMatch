import os
import string
def search_frequentwords(dir_name, file_name):
    frequentwords = ['python', 'c', 'java', 'numpy', 'software', 'management', 'computer', 'computer engineering', 'data', 'machine', 'learning', 
    'apache','spark', 'big', 'opertaing', 'systems', 'networks', 'ios', 'full', 'stack', 'html', 'html5', 'css', 'javascript', 'php', 'sql', 'postgressql', 
    'react', 'spring', 'hadoop', 'hive', 'hbase', 'scala', 'agile', 'algorithms', 'structures', 'security', 'statistics', 'ui', 'ux', 'design', 'development'
    'research','product','forensic','Analytics','Senior','Associate','Engineer','Information','Manager','Release','Delivery','Investigative','responsible'
    ,'customers','experts','key','hardware','deliverables','integration','product', 'services', 'innovation', 'innovative', 'delevolpment', 'community'
    'embedded','familiarity','programming','skills','qualification','communication','expertise','validation']
    ext = file_name.split('.')[1] #check if it is text file
    #print(ext)
    jd_skills = []
    if(ext == 'txt'):
        f = open(dir_name+'/'+file_name, 'r')
        content = f.readlines()
        nl = []
        for line in content:
            line = line.strip()
            words_lines = line.split(' ')
            words_lines = list(map(lambda x:x.lower(),words_lines))
            for s in words_lines:
                s = s.replace(" ", "")
                for char in string.punctuation:
                    s = s.replace(char, ' ')
                nl.extend(s.split(' '))
        dict1={}
        for i in frequentwords:
            ##dict1={}
            if(i in nl):
                if i in dict1:
                    dict1[i]+=1
                else:
                    dict1[i]=1
        print(dict1)
        maxvalue=0
        for p in dict1:
            if dict1[p]>maxvalue:
                maxvalue = dict1[p]
        result=[]
        ##print(maxvalue)
        for l in dict1:
            if dict1[l]==maxvalue:
                ##print(l)
                result.append(l)
        #print(result)
        return result

def iterate(dir_name):
    files = os.listdir(dir_name)
    #print(files)
    for my_file in files:
        search_frequentwords(dir_name, my_file)
    #search_skills(dir_name, files[3])

iterate('text_part1')
#iterate(r'C:\Users\UMA\Desktop\text_files')