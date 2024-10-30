from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    start_time = time.perf_counter()
    
    print(cpu_count())
    a = Process(target=counter, args=(62500000,))
    b = Process(target=counter, args=(62500000,))
    c = Process(target=counter, args=(62500000,))
    d = Process(target=counter, args=(62500000,))
    i = Process(target=counter, args=(62500000,))
    f = Process(target=counter, args=(62500000,))
    g = Process(target=counter, args=(62500000,))
    h = Process(target=counter, args=(62500000,))
    l = Process(target=counter, args=(62500000,))
    m = Process(target=counter, args=(62500000,))
    n = Process(target=counter, args=(62500000,))
    o = Process(target=counter, args=(62500000,))
    p = Process(target=counter, args=(62500000,))
    t = Process(target=counter, args=(62500000,))
    s = Process(target=counter, args=(62500000,))
    k = Process(target=counter, args=(62500000,))
    
    a.start()
    b.start()
    c.start()
    d.start()  
    i.start()
    f.start()
    g.start()
    h.start()
    l.start()
    m.start()
    n.start()
    o.start()
    p.start()
    t.start()
    s.start()
    k.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    i.join()
    f.join()
    g.join()
    h.join()
    l.join()
    m.join()
    n.join()
    o.join()
    p.join()
    t.join()
    s.join()
    k.join()
    

    print("Finished in: ",(time.perf_counter() - start_time)," seconds")

if __name__ == '__main__':
    main()