# Q1
'''
2300
'''

# Q2
'''
WOW WOW LFG

POGGERS is too long
'''

# Q3
def find_top_donor(donations):
    top_donor_value = 0
    top_donor = ""
    for key, value in donations.items():
        if value > top_donor_value:
            top_donor = key
            top_donor_value = value
            
    return top_donor
            
    
donations_set = {
    "neon": 250, 
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donor(donations_set))