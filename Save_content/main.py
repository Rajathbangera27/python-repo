import os

filename = input("Enter the file name: ")

if os.path.exists(filename):
    print("File already found")
else:
    content = input("Enter the content to write into the file: ")
    
    file = open(filename, "w")
    file.write(content)
    file.close()
    
    print("File created and content written successfully")

    # pull request