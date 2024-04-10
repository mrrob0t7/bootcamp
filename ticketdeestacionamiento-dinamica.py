ticket = 130 #minutos

horas = (int)(ticket/60)
minutos = ticket % 60

print("llevas:")
print(horas)
print("horas")

print("y")
print(minutos)
print("minutos")

if ticket >= 300 :
	print ("se le cobrara $79.99 pesos");
else:
	if (ticket >= 240):
		print ("se le cobrara $70 pesos")
	else:
		if (ticket >= 180):
			print ("se le cobrara $65 pesos extra") 
		else:
			if (ticket >= 120):
				print ("se le cobrara $55 pesos extra") 
			else:
				if (ticket >= 60):
					print ("se le cobrara $40 pesos") 
				else:
					print ("se le cobrara $20 pesos")
