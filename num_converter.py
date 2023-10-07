# phone_number_converter

def convert_words_to_digits(phone_number_words):
    # Mapping of words to digits
    word_to_digit_mapping = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Split the phone number words and convert to digits
    words = phone_number_words.split()
    digits = ''.join(word_to_digit_mapping[word] for word in words if word in word_to_digit_mapping)
    return digits
