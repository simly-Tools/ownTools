import net
import pay
import pc
import pg
print(" 1)Network Scanner")
print(" 2)Payload Generater")
print(" 3)Password Cracking")
print(" 4)Strong Password Generater")
num=input(" Enter the option:")
if(num=='1'):
    print("                             Network Scanner                                                 ")
    net.networkscanner()
elif(num=="2"):
    print("                             Payload Generater                                                        ")
    pay.payloadgenerater()
elif(num=="3"):
    print("                             Password Cracking ")
    pc.passwordcracking()
elif(num=="4"):
    print("                             Strong Password Generater")
    pg.passgen()
else:
    print("Invaild Option")
