Actividad de participación #9
POO

Se te ha proporcionado un archivo de texto que contiene logs de tráfico web generados por un servidor. Cada registro de log tiene el siguiente formato:

Dirección IP: <dirección_ip>
Fecha y hora: <fecha_hora>
Método: <método_http>
URL: <url>
Código de respuesta: <código_respuesta>
Tamaño de respuesta: <tamaño_respuesta>
Tu tarea es leer el archivo y procesar la información para generar un informe que contenga las siguientes estadísticas:

Número total de solicitudes recibidas.
Número de solicitudes por método HTTP.
Número de solicitudes por código de respuesta.
Tamaño total de respuesta.
Tamaño promedio de respuesta por solicitud.
Las 10 URL más solicitadas, con el número de solicitudes.
Para resolver este problema, puedes crear una clase llamada AnalizadorLogs que tenga los siguientes métodos:

__init__(self, nombre_archivo: str) que reciba el nombre del archivo a procesar y lo guarde en un atributo de la clase.
procesar_logs(self) -> Dict[str, Any] que lea el archivo de texto, procese los datos y devuelva un diccionario con las estadísticas calculadas.
A continuación, te dejo algunos tips para resolver este ejercicio:

Puedes utilizar la función open para abrir el archivo y leer los datos línea por línea.
Para llevar un registro de las solicitudes por método HTTP y por código de respuesta, puedes utilizar un diccionario. La clave del diccionario sería el método o el código de respuesta, y el valor sería el número de solicitudes registradas.
Para calcular el tamaño total de respuesta y el tamaño promedio de respuesta por solicitud, puedes utilizar variables acumuladoras para sumar los tamaños de respuesta y llevar un contador de solicitudes.
Para determinar las 10 URL más solicitadas, puedes utilizar un diccionario para llevar un registro de las solicitudes por URL, y luego ordenar el diccionario por el valor (número de solicitudes) y tomar los primeros 10 elementos.