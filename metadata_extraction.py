#used to extract all the metadata from the PDF file and store it in firebase.
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import os
import json
import requests
#fp = open('edited_pdf_part1', 'rb')
def extract(pdf_dir):
    all_files = os.listdir(pdf_dir)
    print(all_files)
    
    os.chdir(pdf_dir)
    final_dict = {}
    for my_file in all_files:
        ext = my_file.split('.')[1]
        print(ext)
        if(ext == 'pdf'):
            # file_name = pdf_dir + '/' + i
            # print(file_name)
        
            print("file name: ", my_file)
            my_file = my_file.strip()
            fp = open(my_file, 'rb')
            parser = PDFParser(fp)
            doc = PDFDocument(parser)
            dict1 = doc.info[0]
            #print(dict1)
            newdict={
                "company":dict1["company"],
                "position":dict1["position"],
                "frequentWords":dict1["frequentWords"],
                "skills":dict1["skills"],
                "type":dict1["type"],
            }
            my_file = my_file.split('.')[0].split('_')[0] + '_'+  my_file.split('.')[0].split('_')[1]
            if my_file not in final_dict:
                final_dict[my_file] = newdict
            #print(newdict)

    #print(final_dict)
    final_json = json.dumps(final_dict)
    print(final_json)
    # url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json'
    # response = requests.put(url, final_json)
    # print response
extract("edited_pdf_part1")
    