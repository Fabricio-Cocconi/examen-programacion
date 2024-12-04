# clase_cliente.py

class Usuario:
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

class UsuarioDAO:
    def __init__(self):
        self.usuarios = []  # Simulación de base de datos

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

def registrar_usuario(usuario_dao):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    
    nuevo_usuario = Usuario(nombre, apellido, email, contraseña)
    usuario_dao.agregar_usuario(nuevo_usuario)
    print("Usuario registrado exitosamente.")

def iniciar_sesion(usuario_dao):
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    
    usuario = usuario_dao.buscar_usuario(email)
    if usuario and usuario.contraseña == contraseña:
        return (usuario.nombre, usuario.apellido, usuario.email, usuario.contraseña)
    return None