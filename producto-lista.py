#Issue nro 16
def  producto_lista(lista):
    res =[]
    for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        res.append(producto[x,y])
    return res

producto_lista(genrnd())