#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 15, 2021
# This program asks the user to enter different marks and then calculates the
# average

def calc_average(list):
    # calculates the average of the sum of every number
    # in a list and returns it
    # returns -1 if the list is empty
    sum = 0

    # calculate the sum of the numbers in the list
    for number in list:
        sum += number
    try:
        # calculate the average of the list
        average = sum / len(list)
    except ZeroDivisionError:
        # check if list is empty
        average = -1
    return average


def main():
    # create empty list
    mark_list = []

    # display greeting
    print("This program calculates the average of different marks.")
    print()

    while True:
        # ask the user to enter marks
        user_mark_string = input("Enter a mark between 0 to 100 (enter '-1' to\
 stop): ")

        try:
            # convert from string to int
            user_mark_int = int(user_mark_string)

            if (user_mark_int == -1):
                # break if the user enters -1
                break

            elif (user_mark_int < 0 or user_mark_int > 100):
                # error message if mark is out of range
                print("{} is not between 0 and 100, try again.\
". format(user_mark_int))

            else:
                # add mark to list
                mark_list.append(user_mark_int)

        except ValueError:
            # error message if mark is not a number
            print("{} is not a whole number, try again.\
". format(user_mark_string))

    print()

    # call calc_average function
    user_average = calc_average(mark_list)
    user_average = round(user_average)

    # error message if function returned -1
    if (user_average == -1):
        print("Exception occured. Cannot calculate the average of an empty\
 list.")
    else:
        # display the list and the average
        print("For the list of marks: {}". format(mark_list))
        print("The average is: {}.". format(user_average))


if __name__ == "__main__":
    main()
