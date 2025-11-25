# The riase syntax
'''
raise ExceptionType("Your Message")

Ex.
raise ValueError("Quantity must by at least 1")
raise TypeError("Expected a player object, got a potato")
raise PermissionError("You are not a mod, nice try thoug")
'''

# Just Returning
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    # rest of code
    
# Raising exception
def open_loot_box2(player, qty):
    if qty <= 0:
        raise ValueError("Bad qty")
    # rest of the code
    
    
VALID_PROTIENS = ["chicken", "steak", "barbecoa", "carnitas"]
VALID_RICE = ["white", "brown", 'none']
VALID_BEANS = ["black", 'pinto', 'none']
MAX_FREE_EXTRAS = 3

def build_bowl(protien, rice, extras):
    '''Build a Chipotle Bowl with Validatio
    
    Raises:
    ValueError if protien is invalid
    TypeError if extras is not a list
    '''
    
    # Check is extras is a list
    if not isinstance(extras, list):
         raise TypeError("Extras must be a list")
    if protien.lower() not in VALID_PROTIENS:
        raise ValueError(f"{protien} is not valid! Choose from {VALID_PROTIENS}.")
    return {
        'protein': protien.lower(),
        "rice": rice, 
        "extras": extras,
        "price": 10.50
    }
    
try:
    # bowl = build_bowl("chicken", "brown", "corn")
    bowl = build_bowl("chicken", "brown", ["corn"])
    print(f"Created: {bowl}")
except Exception as e:
    print(f"Error: {e}")