import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
student_fields = ['roll', 'name', 'student_id', 'class_roll', 'batch']
student_database = 'students.csv'

#generating report card...

def reportcard():
    # entering student details...
    print("Enter the Student Details")
    Name=input("Enter the name of the student:")
    Classroll=input("Enter the class roll no.:")
    Sec=input("Enter the sec of the student:")
    Enrollmentno=input("Enter the enrollment no. of the student:")
    Stream=input("Enter the stream of the students:")
    print("The subjects you have-1.PHYSICS  2.MATHEMATICS  3.BIOLOGY  4.MECHANICS  5.BASIC ELECTRICAL ENGINEERING")
    phy=int(input("Enter the physics marks: "))
    math=int(input("Enter the mathematics marks: "))
    bio=int(input("Enter the biology marks: "))
    mech=int(input("Enter the Mecahanics maerks: "))
    bee=int(input("Enter the basiuc electrical engfineering marks: "))
    sum=int((phy+math+bio+mech+bee))
    percentage=((sum/500))*100
    print("Your total marks is ",sum)
    if(percentage<40):
        d="You Are Performed Terrible.......You Secured Grade F"
    elif(40<=percentage<60):
        d="You Are Performed Average........You Secured Grade B"
    elif(60<=percentage<80):
        d="You Are Performed Good.......You Secured Grade A"
    elif(80<=percentage<90):
        d="You are Performed Excellent.......You Secured Grade A+"
    else:
        d="You Are Performed Brilliantly.......You securedc Grade AA" 
    print(percentage)
    print(d)   
    #creating text file for report card....       
    file=open("reportcard.txt","w")
    file.writelines("**************************** Report Card ****************************\n")
    file.writelines(Name)
    file.writelines("\n")
    file.writelines(Stream)
    file.writelines("\n")
    file.writelines(Enrollmentno)
    file.writelines("\n")
    file.writelines(Sec)
    file.writelines("\n")
    file.writelines(Classroll)
    file.writelines("\n")
    file.writelines("RESULT DETAILS \n")
    file.write("The Marks Obtained in Physics: {}".format(phy))
    file.writelines("\n")
    file.write("The Marks Obtained in Mathematics: {}".format(math))
    file.writelines("\n")
    file.write("The Marks Obtained in Biology: {}".format(bio))
    file.writelines("\n")
    file.write("The Marks Obtained in Mechanics: {}".format(mech))
    file.writelines("\n")
    file.write("The Marks Obtained in Basic Electrical Engineering: {}".format(bee))
    file.writelines("\n")
    file.write("The total marks of the student: {}".format(sum))
    file.writelines("\n")
    file.writelines("RESULT REVIEW-----\n")
    file.writelines(d)
    file.writelines("\n")
    file.writelines("Congratulations to all of the students!!!! \n Who cannot performed well try to improve yourself and who performed well they try to retain this")
    print("\n")
    file.close()

# Addition of the students...

def add_student():
    global student_fields
    global student_database
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return

# for view any student....

def view_students():
    global student_fields
    global student_database
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press any key to continue")

# for updating student details...

def update_student():
    global student_fields
    global student_database
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

#for deleting a student from the database...

def delete_student():
    global student_fields
    global student_database
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

#for creating files....which are required

def filetemplate(name,lst):
    with open(f'name','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(lst)
        print(f"{name} file has been UPDATED")

def createfiles():
    #filetemplate('Batch.csv',['Batch ID','Batch Name','Department Name','List of Courses','List of Students'])
    with open(f'Batch.csv','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(['CSE22','CSE 2022-26','CSE'])
        script.writerow(['CSE21','CSE 2021-25','CSE'])
        script.writerow(['ECE22','ECE 2022-26','ECE'])
        script.writerow(['ECE21','ECE 2021-25','ECE'])
        script.writerow(['EE22','EE 2022-26','EE'])
        script.writerow(['EE21','EE 2021-25','EE'])
    #filetemplate('Course.csv',['Course ID','Course Name','Marks Obtained'])
    with open(f'Course.csv','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(['C001','Python Programming'])
        script.writerow(['C002','Math'])
        script.writerow(['C003','Physics'])
        script.writerow(['C004','Chemistry'])
        script.writerow(['C005','Biology'])
        script.writerow(['C006','English'])
    #filetemplate('Department.csv',['Department ID','Department Name','List of Batches'])
    with open(f'Department.csv','a',newline='')as f:
        script= csv.writer(f)
        script.writerow(['CSE','Computer Sience and Engineering'])
        script.writerow(['CSEAI','Computer Sience and Engineering and Artificial Intelligence'])
        script.writerow(['CSEAIML','Computer Sience and Engineering and Artificial Intelligence and Machine Learning'])
        script.writerow(['CSEIOTCSBS','Computer Sience and Engineering and Internet of Things and Business Studies'])
        script.writerow(['IT','Information Technology'])
        script.writerow(['ECE','Electrical and Communications Engineering'])
        script.writerow(['ME','Mechanical Engineering'])
    filetemplate('Student.csv',['Student ID','Name','Class Roll Number','Batch ID'])
    filetemplate('Examination.csv',['Course Name','Student ID','Marks'])

# main code...

while True:
    print("CSE: COMPUTER SCIENCE AND ENGINEERING")
    print("ECE: ELECTRONICS AND COMMUNICATION")
    print("CS(AI & ML): COMPUTER SCIENCE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING")
    print("CS(IOTCSBS): COMPUTER SCIENCE AND ENGINEERING AND INTERNET OF THINGS AND BUISNESS STUDIES")
    print("EE: ELECTRICAL ENGINEERING")
    print("ME: MMECHANICAL ENGINEERING")
    print("IT: INFPRMATION TECHNOLOGY")
    print("-------------------------------------")
    print("This above course are available in I.E.M.")
    print("Enter the datas as per requirement...")
    print("Enter 1 For Add New Student")
    print("Enter 2 For View Students")
    print("Enter 3 For Creating Files")
    print("Enter 4 For Update Student")
    print("Enter 5 For Delete Student")
    print("Enter 6 For Check Report Card")
    print("Enter 7 For Break The Process")
    n= int(input("Enter the correct option number: "))
    if n == 1:
        add_student()
    elif n == 2:
        view_students()
    elif n == 3:
        createfiles()        
    elif n == 4:
        update_student()
    elif n == 5:
        delete_student()
    elif n == 6:
        reportcard()
    else:
        break

