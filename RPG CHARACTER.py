full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    if not all([isinstance(strength, int), isinstance(intelligence, int), isinstance(charisma, int)]):
        return "All stats should be integers"
    
    if any([strength < 1, intelligence < 1, charisma < 1]):
        return "All stats should be no less than 1"
    
    if any([strength > 4, intelligence > 4, charisma > 4]):
        return "All stats should be no more than 4"
    
    if sum([strength, intelligence, charisma]) != 7:
        return "The character should start with 7 points"
    
    character = name
    character += f"\nSTR {full_dot * strength}{empty_dot * (10 - strength)}"
    character += f"\nINT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
    character += f"\nCHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    
    return character


print(create_character('ren', 4, 2, 1))

#FreeCode.camp