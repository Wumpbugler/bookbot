def Main():

    import sys
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    def get_book_text(filepath):
        with open(filepath) as book:
            book_text = book.read()
        return book_text

    from stats import count_words
    from stats import character_count
    from stats import list_counts
    
    filepath = sys.argv[1]
    book_temp = get_book_text(filepath)
    num_words = count_words(book_temp)
    num_letters = character_count(book_temp)
    char_list = list_counts(num_letters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for l in char_list:
        if l["char"].isalpha():
            print(f"{l["char"]}: {l["num"]}")
        
    print("============= END ===============")
    

    return
Main()