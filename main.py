import time
import multiprocessing
from form_filler import fill_form

if __name__ == '__main__':
    url = "https//shop077.com/forgetPassword"

    # Example list of numbers
    numbers_list = [1521585344, 1234567890, 9876543210]
    processes = []
    for number in numbers_list:
        p = multiprocessing.Process(target=fill_form, args=(url, number))
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for process in processes:
        process.join()
    while True:
        for number in numbers_list:
            p = multiprocessing.Process(target=fill_form, args=(url, number))
            p.start()
            processes.append(p)
        time.sleep(60)
