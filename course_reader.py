import csv
import sqlite3
__author__ = 'Sam'

def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as file:
        reader = csv.reader(file);
        for row in reader:
            conn = sqlite3.connect(db_name)
            with conn:
                cur = conn.cursor();
                sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)";
                cur.execute(sql_cmd, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]));

load_course_database('course1.db', 'seas-courses-5years.csv');