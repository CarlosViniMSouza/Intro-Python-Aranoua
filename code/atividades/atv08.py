from IPython.display import clear_output
import requests
import json

def controlConsult():
    option = input("Do you want other consult? (Y|N): ")
    clear_output()

    if option == "Y":
        root()
    elif option == "N":
        print("get off ...")
    else:
        print("option invalid!")
        controlConsult()


def consult(id):
    req = requests.get("https://62507208977373573f3d77f0.mockapi.io/api/lib/library/{}".format(id))
    reqID = req.json()

    if "erro" not in reqID:
        print(f"\n{json.dumps(reqID, sort_keys=True, indent=4)}\n")
    else:
        print(f"Request Invalid!")

def root():
    inputID = input("Write a ID for consult: ")

    consult(inputID)
    controlConsult()


if __name__ == "__main__":
    root()

"""
Libs Interesting:

1. https://62507208977373573f3d77f0.mockapi.io/api/lib/library/
2. https://docs.python.org/3/library/json.html
"""
