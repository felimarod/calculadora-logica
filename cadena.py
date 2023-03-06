def proposicion(p):
	aux=''		
	aux = p.replace('^', ' and ', p.count("^"))		
	p = aux.replace('v', ' or ', p.count("v"))		
	aux = p.replace('→', ' => ', p.count("→"))
	p = aux.replace('↔', ' = ', p.count("↔"))

	return p

def variables(s):
	variables = ''
	if("p" in s and "q" in s and "r" in s):
		variables = ['p', 'q' , 'r']
		return variables
	elif("p" in s and "q" in s):
		variables = ['p' , 'q']
		return variables
	elif("p" in s and "r" in s):
		variables = ['p' , 'r']
		return variables	
