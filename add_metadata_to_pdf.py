from pdfrw import PdfReader, PdfWriter
import string
import os   


def search_internship(dir_name, file_name):
    print("file name in search internship: ", file_name)
    words = ['intern', 'internship']
    ext = file_name.split('.')[1] #check if it is text file
    #print(ext)
    if(ext == 'txt'):
        f = open(dir_name+'/'+file_name, 'r')
        content = f.readlines()
        internship_found = False
        for line in content:
            line = line.strip()
            words_lines = line.split(' ')
            for i in words:
                if(i in words_lines):
                    internship_found = True
        f.close()
        #print(internship_found)
        return internship_found

def search_skills(dir_name, file_name):
    skills = ['python', 'c', 'java', 'numpy', 'software', 'management', 'computer', 'computer engineering', 'data', 'machine', 'learning', 
    'apache','spark', 'big', 'opertaing', 'systems', 'networks', 'ios', 'full', 'stack', 'html', 'html5', 'css', 'javascript', 'php', 'sql', 'postgressql', 
    'react', 'spring', 'hadoop', 'hive', 'hbase', 'scala', 'agile', 'algorithms', 'structures', 'security', 'statistics', 'ui', 'ux', 'design', 'development'
    'research','product','forensic']
    print("file name in search skills: ", file_name)
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
def name_position(dir_name, file_name):
    mylist=[]
    company_name = file_name.split('.')[0].split('_')[1]
    f = open(dir_name+'/'+file_name, 'r')
    x = f.readlines()
    position=(x[0].strip())
    mylist.append(company_name)
    mylist.append(position)
    
    print(mylist)
    f.close()
    return mylist
def search_frequentwords(dir_name, file_name):
    frequentwords = ['python', 'c', 'java', 'numpy', 'software', 'management', 'computer', 'computer engineering', 'data', 'machine', 'learning', 
    'apache','spark', 'big', 'opertaing', 'systems', 'networks', 'ios', 'full', 'stack', 'html', 'html5', 'css', 'javascript', 'php', 'sql', 'postgressql', 
    'react', 'spring', 'hadoop', 'hive', 'hbase', 'scala', 'agile', 'algorithms', 'structures', 'security', 'statistics', 'ui', 'ux', 'design', 'development'
    'research','product','forensic','analytics','senior','associate','rngineer','information','manager','release','delivery','investigative','responsible'
    ,'customers','experts','key','hardware','deliverables','integration','embedded','familiarity','programming','skills','qualification','communication','expertise','validation', 'fast','paced','career']
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
def create_json(file_name, dir_name):
   
    if(search_internship(dir_name, file_name)):
        job_type = "Internship"
    else:
        job_type = "Full Time"
    skills = search_skills(dir_name, file_name)
    company = name_position(dir_name, file_name)[0]
    position = name_position(dir_name, file_name)[1]
    freq_words = name_position(dir_name, file_name)
    my_dict = {
        "jobType" : job_type,
        "skills": skills,
        "company": company,
        "position":position,
        "freqWords": freq_words
    }
    #print(my_dict)
    return my_dict
# trailer = PdfReader("out.pdf")    
# trailer.Info.WhoAmI = "Tarun Lalwani"    
# PdfWriter("out_edited.pdf", trailer=trailer).write()  

def add_meta_to_file(dir_name, file_name, text_file_dir, new_pdf_dir):
    txt_file_name = file_name.split('.')[0]+'.txt'
    print('text file name', txt_file_name)
    metadata = create_json(txt_file_name, text_file_dir)
    pdf_file = dir_name + '/' + file_name
    trailer = PdfReader(pdf_file) 
    new_pdf_file = new_pdf_dir + '/' + file_name.split('.')[0]+'_edited.pdf'
    print(metadata)
    trailer.Info.type = metadata['jobType']
    trailer.Info.skills = ';'.join(metadata['skills'])
    trailer.Info.company = metadata['company']
    trailer.Info.position = metadata['position']
    trailer.Info.frequentWords = ';'.join(metadata['freqWords'])
    PdfWriter(new_pdf_file, trailer=trailer).write()


def add_meta_to_folder(dir_name, text_file_dir, new_pdf_dir):
    files = os.listdir(dir_name)
    print(files)
    c = 0
    for my_file in files:
        try:
            add_meta_to_file(dir_name, my_file, text_file_dir, new_pdf_dir)
            #create_json(my_file, text_file_dir)
            c += 1
            print('completed: ', c)
        except:
            print("Failed")

# add_meta_to_folder('pdf_part1', 'text_part1', 'edited_pdf_part1')
add_meta_to_folder('All_Companies_PDF', 'All_Companies_text', 'All_Companies_PDF_with_metadata')