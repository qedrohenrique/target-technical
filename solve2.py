import json
 
good_days = 0

with open('dados.json') as json_file:
    data = json.load(json_file)
    values = list(d['valor'] for d in data)

	# Acho que seria interessante imprimir o dia do mês em que isso ocorre
	# mas como não foi pedido, optei por omitir isto.

    print("Minimo: ", min(values))	
    print("Maximo: ", max(values))


    avg = sum(values)/len(values)
    for value in values:
    	if value > avg:
    		good_days += 1
    
print("Dias acima da media: ", good_days)
	
