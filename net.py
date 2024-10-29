import subprocess
def networkscanner():
        print("                                         ")
        ip=input("Enter the Victim Ip address or Domain Name:")
        print("1) Scan for OS Detection")
        print("2) Scan for Remote operating Systems")
        print("3) Scan for List All Hosts on a Network")
        print("4) Scan All Ports on a Target")
        print("5) Scan for Open Ports on the Target")
        print("6) Run All Vulnerability Scans on the Target")
        option=input("Enter the Option:")

        if(option=="1"):
                print("                               ")
                subprocess.run(["nmap","-A",ip])
        elif(option=="2"):
                print("                               ")
                subprocess.run(["nmap","-O",ip])
        elif(option=="3"):
                print("                               ")
                subprocess.run(["nmap","-sL",ip])
        elif(option=="4"):
                print("                               ")
                subprocess.run(["nmap","-p-",ip])
        elif(option=="5"):
                print("                               ")
                subprocess.run(["nmap","--open",ip])
        elif(option=="6"):
                print("                               ")
                subprocess.run(["nmap","--script","vuln",ip])
        else:
                print("Invaild Options")
