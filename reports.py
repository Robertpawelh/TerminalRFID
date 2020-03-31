import data_operations
import csv
from data_operations import *

def generate_report(worker_id):
    filename = workers[worker_id]['name'] + "_WORK_TIME_report.csv"
    with open(filename, 'w', newline='') as file:
        csv_columns = ["Enter Terminal", "Enter Time", "Exit Terminal", "Exit Time"]
        writer = csv.writer(file)
        writer.writerow(csv_columns)
        reg = registrations[workers[worker_id]['card_id']]
        for i in range(len(reg['end'])):
            print(reg['begin'][i])
            writer.writerow([reg['begin_t'][i], reg['begin'][i], reg['end_t'][i], reg['end'][i]])

        if len(reg['begin']) > len(reg['end']):
            writer.writerow([reg['begin_t'][i], reg['begin'][i]])