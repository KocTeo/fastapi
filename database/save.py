import csv


def save(user):
    user = dict(user)
    rowcount = 0
    for row in open("database/data.csv"):
        rowcount += 1
    print(user.keys())

    if rowcount > 0:
        with open('database/data.csv', mode='a+', newline='') as csv_file:
            
            fieldnames = ['name', 'age']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow(user)
    else:
        with open('database/data.csv', mode='w', newline='') as csv_file:

            fieldnames = ['name', 'age']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(user)