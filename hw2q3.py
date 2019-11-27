def preliminary_operations(brut: str):
    final = brut.replace('#', '*').replace('?', '')
    if final[-1] == '!':
        final = final[:-1]
    return final


def sentence_mutation(brut: str):
    final_value = ''
    for char in brut:
        if (ord(char) <= ord('Z') and ord(char) >= ord('A')) or (ord(char) <= ord('z') and ord(char) >= ord('a')):
            if ord(char) % 2 == 0:
                if ord(char.upper()) + shift > ord('Z'):
                    final_value += chr(ord(char.upper()) + shift + 6).lower()
                else:
                    final_value += chr(ord(char.upper()) + shift).lower()
            elif ord(char) % 2 != 0:
                if ord(char.lower()) - shift < ord('a'):
                    final_value += chr(ord(char.lower()) - shift - 6).upper()
                else:
                    final_value += chr(ord(char.lower()) - shift).upper()
        else:
            final_value += char
    return final_value


print('Please enter a sentence to encrypt:')
sentence = str(input())
print('Please enter the size of the shift:')
shift = int(input())
cleaned_value = preliminary_operations(sentence)
result = sentence_mutation(cleaned_value)
print(result)
