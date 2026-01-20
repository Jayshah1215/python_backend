month = input("Ente a month:")
match month:
    case month if month in("january","March","may","july","august", "october", "december"):
        print(f"{month} has 31 days")
    case month if month in ("april", "june", "september", "november"):
        print(f"{month} has 30 days")
    case month if month == "february":
        print(f"{month} has 28 or 29 days")
    case _:
        print("Invalid month name")
