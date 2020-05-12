import keyboard
import time
import random
import re
import os

## EDIT THIS --- EDIT THIS --- EDIT THIS --- EDIT THIS

# SIN HYPHENS
numero_estudiante = "802190000"
# Código permanente que puedes setear en home.uprm.edu
codigo_permanente = "0000"
# Últimos 4 dígitos
seguro_social = "0000"
# MMDDYYYY
fecha_nacimiento = "01012000"
#  1 = 1er semestre, 2 = 2do semestre, 3 = 1er verano, 4 = 2do verano
semestre = 1
# Lista de tuplos. No olvides poner pares (CURSO, SECCION) separados por coma
cursos = [
        ("MATE3032", "001"),
        ("INGE3015", "001"),
        ("FISI3171", "001"),
        ]

## EDIT THIS --- EDIT THIS --- EDIT THIS --- EDIT THIS

pause_time = 0.1
pause = False


def make_pause(e):
    global pause
    pause = not pause

keyboard.on_press_key("shift", make_pause)


def access_portal():
    keyboard.press_and_release("win+r")
    time.sleep(0.1)

    write_command("cmd\n", 0.5, 0)

    write_command(f'cd "{os.path.dirname(os.path.abspath(__file__))}"\n', 0.25, 0)
    write_command("setup.bat\n", 0.25, 0)

    write_command(f'cd "{os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssh")}"\n', 0.01, 0)
    write_command("ssh estudiante@rumad.uprm.edu\n", 0, 0)

    keyboard.wait('enter')
    time.sleep(1)
    
def write_command(message, sleep=0.5, interval=None):
    if interval == None:
        interval = 0.15/random.randint(1,3)
    for char in str(message):
        keyboard.write(str(char), exact=True)
        time.sleep(float(interval))
    time.sleep(float(sleep))

def validate_input(message, regex, error_message, prefix="[<<] ", error_prefix="[✗] "):
    message = message.strip() + " "
    error_message = error_message.strip()

    user_input = input(prefix + message)
    user_input.strip()

    while not re.match(regex, user_input):
        user_input = input(error_prefix + error_message + ". " + message)
        user_input.strip()

    return user_input

def main(get_inputs = True):
    global numero_estudiante
    global codigo_permanente
    global seguro_social
    global fecha_nacimiento
    global semestre
    global cursos
    global pause_time
    global pause

    if get_inputs:
        numero_estudiante = validate_input(
                "Entre su número de estudiante:",
                r'\d{3}-\d{2}-\d{4}',
                "Su número de estudiante debe tener el formato xxx-xx-xxxx")

        while "-" in numero_estudiante:
            numero_estudiante = numero_estudiante.replace("-", "")

        codigo_permanente = validate_input(
                "Entre su código permanente:",
                r'\d{4}',
                "Su código permanente debe tener el formato xxxx")

        seguro_social = validate_input(
                "Entre los últimos 4 dígitos de su seguro social:",
                r'\d{4}',
                "Sus dígitos del seguro social debe tener el formato xxxx")

        fecha_nacimiento = validate_input(
                "Entre fecha de nacimiento en formato MMDDYYY:",
                r'\d{4}',
                "No olvide introducir '0' donde hayan dígitos sencillos (1-enero-2000 = 01012000)")

        semestre = validate_input(
                "Entre el semestre que quiere tomar:",
                r'[1-4]',
                "(1 = 1er semestre, 2 = 2do semestre, 3 = 1er verano, 4 = 2do verano)")

        cursos = []

        print("[!] Entre todos los cursos que desee tomar. Deje entrada vacía para terminar")
        while True:
            curso = validate_input(
                    "Entre codificación del curso: ",
                    r'(?:\w{4}[ -]?\d{4}|)',
                    "El formato debe ser 'LLLLxxxx' o 'LLLL xxxx' o 'LLLL-xxxx'")

            if "-" in curso:
                curso = curso.replace("-", "")
            if " " in curso:
                curso = curso.replace(" ", "")
            

            if curso == "":
                break

            seccion = validate_input(
                    "Entre sección del curso: ",
                    r'(?:\d{2,3}\w?|)',
                    "No olvide incluir los '0' correspondientes y solo hasta 1 letra con el tipo de curso")

            if seccion == "":
                break

            cursos.append( (curso, seccion) )
    #  else:
        #  numero_estudiante = "802190000"
        #  codigo_permanente = "0000"
        #  seguro_social = "0000"
        #  fecha_nacimiento = "01012000"
        #  semestre = 1
        #  #  1 = 1er semestre, 2 = 2do semestre, 3 = 1er verano, 4 = 2do verano
        #  cursos = [("MATE4031", "120")]


    def entrar_cursos():
        # Entrar curso y sección uno a uno
        for curso, seccion in cursos:
            write_command(curso, pause_time)
            write_command("\n")
            write_command(seccion, pause_time)
            write_command("\n")
    
    commands = [
        lambda: access_portal(),

        # Entrar a matrícula
        lambda: write_command(2, pause_time, 0.01),

        # Entrar credenciales
        lambda: write_command(numero_estudiante, pause_time, 0.01),
        lambda: write_command(codigo_permanente, pause_time, 0.01),
        lambda: write_command(seguro_social, pause_time, 0.01),
        lambda: write_command(fecha_nacimiento, pause_time, 0.01),

        # Entrar cuál sesión de clases (verano, etc.) a utilizar
        lambda: write_command(semestre, pause_time, 0.01),

        # Dar de "Alta"
        lambda: write_command("A", pause_time, 0.01),

        lambda: entrar_cursos()
    ]


    for i in range(len(commands)):
        while pause:
            pass
        commands[i]()



if __name__=="__main__":
    time.sleep(1)
    main(False)
