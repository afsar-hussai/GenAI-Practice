class InvalidChaiError(Exception): pass

def bill(flavour,cups):
    menu={
        "masala":20,
        "elaichi":25,
        "irani":50
        }
    try:
        if flavour not in menu:
            raise InvalidChaiError("Kindly give correct flavour")
        if not isinstance(cups, int):
            raise InvalidChaiError("Kindly give valid cups number")
        total=menu[flavour]*cups
        print(f"your total is {total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you for visiting our stall")

bill("something",5)
bill("elaichi","five")
bill("masala",5)
