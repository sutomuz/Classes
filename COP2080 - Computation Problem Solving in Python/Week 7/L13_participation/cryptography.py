import hashlib

original_hash = "d077f244def8a70e5ea758bd8352fcd8"

for letter in 'abcdefghijklmnopqrstuvwxyz':
    best_guess = 'ca' + letter
    h = hashlib.new('md5', best_guess.encode('UTF8')).hexdigest()
    print(best_guess, h)
    
    if h == original_hash:
        print("Correct 3 letter word:", best_guess)
        break


    letters = 'abcdefghijklmnopqrstuvwxyz'

for letter1 in letters:
    for letter2 in letters:
        xx = letter1 + letter2
        print(xx)