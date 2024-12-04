

import random
from clase_cliente import UsuarioDAO, registrar_usuario, iniciar_sesion, Usuario
from clase_plan import PlanDAO, crear_planes, Plan
from datetime import datetime

def mostrar_menu():
    usuario_dao = UsuarioDAO()  # Crear una instancia de UsuarioDAO
    plan_dao = PlanDAO()  # Crear una instancia de PlanDAO
    crear_planes(plan_dao)  # Crear los planes en la base de datos

    usuario_actual = None  # Variable para almacenar el usuario actual

    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(usuario_dao)
        elif opcion == '2':
            usuario_data = iniciar_sesion(usuario_dao)  # Almacena el usuario actual
            if usuario_data:
                usuario_actual = Usuario(*usuario_data)  # Crea un objeto Usuario
                print(f"Bienvenido, {usuario_actual.nombre}!")
                
                # Mostrar planes disponibles después de iniciar sesión
                elegir_plan(plan_dao, usuario_actual)  # Pasar el usuario al elegir plan
            else:
                print("Credenciales incorrectas.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def elegir_plan(plan_dao, usuario):
    planes = plan_dao.get_planes()
    print("\n--- Planes Disponibles ---")
    for plan in planes:
        print(f"ID: {plan[0]}, {plan[1]} a ${plan[3]} (Velocidad: {plan[2]}Mb)")

    plan_id = int(input("Seleccione el ID del plan que desea elegir: "))
    
    # Verificar si el ID del plan es válido
    if 1 <= plan_id <= len(planes):
        plan_elegido = planes[plan_id - 1]
        mostrar_contrato(usuario, plan_elegido)
    else:
        print("ID de plan no válido. Intente nuevamente.")

def mostrar_contrato(usuario, plan):
    fecha_instalacion = datetime.now().strftime("%d/%m/%Y %H:%M")
    modem_id = random.randint(100000, 999999)  # Generar un ID de módem aleatorio de 6 dígitos
    print("\n--- Contrato ---")
    print(f"Nombre: {usuario.nombre} {usuario.apellido}")
    print(f"DNI: {usuario.dni}")
    print(f"Plan Elegido: {plan[1]} (ID: {plan[0]})")
    print(f"Velocidad: {plan[2]} Mb")
    print(f"Precio: ${plan[3]}")
    print(f"Fecha y Hora de Instalación: {fecha_instalacion}")
    print(f"ID de Módem: {modem_id}")  # Mostrar el ID de módem
    print("\n--- Gracias por elegirnos! ---")

if __name__ == "__main__":
    mostrar_menu()