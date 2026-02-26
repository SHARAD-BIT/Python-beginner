secret_word = "lion"
guess = ""
counter = 0
limit =3
lol = false
while guess != secret_word:
    if counter < limit:
       guess = input("Guess a letter: ")
       counter += 1
    else:
        lol = True

