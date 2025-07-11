# 1. Create a text file and write student names to it

with open("prac.txt", "w") as f:
    f.write("abc\n")
    f.write("def\n")
    f.write("ghi\n")
    f.write("jkl\n")


#-------------------------------------------------------------------

# 2. Read and print the content of that file line by line

with open("prac.txt", "r") as f:
    x = f.read()
    print(x)

#-------------------------------------------------------------------

# 3. Append exam scores to the file

with open("prac.txt", "a") as f:
    f.write("\nExam Scores: \n")
    subj = ["Math : 88\n", "English : 91\n", "Economics : 90\n"]
    for s in subj:
        f.write(s)

    
#-------------------------------------------------------------------