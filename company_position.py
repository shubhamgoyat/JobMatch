import os

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
    #print(company_name)

def iterate(dir_name):
    mylist=[]
    files = os.listdir(dir_name)
    ##mylist.append(files)
    ##print(mylist)
    ##print(files)
    for my_file in files:
        name_position(dir_name, my_file)




# iterate(r'C:\Users\UMA\Downloads\text_part1')