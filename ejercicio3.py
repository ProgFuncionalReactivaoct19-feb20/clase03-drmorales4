"""
	@drmorales4
	Funcional - aplicando funcion filter
"""

datos = [1, 2, 10, 11, 12, 13]
resultado = filter(lambda x: x % 2 == 0, datos)
print(resultado)
print(list(resultado))
