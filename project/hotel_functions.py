import json

# Function to load hotel data from a JSON file
def load_hotels(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception:
        return []

# Function to save hotel data to a JSON file
def save_hotels(hotels, filename):
    with open(filename, 'w') as file:
        json.dump(hotels, file, indent=4)

def add_hotel():
    return "hotel_data"

def delete_hotel(hotels_):
    search_hotel_id = int(input("Enter hotel Id"))
    for hotel in hotels_:
        if(search_hotel_id == hotel["ID"]):
            hotels_.remove(hotel)
            print(f"hotel removed successfully")
            break
    else:
        print("Hotel not found")

def update_rating(hotels_,FILENAME):
    #hotel id
    search_hotel_id = int(input("Enter hotel Id"))

def fetch_hotel(hotels_):
    for hotel in hotels_:
        print( "ID: {}, {}, {}, {}".format(hotel["ID"], hotel["name"], hotel["location"], hotel["rating"]))

def find_hotel(hotels_):
    print("Hotel not found")

