import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
input_string = "Hello Class"
    print(vowel_count(input_string))  # Output: 3
input_string = "Give me an A"
    print(vowel_count(input_string))  # Output: 5
#Input it "Hello Class" and output of vowel count is 3.

    # Part 2
input_data = [[1, 2], [3, 4, 5], [6, 7], [8]]
    print(short_lists(input_data))  # Output: [[1, 2], [6, 7]]
input_data = [[1, 2], [3], [9, 10]]
    print(short_lists(input_data))  # Output: [[1, 2], [9, 10]]
#Input a list that consists of other lists, such as [[1, 2], [3], [9, 10]]
#which gives us an output that only consists of the existing lists in that
#list that are length of 2, which would be [[1, 2], [9, 10]]

    # Part 3
input_data = [[5, 1], [3, 5, 4], [6, 2]]
    print(ascending_pairs(input_data))  # Output: [[1, 5], [3, 5, 4], [2, 6]]
input_data = [[1, 5], [2, 5, 1], [9, 8]]
    print(ascending_pairs(input_data))  # Output: [[1, 5], [2, 5, 1], [8, 9]]
#Input a list of lists that consists of intergers. If the len(list) == 2, then the
# order of the variables of the list will be reordered in ascending order.
# Input : [[5, 1], [3, 5, 4], [6, 2]] Output: [[1, 5], [3, 5, 4], [2, 6]]

    # Part 4
price1 = Price(5, 75)  # $5.75
price2 = Price(3, 50)  # $3.50

total_price = add_prices(price1, price2)
    print(total_price)  # Output: Price(9, 25)
price1 = Price(5, 95)  # $5.75
price2 = Price(4, 05)  # $4.05

total_price = add_prices(price1, price2)
    print(total_price)
# Input: $5.75 and $3.50 Output: Price(9, 25)
# Input: $5.95 and $4.05 Output: Price(10, 00)

    # Part 5
top_left = Point(1, 4)
bottom_right = Point(5, 1)
rect = Rectangle(top_left, bottom_right)

area = rectangle_area(rect)
    print(area)
# Input: (1, 4) & (5, 1)  Output: 12.0

    # Part 6
book1 = Book(["George Orwell"], "1984")
book2 = Book(["George Orwell"], "Animal Farm")
book3 = Book(["Aldous Huxley"], "Brave New World")

books = [book1, book2, book3]

orwell_books = books_by_author("George Orwell", books)
    print(orwell_books)  # Output: [Book(['George Orwell'], '1984'), Book(['George Orwell'], 'Animal Farm')]
# Input: [George Orwell, Aldours Huxley], ["1984", "Animal Farm", "Brave New World"]
# Output: [Book(['George Orwell'], '1984'), Book(['George Orwell'],

    # Part 7
rtop_left = Point(1, 5)
bottom_right = Point(4, 1)
rect = Rectangle(top_left, bottom_right)
bounding_circle = circle_bound(rect)
    print(bounding_circle)  # Output: Circle(Point(2.5, 3.0), 2.5)

    # Part 8
employees = [
    Employee("Alice", 50000),
    Employee("Bob", 45000),
    Employee("Charlie", 55000),
    Employee("Daisy", 40000)
]

result = below_pay_average(employees)
print(result)  # Output: ['Bob', 'Daisy']




if __name__ == '__main__':
    unittest.main()
