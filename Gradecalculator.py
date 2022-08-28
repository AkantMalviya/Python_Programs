Akant = {"name":"Akant Malviya","assignment":[90,85,95,88],"test":[85,94],"lab":[88.20,98.20]}
Shivam = {"name":"Shivam Kothekar","assignment":[85,89,92,90],"test":[82,91],"lab":[83.20,80.20]}
Sumit = {"name":"Sumit Pawar","assignment":[90,81,85,68],"test":[74,93],"lab":[74.20,80.20]}
Vishal = {"name":"Vishal Satpute","assignment":[89,80,75,78],"test":[78,91],"lab":[72.20,78.20]}
Jayesh = {"name":"Jayesh Kumbhare","assignment":[91,84,94,86],"test":[84,92],"lab":[81.20,94.20]}
while(True):
    Name = input("Enter Student Name : ")
    if Name != "done":
        if Name == "Akant":
            score = 0
            temp = 0
            for i,j in Akant.items():
                
                if i=="name":
                    print(j)
                    continue
                else:
                    total = 0
                    for k in j:
                        total+=k
                    temp= (total*30)/100
                score+=temp   
            print(score)         
        elif Name == "Shivam":
            print(Shivam.items())
        elif Name == "Sumit":
            print(Sumit.items()) 
        elif Name == "Vishal":
            print(Vishal.items())
        elif Name == "Jayesh":
            print(Jayesh.items())
        else:
            print("Student Not Found")
    else:
        print("Program Done")
        break        