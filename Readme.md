# Tech Society Applicant Tracker

A command-line student society management system built purely on Object-Oriented Programming (OOP) concepts[cite: 10]. This project is designed to manage applicant states, track recruitment statuses, and enforce society-wide rules efficiently[cite: 10].

## Core Features
* **State Management**: Utilizes instance variables to maintain unique data per applicant, while class variables track global states like total applicant counts and recruitment caps[cite: 10, 11].
* **Encapsulation**: Keeps evaluation logic and status transitions strictly within class methods to prevent external interference[cite: 10].
* **Data Validation**: Automatically verifies institutional formatting for roll numbers before object creation[cite: 10].

## Class Architecture

### 1. `Applicant` Class
The core entity representing an individual student applying for a position[cite: 10].
* **Instance Variables**: Stores Name, Roll Number, Technical Domain, and Status (default: "Under Review")[cite: 10].
* **Class Variable**: `Total Count` (increments automatically upon new instantiation)[cite: 10].
* **Instance Method**: `Evaluate Score` (accepts interview score and updates status to "Accepted", "Probation", or "Rejected")[cite: 10].
* **Static Method**: `Validate Roll No` (verifies the roll number is exactly 8 digits)[cite: 10].
* **Class Method**: `Alternative Init` (parses a comma-separated string to return a fully formed Applicant instance)[cite: 10].

### 2. `SocietyTracker` Class
The aggregate manager class responsible for housing the roster and enforcing operational rules[cite: 11].
* **Instance Variables**: Stores Society Name and the Registry State (a list holding verified Applicant objects)[cite: 11].
* **Class Variable**: `Recruitment Quota` (global cap for inducted students)[cite: 11].
* **Instance Method**: `Register Applicant` (checks current registry size against the quota and appends the applicant if space permits)[cite: 11].
* **Class Method**: `Update Quota` (modifies the global recruitment limit)[cite: 11].
