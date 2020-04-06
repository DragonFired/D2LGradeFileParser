#!/usr/bin/env python
__author__ = "Arana Fireheart"

from csv import reader, writer
from assignmentObjects import Assignment, AssignmentManager

csvFilename = "CS-114-06806 Intro to Software Engineering 20SPDAY_GradesExport_2020-04-06-19-42.csv"
gradesFilename = "allGrades.csv"
gradesExportFilename = "gradesForD2L.csv"


def assignmentListGen(headerRowList):
    for position, element in enumerate(headerRowList):
        try:
            if element.find(" Points Grade ") >= 0:
                endPosition = element.index(" Points Grade ")
                assignmentName = element[:endPosition]
                if assignmentName != "Attendance":
                    yield (assignmentName, position)
        except ValueError:
            print("Booom!")


manager = AssignmentManager()

with open(gradesFilename, 'r') as gradesInputFile:
    gradeCsvReader = reader(gradesInputFile)
    header = next(gradeCsvReader)
    for studentName, topic, filename, studentFoldername, gradebookColumn, colorGrade, numericGrade in gradeCsvReader:
        manager.addAssignment(Assignment(studentName, topic, filename, studentFoldername, gradebookColumn, numericGrade))


def calculateGrade(studentName, GBColumnName):
    assignmentGrades = []
    for assignment in manager.getAssignmentsByGBColumn(studentName, GBColumnName):
        assignmentGrades.append(assignment.getGrade())
    if len(assignmentGrades) > 0:
        if max(assignmentGrades) == 0:
            return ''
        else:
            return max(assignmentGrades) / 10
    else:
        return ''

with open(csvFilename) as csvInputFile, open(gradesExportFilename, 'w') as gradesOutputFile:
    csvReader = reader(csvInputFile)
    gradesWriter = writer(gradesOutputFile)
    assignmentDictionary = {}
    for rowNumber, row in enumerate(csvReader):
        if rowNumber == 0:
            headers = row
            for assignmentName, rowIndex in assignmentListGen(headers):
                assignmentDictionary[assignmentName] = rowIndex
            # print(assignmentDictionary.keys())
            name = row[2]
            # print(row[2], row[1])
            gradesWriter.writerow(headers)
        else:
            name = row[2]
            if not manager.hasStudent(name):
                name = row[2] + row[1][0]
            print(f"F: {row[2]} L: {row[1]}")
            for gradeBookEntry in assignmentDictionary.keys():
                currentGrade = calculateGrade(name, gradeBookEntry)
                columnNumber = assignmentDictionary[gradeBookEntry]
                row[columnNumber] = currentGrade
                print(f"{name} {gradeBookEntry} {calculateGrade(name, gradeBookEntry)}")
            gradesWriter.writerow(row)
