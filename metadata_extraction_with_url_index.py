#used to extract all the metadata from the PDF file and store it in firebase.
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import os
import json
import requests
import csv
#fp = open('edited_pdf_part1', 'rb')
def extract(pdf_dir, csv1, csv2, csv3, csv4, pdf_file_links):
    all_files = os.listdir(pdf_dir)
    print(all_files)
    
    os.chdir(pdf_dir)
    final_dict = {}
    c = 0
    skills_index = {}
    for my_file in all_files:
        ext = my_file.split('.')[1]
        print(ext)
        if(ext == 'pdf'):
            # file_name = pdf_dir + '/' + i
            # print(file_name)
        
            print("file name: ", my_file)
            my_file = my_file.strip()
            with open('../'+pdf_file_links) as csvfile:
                rows = csv.reader(csvfile)
                res = list(rows)
            dataset = res[1:]
            pdf_link = ""
            for row in dataset:
                
                if(row[0] == my_file):
                    pdf_link = row[1]
            print(pdf_link)
            split_file_name = my_file.split('#')
            folder_id = split_file_name[0]
            job_id = split_file_name[1]
            # print(os.getcwd())
            if(folder_id == '1'):
                csv_file = csv1
            elif(folder_id == '2'):
                csv_file = csv2
            elif(folder_id == '3'):
                csv_file = csv3
            else:
                csv_file = csv4

            with open('../'+csv_file) as csvfile:
                rows = csv.reader(csvfile)
                res = list(rows)
            dataset = res[1:]
            for row in dataset:
                val = row[0]+'_'+row[1]+'_edited.pdf'
                # print(val)
                # print(job_id)
                if(val == job_id):
                    url_val = row[3]
            # c = 0
            # for row in dataset:
            #     dest_file = dest_folder + '/'+ row[0]+'_'+row[1].strip()+'.txt'
            #     print(dest_file)
            #     convert_to_text(row[3], dest_file)
            #     print("Completed file number: ", c)
            #     c += 1
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
                "url":url_val,
                "pdfURL":pdf_link
            }
            

            final_file_name = str(c) + '_' + my_file.split('#')[1].split('.')[0]
            my_file = my_file.split('.')[0].split('_')[0] + '_'+  my_file.split('.')[0].split('_')[1]
            if my_file not in final_dict:
                final_dict[final_file_name] = newdict
            s_vals = dict1["skills"].split(';')
            for i in s_vals:
                if i in skills_index:
                    skills_index[i].append(final_file_name)
                else:
                    skills_index[i] = [final_file_name]
            
            #print(newdict)
            c += 1
    #print(final_dict)
    # final_json = json.dumps(final_dict)
    # print(final_json)
    # url = 'https://skillsmatch-820bf.firebaseio.com/skillsmatch-820bf.json'
    # response = requests.put(url, final_json)
    # print response
    print(skills_index)
    final_json = json.dumps(skills_index)
    print(final_json)
    url = 'https://skillsmatch-820bf.firebaseio.com/index.json'
    response = requests.put(url, final_json)
    print response
    
#extract("All_Companies_PDF_with_metadata","Final_Companies_1.csv", "Final_Companies_2.csv", "Final_Companies_3.csv", "Final_Companies_4.csv")

extract("All_Companies_PDF_with_metadata","Final_Companies_1.csv", "Final_Companies_2.csv", "Final_Companies_3.csv", "Final_Companies_4.csv", 'pdf_links_S3.csv')