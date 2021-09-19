"""
DO NOT MODIFY ANY VARIABLE NAMES. YOU MAY COMMENT YOUR CODE IF NEEDED. 
"""

# You must fill in your Pennkey and your 8 digit Penn ID below:

pennkey = "cheng24"
penn_id = "57477468"

# The database you set up on RDS - SPECIFICALLY FOR SUBMISSION

db_config = {
    "username" : "admin",
    "host": "database-2.cl03devemfhy.us-east-2.rds.amazonaws.com",
    "port": "3306",
    "password": "88888888"
}


# MYSQL QUERIES (Part 2)

# Fill in DDL statements in the order of execution. A deduction might be applied for an incorrect order.
# Create query for Courses
answer1a = """
CREATE TABLE Courses(CID varchar(10), name varchar(25), PRIMARY KEY (CID));
INSERT INTO Courses (CID, name) VALUES ("CIS121", "Data Structures"), ("CIS160",
"Discrete Math"), ("CIS320", "Algorithms"), ("CIS550","Databases");
"""

# Create query for Students
answer1b = """
CREATE TABLE Students(SID int, name varchar(25), PRIMARY KEY(SID));
INSERT INTO Students (SID, name) VALUES (1, "Alice"), (2, "Paul"), (3, "Carrie");
"""

# Create query for Prereqs
answer1c = """
CREATE TABLE Prereqs(CID varchar(10), PRIMARY KEY (CID), FOREIGN KEY (CID) REFERENCES Courses (CID));
INSERT INTO Prereqs(CID) VALUES ("CIS121"), ("CIS160");
"""

# Create query for Takes
answer1d = """
CREATE TABLE Takes(SID int, CID varchar(10), PRIMARY KEY (SID, CID), FOREIGN KEY (SID) REFERENCES Students (SID), FOREIGN KEY (CID) REFERENCES Courses (CID));
INSERT INTO Takes (SID, CID) VALUES (1, "CIS121"), (1, "CIS160"), (2, "CIS121"),
(2, "CIS160"), (2, "CIS320"), (3, "CIS121"), (3, "CIS320");
"""

answer2 = """
SELECT DISTINCT SID
FROM Takes 
WHERE CID IN ("CIS160", "CIS121");
"""

answer3 = """
SELECT DISTINCT CID
FROM Takes
ORDER BY CID ASC;
"""

answer4 = """
SELECT DISTINCT SID
FROM Takes t
JOIN Prereqs p
ON t.CID = p.CID;
"""

answer5 = """
SELECT s.name AS studentName, c.name AS courseName
FROM Takes t
JOIN Courses c
ON t.CID = t.CID
JOIN Students s
ON t.SID = s.SID;
"""

