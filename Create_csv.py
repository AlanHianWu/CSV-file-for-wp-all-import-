#!/usr/bin/env python
from Create_CSV_01 import Line
import csv
import sys
import os

def main():
    A = 'Sku'
    B = 'Barcode'
    C = 'Image_file_name'
    D = 'Title'
    E = 'Variable'
    F = 'Variable_Name_01'
    G = 'Variable_Value_01'
    H = 'Variable_Name_02'
    I = 'Variable_Value_02'
    J = 'Description_01'
    K = 'Description_02'
    L = 'Price'
    M = 'Price_Exclude_VAT'    
    N = 'Brand'
    O = 'Category'
    P = 'Images'
    rows, columns = os.popen('stty size', 'r').read().split()

    Initial_Ask = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]

    print('your input eg. 0,1,2 max 15')
    Checking = True
    while Checking != False:
        index = input()
        index = index.split(',')
        All_in_All = True
        for numbers in index:
            if numbers.isdigit() is False:
                All_in_All = False
        if All_in_All is False:
            print('Invalid numbers')
        else:
            print('\nyou have selected:\n{}\n'.format( "\n".join([Initial_Ask[int(i)] for i in index])))
            print('Is this correct?.....[y/n]')
            Yes_No = input()
            if Yes_No == 'y':
                Checking = False
            elif Yes_No == 'n':
                print('Please re-enter your selection')
                Checking = True
            else:
                print('Invalid cammand')
                Checking = True

    Asking = [Initial_Ask[int(i)] for i in index]

    normal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    New_Asking = []
    for i in normal:
        if str(i) not in index:
            New_Asking.append('x')
        else:
            New_Asking.append(i)

    with open('output_log.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(Initial_Ask)

    with open('New_item_log.txt', 'w') as text_file:
        text_file.write("")

    Continue = 'y'
    while Continue == 'y':
        Item_instance = {}
        Row = []
        Big = 0

        for calls in New_Asking:
            if calls != 'x':
                print("Please enter: {}".format(Initial_Ask[int(calls)]))
                Value = input()
                Item_instance[Initial_Ask[int(calls)]] = Value
                Row.append(Value)
                if len(Value) > Big:
                    Big = len(Value)
            else:
                Row.append('')

        x = Line(**Item_instance)
        attributes = vars(x)

        print('=' * int(columns))
        print(' ' * 14 + 'New Item!!')

        for i in Asking:
            print('{:>17} : {:>{}}'.format(i, attributes[i], Big))

        print('=' * int(columns))

        with open('output_log.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(Row)

        with open('New_item_log.txt', 'a') as text_file:
            text_file.write("{} {}\n".format(x.Sku, x.Barcode))

        print('Continue??.....[y/n]')

        checking = True
        while checking != False:
            Continue = input()
            if Continue == 'y':
                print('Go---->')
                checking = False
            elif Continue == 'n':
                print('Stopping')
                checking = False
            else:
                print('Invalid cammand')

if __name__ == '__main__':
    main()
