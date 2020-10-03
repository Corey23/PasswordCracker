import hashlib
import string

print('begin')
with open("output.txt", "w") as w:
    with open("salt.txt", "r") as f:
        salt = f.read().strip()


    hashes = []
    hashed = []
    for h in range(0, 51):
        hashed.append(0)

    with open("hashes.txt", "r") as f:
        for line in f:
            # strip new line character
            hash = line.strip()
            hashes.append(hash)

    passwords = []
    with open("rockyou.txt", "r", errors = "ignore") as f:
        for line in f:
            password = line.strip()
            passwords.append(password)

    numCorrect = 0
    i = 0
    for h in hashes:

        if hashed[i] == 0:
            for p in passwords:
        
                # concat salt and password, encode to utf-8
                salted_password = (salt + p).encode('utf-8')
                # hash salted password
                hash_value = hashlib.sha256(salted_password).hexdigest()

                if hash_value == h:
                    print(h + ": " + p, file=w)
                    hashed[i] = 1
                    numCorrect = numCorrect + 1
                    break
        i = i + 1

    i = 0
    for h in hashes:
        if hashed[i] == 0:

            with open("passwordDatabase.txt", "r", errors = "ignore") as f:
                for line in f:
                    p = line.strip()
                    # concat salt and password, encode to utf-8
                    salted_password = (salt + p).encode('utf-8')
                    # hash salted password
                    hash_value = hashlib.sha256(salted_password).hexdigest()
                    if hash_value == h:
                        print(h + ": " + p, file=w)
                        hashed[i] = 1
                        numCorrect = numCorrect + 1
                        break
        i = i+1

    i = 0
    for h in hashes:
        if hashed[i] == 0:

            with open("morewords.txt", "r", errors = "ignore") as f:
                for line in f:
                    p = line.strip()
                    # concat salt and password, encode to utf-8
                    salted_password = (salt + p).encode('utf-8')
                    # hash salted password
                    hash_value = hashlib.sha256(salted_password).hexdigest()
                    if hash_value == h:
                        print(h + ": " + p, file=w)
                        hashed[i] = 1
                        numCorrect = numCorrect + 1
                        break
        i = i+1

    alphabet = []
    alphabet = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    #words4 = []
    words3 = []
    words2 = []

    for a in alphabet:

        for b in alphabet:
            word = a + b
            words2.append(word)
            for c in alphabet:
                word = a + b + c
                words3.append(word)
                #for d in alphabet:
                    #word = a+b+c+d
                    #words4.append(word)

    for o in words2:
        i = 0
        for h in hashes:
            if hashed[i] == 0:

                # concat salt and password, encode to utf-8
                salted_password = (salt + o).encode('utf-8')
                # hash salted password
                hash_value = hashlib.sha256(salted_password).hexdigest()
                if hash_value == h:
                    print(h + ": " + o, file=w)
                    hashed[i] = 1
                    numCorrect = numCorrect + 1
                    break
            i = i + 1

    for o in words3:
        i = 0
        for h in hashes:
            if hashed[i] == 0:

                # concat salt and password, encode to utf-8
                salted_password = (salt + o).encode('utf-8')
                # hash salted password
                hash_value = hashlib.sha256(salted_password).hexdigest()
                if hash_value == h:
                    print(h + ": " + o, file=w)
                    hashed[i] = 1
                    numCorrect = numCorrect + 1
                    break
            i = i + 1

    print(numCorrect, file=w)
    i = 0
    for h in hashes:
        if hashed[i] == 0:
            print(h + ":", file=w)
        i = i + 1
