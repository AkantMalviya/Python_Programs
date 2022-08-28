def get_input():
    command = input(":").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown Verb {}".format(verb_word))
        return
    if len(command) >= 2:
        noun_word = command[1]
        print(f"you said {noun_word}")
    else:
        print("Nothing")

verb_dict = {"say": "say"}
while True:
    get_input()
