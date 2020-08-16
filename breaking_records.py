
def breaking_records(records = None):

    if records is None:
        raise Exception('please enter record')

    max_score = None
    min_score = None
    num_breaking_records = 0
    num_least_records = 0
    result = []

    for record in records:
        if max_score is None or min_score is None:
            max_score = record
            min_score = record
            continue

        if record > max_score:
            max_score = record
            num_breaking_records += 1

        if record < min_score:
            min_score = record
            num_least_records += 1

    result.append(num_breaking_records)
    result.append(num_least_records)

    return f"{num_breaking_records} {num_least_records}"


if __name__ == '__main__':

    records = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    records = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    result = breaking_records(records=records)
    print(result)

