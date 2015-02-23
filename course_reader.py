import csv
__author__ = 'Sam'

def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU'):
        reader = csv.reader(csv_filename);
        for row in reader:
            print(row);

load_course_database('course1.db', 'seas-courses-5years.csv');
