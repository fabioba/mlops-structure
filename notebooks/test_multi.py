import multiprocessing

print('running')

class Test():
    def __init__(self):
        print('ciao')

    def worker(self, i,return_dict):
        print('worker: {}'.format(i))
        return_dict=i

'''
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        t=Test()
        p = multiprocessing.Process(target=t.worker, args=(i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())
'''

def print_test(i,return_dict):
    print('print_test: {}'.format(i))
    return_dict[i]=i

def print_no_test(i,return_dict):
    print('print_no_test: {}'.format(i))
    return_dict[i]=i

def run():

    print(multiprocessing.cpu_count())

    jobs=[]
    p_print_no_test = multiprocessing.Process(target=print_no_test, args=(1,{}))
    p_print_no_test.start()
    jobs.append(p_print_no_test)

    p_print_test = multiprocessing.Process(target=print_test, args=(1,{}))
    p_print_test.start()   
    jobs.append(p_print_test)

    for j in jobs:
        j.join()


if __name__ == "__main__":
    run()

    
