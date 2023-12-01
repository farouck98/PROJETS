import json

dict_to_convert = {
    "application_id": "54a32cba-994f-44ba-957b-77d156b3207b",
    "developer_id": "20e2662b-c39d-4327-b4c3-96013c4645f9",
    "name": "Super Python JSON debugger.",
    "paid": True,
    "price": 42.2,
    "price_unit": "euros",
}

target_filename = "9.6.dict_to_json.json"

def main():
    with open(target_filename, "w") as json_file:
        json.dump(dict_to_convert, json_file)

if __name__ == "__main__":
    main()