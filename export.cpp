#include <string>
// Include the BusReservation C++ class from busReservation.cpp file.
#include "busReservation.cpp"

using namespace std;

// Specify that the functions inside this block have C linkage.
extern "C" {

    // Function to create a new instance of BusReservation and return a pointer to it.
    __attribute__ ((visibility ("default"))) BusReservation* BusReservation_constructor() {
        return new BusReservation(); // Allocate a new BusReservation on the heap and return its pointer.
    }

    // Function to buy a ticket by calling the buyTicket method of BusReservation.
    __attribute__ ((visibility ("default"))) const char* BusReservation_buyTicket(BusReservation* cls, int bus, int seat) {
        // Call the buyTicket method of BusReservation and store the result in a string.
        string result = cls->buyTicket(bus, seat);
        // Convert the string to a C-style string.
        char* cstr = new char[result.length() + 1];
        strcpy(cstr, result.c_str());
        return cstr; // Return the C-style string.
    }

    // Function to cancel a ticket by calling the cancelTicket method of BusReservation.
    __attribute__ ((visibility ("default"))) const char* BusReservation_cancelTicket(BusReservation* cls, int bus, int seat) {
        // Call the cancelTicket method of BusReservation and store the result in a string.
        string result = cls->cancelTicket(bus, seat);
        // Convert the string to a C-style string.
        char* cstr = new char[result.length() + 1];
        strcpy(cstr, result.c_str());
        return cstr; // Return the C-style string.
    }

    // Function to get all tickets by calling the getAllTickets method of BusReservation.
    __attribute__ ((visibility ("default"))) TicketsResult BusReservation_getAllTickets(BusReservation* cls) {
        return cls->getAllTickets(); // Call the getAllTickets method and return the result.
    }

    // Function to free the memory allocated by getAllTickets.
    __attribute__ ((visibility ("default"))) void BusReservation_freeAllTickets(BusReservation* cls, char** tickets, int rows) {
        cls->freeAllTickets(tickets, rows); // Call the freeAllTickets method.
    }
}
