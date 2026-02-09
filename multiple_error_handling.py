def process_order(item,quantity):
    try:
        price={
        "masala":20,
        "elaichi":25,
        "irani":50
        }[item]
        cost=price*int(quantity)
        print(f"total cost is {cost}")
    except ValueError as v:
        print("Please give correct quantity")
    except KeyError as k:
        print("Please give correct chai type")
    
process_order("syhgfjfu",20)
process_order("elaichi","five")

