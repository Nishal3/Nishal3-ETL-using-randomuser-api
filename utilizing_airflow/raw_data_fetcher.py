import random
import json
import requests
import time


def data_fetcher(data_to_load=1, link="https://randomuser.me/api/"):
    with open("raw_user_data.json", "w") as output_file:
        final_output = []
        while data_to_load > 0:
            api = requests.get(link)
            cleaned = json.loads(api.text)["results"][0]
            final_output.append(cleaned)
            data_to_load -= 1
            time.sleep(0.01)

        json.dump(final_output, output_file, indent=4)


if __name__ == "__main__":
    data_fetcher(2)
