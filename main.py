import calendar
from datetime import date, datetime, timedelta

users = [{"name": "Tanya", "birthday": datetime(1960, 3, 4)},
         {"name": "Sonya", "birthday": datetime(2015, 2, 19)},
         {"name": "Bill", "birthday": datetime(1965, 2, 23)},
         {"name": "Jill", "birthday": datetime(1988, 2, 23)},
         {"name": "Kim", "birthday": datetime(1965, 2, 22)},
         {"name": "Nastya", "birthday": datetime(1990, 10, 22)}
]

def get_birthdays_per_week(users):
    now = datetime.now()

    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []

    next_week = datetime.now() + timedelta(days=7)

    for user in users:

        if now.month <= user['birthday'].month <= next_week.month:

            if  now.day <= user['birthday'].day <= next_week.day:

                if user['birthday'].weekday() == 0:
                    monday.append(user['name'])

                elif user['birthday'].weekday() == 1:
                    tuesday.append(user['name'])

                elif user['birthday'].weekday() == 2:
                    wednesday.append(user['name'])

                elif user['birthday'].weekday() == 3:
                    thursday.append(user['name'])

                elif user['birthday'].weekday() == 4:
                    friday .append(user['name'])

                elif user['birthday'].weekday() == 5:
                    monday.append(user['name'])

                elif user['birthday'].weekday() == 6:
                    monday.append(user['name'])

    if len(monday) != 0:
        print(f"Monday:", ', '.join(monday))
    if len(tuesday) != 0:
        print(f"Tuesday :", ', '.join(tuesday))
    if len(wednesday) != 0:
        print(f"Wednesday :", ', '.join(wednesday))
    if len(thursday) != 0:
        print(f"Thursday :", ', '.join(thursday))
    if len(friday) != 0:
        print(f"Friday :", ', '.join(friday))

if __name__ == "__main__":
    get_birthdays_per_week(users)
