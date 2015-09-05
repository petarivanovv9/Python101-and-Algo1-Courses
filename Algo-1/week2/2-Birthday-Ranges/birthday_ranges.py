# Return a vector with the number of people born in the specific ranges.
# birthdays - [int]
# ranges - [(int, int)]


def birthdays_count(birthdays, ranges):
    dates = [0] * 366
    prefix_sum = [0]
    result = []

    for date in birthdays:
        dates[date] += 1

    for date_count in dates:
        prefix_sum.append(prefix_sum[-1] + date_count)

    for elem in ranges:
        result.append(prefix_sum[elem[-1] + 1] - prefix_sum[elem[0]])

    return result


def main():

    birthdays = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
    ranges = [(4, 9), (6, 7), (200, 225), (300, 365)]

    print(birthdays_count(birthdays, ranges))


if __name__ == '__main__':
    main()
