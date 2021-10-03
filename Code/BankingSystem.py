#######################################################
# 
# BankingSystem.py
# Python implementation of the Class BankingSystem
# Generated by Enterprise Architect
# Created on:      20-Sep-2021 11:10:39 PM
# Original author: Caleb Dunham
# 
#######################################################
import pandas as pd
from datetime import datetime
import pathlib


class BankingSystem:
    """
    The BankingSystem Class is the foundation of the Banking System project
    and is where employee login and verifications are performed
    and activity logging is initiated
    ...

    Attributes
    ----------
    _log_file : pathlib
        path to the user activity log file
    _emp_db_path : pathlib
        path to the employee database

    Methods
    -------
    _confirm_emp()
        confirms entered employee id is found in database
    _connect_emp_db()
        connects to employee database
    _get_activity_dt(activity)
        creates a list of values to be logged
    _log_activity()
        logs each activity performed
    get_emp_info()
        displays current employee information
    login()
        requests an employee id and calls connection to db
    logout()
        removes employee id so no further activity can occur without new login
    """
    _log_file = pathlib.Path(r'G:\My Drive\Springboard\gitRepo\mini_project1\user_activity_log.csv')
    _emp_db_path = pathlib.Path(r'G:\My Drive\Springboard\gitRepo\mini_project1\EmployeeDB.txt')

    def __init__(self):
        """
        Parameters
        ----------
        _employee_id : int
            initializes employee id
        _customer_id : int
            initializes customer id
        _confirmed_emp : bool
            initializes confirmed employee to False
        _confirmed_cust : bool
            initializes confirmed customer to False
        """
        self._employee_id = 111111
        self._customer_id = 222222
        self._confirmed_emp = False
        self._confirmed_cust = False

    def _confirm_emp(self):
        """Confirms employee id is found in employee database.
        """
        if self._emp_db.loc[self._emp_db.emp_id == self._employee_id].empty:
            self._get_activity_dt('EMP NOT FOUND')
            self._confirmed_emp = False
            print('Employee not found.')
        else:
            self.curr_emp = self._emp_db.loc[self._emp_db.emp_id == self._employee_id]
            self._get_activity_dt('EMP CONFIRMED')
            self._confirmed_emp = True
            print('Employee confirmed.')

    def _connect_emp_db(self):
        """Creates connection to employee database.
        """
        self._emp_db = pd.read_csv(self._emp_db_path)
        self._get_activity_dt('CONNECTED EMP DB')
        self._confirm_emp()

    def _get_activity_dt(self, activity):
        """Creates list of user activities to be logged.

        Parameters
        ----------
        activity : str
            Description of the activity to be logged
        """
        self._activity = [self._employee_id, activity, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]]
        self._log_activity()

    def _log_activity(self):
        """Logs the activity attributes to the user activity log file.
        """
        lg_df = pd.DataFrame(self._activity).T
        if self._log_file.is_file():
            lg_df.to_csv(self._log_file, mode='a', index=False, header=False)
        else:
            lg_df.to_csv(self._log_file, index=False, header=False)

    def get_emp_info(self):
        """Displays employee info for the currently logged in employee.
        """
        for k, v in self.curr_emp.items():
            setattr(self, k, v[0])
            print(f'{k}: {v[0]}')
        self._get_activity_dt('GET EMP INFO')

    def login(self):
        """Requests employee id input.
        """
        self._employee_id = int(input('Enter Employee ID: '))
        self._get_activity_dt('LOGIN')
        self._connect_emp_db()

    def logout(self):
        """Removes instance of employee id and sets confirmed employee to false.
        """
        self._get_activity_dt('LOGOUT')
        del self._employee_id
        self._confirmed_emp = False
        print('Successfully Logged Out.')
