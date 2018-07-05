import argparse
import tracemalloc
import threading
import time

#Start tracing memory usage
tracemalloc.start()

# Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("--array_count", help="Number of items to add to the array", type=int, default=1000000)
ap.add_argument("--word_to_add", help="Word to add array_count times", default="1234567890")
ap.add_argument("--create_in_thread", help="When True, runs the function use_memory in a thread, otherwise calls without threads", default=True)
ap.add_argument("--threads_after_memory_hog", help="When true, creates 10 threads which sleep for 15 seconds after the memory hog has already taken place to see how memory is affected", default=True)
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
    time.sleep(15)

def convert_to_mb(bytes):
    mb_size = 1024*1000
    return (bytes/mb_size)

def use_memory():
    i = 0
    while i < args.array_count:
        try:
            mem_hog.append(args.word_to_add)
            i = i + 1
        except:
            print("Added", i, "items out of", args.array_count)

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

