import time
seconds = 30
def timecheck():
    while True:
        main()
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > seconds:
            print("Time out")
            print(textlist)
            break

timecheck()