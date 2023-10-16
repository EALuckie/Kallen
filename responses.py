#responses.py
'''
RESPUESTAS ESPAÑOL
'''
import random

hola=["Hola cara de bola", "Hola crayola", "Holiwis", "¿Qué pedo?", "Sup bitch?", "Wenas"]

def handle_response(user_message) -> str:
    m= user_message.lower();
    if "kallen" in m:
        if m == "kallen hola" or "kallen":
            n= random.choice(hola)
            return n
        if m=="kallen adios":
            return "Sayounara!!"
        else:
            return "Instrucción no reconocida \n Sorry!"
    else:
        return 
    
def main():
    """The main function in case we need it"""
    print("Hello from responses.py main function");
    #handle_response("!Help");

if __name__ == '__main__':
    main();