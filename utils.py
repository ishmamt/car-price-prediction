# file to hold functions

def assign_owner(num_owners):
    if num_owners == "New car":
        return 0
    elif num_owners == "1":
        return 1
    elif num_owners == "2":
        return 2
    elif num_owners == "3":
        return 3
    else:
        return 4


def assign_fuel(fuel_type):
    if fuel_type == "CNG":
        return (0, 0, 0, 0)
    elif fuel_type == "Diesel":
        return (1, 0, 0, 0)
    elif fuel_type == "Hybrid":
        return (0, 1, 0, 0)
    elif fuel_type == "LPG":
        return (0, 0, 1, 0)
    else:
        return (0, 0, 0, 1)


def assign_seller(seller_type):
    if seller_type == "Dealer":
        return (0, 0)
    elif seller_type == "Individual":
        return (1, 0)
    else:
        return (0, 1)


def assign_trans(trans_type):
    if trans_type == "Automatic":
        return 0
    else:
        return 1
