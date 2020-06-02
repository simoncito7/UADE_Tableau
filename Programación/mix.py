# General Buen día! en base a lo conversado con el equipo docente, me han comentado que dentro del grupo existen personas con conocimientos 
# intermedios/avanzados en Python, lo que va a ser de utilidad para el desarrollo de la cursada. Para la próxima clase, la idea es poder generar
# grupos heterogéneos con el objetivo de desarrollar ejercitación. Entraremos en detalle el viernes 8. Lo que nos gustaría pedirles a modo de 
# práctica a los que conocen Python, es si pueden desarrollar un programa que arme grupos aleatorios de 6 personas. Me han pasado una lista 
# tentativa de participantes y quisiera que desarrollen algo, pero con un pequeño detalle, los invitaremos a explicar el código durante la clase, 
# por lo que les pedimos que el programa sea lo más amigable posible para poder explicar. A modo de ayuda, les adjunto la lista de participantes. 
# Pido disculpas si me he olvidado de alguno, tengan a bien agregarlo. 
# Aquí el código para comenzar a desarrollar.  Si copian código de Stackoverflow, u otra fuente (Si, si.. se que lo harán hoy o en algún momento de la 
# cursada, y esta muy bien!), cambien el nombre de las variables para que sea fácil de leer. Happy <Coding>!!


import random

# Función 1
def mezcla1(alumnos, numIntegrantes):
    """Este método permite obtener los integrantes de un grupo de manera aleatoria. Recibe una lista y la cantidad de integrantes"""

    print("ESTA ES LA FUNCIÓN 1: \n")
    # Longitud de lista pasada por argumento
    cantidadAlumnos = len(alumnos)
    
    alumnosQueYaTienenGrupo = []

    contador1 = 0               # almacena la cantidad de veces que va iterando en los grupos
    contador2 = 0               # almacena la cantidad de veces que va iterando en la cantidad total de alumnos
    contador3 = 0               # almacena la cantidad de veces que va iterando en la cantidad de integrantes

    grupo = []                  # se define lista vacía

    while contador2 < cantidadAlumnos:           # bucle se ejecuta tantas veces como cantidad de alumnos hayan

        while contador3 < numIntegrantes:        # bucle que itera tantas veces como integrantes de grupo hayan

            integrante = random.choice(alumnos)  # choice() hace una elección aleatoria de un elemento de la lista "alumnos" y lo almacena en "integrante"

            if integrante not in alumnosQueYaTienenGrupo:       # si integrante no está en "alumnosQueYaTienenGrupo"
                grupo.append(integrante)
                alumnosQueYaTienenGrupo.append(integrante)
                contador3 = contador3 + 1
                contador2 = contador2 + 1

                if contador2 == cantidadAlumnos:
                    print("El grupo ", contador1 + 1 , " es: ", grupo)  
                    break
                
            else:
                pass
            
        contador3 = 0
        if contador2 < cantidadAlumnos:
            print("El grupo ", contador1 + 1 , " es: ", grupo)
        contador1 = contador1 + 1
        grupo[:] = []
    

# Función 2
def mezcla2(participantes):

    print("ESTA ES LA FUNCIÓN 2: \n")

    cantidad = len(participantes)
    participantes_original = participantes.copy()
     
    random.shuffle(participantes)
    print(participantes_original)
    print("\n El grupo 1 es : ", participantes[0:6], "\n El grupo 2 es: ",participantes[6:12],"\n El grupo 3 es: ", participantes[12:19])

# Función 3
def mezcla3(participantes):

    print("ESTA ES LA FUNCIÓN 3: \n")

    cantidadAlumnos = len(participantes)
    
    alumnosQueYaTienenGrupo = []
    contador1 = 0               # almacena la cantidad de veces que va iterando en los grupos
    contador2 = 0               # almacena la cantidad de veces que va iterando en la cantidad total de alumnos
    contador3 = 0               # almacena la cantidad de veces que va iterando en la cantidad de integrantes

    grupo = []


    while contador2 < cantidadAlumnos:           # bucle se ejecuta tantas veces como cantidad de alumnos hayan

        while contador3 < numIntegrantes:        # bucle que itera tantas veces como integrantes de grupo hayan

        
            num_aleatorio = random.randrange(0,cantidadAlumnos)     
            integrante = participantes[num_aleatorio]

            if integrante not in alumnosQueYaTienenGrupo:
                grupo.append(integrante)
                alumnosQueYaTienenGrupo.append(integrante)
                contador3 = contador3 + 1
                contador2 = contador2 + 1

                if contador2 == cantidadAlumnos:
                    print("El grupo ", contador1 + 1 , " es: ", grupo)  
                    break
                
            else:
                pass
            
        contador3 = 0
        if contador2 < cantidadAlumnos:
            print("El grupo ", contador1 + 1 , " es: ", grupo)
        contador1 = contador1 + 1
        grupo[:] = []


# Lista de participantes
participantes=["Simon Valenzuela", "Nicolas Sarubbi", "Cristian Ramirez", "Artur Sadovenko", "Emiliano Romero", "Gerardo Santa Cruz", 
              "Manuel Quintana", "Fabian Fullone", "Ignacio Perozzi", "Feliz Molina", "Yesica Gallo", "Lucia Callejon", 
              "Florencia Szulak", "Lucia Stefanuto", "Florencia Sidotti", "Daniela Araujo", "Alejandro Mercado", "Hernan Bevilacqua","batata"]

numIntegrantes = 6

# Llamada a funciones
mezcla1(participantes, numIntegrantes)
# mezcla2(participantes)
# mezcla3(participantes)


