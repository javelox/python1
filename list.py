demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["Red", "Green", "Blue"]

#para hacer uso de la palabra reservada list debemos pasarle solo un argumento en este caso pasaremos una tupla

numbers_list =  list({1, 2, 3, 4})
# print(numbers_list)


#Tener encuenta que usando este metodo range se creara la lista pero llega un numero antes de el segundo parametro  en este caso al 9
# r = list(range(1, 10))
# print(r)

# print(dir(colors)) # Con este metodo dir muestra que metodos podemo usar 
# print(len(demo_list)) # mustra la longitud de la lista
# print(colors[1])
# print("Green" in colors) # No sirve para comprobar si el dato existe en la lista

# print(colors)
# colors[1] = "Yellow"
# print(colors)

# colors.append("Violet") # De esta manera podemos agregar datos nuevo a la listo pero solo podemos agregar uno 
# colors.append({"Violet", "Yellow"}) # de esta manera agregamos varios datos pero quedaran en un tupla
# colors.extend(["Violet", "Yellow"]) # usando el metodo extend podemos agregar la catidad de datos necesarios para el proceso
# colors.extend(["Pink", "Black"])

# colors.insert(1, "Violet")
# colors.insert(len(colors), "Violet") # insertamos un valor en la lista usando el metodo len para agregarlo en la longitud de la lista
# print(colors)

# colors.pop() #con este metodo se puede quitar el ultimo objeto de una lista, tambien podemos eliminar con el indice de el dato  
# print(colors)

# colors.remove("Green") # se puede borrar cualquier dato de una lista nombrandolo especificamente 
# print(colors)

# colors.clear() # lo que hace este metodo es eliminar todos lo elementos de la lista 

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)