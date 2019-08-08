def main():
    import _thread, time

    lock = _thread.allocate_lock()

    global counter
    counter = 0

    def func(args):
        for arg in args:
            lock.acquire()
            print(arg)
            time.sleep(0.5)
            lock.release()
            time.sleep(1)
        global counter
        counter += 1
        return 0

    list_args = ((1,2,3),(4,5,6),(7,8,9))

    for args in list_args:
        _thread.start_new_thread(func, (args,))

    while counter < len(list_args):
        pass

if __name__ == '__main__':
    main()
