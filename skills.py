import os
import string
def search_skills(dir_name, file_name):
    skills = ['python', 'c', 'java', 'numpy', 'software', 'management', 'computer', 'computer engineering', 'data', 'machine', 'learning', 
    'apache','spark', 'big', 'opertaing', 'systems', 'networks', 'ios', 'full', 'stack', 'html', 'html5', 'css', 'javascript', 'php', 'sql', 'postgressql', 
    'react', 'spring', 'hadoop', 'hive', 'hbase', 'scala', 'agile', 'algorithms', 'structures', 'security', 'statistics', 'ui', 'ux', 'design', 'development'
    'research','product','forensic']
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
                #nl.append(s)
            #print(words_lines)
        #print(nl)
        for i in skills:
            if(i in nl):
                jd_skills.append(i)
        f.close()
        #print(jd_skills)
        return jd_skills

def iterate(dir_name):
    files = os.listdir(dir_name)
    #print(files)
    for my_file in files:
        search_skills(dir_name, my_file)
    #search_skills(dir_name, files[3])

#iterate('text_part1')
iterate('text_part2')