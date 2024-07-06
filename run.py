import json
from requests import request
from time import time
from math import ceil
from colorama import Fore, Style
import pickle

json_decoder = json.JSONDecoder()
json_encoder = json.JSONEncoder()


def fetch_data(product):
    return request(
        method="POST",
        url="http://localhost:8000/create",
        data=json_encoder.encode(product),
        headers={"Content-Type": "application/json"},
    )


if __name__ == "__main__":
    with open("utils/output.json", "r") as json:
        with open("data.pkl", "rb") as f:
            items = pickle.load(f)
        content = json.read()
        count = len(items)
        total_items_count_to_complete = count + 10
        t0 = time()
        for product in json_decoder.decode(content):
            if count >= total_items_count_to_complete:
                with open("data.pkl", "ab") as f:
                    print("writing output")
                    pickle.dump(items, f)
                break
            res = fetch_data(product)
            items.append(res.json())
            count += 1
            print(f"Done with Item no. {count}")
        print(
            f"Done {Fore.GREEN + str(count) + Style.RESET_ALL} products in {Fore.GREEN + str(round((time() - t0) / 60, 2)) + Style.RESET_ALL} mins."
        )
