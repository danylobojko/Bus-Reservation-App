// This is a header guard which prevents this file from being included multiple times.
#pragma once

// Include necessary libraries and files.
// For input-output stream.
#include <iostream>
// For using the string data type.
#include <string>
// For using strcpy.
#include <cstring>
// Includes an external file named Db.cpp which presumably contains a database class.
#include "Db.cpp"

// Use the standard namespace, allows the program to avoid prepending std:: to common functions and types.
using namespace std;

// Define a struct named TicketsResult to store the query results.
struct TicketsResult {
    // Pointer to an array of character arrays, used to store rows of ticket data.
    char** data;
    // Number of rows in the data.
    int rows;
};

// Define the BusReservation class.
class BusReservation {
public:
    // Define member variables for the database file and table name.
    string dbFile = "bus.db";
    string tableName = "busReservation";
    
    // Create an instance of the Db class (presumably defined in Db.cpp).
    Db db = Db(dbFile);

    // Constructor to initialize the BusReservation object.
    BusReservation() {
        // SQL query string to create a table if it does not already exist.
        string createTable = "CREATE TABLE IF NOT EXISTS " + tableName + " (id INTEGER PRIMARY KEY AUTOINCREMENT, bus INTEGER, seat INTEGER)";
        db.execute(createTable); // Execute the SQL query using the Db class.
    }

    // Method to buy a ticket.
    string buyTicket(int bus, int seat) {
        // SQL query string to check if the seat is already booked.
        string sql = "SELECT * FROM " + tableName + " WHERE bus = " + to_string(bus) + " AND seat = " + to_string(seat);
        auto result = db.query(sql); // Execute the query.
        
        // If the seat is already booked, return a message indicating that.
        if (result.size() > 0) {
            return "Seat " + to_string(seat) + " in bus " + to_string(bus) + " is already booked";
        }

        // SQL query string to insert a new ticket into the table.
        sql = "INSERT INTO " + tableName + " (bus, seat) VALUES (" + to_string(bus) + ", " + to_string(seat) + ")";
        db.execute(sql); // Execute the query.

        // Return a success message.
        return "Ticket for Bus: " + to_string(bus) + ", Seat: " + to_string(seat) + " bought successfully";
    }

    // Method to cancel a ticket.
    string cancelTicket(int bus, int seat) {
        // SQL query string to check if the seat is booked.
        string sql = "SELECT * FROM " + tableName + " WHERE bus = " + to_string(bus) + " AND seat = " + to_string(seat);
        auto result = db.query(sql); // Execute the query.

        // If the seat is not booked, return a message indicating that.
        if (result.size() == 0) {
            return "Seat " + to_string(seat) + " in bus " + to_string(bus) + " is not booked yet. Nothing to cancel";
        }

        // SQL query string to delete the ticket from the table.
        sql = "DELETE FROM " + tableName + " WHERE bus = " + to_string(bus) + " AND seat = " + to_string(seat);
        db.execute(sql); // Execute the query.

        // Return a success message.
        return "Ticket for Bus: " + to_string(bus) + ", Seat: " + to_string(seat) + " cancelled successfully";
    }

    // Method to get all tickets.
    TicketsResult getAllTickets() {
        // SQL query string to select all tickets from the table.
        string sql = "SELECT * FROM " + tableName;
        vector<vector<string>> result = db.query(sql); // Execute the query.

        // Convert the result to an array of character arrays.
        int rows = result.size();
        char** resultSet = new char*[rows];
        for (int i = 0; i < rows; i++) {
            string rowStr;
            for (const auto& value : result[i]) {
                rowStr += value + " ";
            }
            resultSet[i] = new char[rowStr.length() + 1];
            strcpy(resultSet[i], rowStr.c_str());
        }

        // Package the result into the TicketsResult struct.
        TicketsResult ticketsResult;
        ticketsResult.data = resultSet;
        ticketsResult.rows = rows;

        return ticketsResult; // Return the result.
    }

    // Method to free the memory allocated by getAllTickets.
    void freeAllTickets(char** tickets, int rows) {
        // Loop through each row and delete the allocated memory.
        for (int i = 0; i < rows; i++) {
            delete[] tickets[i];
        }
        delete[] tickets; // Delete the array itself.
    }
};
