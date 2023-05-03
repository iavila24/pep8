# Clases con CamelCase
# Identacion: 4 espacios (no tabs)
# Parametros separados por comas separados por 1 espacio
# Variables con snake_case
# 2 Espacios entre operadores
# Terminar scripts con un salto de linea
# https://pep8.org/

class UserAdmin():


    def __init__(self, username, password = ''):
        self.username = username
        self.password = password


    def set_password(self):
        pass


cody_user = UserAdmin('Cody')
