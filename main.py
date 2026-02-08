from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    calculate_salary(count=348)
    get_employees('Dan')
    print(datetime.now())
