"""Programa que emula actividades relacionadas a hoteles"""

import json
import os


class Hotel:
    """Clase para manejar hoteles y reservas"""
    FILE = "hotels.json"

    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms  # Numero total de habitaciones
        self.reservations = []  # Lista de reservas

    def to_dict(self):
        """Convierte el objeto a diccionario para almacenarlo"""
        return {
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms,
            "reservations": self.reservations
        }

    @staticmethod
    def save_hotels(hotels):
        """Guarda la lista de hoteles en un archivo"""
        with open(Hotel.FILE, "w", encoding="utf-8") as f:
            json.dump([hotel.to_dict() for hotel in hotels], f, indent=4)

    @staticmethod
    def load_hotels():
        """Carga los hoteles desde el archivo"""
        if not os.path.exists(Hotel.FILE):
            return []
        with open(Hotel.FILE, "r", encoding="utf-8") as f:
            hotel_data = json.load(f)
            hotels = []
            for data in hotel_data:
                # Se extraen los valores correctos sin pasar 'reservations' al constructor
                hotel = Hotel(data["name"], data["location"], data["rooms"])
                hotel.reservations = data.get("reservations", [])  # Se asigna después de la inicialización
                hotels.append(hotel)
            return hotels

    @staticmethod
    def find_hotel(name):
        """Encuentra un hotel por nombre"""
        hotels = Hotel.load_hotels()
        for hotel in hotels:
            if hotel.name.lower() == name.lower():
                return hotel
        return None

    def reserve_room(self, customer_name, reservation_id):
        """Realiza una reserva en el hotel"""
        if len(self.reservations) < self.rooms:
            self.reservations.append({"id": reservation_id, "customer": customer_name})
            return True
        return False


class Customer:
    """Clase para manejar clientes"""

    FILE = "customers.json"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte el objeto a diccionario para almacenarlo"""
        return {"name": self.name, "email": self.email}

    @staticmethod
    def save_customers(customers):
        """Guarda los clientes en un archivo"""
        with open(Customer.FILE, "w", encoding="utf-8") as f:
            json.dump([customer.to_dict() for customer in customers], f, indent=4)

    @staticmethod
    def load_customers():
        """Carga los clientes desde el archivo"""
        if not os.path.exists(Customer.FILE):
            return []
        with open(Customer.FILE, "r", encoding="utf-8") as f:
            return [Customer(**customer) for customer in json.load(f)]

    @staticmethod
    def find_customer(name):
        """Encuentra un cliente por nombre"""
        customers = Customer.load_customers()
        for customer in customers:
            if customer.name.lower() == name.lower():
                return customer
        return None


class Reservation:
    """Clase para manejar reservas"""

    FILE = "reservations.json"

    def __init__(self, customer_name, hotel_name, reservation_id):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.reservation_id = reservation_id

    def to_dict(self):
        """Convierte el objeto a diccionario para almacenarlo"""
        return {
            "customer_name": self.customer_name,
            "hotel_name": self.hotel_name,
            "reservation_id": self.reservation_id
        }

    @staticmethod
    def save_reservations(reservations):
        """Guarda las reservas en un archivo"""
        with open(Reservation.FILE, "w", encoding="utf-8") as f:
            json.dump([res.to_dict() for res in reservations], f, indent=4)

    @staticmethod
    def load_reservations():
        """Carga las reservas desde el archivo"""
        if not os.path.exists(Reservation.FILE):
            return []
        with open(Reservation.FILE, "r", encoding="utf-8") as f:
            return [Reservation(**res) for res in json.load(f)]
