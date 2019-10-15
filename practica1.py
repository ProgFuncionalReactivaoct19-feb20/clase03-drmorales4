"""
	Practica en clases
	@drmorales4
	Dado un conjunto de palabras filtrar todas las que sean palindromas

"""
# lista de palabras
palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

# uso de lambda y filter
resultado = filter(lambda x: "".join(reversed(x)) == x, palabras)

print(resultado)
print(list(resultado))
