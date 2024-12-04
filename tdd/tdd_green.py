import unittest
from clase_cliente import Usuario, UsuarioDAO

class TestUsuario(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.usuario_dao = UsuarioDAO()  # Simulamos el acceso a la base de datos
        self.usuario = Usuario(
            nombre="Juan",
            apellido="Pérez",
            dni="12345678",
            email="juan.perez@example.com",
            password="contraseña123",
            telefono="123456789",
            direccion="Calle Falsa 123"
        )

    def test_validar_dni(self):
        """Prueba que el DNI sea válido."""
        self.assertTrue(self.usuario.validar_dni())
        
        # Probar un DNI inválido
        self.usuario.dni = "1234567"  # Menos de 8 dígitos
        self.assertFalse(self.usuario.validar_dni())

    def test_validar_email(self):
        """Prueba que el email sea válido."""
        self.assertTrue(self.usuario.validar_email())
        
        # Probar un email inválido
        self.usuario.email = "juan.perez@com"  # Formato incorrecto
        self.assertFalse(self.usuario.validar_email())

    def test_registrar_usuario(self):
        """Prueba el registro de un usuario."""
        # Simulamos el registro
        self.usuario_dao.Registrar_cliente(self.usuario)
        
        # Verificamos que el usuario se haya registrado correctamente
        registrado = self.usuario_dao.iniciar_sesion(self.usuario.email, self.usuario.password)
        self.assertIsNotNone(registrado)

    def test_iniciar_sesion(self):
        """Prueba el inicio de sesión de un usuario."""
        self.usuario_dao.Registrar_cliente(self.usuario)
        
        # Intentar iniciar sesión con credenciales correctas
        self.assertIsNotNone(self.usuario_dao.iniciar_sesion(self.usuario.email, self.usuario.password))
        
        # Intentar iniciar sesión con credenciales incorrectas
        self.assertIsNone(self.usuario_dao.iniciar_sesion(self.usuario.email, "contraseña_incorrecta"))

if __name__ == '__main__':
    unittest.main()