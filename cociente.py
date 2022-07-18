#Issue nro 7 - Lina
def cociente(x,y):
  try:
    res=x/y
  except ZeroDivisionError:
    return 'No se puede dividir por cero'
  else:
    return res
  