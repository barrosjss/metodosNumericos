# Team @barros
# Curso : Metodos Numericos

"""
DESCRIPCION: Determinar el Epsilon de la maquina para su computadora.
"""

#----------------------------------codigo-----------------------------------

epsilon = 1.0   
while (epsilon+1) > 1:
  epsilon = epsilon/2  
  print(epsilon)

epsilon = 2*epsilon  
print(epsilon)