import datetime
from application import salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(get_employees(3))
    print(salary.calculate_salary(3))
    print(datetime.datetime.now())
