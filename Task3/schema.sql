CREATE TABLE Student (
    StudentID   INT          NOT NULL,
    StudentName VARCHAR(100) NOT NULL,
    Email       VARCHAR(150) NOT NULL UNIQUE,
    PRIMARY KEY (StudentID)
);

CREATE TABLE Club (
    ClubID     INT          NOT NULL AUTO_INCREMENT,
    ClubName   VARCHAR(100) NOT NULL,
    ClubRoom   VARCHAR(20),
    ClubMentor VARCHAR(100),
    PRIMARY KEY (ClubID)
);

CREATE TABLE Membership (
    MembershipID INT  NOT NULL AUTO_INCREMENT,
    StudentID    INT  NOT NULL,
    ClubID       INT  NOT NULL,
    JoinDate     DATE NOT NULL,
    PRIMARY KEY (MembershipID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubID)    REFERENCES Club(ClubID)
);