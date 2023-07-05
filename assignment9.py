from assignment9_1 import File_Operations, MyCustomException

op = File_Operations()

fl=input("Enter file name to open:")
print("File created: ",fl)
try:
     op=open(fl,"w")
except FileExistsError as e:
    print("File already exist")

  
data=input("Enter data to write: ")
print("Data written successfully: ",data)
try:
    op.write(data)
except Exception as e:
    print(e)

try:
    while True:
        ch = input("Do you want to add more data to the file? (yes/no): ")
        if ch.lower() == "no":
            break
        elif ch.lower() == "yes":
            app_ch= input("Do you want to append the data or overwrite the existing data? (append(a)/overwrite)(o):")
            if app_ch == "a":
                data = input("Enter data to append to the file: ")
                op.write(data)
                print("Data appended successfully!")
            elif app_ch == "o":
                data = input("Enter data to overwrite the file: ")
                op.seek(0)
                op.write(data)
                print("Data overwritten successfully!")
        else:
            print("Invalid choice. Please enter 'append(a)' or 'overwrite(o)'.")

except IOError:
    print("Error: Could not open or write to the file.")