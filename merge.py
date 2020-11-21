import os
from shutil import copy2
def merge(text_folder_src, pdf_folder_src, text_folder_dest, pdf_folder_dest, index):
   text_files = os.listdir(text_folder_src)
   pdf_files = os.listdir(pdf_folder_src)
   text_files_names = map(lambda x: x.split('.')[0], text_files)
   pdf_files_names = map(lambda x: x.split('.')[0], pdf_files)
   print(text_files_names)
   print(pdf_files_names)
   for i in pdf_files_names:
       if i in text_files_names:
           if(i != ''):
            src = text_folder_src+'/'+i+'.txt'
            dest = text_folder_dest+'/'+index+'#'+i+'.txt'
            print(src, dest)
            copy2(src, dest)
            src = pdf_folder_src+'/'+i+'.pdf'
            dest = pdf_folder_dest+'/'+index+'#'+i+'.pdf'
            copy2(src, dest)

#merge('Final_Companies_1_text', 'Final_Companies_1_PDF', 'All_Companies_text', 'All_Companies_PDF', '1')
# merge('Final_Companies_2_text', 'Final_Companies_2_PDF', 'All_Companies_text', 'All_Companies_PDF', '2')
# merge('Final_Companies_3_text', 'Final_Companies_3_PDF', 'All_Companies_text', 'All_Companies_PDF', '3')
merge('Final_Companies_4_text', 'Final_Companies_4_PDF', 'All_Companies_text', 'All_Companies_PDF', '4')