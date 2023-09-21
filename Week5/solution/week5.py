from csv import *

header = ['SID','SNAME','CITY','CONTACT']

file_record=[
    [1,'dharmesh','Surat',9926532150],
    [2,'nayan','Bardoli',9586144256],
    [3,'ketan','Vyara',9825743056],
    [4,'hardik','Surat',9563256213],
    [5,'jatin','Surat',9909275829]
    ]

main_list=[]
for i in range(5):
    sid=int(input("Enter Student Id :"))
    sname=input("Enter Student Name :")
    scity=input("Enter Student City :")
    scontact=int(input("Enter Student Contact :"))
    sub_lis=[sid,sname,scity,scontact]
    main_list.append(sub_lis)

file_record.extend(main_list)

with open('student.csv','w',newline="") as file_create:
    file_date = writer(file_create)
    file_date.writerow(header)
    file_date.writerows(file_record)

with open("student.csv",'r') as file_read:
    read_date = reader(file_read)
    for i in read_date:
        print(i)
