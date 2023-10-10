def sort_students(student_list):
    sort_list=sorted(student_list,key=lambda a:a[2],reverse=True)
    return sort_list
      
students=[["Thilak",6245,7],["prathas",8745,9.3],["ram",2384,4.9],["Mari",6230,6.8]]

sortedstudent=sort_students(students)
for i in range(len(sortedstudent)):
    print("Name :{}, Rollnumber :{}, cgpa :{}".format(sortedstudent[i][0],sortedstudent[i][1],sortedstudent[i][2]))
    
