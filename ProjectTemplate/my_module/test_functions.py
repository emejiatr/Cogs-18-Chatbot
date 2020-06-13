from functions import compliment
from functions import insult
from functions import love
from functions import remove_punctuation

def compliment_test():
    assert compliment(['Hello', 'Too', 'pumpkin', 'compliment']) == True

def insult_test():
    assert insult(['cute', 'mango', 'insult', 'orange']) == True
    
def love_test():
    assert love(['nope', 'eye', 'love', 'corn']) == True
    
def remove_test():
    assert remove_punctuation('!!!Hello!@#?') == 'Hello'

