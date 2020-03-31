import data_operations
import csv
from data_operations import *

def generate_report(worker_id):
    filename = workers['name'] + "_job_raport.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Name", "Contribution"])
        writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
        writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
        writer.writerow([3, "Guido van Rossum", "Python Programming"])