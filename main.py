import requests

API_URL = "http://localhost:8000/api/"

URLS = {
    "add": "add/",
    "substract": "substract/",
    "multiply": "multiply/",
    "divide": "divide/",
}

def call_api(operation: str, data: dict[str,float]) -> None:
    url = f'{API_URL}{URLS[operation]}'
    response = requests.post(url, json=data)

    return response.text


def valid_float(number: str) -> bool:
    try:
        float(number)
    except Exception as _:
        return False

    return True


def valid_input(operation: str, first: str, second: str) -> bool:
    if operation not in URLS.keys():
        return False

    if not valid_float(first):
        return False

    if not valid_float(second):
        return False

    return True


def main() -> None:
    while True:
        command = input(">> ")

        match command.split():
            case ["help"]:
                print("operation fisrt-number second-number")
            case ["exit"] | ["quit"] | ["q"]:
                return
            case [operation, first, second]:
                if not valid_input(operation, first, second):
                    print("There was an error processing the command")
                    continue

                response = call_api(operation, {
                    "first": float(first),
                    "second": float(second),
                })

                print(response)
            case _:
                print("There was an error processing the command")


if __name__ == "__main__":
    main()
