import requests
import json
from IPython.display import clear_output

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


def consult(cep):
    req = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    address = req.json()

    if "erro" not in address:
        print("CEP founded!\n")
        print(f"{json.dumps(address, sort_keys=True, indent=4)} \n")
    else:
        print(f"CEP {format(cep)} invalid!")

def root():
    cep_input = input("Write a Zip-Code for consultation: ")

    if (len(cep_input)) == 8:
        consult(cep_input)
    else:
        print("CEP Invalid!")

    controlConsult()


if __name__ == "__main__":
    root()
