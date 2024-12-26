from collections import deque

def is_palindrome(value):
    value = value.replace(" ", "")
    value = value.lower()
    word_deque = deque()

    for char in value:
        word_deque.append(char)

    while word_deque:
        if len(word_deque) == 1:
            return True
        elif word_deque.pop() != word_deque.popleft():
            return False
    return True


def main():
    while True:
        user_word = input("Please write a word ")
        if is_palindrome(user_word):
            print(user_word + " is a palindrome")
        else:
            print(user_word + " is not a palindrome")

if __name__ == "__main__":
    main()