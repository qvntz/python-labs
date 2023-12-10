import codecs
import sys
import time
from multiprocessing import Pipe, Process, Queue


def process_a(queue, pipe):
    while True:
        msg = pipe.recv()
        if msg == "END":
            break
        msg = msg.lower()
        queue.put(msg)


def process_b(main_conn, queue):
    while True:
        msg = queue.get()
        if msg == "END":
            break
        msg = codecs.encode(msg, "rot_13")
        main_conn.send(msg)


def main():
    with open("interaction.txt", "w") as f:
        time_format = "%Y-%m-%d %H:%M:%S"

        queue = Queue()
        main_conn, a_conn = Pipe()
        main_conn_b, b_conn = Pipe()
        p_a = Process(target=process_a, args=(queue, a_conn))
        p_b = Process(target=process_b, args=(b_conn, queue))
        p_a.start()
        p_b.start()

        while True:
            user_input = sys.stdin.readline()
            if not user_input.strip():
                break

            current_time = time.strftime(time_format, time.localtime())
            a_conn.send(user_input.strip())
            f.write(f"{current_time} [User] {user_input.strip()}\n")

            time.sleep(5)
            new_msg = main_conn.recv()
            current_time = time.strftime(time_format, time.localtime())
            f.write(f"{current_time} [Program] {new_msg}\n")
            print(f"{new_msg}")

        a_conn.send("END")
        main_conn.recv()  # Дожидаемся заверешния процесса B
        p_a.join()
        p_b.join()


if __name__ == "__main__":
    main()
