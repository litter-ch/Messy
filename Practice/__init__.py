def count_time(func):
    def count(n):
        import time
        s = time.time()
        time.sleep(1)
        r = func(n)
        e = time.time()
        print(e - s)
        return r
    return count


@count_time
def main(n):
    for i in range(n):
        print(i)
    return


main(100)