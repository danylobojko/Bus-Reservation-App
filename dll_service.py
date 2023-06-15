# ctypes is a foreign function library for Python. It provides C compatible data types.
import ctypes
# os module provides a way of using operating system dependent functionality.
import os
# csv module implements classes to read and write tabular data in CSV format.
import csv
# StringIO module implements an in-memory file-like object, useful for working with strings as file-like objects.
from io import StringIO

# Construct the path to the DLL file.
PATH_TO_LIB = os.getcwd() + "/cpp/busReservation.dll"


# Define a C structure using ctypes. This structure corresponds to the structure defined in the DLL.
class TicketsResult(ctypes.Structure):
    _fields_ = [("data", ctypes.POINTER(ctypes.c_char_p)),
                ("rows", ctypes.c_int)]


# Define the DLLService class which serves as a Python wrapper around the DLL.
class DLLService:
    def __init__(self):
        # Load the DLL.
        self.dll = ctypes.CDLL(PATH_TO_LIB)

        # Map the constructor function from the DLL.
        self.constructorFn = self.dll.BusReservation_constructor
        self.constructorFn.argtypes = []
        self.constructorFn.restype = ctypes.c_void_p

        # Map the buyTicket function from the DLL.
        self.buyTicketFn = self.dll.BusReservation_buyTicket
        self.buyTicketFn.argtypes = [
            ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        self.buyTicketFn.restype = ctypes.c_char_p

        # Map the cancelTicket function from the DLL.
        self.cancelTicketFn = self.dll.BusReservation_cancelTicket
        self.cancelTicketFn.argtypes = [
            ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
        self.cancelTicketFn.restype = ctypes.c_char_p

        # Map the getAllTickets function from the DLL.
        self.getAllTicketsFn = self.dll.BusReservation_getAllTickets
        self.getAllTicketsFn.argtypes = [ctypes.c_void_p]
        self.getAllTicketsFn.restype = TicketsResult

        # Map the freeAllTickets function from the DLL.
        self.freeAllTicketsFn = self.dll.BusReservation_freeAllTickets
        self.freeAllTicketsFn.argtypes = [
            ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int]
        self.freeAllTicketsFn.restype = None

        # Create an instance of the class defined in the DLL.
        self.instance = self.constructorFn()

    # Define a method to buy a ticket.
    def buyTicket(self, bus, seat):
        # Call the buyTicket function from the DLL.
        result_raw = self.buyTicketFn(self.instance, bus, seat)
        # Decode the result to a Python string.
        result = result_raw.decode()
        return result

    # Define a method to cancel a ticket.
    def cancelTicket(self, bus, seat):
        # Call the cancelTicket function from the DLL.
        result_raw = self.cancelTicketFn(self.instance, bus, seat)
        # Decode the result to a Python string.
        result = result_raw.decode()
        return result

    # Define a method to get all tickets.
    def getAllTickets(self):
        # Call the getAllTickets function from the DLL.
        tickets_result = self.getAllTicketsFn(self.instance)
        data = tickets_result.data
        rows = tickets_result.rows
        result = []

        # Process the raw data returned from the DLL
        for i in range(rows):
            parts = data[i].decode().strip().split()
            ticket = {"id": int(parts[0]), "bus": int(
                parts[1]), "seat": int(parts[2])}
            result.append(ticket)

        # Free the memory allocated by the getAllTickets function in the DLL
        self.freeAllTicketsFn(self.instance, data, rows)

        return result
