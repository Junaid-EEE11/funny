import time
import multiprocessing
from form_filler import fill_form
from register import register_form

if __name__ == '__main__':
    url_form = "https//shop077.com/forgetPassword"
    url_register="https://shop077.com/register"

    # Example list of numbers
    numbers_list = [1521585344, 1234567890, 9876543210]
    processes = []
    for number in numbers_list:
        p = multiprocessing.Process(target=fill_form, args=(url_form, number))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    while True:
        for number in range(0,5):
            p = multiprocessing.Process(target=registe, args=url)
            p.start()
            processes.append(p)
        time.sleep(60)
