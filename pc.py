import subprocess
def passwordcracking():
    print("                                         ")
    print("1) Crack PDF File")
    print("2) Crack Zip File")
    num = input("Enter the Option:")

    if num == "1":
        file = input("Enter the pdf file name:")
        subprocess.run(["pdf2john", file], stdout=open("pdf.hash", "w"))
        subprocess.run(["john", "pdf.hash"])
    elif num == "2":
        # Add your code to crack Zip files here
        file = input("Enter the zip file name:")
        # You can use the zip2john tool to extract the hash from the zip file
        subprocess.run(["zip2john", file], stdout=open("zip.hash", "w"))
        subprocess.run(["john", "zip.hash"])
    else:
        print("Invalid option. Please enter 1 or 2.")










#pdf2john raw.pdf> raw.hash