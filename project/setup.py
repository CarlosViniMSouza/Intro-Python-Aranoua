import requests

def main():
    
    # Method GET
    req = requests.get("https://console.firebase.google.com/u/1/project/app02-aranoua/database/app02-aranoua-default-rtdb/data/~2F")

    print(req.status_code)
    print(req.json)

    # Method POST
    data = {
            "98670534": {
                "email": "souza@gmail.com", 
                "name": "Carlos", 
                "numero": "98670534"
            },
            "98076798": {
                "email": "vinisouza@gmail.com", 
                "name": "Vinicius", 
                "numero": "98076798"
            }
        }
    
    req = requests.post("https://console.firebase.google.com/u/1/project/app02-aranoua/database/app02-aranoua-default-rtdb/data/~2F", data=data)

    print(req.status_code)
    print(req.json)


if __name__ == "__main__":
    main()
