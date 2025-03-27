import re

def cargar_mensajes(ruta_archivo):
    # Patrón más flexible para reconocer líneas de mensajes de WhatsApp
    pattern = r'^\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} - [^:]+: .+'
    
    # Lista para almacenar los mensajes
    messages = []
    
    # Leer el archivo y filtrar los mensajes
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                # Eliminar saltos de línea y espacios al inicio y final
                linea = linea.strip()
                
                # Comprobar si la línea coincide con el patrón de mensaje
                if re.match(pattern, linea):
                    messages.append(linea)
        
        return messages
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def contadorpalabra(messages, palabra):
    palabra = palabra.lower()
    contador = sum(line.lower().count(palabra) for line in messages)
    return contador

# Cargar los mensajes
messages = cargar_mensajes("WhatsappChat.txt")

# Imprimir número de mensajes encontrados
print(f"Mensajes encontrados: {len(messages)}")

# Buscar una palabra específica
palabra_buscada = "te echo de menos"
veces_encontrada = contadorpalabra(messages, palabra_buscada)
print(f'La palabra "{palabra_buscada}" fue encontrada {veces_encontrada} veces.')