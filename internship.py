import os
def search_internship(dir_name, file_name):
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

def iterate(dir_name):
    files = os.listdir(dir_name)
    print(files)
    for my_file in files:
        search_internship(dir_name, my_file)


iterate('text_part3')