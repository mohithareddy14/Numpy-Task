
import numpy as np

# -----------------------------------------
# TASK 1 – Random Decimal Matrix
# -----------------------------------------
print("\nTASK 1: Random Decimal Matrix")

arr1 = np.random.random((4, 4))
print("4x4 Random Matrix:")
print(arr1)


# -----------------------------------------
# TASK 2 – Filter rand() Output
# -----------------------------------------
print("\nTASK 2: Filter rand() Output")

arr2 = np.random.rand(3, 3)
print("Original Matrix:")
print(arr2)

filtered = arr2[arr2 > 0.5]
print("Elements greater than 0.5:")
print(filtered)


# -----------------------------------------
# TASK 3 – Normal Distribution Sample
# -----------------------------------------
print("\nTASK 3: Normal Distribution Sample")

arr3 = np.random.randn(20)
print("Original Values:")
print(arr3)

positive_count = np.sum(arr3 > 0)
negative_count = np.sum(arr3 < 0)

print("Positive Values Count:", positive_count)
print("Negative Values Count:", negative_count)

arr3[arr3 < 0] = 0
print("After Replacing Negative Values with Zero:")
print(arr3)


# -----------------------------------------
# TASK 4 – Random Integers Statistics
# -----------------------------------------
print("\nTASK 4: Random Integers Statistics")

arr4 = np.random.randint(1, 101, size=25)
print("Random Integers:")
print(arr4)

print("Maximum Value:", np.max(arr4))
print("Minimum Value:", np.min(arr4))
print("Mean:", np.mean(arr4))

even_numbers = arr4[arr4 % 2 == 0]
print("Even Numbers:")
print(even_numbers)


# -----------------------------------------
# TASK 5 – Random Selection of Marks
# -----------------------------------------
print("\nTASK 5: Random Selection of Marks")

marks = np.array([35, 45, 55, 65, 75, 85, 95])

selected_marks = np.random.choice(marks, size=4, replace=False)

print("Original Marks:", marks)
print("Four Selected Distinct Marks:", selected_marks)


# -----------------------------------------
# TASK 6 – Shuffle Sequence
# -----------------------------------------
print("\nTASK 6: Shuffle Sequence")

arr6 = np.arange(1, 21)

print("Before Shuffling:")
print(arr6)

np.random.shuffle(arr6)

print("After Shuffling:")
print(arr6)


# -----------------------------------------
# TASK 7 – Permutation Check
# -----------------------------------------
print("\nTASK 7: Permutation Check")

arr7 = np.arange(10, 101, 10)

print("Original Array:")
print(arr7)

permuted = np.random.permutation(arr7)

print("Permuted Array:")
print(permuted)

print("Original Array After Permutation:")
print(arr7)

print("Is Original Array Unchanged?",
      np.array_equal(arr7, np.arange(10, 101, 10)))


# -----------------------------------------
# TASK 8 – Boolean Masking of Student Marks
# -----------------------------------------
print("\nTASK 8: Boolean Masking of Student Marks")

student_marks = np.random.randint(0, 101, size=20)

print("Student Marks:")
print(student_marks)

failed = student_marks[student_marks < 40]
passed = student_marks[student_marks >= 40]
distinction = student_marks[student_marks >= 75]

print("Failed Students (<40):")
print(failed)

print("Passed Students (>=40):")
print(passed)

print("Distinction Students (>=75):")
print(distinction)


# -----------------------------------------
# TASK 9 – Salary Analysis with Masks
# -----------------------------------------
print("\nTASK 9: Salary Analysis with Masks")

salary = np.random.randint(20000, 100001, size=15)

print("Original Salaries:")
print(salary)

high_salary = salary[salary > 50000]
print("Salaries Greater Than 50000:")
print(high_salary)

medium_salary = salary[(salary >= 30000) & (salary <= 70000)]
print("Salaries Between 30000 and 70000:")
print(medium_salary)

salary[salary < 25000] = 25000
print("Salaries After Replacing Values Below 25000:")
print(salary)


# -----------------------------------------
# TASK 10 – Online Shopping Price Pipeline
# -----------------------------------------
print("\nTASK 10: Online Shopping Price Pipeline")

prices = np.random.randint(100, 10001, size=20)

print("Original Product Prices:")
print(prices)

# Select 5 random prices
selected_prices = np.random.choice(prices, size=5, replace=False)
print("Five Randomly Selected Prices:")
print(selected_prices)

# Shuffle the full price list
np.random.shuffle(prices)

print("Shuffled Price List:")
print(prices)

# Identify prices above 5000
high_prices = prices[prices > 5000]
print("Prices Above 5000:")
print(high_prices)

# Apply 10% discount to prices above 5000
discounted_prices = prices.astype(float)
discounted_prices[discounted_prices > 5000] *= 0.90

print("Prices After 10% Discount:")
print(discounted_prices)

# Calculate total cost after discount
total_cost = np.sum(discounted_prices)

print("Total Cost After Discounts: ₹", round(total_cost, 2))




