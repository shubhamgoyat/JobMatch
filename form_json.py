import os
from internship import search_internship
from skills import search_skills
def create_json(file_name, dir_name):
   
    if(search_internship(file_name, dir_name)):
        job_type = "Internship"
    else:
        job_type = "Full Time"
    skills = search_skills(file_name, dir_name)
    my_dict = {
        "jobType" : job_type,
        "skills": skills
    }
    #print(my_dict)
    return my_dict
    


def iterate(dir_name):
    files = os.listdir(dir_name)
    #print(files)
    for my_file in files:
        create_json(dir_name, my_file)
    #search_skills(dir_name, files[3])

#iterate('text_part2')
iterate('text_part3')