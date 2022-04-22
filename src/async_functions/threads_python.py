import threading
import time


def countdown(object, number):
    for num in range(1, number + 1):
        print(f'{num} {object}(s)...')
        time.sleep(1)


def main():
    th = threading.Thread(target=countdown, args=('elephant', 10))

    # th.start include the "th" function on pool to be executed.
    th.start()

    print('The programming is running... until the threads are wating.')
    print('Python Senior Developer ' * 2)

    # Tells to thread stop the programming until de threads are completed.
    th.join()

    print('Finished!')


if __name__ == '__main__':
    main()
