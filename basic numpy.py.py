first_semester=[40,50,70,80,90]
total=0
for subjects in range(len(first_semester)):
    total=total+first_semester[subjects]
    if(subjects==len(first_semester)-1):
        print("total Marks=",total)
        print("Average Marks=",total/len(first_semester))