import threading
import time


def countdown(object, number):
    for num in range(1, number + 1):
        print(f'{num} {object}(s)...')
        time.sleep(1)


def main():
    threads = [
        threading.Thread(target=countdown, args=('computer', 10)),
        threading.Thread(target=countdown, args=('notebook', 9)),
        threading.Thread(target=countdown, args=('developer', 8)),
        threading.Thread(target=countdown, args=('cellphone', 12)),
    ]

    # th.start include the "th" function on pool to be executed.
    [thread.start() for thread in threads]

    print('The programming is running... until the threads are wating.')
    print('Python Senior Developer ' * 2)

    # Tells to thread stop the programming until de threads are completed.
    [thread.join() for thread in threads]

    print('Finished!')


if __name__ == '__main__':
    main()
