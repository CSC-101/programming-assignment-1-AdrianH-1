import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count
# The purpose of this function is to take and input of words from a
# string and give us a count of the amount of vowels whether upper or lower case.
# In the test case provided, the input was "Hello Class" and the out put was a count of 3.

# Part 2
def short_lists(input_list):
    return [lst for lst in input_list if len(lst) == 2]
# The purpose of this function is to take the lists provided within another list and give
# give us the output of those lists whose length = 2.
# Input: [[1, 2], [3], [9, 10]] Output: [[1, 2], [9, 10]]

# Part 3
def ascending_pairs(input_list):
    result = []
    for lst in input_list:
        if len(lst) == 2:
            result.append(sorted(lst))  # Sort the list of length 2
        else:
            result.append(lst)  # Keep other lists as they are
    return result
#The purpose of this function is to get the lists provided and reorder
# the integers inside each list with a length of 2 in ascending order.
# Input : [[5, 1], [3, 5, 4], [6, 2]] Output: [[1, 5], [3, 5, 4], [2, 6]]

# Part 4
def add_prices(price1: Price, price2: Price) -> Price:

    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    total_dollars += total_cents // 100
    total_cents = total_cents % 100

    return Price(total_dollars, total_cents)
#This functions purpose is to gather the price of two different
# lists them add them up together and make a total sum.
# Input: $5.75 and $3.50 Output: Price(9, 25)
# Input: $5.95 and $4.05 Output: Price(10, 00)

# Part 5
def rectangle_area(rect: Rectangle) -> float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y  # top_left.y is greater than bottom_right.y

    area = width * height
    return area

top_left = Point(1, 4)
bottom_right = Point(5, 1)
rect = Rectangle(top_left, bottom_right)

area = rectangle_area(rect)
    print(area)  # Output: 12.0
# The purpose of this function is to gather the area between two different
# point and make it a rectangle. # Input: (1, 4) & (5, 1)  Output: 12.0

# Part 6
def books_by_author(author_name: str, book_list: list[Book]) -> list[Book]:
    return [book for book in book_list if author_name in book.authors]


book1 = Book(["George Orwell"], "1984")
book2 = Book(["George Orwell"], "Animal Farm")
book3 = Book(["Aldous Huxley"], "Brave New World")

books = [book1, book2, book3]

orwell_books = books_by_author("George Orwell", books)
print(orwell_books)  # Output: [Book(['George Orwell'], '1984'), Book(['George Orwell'], 'Animal Farm')]
# Function of this to gather an input of different books by different authors than determine
# which books were written by a specific author.
# Input: [George Orwell, Aldours Huxley], ["1984", "Animal Farm", "Brave New World"]
# Output: [Book(['George Orwell'], '1984'), Book(['George Orwell']

# Part 7
def circle_bound(rect: Rectangle) -> Circle:
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2
    center = Point(center_x, center_y)

    radius = math.sqrt((center.x - rect.top_left.x) ** 2 + (center.y - rect.top_left.y) ** 2)

    return Circle(center, radius)
# The purpose of this function is to gather the points of a rectnalg and determine where the middle of that rectangle
# is then place the center of the circle in their with a raidus that fits inside.

# Part 8
class Employee:
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate

    def __repr__(self):
        return "Employee('{}', {})".format(self.name, self.pay_rate)
    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate)
def below_pay_average(employees):
    if not employees:
        return []

    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)

    return [employee.name for employee in employees if employee.pay_rate < average_pay]

employees = [
    Employee("Alice", 50000),
    Employee("Bob", 45000),
    Employee("Charlie", 55000),
    Employee("Daisy", 40000)
]

result = below_pay_average(employees)
print(result)  # Output: ['Bob', 'Daisy']
# The purpose of this function was to gather a list of employees and compare
# their wage with the average of all other employees on the list. And would
# output which employees have a wage that is less than the average
# Input: ["Alice", "Bob", "Charlie", "Daisy"] Output: ["Bob", "Daisy"]

