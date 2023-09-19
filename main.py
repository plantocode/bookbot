with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)

    lower_text = file_contents.lower()
    normal_lower_text = "".join(ch for ch in lower_text if ch.isalpha())

    count_of_letter = {}
    for letter in normal_lower_text:
        if letter != " ":
            if letter not in count_of_letter.keys():
                count_of_letter[letter] = 1
            else:
                count_of_letter[letter] += 1
    
    sorted_count_of_letter = sorted(count_of_letter.items(), key=lambda x:x[1], reverse = True)

    print(
        f"--- Begin report of books/frankensteint.txt ---\n"
        f"{num_words} found in the document \n\n"
    )

    for i in range (len(sorted_count_of_letter)):
        print(f"The '{sorted_count_of_letter[i][0]}' character was found {sorted_count_of_letter[i][1]} times ")
    
    print("--- End of report ---")


    


