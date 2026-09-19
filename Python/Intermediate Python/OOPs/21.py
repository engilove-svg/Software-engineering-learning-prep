# Create a Custom Timer Context Manager

# You'll build a context manager that
#  measures how long a block of code takes to execute.
#  This is useful for performance monitoring in software engineering.


import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"Execution time: {execution_time:.2f} seconds")

with Timer():
    time.sleep(2)
    print("Code is running...")