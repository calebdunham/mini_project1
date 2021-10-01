#######################################################
# 
# Customer.py
# Python implementation of the Class Customer
# Generated by Enterprise Architect
# Created on:      20-Sep-2021 11:10:39 PM
# Original author: caleb
# 
#######################################################
from BankingSystem import BankingSystem
import pandas as pd
import pathlib
from random import randint


# noinspection SpellCheckingInspection
class Customer(BankingSystem):
    _cust_db_path = pathlib.Path(r'G:\My Drive\Springboard\gitRepo\mini_project1\CustomerDB.txt')

    def __init__(self):
        BankingSystem.__init__(self)
        if self._confirmed_emp:
            pass
        else:
            print('Employee Login Not Confirmed')
            BankingSystem.login(self)

    def _confirm_cust(self):
        if self._cust_db.loc[self._cust_db.cust_id == self._customer_id].empty:
            self._get_activity_dt('CUST NOT FOUND')
            self._confirmed_cust = False
            print('Customer not found.')
        else:
            self.curr_cust = self._cust_db.loc[self._cust_db.cust_id == self._customer_id]
            self._get_activity_dt('CUST CONFIRMED')
            self._confirmed_cust = True
            print('Customer confirmed.')

    def _connect_cust_db(self):
        self._cust_db = pd.read_csv(self._cust_db_path)
        self._get_activity_dt('CONNECTED CUST DB')
        self._confirm_cust()

    def add_customer(self):

        def gen_id():
            range_start = 10 ** (6 - 1)
            range_end = (10 ** 6) - 1
            cid = randint(range_start, range_end)
            while not self._cust_db.loc[self._cust_db.cust_id == cid].empty:
                gen_id()
            return cid

        new_customer_id = gen_id()
        new_cust_fname = input('Enter Customer First Name: ')
        new_cust_lname = input('Enter Customer Last Name: ')
        new_cust_info = input('Enter Customer Info: ')
        new_cust = pd.DataFrame({'cust_id': new_customer_id, 'cust_fname': new_cust_fname, 'cust_lname': new_cust_lname,
                                 'cust_info': new_cust_info}, index=[0])
        new_cust.to_csv(self._cust_db_path, mode='a', index=False, header=False)
        print('Customer Added\n--------------')
        for k, v in new_cust.items():
            # setattr(self, k, v[0])
            print(f'{k}: {v[0]}')
        self._get_activity_dt('CUSTOMER ADDED')

    # def del_customer(self):
    #     pass

    def get_customer_info(self):
        self._customer_id = int(input('Enter Customer ID: '))
        self._get_activity_dt('GET CUST INFO')
        self._connect_cust_db()
