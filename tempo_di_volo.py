carburante = raw_input("Inserisci il carburante in galloni: ")
n_carburante = float(carburante)

consumo_orario = raw_input("Inserisci il consumo orario in galloni/h: ")
n_consumo_orario = float(consumo_orario)

if n_carburante < 0 :
	print("Puoi mai avere il carburante inferiore allo 0?!")
elif n_consumo_orario < 0 :
	print("Il consumo orario deve essere maggiore di zero!")
else:
	tempo = n_carburante / n_consumo_orario
	ora = int (tempo)

 	minuti = (tempo - ora) * 60
	minuti_int = int (minuti)

	secondi = (minuti - minuti_int ) * 60
	secondi_int = int (secondi)
	
	print "il tempo di volo e' di h:", ora, " min:", minuti_int, "sec:", secondi_int


