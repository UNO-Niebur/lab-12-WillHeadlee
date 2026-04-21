# SearchSortLab.py
# Name: William Headlee
# Date: 4/21/26
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    
    for i in data:
        if i == target:
            return data.index(i)
    # TODO: implement linear search
    
    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            current = data[i]
            next = data[i+1]

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    # TODO: implement bubble sort
    
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    main()

""" 
Which list was easiest to sort? Why?

    The easiest list to sort was the already sorted list. 
    Given that all of the numbers are laready in the right positions,
    the script doesn't have to make any position swaps,
    leading to a lower sorting time. 

Which list required the most work?

    Using bubble sort, the hardest list to sort is the reversed list.
    It has to repeatedly switch positions of values with many "wasted" moves.

Why is sorting useful before searching?

    Sorting a list is helpful for both humans and computers.

    When a list is sorted for a human, we can jump to the area of the value
    much like in a dictionary where you can turn to a page that starts with 
    the same letter as the word you are looking for.

    Sorting a list for a computer can help cut search times.
    If the value you are looking for is low, it will find it faster in a 
    regularily sorted list. Use a reversed list for high numbers.

When might linear search still be useful?

    If you don't have time to sort a list or the list is relatively short,
    linear search can be fast. If the list is super long or the value doesn't exist,
    a linear search will take ages.
"""
