#import seaborn as sns
#import pandas as pd


#Question 1

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence

    Args:
        n (int): position in the sequence starting at 0

    Returns:
        int: Fibonacci value at position n
    """

    # Bases cases: first two numbers
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive step
    return fibonacci(n-1) + fibonacci(n-2)

# Test
# print(fibonacci(9)) => 34

# Question 2

def to_binary(n):
    """
    Convert a non-negative integer to its binary representation

    Args:
        n (int): integer to convert

    Returns:
        str: binary representation of n
    """

    # Base case: smallest values
    if n < 2:
        return str(n)
    
    # Recursive step: build binary from higher bits to lower bits
    return to_binary(n // 2) + str(n % 2)

# Tests
#print(to_binary(2)) => 10
#print(to_binary(12)) => 1100

# Question 3
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# Task i
def task_i():
    """Return column names sorted form least missing values to most missing values
    """

    df = df_bellevue.copy()

    # Fix issue with gender column (named "gender")
    df['gender'] = df['gender'].astype(str).str.strip().str.lower()

    missing_counts = df.isna().sum().sort_values()
    return list(missing_counts.index)

# Task ii
def task_ii():
    """
    Return a DataFrame with total admissions per year
    """

    df = df_bellevue.copy()

    admissions = (
        df.groupby('year')
            .size()
            .reset_index(name='total_admissions')
    )

    return admissions


# Task iii
def task_iii():
    """
    Return a series with gender as the index and average age as the values
    """

    df = df_bellevue.copy()

    #clean columns
    df['gender'] = df['gender'].astype(str).str.strip().str.lower()
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    return df.groupby('sex')['age'].mean()


# Task iv
def task_iv():
    """
    Return a list of the five most common professions
    """

    df = df_bellevue.copy()

    # Clean profession text
    df['profession'] = df['profession'].astype(str).str.strip().str.lower()

    top_five = (
        df['profession']
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return top_five



