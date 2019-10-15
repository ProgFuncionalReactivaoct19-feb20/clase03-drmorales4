"""
	Practica en clases
	@drmorales4
"""

def es_vocal (x) :
	letrasProvincia = ["l", "p", "a", "i", "e"]
	l = x[0]
	if l in letrasProvincia:
		return True
	else:
		return False

# lista de placas
placas = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002"]
resultado = filter(es_vocal, placas)
print(list(resultado))
