"""
	Practica en clases
	@drmorales4
"""
# lista de provincias
provicias = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala",  "Portoviejo", "Macas"]

# uso de lambda y filter
resultado = filter(lambda x: len(x)%2 == 0, provicias)
print(list(resultado))
