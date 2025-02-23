import json
data = {
    "ім'я": "Марія",
    "вік": "14",
    "улюблені предмети": [
        "математика",
        "інформатика"
    ]
}

with open ("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)