def word_count(text):
    num_words = len(text.split())
    return num_words

def character_count(text):
    character_dict = {}
    for character in text.lower():
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def sorted_count(text):
    character_dict = character_count(text)
    sorted_characters = []
    for character in character_dict:
        sorted_characters.append({character: character_dict[character]})
    return sorted_characters