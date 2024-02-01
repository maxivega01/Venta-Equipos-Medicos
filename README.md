Vega Marconetto, Máximo (90788) - 1k6

Turno 3 - Enunciado 3 (T3E3) (Copie el enunciado siguiente como comentario al inicio de su archivo principal de código fuente)

Una empresa de venta de equipamiento médico mantiene información sobre los distintos aparatos que tiene a la venta.
Por cada equipo se registran los datos siguientes: número de identificación (un entero), nombre (una cadena), precio,
tipo de aparato (un número entero entre 0 y 39 incluidos, para indicar (por ejemplo): 0: aparato de rayos X, 1: tomógafo, etc.)
y código de pais de origen (un valor entre 0 y 19, para indicar (por ejemplo): 0: Argentina, 1: USA, 2: Italia, etc.)

Se pide definir un tipo registro Equipo con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Equipo en un arreglo de registros (cargue n por teclado).
Valide que el tipo y el pais de origen estén dentro de los valores descriptos. Puede cargar los datos manualmente,
o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual,
y si la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor,
según el precio, y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria.
Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final,
o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea, pero muestre solo los registros cuyo precio sea
mayor a un valor p cargado por teclado, y que no vengan del país número 8.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación sea igual a num (cargar num por teclado).
Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un mensaje.
La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros cuyo precio sea
menor al precio promedio de todos los artículos del arreglo.

5- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla. Al final del listado,
mostrar una línea adicional que indique la cantidad de registros que se mostraron.
