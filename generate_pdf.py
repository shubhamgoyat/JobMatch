import pdfkit
import csv
p=[]
with open('Final_Companies_4.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
your_list=your_list[1:]
c=0
for i in your_list:
    print(i[3])
    try:
        new_file='Final_Companies_4_PDF/'+i[0]+'_'+i[1]+'.pdf'
        pdfkit.from_url(i[3],new_file)
    except:
        print("not converted")
    c+=1
    print ("file: ",c)
print (p)
##for m in p:
    
##print(out.pdf)
