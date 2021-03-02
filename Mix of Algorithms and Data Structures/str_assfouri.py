def str_assfouri(string):
    new_string = ''
    for char in string:
        # isalpha() method return True if the character is letter, False otherwise
        if char.isalpha():
            new_string += char + 's'
        else:
            new_string += char
    return new_string


if __name__ == '__main__':
    print(str_assfouri('aab@=5 c') == 'asasbs@=5 cs')
    print(str_assfouri('Enjoying FCS') == 'Esnsjsosysisnsgs FsCsSs')
