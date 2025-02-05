import timeit

# Code to time
code_to_time = """
[i**2 for i in range(1, 10)]
"""

# Measure the execution time
execution_time = timeit.timeit(code_to_time, number=1000000)

print(f"Execution time: {execution_time} seconds")