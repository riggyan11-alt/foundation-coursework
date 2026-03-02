\# ST4015CMD — Foundations of Computer Science

\## Investigation and Analysis of Computing Data for Data Management



\*\*Student:\*\* Riggyan  

\*\*Student ID:\*\* \250325
\*\*Institution:\*\* Softwarica College of IT and E-Commerce  

\*\*Module:\*\* ST4015CMD — Foundations of Computer Science  



---



\## Overview



This repository contains the complete coursework submission for ST4015CMD. 

The project investigates core computing concepts including data encoding, 

algorithmic problem solving, and relational database design. Each task is 

organised into its own folder with all relevant scripts and outputs.



---



\## Repository Structure



| Folder  | File                      | Description                                      |

|---------|---------------------------|--------------------------------------------------|

| Task1/  | encoding\_demo.py          | Demonstrates Base64, URL, Hex encoding and SHA-256 hashing |

| Task2/  | brute\_force\_seating.py    | Solves seating problem by checking all permutations |

| Task2/  | heuristic\_seating.py      | Solves seating problem using a smart heuristic approach |

| Task3/  | schema.sql                | SQL script to create and populate the database   |

| Task3/  | er\_diagram.png            | Entity-Relationship diagram generated from MySQL Workbench |



---



\## Task 1 — Data Encoding



The script encoding\_demo.py demonstrates four different encoding and hashing techniques:



\- \*\*Base64 Encoding\*\* — Converts text into a Base64 encoded string and decodes it back

\- \*\*URL Encoding\*\* — Encodes special characters in a URL query string

\- \*\*Hex Encoding\*\* — Converts text into its hexadecimal representation

\- \*\*SHA-256 Hashing\*\* — Generates a secure one-way hash of a message



\### How to Run Task 1

Make sure Python 3 is installed, then run:

---



\## Task 2 — Seating Problem Solver



This task solves a constrained seating arrangement problem where students 

cannot sit next to their friends or next to someone from the same city.

Two approaches are implemented and compared:



\- \*\*Brute Force\*\* — Generates every possible permutation and checks each one against the constraints until a valid arrangement is found

\- \*\*Heuristic\*\* — Uses a smarter strategy by sorting students by how constrained they are first, then placing them one by one into valid positions



---



\## Task 3 — Relational Database and ER Diagram



A normalised relational database was designed for a college clubs management system.

The database contains three tables:



\- \*\*Student\*\* — Stores student ID, name and email

\- \*\*Club\*\* — Stores club ID, name, room and mentor

\- \*\*Membership\*\* — Links students to clubs with a join date (junction table)



The schema follows Third Normal Form (3NF) to eliminate data redundancy.

Foreign keys enforce referential integrity between tables.



\### How to Run Task 3

1\. Install MySQL and open MySQL Workbench

2\. Connect to your local MySQL server

3\. Open and run schema.sql to create the database, tables and insert all sample data

4\. View er\_diagram.png for the full Entity-Relationship diagram



---



---



\## Technologies Used



\- Python 3

\- MySQL 8.0

\- MySQL Workbench

\- Git and GitHub



