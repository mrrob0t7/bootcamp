ticket = 239 #minutos
dia = "viernes"

if dia == "viernes":
    if ticket >= 300 or ticket >= 240 :
        print ("se le cobrara $80 pesos");
    else: 
        if (ticket >= 180):
            print ("se le cobrara $80 pesos :D")
        else:
            if (ticket >= 120):
                print ("se le cobrara $60 pesos") 
            else:
                if (ticket >= 60):
                    print ("se le cobrara $40 pesos") 
                else:
                    print ("se le cobrara $20 pesos")
else:
    if ticket >= 300 :
        print ("se le cobrara $100 pesos");
    else:
        if (ticket >= 240):
            print ("se le cobrara $100 pesos") 
        else:
            if (ticket >= 180):
                print ("se le cobrara $80 pesos") 
            else:
                if (ticket >= 120):
                    print ("se le cobrara $60 pesos") 
                else:
                    if (ticket >= 60):
                        print ("se le cobrara $40 pesos") 
                    else:
                        print ("se le cobrara $20 pesos")
