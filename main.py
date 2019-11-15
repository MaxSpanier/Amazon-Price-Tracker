from worker import start_routine, change_product
from visualizer import visualize
import time
import os

clear = lambda: os.system('cls')

def start():
    clear()
    print('Select an option')
    print('------------------------')
    print('1) Start scraping')
    print('2) Visualize the data')
    print('3) Change Product')
    print('4) Exit')
    print('')
    choice = input('Your Choice: ')

    if choice == '1':
        clear()
        start_routine()
    elif choice == '2':
        visualize()
    elif choice == '3':
        print('Coming Soon...')

        #give_url = input('Insert url: ')
        #given_excel = input('Insert Excel-File name: ')
        #change_product()

        '''
        change URL in worker.py
        if excel file with given name exists
            change excel_file_name to given_excel
        else 
            create excel file with the name(given_excel)
            change excel_file_name to given name

        '''
    elif choice == '4':
        raise SystemExit
    else:
        print('Invalid Input')
        print('Please try again...')
        choice = 0
        time.sleep(1)
        clear()
        start()

start()
