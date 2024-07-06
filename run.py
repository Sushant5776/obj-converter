import json
from requests import request
from time import time
from colorama import Fore, Style
import pickle
import threading
from queue import Queue

json_decoder = json.JSONDecoder()
json_encoder = json.JSONEncoder()

result_queue = Queue()


def fetch_data(product):
    return request(
        method="POST",
        url="http://localhost:8000/create",
        data=json_encoder.encode(product),
        headers={"Content-Type": "application/json"},
    )


def calculate(iter_range: tuple[int, int], content, result_queue):
    t0 = time()
    items = []
    count = iter_range[0]
    thread_name = threading.current_thread().name

    for product in content[iter_range[0] : iter_range[1]]:
        res = fetch_data(product)
        items.append(res.json())

        count += 1

        print(f"Done with Item no. {count}")

    result_queue.put(
        {
            "name_of_thread": thread_name,
            "items_processed_by_thread": items,
        }
    )

    print(
        f"Thread {Fore.GREEN + thread_name + Style.RESET_ALL} processed {Fore.GREEN + str(count) + Style.RESET_ALL} products in {Fore.GREEN + str(round((time() - t0) / 60, 2)) + Style.RESET_ALL} mins."
    )


if __name__ == "__main__":
    offset = int(input("Please enter offset: "))
    thread_count = int(input("Please enter thread count: "))

    with open("utils/output.json", "r") as file_data:
        try:
            with open("data.pkl", "rb") as f:
                items = pickle.load(f)
                print("items loaded from pkl file")
        except Exception as _:
            print(
                "Failed to load items will generate pkl file once process gets completed!"
            )
            items = []

        content = file_data.read()
        content = json_decoder.decode(content)

        count = len(items)

        print(f"{count} items already processed!")

        threads = []

        for i in range(thread_count):
            start_idx = count + (offset * i)
            end_idx = start_idx + offset

            threads.append(
                threading.Thread(
                    target=calculate,
                    args=((start_idx, end_idx), content, result_queue),
                    name=str(i + 1),
                )
            )

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
            print(f"Thread {thread.name} completed processing!")

        while not result_queue.empty():
            product = result_queue.get()
            name_of_thread = product["name_of_thread"]
            items_processed_by_thread = product["items_processed_by_thread"]

            items.extend(items_processed_by_thread)

            print(f"{name_of_thread}'s items saved in list.")

            print(f"Count after thread {name_of_thread}: {len(items)}")

        with open("data.pkl", "wb") as f:
            print("Writing Output")
            pickle.dump(items, f)
