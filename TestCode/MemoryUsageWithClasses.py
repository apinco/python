import argparse
import tracemalloc
import threading
import time

#Start tracing memory usage
tracemalloc.start()

# Define classes here (normally would be in another file, but for learning I am dropping it here
# to remove one layer of complexity
class Person:
    count = 0

    def __init__(self):
        Person.count += 1
        self.name = ""
    def set_name(self, name):
        self.name = name

class Employee(Person):
    count = 0

    def __init__(self):
        super().__init__()
        Employee.count += 1

class Student(Person):
    count = 0

    def __init__(self):
        super().__init__()
        Student.count += 1

# Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("--array_count", help="Number of items to add to the array", type=int, default=10000000)
ap.add_argument("--word_to_add", help="Word to add array_count times", default="1234567890")
ap.add_argument("--create_in_thread", help="When True, runs the function use_memory in a thread, otherwise calls without threads", default=True)
ap.add_argument("--threads_after_memory_hog", help="When true, creates 10 threads which sleep for 5 seconds after the memory hog has already taken place to see how memory is affected", default=True)
args = ap.parse_args()

#Define Globals
mem_hog = []

#Functions
def show_mem_usage(msg):
    print(msg)
    print("Length of array", len(mem_hog))
    (current, peak) = tracemalloc.get_traced_memory()
    print("current:", convert_to_mb(current), "peak:", convert_to_mb(peak))

def sleep_thread():
    time.sleep(5)

def convert_to_mb(bytes):
    mb_size = 1024*1000
    return (bytes/mb_size)

def use_memory():
    i = 1
    while i <= args.array_count:
        try:
            if (i % 2):
                o = Employee()
            else:
                o = Student()
            o.set_name(type(o).__name__ + str(o.count))
            mem_hog.append(o)
            i = i + 1
        except Exception as e:
            print("Error hit")
            print(e.__doc__)
            exit(0)

#Main Start
if (args.create_in_thread):
    print("Using threads")
    t = threading.Thread(target=use_memory)
    t.start()
    t.join()
else:
    print("No threads")
    use_memory()

if args.threads_after_memory_hog:
    for tc in range(10):
        t = threading.Thread(target=sleep_thread)
        t.start()
    show_mem_usage("Data after threads started:")
    mt = threading.current_thread()
    for tn in threading.enumerate():
        if tn is mt:
            continue
        tn.join()
    show_mem_usage("Data after threads joined:")

show_mem_usage("Data after Function:")

