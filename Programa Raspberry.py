import sys  #Importamos las librerías necesarias.
import requests
import json
from evdev import InputDevice, list_devices, ecodes, categorize

CODE_MAP_CHAR = {   #Creamos un mapa de caracteres, esto nos servirá para asociar caracteres a la lectura del lector de códigos QR. 
    'KEY_MINUS': "-",
    'KEY_SPACE': " ",    
    'KEY_U': "U",
    'KEY_W': "W",
    'KEY_BACKSLASH': "\\",
    'KEY_GRAVE': "`",
    'KEY_NUMERIC_STAR': "*",
    'KEY_NUMERIC_3': "3",
    'KEY_NUMERIC_2': "2",
    'KEY_NUMERIC_5': "5",
    'KEY_NUMERIC_4': "4",
    'KEY_NUMERIC_7': "7",
    'KEY_NUMERIC_6': "6",
    'KEY_NUMERIC_9': "9",
    'KEY_NUMERIC_8': "8",
    'KEY_NUMERIC_1': "1",
    'KEY_NUMERIC_0': "0",
    'KEY_E': "E",
    'KEY_D': "D",
    'KEY_G': "G",
    'KEY_F': "F",
    'KEY_A': "A",
    'KEY_C': "C",
    'KEY_B': "B",
    'KEY_M': "M",
    'KEY_L': "L",
    'KEY_O': "O",
    'KEY_N': "N",
    'KEY_I': "I",
    'KEY_H': "H",
    'KEY_K': "K",
    'KEY_J': "J",
    'KEY_Q': "Q",
    'KEY_P': "P",
    'KEY_S': "S",
    'KEY_X': "X",
    'KEY_Z': "Z",
    'KEY_KP4': "4",
    'KEY_KP5': "5",
    'KEY_KP6': "6",
    'KEY_KP7': "7",
    'KEY_KP0': "0",
    'KEY_KP1': "1",
    'KEY_KP2': "2",
    'KEY_KP3': "3",
    'KEY_KP8': "8",
    'KEY_KP9': "9",
    'KEY_5': "5",
    'KEY_4': "4",
    'KEY_7': "7",
    'KEY_6': "6",
    'KEY_1': "1",
    'KEY_0': "0",
    'KEY_3': "3",
    'KEY_2': "2",
    'KEY_9': "9",
    'KEY_8': "8",
    'KEY_LEFTBRACE': "[",
    'KEY_RIGHTBRACE': "]",    
    'KEY_COMMA': ",",
    'KEY_EQUAL': "=",    
    'KEY_SEMICOLON': ";",
    'KEY_APOSTROPHE': "'",
    'KEY_T': "T",
    'KEY_V': "V",
    'KEY_R': "R",
    'KEY_Y': "Y",
    'KEY_TAB': "\t",
    'KEY_DOT': ".",
    'KEY_SLASH': "/",
}

def parse_key_to_char(val):
    return CODE_MAP_CHAR[val] if val in CODE_MAP_CHAR else ""

if __name__ == "__main__":              # Imprimimos una lista de los dispositivos USB disponibles. Aquí, elegiremos el puerto del lector introduciendo el número correspondiente.
    print "List of your devices :"
    devices = [InputDevice(fn) for fn in list_devices()]
    for device in devices:
        print "\t{}\t{}".format(device.fn, device.name)
        
    print "Choose event ID :",          #Elegimos el dispositivo.
    event_id = raw_input()
    
    print "Exclusive access to device ? [1 or 0] : ",   #Permitimos acceso al dispositivo, esto hace que el lector solo se pueda utilizar en este programa.
    exclusive_access = raw_input()
    
    device = InputDevice('/dev/input/event{}'.format(event_id))  #Guardamos la lectura del lector en una variable llamada data. Hay que tener en cuenta que esta variable es un string.
    if int(exclusive_access) == 1:
        device.grab()
    data = ''

    for event in device.read_loop():        #Hacemos un bucle en el cual, siempre que haya una lectura, al pulsar la tecla enter se ejecutarán los if de debajo. La tecla enter se pulsa automaticamente después de leer un código QR.
        if event.type == ecodes.EV_KEY:
            e = categorize(event)
            if e.keystate == e.key_up:
                if e.keycode == "KEY_ENTER":
                    
                    response = requests.get("http://robotika.ddns.net/api/siguienteHabitacion") #Creamos una variable en la cual tenemos la url de la api que vamos a utilizar.
                    response = json.loads(response)
                    
                    if (data==str(response['room_id'])):            #Aquí comparamos la lectura del lector con el valor de la api. 
                        import serial, time
                        arduino = serial.Serial ('/dev/ttyACM0', 9600)
                        orden="a"                                   #Si ambos datos son iguales, la raspberry enviará por serie al arduino una "a" y este hará que los motores se paren.
                        envio= orden.encode ('utf-8')
                        arduino.write(envio)
                        url = "http://robotika.ddns.net/api/llegada/"
                        data=str(data)
                        llegada = requests.get(url,data)            #En esta parte nos comunicamos con el servidor enviandole el valor de data para comunicar que ya hemos llegado al lugar indicado.
                        
                    data = ''                                       #Por último, ponemos a 0 el valor de data para poder hacer la siguiente lectura. Este proceso se repetirá constantemente hasta que la Raspberry se apague o lo paremos manualmente.                  

                else:
                    data += parse_key_to_char(e.keycode) 
