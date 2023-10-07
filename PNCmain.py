from num_converter import convert_words_to_digits

def main():
    phone_number_words = input("enter number in words:")
    phone_number_digits = convert_words_to_digits(phone_number_words)
    print("Phone number in words:", phone_number_words)
    print("Phone number in digits:", phone_number_digits)

if __name__ == "__main__":
    main()
