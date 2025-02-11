"""
Modulo de pruebas unitarias para hotel_system.py.

Este modulo usa unittest para verificar el correcto funcionamiento
de las clases Hotel, Customer y Reservation.
"""

import sys
import unittest
import os
from hotel_system import Hotel, Customer, Reservation
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))



class TestHotel(unittest.TestCase):
    """Pruebas para la clase Hotel"""

    def setUp(self):
        """Configura un hotel antes de cada prueba"""
        self.hotel = Hotel("Grand Hotel", "CDMX", 10)

    def tearDown(self):
        """Limpia archivos generados en las pruebas"""
        if os.path.exists(Hotel.FILE):
            os.remove(Hotel.FILE)

    def test_crear_hotel(self):
        """Verifica que los atributos del hotel sean correctos"""
        self.assertEqual(self.hotel.name, "Grand Hotel")
        self.assertEqual(self.hotel.location, "CDMX")
        self.assertEqual(self.hotel.rooms, 10)

    def test_guardar_y_cargar_hoteles(self):
        """Prueba guardar y cargar hoteles desde un archivo"""
        Hotel.save_hotels([self.hotel])
        loaded_hotels = Hotel.load_hotels()
        self.assertEqual(len(loaded_hotels), 1)
        self.assertEqual(loaded_hotels[0].name, "Grand Hotel")

    def test_encontrar_hotel(self):
        """Prueba encontrar un hotel por su nombre"""
        Hotel.save_hotels([self.hotel])
        hotel_encontrado = Hotel.find_hotel("Grand Hotel")
        self.assertIsNotNone(hotel_encontrado)
        self.assertEqual(hotel_encontrado.name, "Grand Hotel")

    def test_reservar_habitacion_exito(self):
        """Verifica que se puede realizar una reserva"""
        result = self.hotel.reserve_room("Juan Perez", 1)
        self.assertTrue(result)
        self.assertEqual(len(self.hotel.reservations), 1)

    def test_reservar_habitacion_falla(self):
        """Verifica que no se pueda reservar si el hotel esta lleno"""
        for i in range(10):
            self.hotel.reserve_room(f"Cliente {i}", i)
        result = self.hotel.reserve_room("Cliente Extra", 11)
        self.assertFalse(result)


class TestCustomer(unittest.TestCase):
    """Pruebas para la clase Customer"""

    def setUp(self):
        """Configura un cliente antes de cada prueba"""
        self.customer = Customer("Maria Lopez", "maria@example.com")

    def tearDown(self):
        """Limpia archivos generados en las pruebas"""
        if os.path.exists(Customer.FILE):
            os.remove(Customer.FILE)

    def test_crear_cliente(self):
        """Verifica que los atributos del cliente sean correctos"""
        self.assertEqual(self.customer.name, "Maria Lopez")
        self.assertEqual(self.customer.email, "maria@example.com")

    def test_guardar_y_cargar_clientes(self):
        """Prueba guardar y cargar clientes desde un archivo"""
        Customer.save_customers([self.customer])
        loaded_customers = Customer.load_customers()
        self.assertEqual(len(loaded_customers), 1)
        self.assertEqual(loaded_customers[0].name, "Maria Lopez")

    def test_encontrar_cliente(self):
        """Prueba encontrar un cliente por su nombre"""
        Customer.save_customers([self.customer])
        cliente_encontrado = Customer.find_customer("Maria Lopez")
        self.assertIsNotNone(cliente_encontrado)
        self.assertEqual(cliente_encontrado.name, "Maria Lopez")


class TestReservation(unittest.TestCase):
    """Pruebas para la clase Reservation"""

    def setUp(self):
        """Configura una reserva antes de cada prueba"""
        self.reservation = Reservation("Maria Lopez", "Grand Hotel", 101)

    def tearDown(self):
        """Limpia archivos generados en las pruebas"""
        if os.path.exists(Reservation.FILE):
            os.remove(Reservation.FILE)

    def test_crear_reserva(self):
        """Verifica que los atributos de la reserva sean correctos"""
        self.assertEqual(self.reservation.customer_name, "Maria Lopez")
        self.assertEqual(self.reservation.hotel_name, "Grand Hotel")
        self.assertEqual(self.reservation.reservation_id, 101)

    def test_guardar_y_cargar_reservas(self):
        """Prueba guardar y cargar reservas desde un archivo"""
        Reservation.save_reservations([self.reservation])
        loaded_reservations = Reservation.load_reservations()
        self.assertEqual(len(loaded_reservations), 1)
        self.assertEqual(loaded_reservations[0].customer_name, "Maria Lopez")


if __name__ == "__main__":
    unittest.main()
