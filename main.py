from pyscript import document

def candidate_checker(e):
    # Python 
    club_members = [
        'amor rita', 
        'cap jornales', 
        'jobe bellingham', 
        'stephanie garber', 
        'maui tang', 
        'conrad fisher', 
        'kiehla abuiza', 
        'hariette mae'
    ]
    
    # values from input fields
    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()
    
    candidate = f"{f_name} {l_name}"
    
    # evaluates to True or False
    member_checker = candidate.lower() in club_members

    messages = (
        f"Sorry {candidate}, your name is not on the list.",
        f"Congratulations {candidate}! You are now part of the Literary Creatives Club."
    )
    
    document.getElementById('output').innerHTML = messages[member_checker]