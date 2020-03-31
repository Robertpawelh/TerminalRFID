import csv
from data_operations import *


def generate_report(worker_id):
    filename = workers[worker_id]['name'] + "_WORK_TIME_report.csv"
    with open(filename, 'w', newline='') as file:
        csv_columns = ["Enter Terminal", "Enter Time", "Exit Terminal", "Exit Time", "Card ID"]
        filtered_registrations = dict(filter(lambda x: worker_id in x[1].keys(), registrations.items()))
        writer = csv.writer(file)
        writer.writerow(csv_columns)
        for card_id, data in filtered_registrations.items():
            worker_info = data[worker_id]
            loop_len = len(worker_info['end'])
            for i in range(loop_len):
                print(worker_info['begin'][i])
                writer.writerow([worker_info['begin_t'][i],
                                 worker_info['begin'][i],
                                 worker_info['end_t'][i],
                                 worker_info['end'][i],
                                 card_id])

            if len(worker_info['begin']) > loop_len:
                writer.writerow([worker_info['begin_t'][loop_len],
                                 worker_info['begin'][loop_len],
                                 None,
                                 None,
                                 card_id])
