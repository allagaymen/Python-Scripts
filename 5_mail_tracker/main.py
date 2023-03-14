PLACEHOLDER = "[name]"

with open("./mail/inviters.txt") as names_file:
    names = names_file.readlines()

with open("./mail/starting_latter.text") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_latter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./sent_mails/letter_for_{stripped_name}.txt", mode="w") as confirmed_letters:
            confirmed_letters.write(new_latter)
