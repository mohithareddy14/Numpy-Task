# NumPy Random Generation, Masking, and Array Manipulation

## Project Overview

This project demonstrates the use of NumPy, a Python library used for numerical computing and array operations.

The assignment focuses on generating random datasets, applying Boolean masking, performing statistical calculations, selecting random elements, shuffling arrays, and manipulating numerical data.

The project simulates basic data analyst activities such as student marks analysis, salary analysis, random sampling, and online shopping price calculations.

## Objectives

- Generate random numbers using NumPy.
- Create and manipulate one-dimensional and two-dimensional arrays.
- Apply Boolean masking to filter array elements.
- Perform statistical operations such as minimum, maximum, mean, and sum.
- Select random elements from an array.
- Understand the difference between shuffle and permutation.
- Apply conditional modifications to array elements.
- Perform a simple price analysis pipeline using NumPy.

## Technologies Used

- **Programming Language:** Python
- **Library:** NumPy
- **IDE:** Visual Studio Code (VS Code)

## Tasks Implemented

### Task 1 – Random Decimal Matrix
- Generated a 4 × 4 matrix using `np.random.random()`.
- Generated random floating-point values between 0 and 1.

### Task 2 – Filter rand() Output
- Created a 3 × 3 random matrix using `np.random.rand()`.
- Extracted elements greater than 0.5 using Boolean masking.

### Task 3 – Normal Distribution Sample
- Generated 20 random values using `np.random.randn()`.
- Counted positive and negative values.
- Replaced all negative values with zero.

### Task 4 – Random Integers Statistics
- Generated 25 random integers between 1 and 100.
- Calculated maximum, minimum, and mean values.
- Extracted all even numbers.

### Task 5 – Random Selection of Marks
- Created an array containing student marks.
- Selected four distinct marks using `np.random.choice()`.
- Used `replace=False` to avoid duplicate selections.

### Task 6 – Shuffle Sequence
- Created an array containing integers from 1 to 20.
- Displayed the original array.
- Shuffled the array in-place using `np.random.shuffle()`.

### Task 7 – Permutation Check
- Created an array containing values from 10 to 100 with a step of 10.
- Generated a permuted array using `np.random.permutation()`.
- Verified that the original array remained unchanged.

### Task 8 – Boolean Masking of Student Marks
- Generated random marks for 20 students between 0 and 100.
- Categorized marks into:
  - Failed: Below 40
  - Passed: 40 and above
  - Distinction: 75 and above
- Used Boolean masks to filter the marks.

### Task 9 – Salary Analysis with Masks
- Generated 15 random salaries between ₹20,000 and ₹1,00,000.
- Extracted salaries greater than ₹50,000.
- Filtered salaries between ₹30,000 and ₹70,000 (inclusive).
- Replaced salaries below ₹25,000 with ₹25,000.

### Task 10 – Online Shopping Price Pipeline
- Generated 20 random product prices between ₹100 and ₹10,000.
- Selected five random prices without replacement.
- Shuffled the complete price array.
- Identified prices greater than ₹5,000.
- Applied a 10% discount to high-priced products.
- Calculated the total cost after applying discounts.

## NumPy Functions Used

| Function | Description |
|---|---|
| `np.random.random()` | Generates random decimal values |
| `np.random.rand()` | Generates random values in a specified shape |
| `np.random.randn()` | Generates normally distributed random values |
| `np.random.randint()` | Generates random integers |
| `np.random.choice()` | Selects random array elements |
| `np.random.shuffle()` | Shuffles an array in-place |
| `np.random.permutation()` | Returns a randomly permuted array |
| `np.arange()` | Creates a sequence of numbers |
| `np.max()` | Returns the maximum value |
| `np.min()` | Returns the minimum value |
| `np.mean()` | Calculates the arithmetic mean |
| `np.sum()` | Calculates the sum or counts Boolean matches |
| `np.array_equal()` | Compares two arrays |
| `astype(float)` | Converts an array into floating-point values |

## Installation and Execution

### Step 1 – Install Python

Install Python on your system if it is not already installed.

### Step 2 – Install NumPy

Open the VS Code terminal and execute:

```bash
pip install numpy
```

### Step 3 – Create Python File

Create a Python file named:

```text
practice_numpy.py
```

### Step 4 – Execute the Program

Run the following command in the VS Code terminal:

```bash
python practice_numpy.py
```

### Step 5 – View Output

The program displays the results of all 10 tasks in the terminal.

## Key Concepts Learned

- NumPy array creation and manipulation.
- Random number generation.
- Statistical operations.
- Boolean indexing and masking.
- Conditional filtering.
- Random sampling.
- Array shuffling and permutation.
- In-place array modification.
- Data transformation and analysis.

## Conclusion

This assignment helped me understand how NumPy can be used for numerical data generation, filtering, statistical analysis, and array manipulation.

By completing all 10 tasks, I gained practical experience with random data generation, Boolean masking, conditional operations, and basic data-processing techniques.

These concepts are useful in data analysis, data science, and scientific computing.

---

**Project Status:** Completed

**Author:** Mohitha Reddy

**Repository:** NumPy Random Generation, Masking, and Array Manipulation
