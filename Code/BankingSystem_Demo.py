#!/usr/bin/env python3

#######################################################
#
# Simple demo script to walk thru how mini_project1
# BankingSystem functions
#
#######################################################

from BankingSystem import BankingSystem
from Accounts import Accounts
from Customer import Customer
from Services import Services

"""
The BankingSystem class has three public methods:
- login()
- get_emp_info()
- logout()
"""
bks = BankingSystem()
bks.login()
bks.get_emp_info()
bks.logout()

"""
The Customer class has two public methods:
- add_customer()
- get_customer_info()
"""
cst = Customer()
cst.add_customer()
cst.get_customer_info()

"""
The Accounts class has three public methods:
- balance()
- deposit()
- withdrawal()
"""
act = Accounts()
act.balance()
act.deposit()
act.withdrawal()

"""
The Services class has one public method:
- add_service()
"""
srv = Services()
srv.add_service()
