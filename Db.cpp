// This is a header guard which prevents this file from being included multiple times.
#pragma once

// Include necessary libraries and files.
// For input-output stream.
#include <iostream>
// For using vectors.
#include <vector>
// For using the string data type.
#include <string>
// For SQLite3 database functionality.
// #include "sqlite/sqlite3.h"
#include <sqlite3.h>

// Use the standard namespace, allows the program to avoid prepending std:: to common functions and types.
using namespace std;

// Define the Db class.
class Db {
private:
    sqlite3* db_; // Pointer to the SQLite database.

    // Static callback function used to process the result of a SELECT statement.
    static int callback(void* data, int argc, char** argv, char** azColName) {
        // Convert the void pointer to vector<vector<string>> pointer.
        vector<vector<string>>* result = static_cast<vector<vector<string>>*>(data);

        vector<string> row; // Vector to hold a single row of results.
        // Iterate over each column in the result row.
        for (int i = 0; i < argc; i++) {
            // Push the value of each column into the row vector. If NULL, store the string "NULL".
            row.push_back(argv[i] ? argv[i] : "NULL");
        }

        // Push the row into the result vector.
        result->push_back(row);
        return 0; // 0 indicates success.
    }

public:
    // Constructor: Takes the filename as an argument and opens the SQLite database.
    Db(const string& filename) {
        int result = sqlite3_open(filename.c_str(), &db_); // Open database file.
        // If opening the database fails, print error message and exit.
        if (result != SQLITE_OK) {
            cerr << "Error opening database: " << sqlite3_errmsg(db_) << endl;
            exit(1);
        }
    }

    // Destructor: Closes the SQLite database when the Db object is destroyed.
    ~Db() {
        sqlite3_close(db_); // Close the database.
    }

    // Method for executing SQL queries that return data (e.g., SELECT statements).
    vector<vector<string>> query(const string& sql) {
        vector<vector<string>> result; // Vector to store the result of the query.

        // Execute the SQL query and process the result through the callback function.
        int rc = sqlite3_exec(db_, sql.c_str(), callback, &result, nullptr);
        // If there was an error executing the query, print error message.
        if (rc != SQLITE_OK) {
            cerr << "Error executing query: " << sqlite3_errmsg(db_) << endl;
        }

        return result; // Return the result of the query.
    }

    // Method for executing SQL queries that do not return data (e.g., CREATE, INSERT).
    void execute(const string& sql) {
        char* errMsg; // Pointer to store error message.
        // Execute the SQL query.
        int rc = sqlite3_exec(db_, sql.c_str(), nullptr, nullptr, &errMsg);
        // If there was an error executing the query, print error message.
        if (rc != SQLITE_OK) {
            cerr << "Error executing create table query: " << errMsg << endl;
            sqlite3_free(errMsg); // Free the memory allocated for error message.
        }
    }
};
