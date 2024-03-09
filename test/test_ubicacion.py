import unittest
from main import admin_ubicacion, Ubicacion 

class TestAdminUbicacion(unittest.TestCase):
    def setUp(self):
        self.user = Ubicacion("direccion", "ciudad", "pais")

    def test_modificar_ubicacion(self):
        self.user.ubicacio_n = Ubicacion("direccion1", "ciudad1", "pais1")
        admin_ubicacion(self.user, 1, "direccion2", "ciudad2", "pais2")
        self.assertEqual(self.user.ubicacio_n.direccion, "direccion2")
        self.assertEqual(self.user.ubicacio_n.ciudad, "ciudad2")
        self.assertEqual(self.user.ubicacio_n.pais, "pais2")

    def test_ver_ubicacion(self):
        self.user.ubicacio_n = Ubicacion("direccion1", "ciudad1", "pais1")
        result = admin_ubicacion(self.user, 2)
        self.assertEqual(result, str(self.user.ubicacio_n))

if __name__ == "__main__":
    unittest.main()