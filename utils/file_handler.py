import csv

def read_csv(path):
    data = []

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def write_csv(path, data):

    if not data:
        return

    fieldnames = data[0].keys()

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)