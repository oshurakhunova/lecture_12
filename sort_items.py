import csv
import os
import random

cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as numbers:
        csv_reader = csv.reader(numbers, delimiter='\t')
        for row in csv_reader:
            data = []
            for item in row:
                data.append(int(item))
    return data


def selection_sort(number_array):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """


def main():
    data = read_row('numbers_one.csv')
    # Ukol: Selection Sort


    # Ukol: Selection Sort - se smerem razeni
    

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

