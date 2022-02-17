"""
Assignment 1

Marko Vrljes
501032932

The code under is an added code to the translate.py code given.
It has multiple improvements that make the code much better.
"""

"""
# This function helped me make my English to Spanish Dictionary and also
# reversed this dictionary which gave me the Spanish to English dictionary
def make_dict():
    inp = ""

    our_dict = {}

    while inp != "stop":
        inp = input("Please enter a key: ")
        inp_prod = input("Now please enter a value: ")
        # Creates a key and associated value
        our_dict[inp] = inp_prod
        inp = input("Would you like to continue? Type 'stop' to stop. ")

    # this line reverse the above dictionary ( our_dict() ) that was made
    reversed_dictionary = {value: key for (key, value) in our_dict.items()}

    print('EtoS = ', our_dict)
    print('StoE = ', reversed_dictionary)


make_dict()
"""

# This is the English to Spanish dictionary made
# the domain for it is sports
EtoS = {'soccer': 'futbol', 'basketball': 'baloncesto', 'hockey': 'hockey', 'swimming': 'nadando',
        'vollyball': 'voleibol', 'riding': 'montando', 'bicycle': 'bicicleta', 'shot': 'disparo', 'save': 'salvar',
        'ski': 'esqui', 'sports': 'deportes', 'love': 'amor', 'play': 'tocar', 'fun': 'divertido', 'he': 'el',
        'she ': 'ella', 'her': 'su', 'ball': 'pelota', 'throw': 'lanzar', 'puck': 'disco', 'run': 'correr',
        'running': 'corriendo', 'what': 'que', 'to': 'a', 'water': 'agua', 'drink': 'beber', 'I': 'yo', 'me': 'yo',
        'with': 'con', 'good': 'bien', 'very': 'muy', 'have': 'tener', 'game': 'juego', 'athlete': 'atleta',
        'champion': 'campeon', 'gym': 'gimnasio', 'pool': 'piscina', 'race': 'carrera', 'scored': 'anotado',
        'strike': 'huelga', 'tennis': 'tenis', 'team': 'equip', 'uniform': 'uniforme', 'friend': 'amigo',
        'win': 'ganar', 'weight': 'peso', 'goal': 'objectivo', 'defense': 'defensa', 'attack': 'ataque', 'an' : 'un',
        'goalie': 'portero', 'foul': 'falta', 'class': 'clase', 'car': 'coche', 'bucket': 'cubeta', 'gamble': 'jugar'}

# This is the Spanish to English dictionary
StoE = {'futbol': 'soccer', 'baloncesto': 'basketball', 'hockey': 'hockey', 'nadando': 'swimming', 'montando': 'riding',
        'bicicleta': 'bicycle', 'disparo': 'shot', 'salvar': 'save', 'esqui': 'ski', 'deportes': 'sports',
        'amor': 'love', 'tocar': 'play', 'divertido': 'fun', 'el': 'he', 'ella': 'she ', 'su': 'her',
        'amigo': 'friend', 'pelota': 'ball', 'lanzar': 'throw', 'tiro': 'threw', 'disco': 'puck', 'correr': 'run',
        'corriendo': 'running', 'que': 'what', 'a': 'to', 'agua': 'water', 'beber': 'drink', 'yo': 'me', 'con': 'with',
        'bien': 'good', 'muy': 'very', 'tener': 'have', 'juego': 'game', 'atleta': 'athlete', 'campeon': 'champion',
        'gimnasio': 'gym', 'piscina': 'pool', 'carrera': 'race', 'anotado': 'scored', 'huelga': 'strike',
        'tenis': 'tennis', 'equip': 'team', 'uniforme': 'uniform', 'ganar': 'win', 'peso': 'weight', 'objetivo': 'goal',
        'defensa': 'defense', 'ataque': 'attack', 'portero': 'goalie', 'falta': 'foul', 'clase': 'class', 'un' : 'an',
        'coche': 'car', 'cubeta': 'bucket', 'jugar': 'gamble'}

# A dictionary later used for the direction of translation and also shows what each language corresponds to which
# dictionary
dicts = {'English to Spanish': EtoS, 'Spanish to English': StoE}


# This function takes the word given from the translate(phrase) function and checks if it is in the dictionary,
# If it is in the dictionary then it just returns the translated word it, but if it isn't then the dict then it returns
# the word with quotations around it
def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word


# This function splits up the phrase into characters and groups the words if they are in the domain of characters,
# it then send them to the above function
# it then adds up all of the outputs from the above function into the final translated phrase
def translate(phrase):
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    # this helped with automatically knowing which direction to translate it without specification
    for key in phrase.split():
        if key in EtoS:
            dictionary = dicts['English to Spanish']
        elif key in StoE:
            dictionary = dicts['Spanish to English']
    translation = ''
    word = ''
    # this is wear it goes through each letter till a space then groups the words and form the final translation
    for character in phrase:
        if character in letters:
            word = word + character
        else:
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    # removed the + character at the end which resolves the period problem
    translation = translation + translateWord(word, dictionary)
    return translation


# THIS FUNCTION WORKS BUT NOT FOR THIS PROGRAM SINCE I DON'T KNOW HOW TO MAKE THE PARAMETER A STRING
# This function makes the word a plural if there was a 2 in the sentence
# Example -- 2 campeon (2 champion) would of been 2 campeons (2 champions)
def improvePlural(final):
    final = str(final)
    end = final[:]
    # if one of these words was in the sentence with a 2 in it an added s would come after the word
    for word in final.split():
        if word == 'disparo' or word == 'campeon' or word == 'clase' or word == 'objectivo':
            if '2' in final:
                end = final.replace(word, word + 's')
            else:
                end = final
    # .capitalize() fixes the problem with the capital letter at the start
    return end.capitalize()


if __name__ == '__main__':
    sentence = 'I love to play soccer with my friend.'
    translated = translate(sentence)
    translated = str(translated)
    print('--------------------------------------')
    print('Input:', sentence.capitalize())
    print('Output:', improvePlural(translated))
    print('--------------------------------------')

    sentence = 'su equip anotado un asombroso objectivo.'
    translated = translate(sentence)
    print('Input:', sentence.capitalize())
    print('Output:', improvePlural(translated))
    print('--------------------------------------')
    # Option for user input
    sentence = str(input("Enter what you want to be translated: "))
    translated = translate(sentence)
    print('--------------------------------------')
    print('Input:', sentence.capitalize())
    print('Output:', improvePlural(translated))
    print('--------------------------------------')
