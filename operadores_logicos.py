'''
operadores logicos 

Aquellos que operan unicamente 
con valores boleanos (V F)
Acorde a las tablas 



'''
#Ejemplo 1: Oerador not:
y = not True 
print("El resultado de operar con not es",y)

#ejemplos 2: Operador and
y = False and True 
print("El resultado de operar con and es" ,y)

#ejemplo 3: Operador or
y = False or False
print(" El resultado de operar con or es" ,y)

'''
Jerarquia de predecia de operadores
(logicos inclusive)
1.    ()
2.    **
3.   *, /, %,
4.   +, -
5.   >,<,>=, <=, !=, ==
6.    not 
7.    and
8.    or
9.=

'''

#Ejemplo 4: Jerarquia de operadores
y = False and not True or False
print(" El resultado de operar con jerarquia de operadores es" ,y)




#Ejemplo 5: operadores relacionales y logicos
y= not 3 > 4 and 4 == 4 or 3 < 2
