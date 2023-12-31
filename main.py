import time
import multiprocessing
from form_filler import fill_form
from register import register_form

if __name__ == '__main__':
    url_form = "https://shop077.com/forgetPassword";
    url_register="https://shop077.com/register?invide_code=fa4e9ec";
    
    numbers_list = [1521585344, 1713850617, 1312429829, 1512429529];
    processes = [];
    for number in numbers_list:
        p = multiprocessing.Process(target=fill_form, args=(url_form, number))
        p.start();
        processes.append(p);
    for process in processes:
        process.join()
    while True:
        for number in range(0,2):
            p = multiprocessing.Process(target=register_form, args=(url_register,number))
            p.start()
            processes.append(p)
        time.sleep(60)
