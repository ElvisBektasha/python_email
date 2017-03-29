filename = 'output.txt'
reference = 'reference.txt'
referenca = open(reference,'r')
from validate_email import validate_email
lista = [l for l in (line.strip() for line in referenca) if l]
for index in range(len(lista)):
	is_valid = validate_email(lista[index],verify=True)
	print lista[index]+","+str(is_valid)
	output = open(filename,'a')
	output.write(lista[index]+","+str(is_valid)+"\n")
	output.close()
referenca.close()
