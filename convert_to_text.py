import urllib
from bs4 import BeautifulSoup
import ssl
import csv
import os
def convert_to_text(my_url, dest_file):
    url = my_url
    context = ssl._create_unverified_context()
    html = urllib.urlopen(url, context=context)
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    print(os.getcwd())
    file = open(dest_file,'w') 
    file.write(text) 
    file.close()
#convert_to_text('https://jobs.intel.com/ShowJob/Id/1822258/Software-Engineer/', 'check.txt')

def convert_csv(src_csv, dest_folder):
    with open(src_csv) as csvfile:
        rows = csv.reader(csvfile)
        res = list(rows)
    dataset = res[1:]
    print(dataset[0])
    c = 0
    for row in dataset:
        dest_file = dest_folder + '/'+ row[0]+'_'+row[1].strip()+'.txt'
        print(dest_file)
        convert_to_text(row[3], dest_file)
        print("Completed file number: ", c)
        c += 1

#convert_csv('new_companies_shreyasi.csv','text_part1')
#convert_csv('companies_uma.csv','text_part2')
#convert_csv('new_companies_uma.csv','text_part2')
#convert_csv('companies_internships.csv','text_part3')
#convert_csv('Final_Companies_1.csv','Final_Companies_1_text')
#convert_csv('Final_Companies_2.csv','Final_Companies_2_text')
#convert_csv('Final_Companies_3.csv','Final_Companies_3_text')
convert_csv('Final_Companies_4.csv','Final_Companies_4_text')