# # Finds the square root of a number using binary search
# # number - int

ROUND = 5


def square_root(number):
    left = 0
    right = number

    while left < right:
        middle = left + ((right - left) / 2.0)
        squared = middle ** 2

        if number - squared < 0.00001 and number - squared > 0:
            return round(middle, ROUND)
        elif squared > number:
            right = middle
        elif squared < number:
            left = middle


# def square_root(number):
#     left = 0
#     right = number
#     mid = left + ((right - left) / 2.0)

#     while True:
#         if mid**2 < number:
#             left = mid
#         if mid**2 > number:
#             right = mid
#         if abs(mid**2 - number) < 0.00001:
#             break
#         mid = left + ((right - left) / 2.0)

#     return round(mid, 5)


def main():
    num = int(input())
    print(square_root(num))


if __name__ == '__main__':
    main()
