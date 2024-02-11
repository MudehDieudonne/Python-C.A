trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', 
         '10': 'shi'}

def convert_to_mandarin(num):
    """Convert a number (between 0 and 99) to Mandarin"""
    if num < 10:
        return trans[str(num)]
    elif num < 20:
        return trans['10'] + trans[str(num - 10)]
    elif num < 100:
        tens = num // 10
        ones = num % 10
        if ones == 0:
            return trans[str(tens)] + trans['10']
        else:
            return trans[str(tens)] + trans['10'] + trans[str(ones)]

num = 36
mandarin = convert_to_mandarin(num)
print(f"{num} in Mandarin is {mandarin}.")
