#!/usr/bin/env python
__author__ = "Arana Fireheart"


class AssignmentManager(object):
    def __init__(self):
        self.studentAssignments = {}
    def __str__(self):
        return ""
    def hasStudent(self, studentName):
        return studentName in self.studentAssignments.keys()
    def addAssignment(self, assignmentObject):
        studentFirstName = assignmentObject.getStudentFName()
        if studentFirstName in self.studentAssignments:
            self.studentAssignments[studentFirstName].append(assignmentObject)
        else:
            self.studentAssignments[studentFirstName] = [assignmentObject]
    def getAssignmentsByStudent(self, studentFName, studentLName = ""):
        returnList = []
        for assignment in self.studentAssignments:
            if studentFName == "":
                if assignment.getStudentFName() == studentFName:
                    returnList.append(assignment)
            else:
                if assignment.getStudentFName() == studentFName and assignment.getStudentLName()[0] == studentLName[0]:
                    returnList.append(assignment)

        return returnList
    def getAssignmentsByTopic(self, studentFName, assignmentTopic):
        if studentFName in self.studentAssignments:
            for assignment in self.studentAssignments[studentFName]:
                if assignment.getTopic(assignmentTopic) is not None:
                    return assignment.getTopic(assignmentTopic)
        else:
            return None
    def getAssignmentsByGBColumn(self, studentFName, gradeBookColumnName):
        returnList = []
        if studentFName in self.studentAssignments:
            assignmentList = self.studentAssignments[studentFName]
            for assignment in assignmentList:
                if assignment.getGBColumn() == gradeBookColumnName:
                    returnList.append(assignment)
        return returnList

class Assignment(object):
    def __init__(self, studentFName, assignmentTopic, assignmentFile, assignmentName, gradebookEntryName, numericGrade, studentLName = ""):
        self.firstName = studentFName
        self.lastName = studentLName
        self.topic = assignmentTopic
        self.filename = assignmentFile
        self.studentsAssignmentName = assignmentName
        self.gradebookColumn = gradebookEntryName
        try:
            self.numericGrade = int(numericGrade)
        except ValueError:
            if numericGrade == '-':
                self.numericGrade = 0
            else:
                self.numericGrade = -1
                print(f"Grade was not an integer {numericGrade}")
    def __str__(self):
        return f"N:{self.firstName} T:{self.topic} F:{self.filename} GB:{self.gradebookColumn} G:{self.numericGrade}"
    def getStudentFName(self):
        return self.firstName
    def getStudentLName(self):
        return self.lastName
    def getTopic(self):
        return self.topic
    def getGBColumn(self):
        return self.gradebookColumn
    def getGrade(self):
        return self.numericGrade
