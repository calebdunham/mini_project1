#######################################################
# 
# BankingSystem.py
# Python implementation of the Class BankingSystem
# Generated by Enterprise Architect
# Created on:      20-Sep-2021 11:10:39 PM
# Original author: caleb
# 
#######################################################
import pandas as pd


class BankingSystem:

    def __init__(self):
        """

        """
        self.employee_id = int(input('Enter Employee ID: '))
        pass

    def _confirm_emp(self):
        if self._emp_db.loc[self._emp_db.emp_id == self.employee_id].empty:
            print('Employee not found.')
        else:
            self.curr_emp = self._emp_db.loc[self._emp_db.emp_id == self.employee_id]
            print('Employee confirmed.')
        pass

    def _connect_emp_db(self):
        self._emp_db = pd.read_json(r'G:\My Drive\Springboard\gitRepo\mini_project1\EmployeeDB.json', orient='index')
        self._confirm_emp()
        pass

    def _get_activity_dt(self):
        pass

    def _log_activity(self):
        pass

    def get_emp_info(self):
        for k, v in self.curr_emp.items():
            setattr(self, k, v[0])

        pass

    def login(self):
        self._connect_emp_db()
        pass

    def logout(self):
        pass
