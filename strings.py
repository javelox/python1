myStr = "Hello World"

# print(dir(myStr))

print(myStr.upper()) #Pasar a Mayusculas 
print(myStr.lower()) # Pasar a Minusculas 
print(myStr.swapcase()) # Cambiar las letras de mayusculas a minusculas o al reves
print(myStr.capitalize()) # Capitaliza el texto     
print(myStr.replace('Hello', 'bye')) # Cambia el valor de la variable 
print(myStr.count(" ")) # Cuenta la cantidad de caracteres que nombramos en los parentesis 
print(myStr.startswith('Hello')) # Compara si la variable inicia desde donde se pone la instrucion 
print(myStr.endswith('World')) # Compara si de verdad termina en la instruccion entregada
print(myStr.split()) # Separa la variable en una list 
print(myStr.find('o')) # Cuenta en que posicion esta el caracter indicado en los parentesis
print(len(myStr)) # Me da el tamaño de todos los caracteres de la variable
print(myStr.index('e')) # El método devuelve la posición en la primera aparición del valor especificado.index()
print(myStr.isnumeric()) # mira si el valor es numerico
print(myStr.isalpha()) # mira si el valor es alfa numerico
print(myStr[4]) # imprime la posicion de el caracter solicitado 
print(myStr[-5]) # No entrega el valor a la inversa  

print(f"{myStr} mel")