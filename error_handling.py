def chai_order(type_):
    try:
        print("preparing chai...")
        if type_ == "unknown":
           raise ValueError("sorry we don't serve this type of chai")
    except ValueError as v:
        print("Error: ",v)
    else:
        print("serving chai, Enjoy....")
    finally:
        print(f"All done for this {type_}")
        
    
chai_order("unknown")
chai_order("something")
    