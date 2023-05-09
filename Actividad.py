from typing import Dict, Any


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        # Inicializar variables para llevar el registro de las estadísticas
        num_solicitudes_total = 0
        solicitudes_por_metodo = {}
        solicitudes_por_codigo = {}
        tamano_total_respuesta = 0
        num_solicitudes_con_respuesta = 0
        url_solicitudes = {}

        # Abrir el archivo de logs y leer los datos línea por línea
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Parsear cada línea del archivo y extraer la información relevante
                direccion_ip = linea.split(' ')[2]
                fecha_hora = linea.split('[')[1].split(']')[0]
                metodo = linea.split('"')[1].split(' ')[0]
                url = linea.split('"')[1].split(' ')[1]
                codigo_respuesta = int(linea.split(' ')[-2])
                tamano_respuesta = int(linea.split(' ')[-1])

                # Actualizar las estadísticas correspondientes
                num_solicitudes_total += 1
                if metodo in solicitudes_por_metodo:
                    solicitudes_por_metodo[metodo] += 1
                else:
                    solicitudes_por_metodo[metodo] = 1
                if codigo_respuesta in solicitudes_por_codigo:
                    solicitudes_por_codigo[codigo_respuesta] += 1
                else:
                    solicitudes_por_codigo[codigo_respuesta] = 1
                tamano_total_respuesta += tamano_respuesta
                if codigo_respuesta != 0:
                    num_solicitudes_con_respuesta += 1
                if url in url_solicitudes:
                    url_solicitudes[url] += 1
                else:
                    url_solicitudes[url] = 1

        # Calcular estadísticas adicionales
        tamano_promedio_respuesta = tamano_total_respuesta / num_solicitudes_con_respuesta
        url_solicitudes = {k: v for k, v in
                           sorted(url_solicitudes.items(), key=lambda item: item[1], reverse=True)[:10]}

        # Crear un diccionario con las estadísticas calculadas
        estadisticas = {
            'num_solicitudes_total': num_solicitudes_total,
            'solicitudes_por_metodo': solicitudes_por_metodo,
            'solicitudes_por_codigo': solicitudes_por_codigo,
            'tamano_total_respuesta': tamano_total_respuesta,
            'tamano_promedio_respuesta': tamano_promedio_respuesta,
            'url_solicitudes': url_solicitudes
        }

        return estadisticas