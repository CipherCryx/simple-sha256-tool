import hashlib

# Ask the user what action to perform
action = int(input("For hashing a number enter 1, for reversing a hash enter 2: "))

if action == 1:
    number = input("Please enter a number to hash: ")
    result_hash = hashlib.sha256(number.encode()).hexdigest()
    print(result_hash)

elif action == 2:
    target_hash = input("Please enter the hash to reverse: ")

    # Test numbers from 0 to 999999
    for i in range(1000000):
        guess = str(i)
        guess_hash = hashlib.sha256(guess.encode()).hexdigest()

        if guess_hash == target_hash:
            print("Original number is:", guess)
            break
    else:
        print("Number not found up to 1000000.")

else:
    print("Invalid input. Enter 1 or 2.")