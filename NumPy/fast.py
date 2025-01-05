

import timeit

# Define a code snippet to time
# code_to_test = """
# my_list = [i for i in range(1000)]
# """
code_to_test= [2,3,4,5,6]
# Use timeit to measure the execution time
execution_time = timeit.timeit(code_to_test)
print(f"Time taken to create the list: {execution_time} seconds")