import random

def hangman():
    # Список слов для угадывания
    words = ["питон", "программа", "алгоритм", "виселица", "компьютер", "клавиатура"]
    secret_word = random.choice(words).lower()
    guessed_letters = set()  # Уже названные буквы
    attempts = 6  # Количество попыток
    
    print("Добро пожаловать в игру 'Виселица'!")
    print(f"Угадайте слово (оно состоит из {len(secret_word)} букв). У вас {attempts} попыток.")
    
    while attempts > 0:
        # Показываем текущее состояние слова (например, "_ _ _ _ _")
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"\nСлово: {display_word}")
        print(f"Осталось попыток: {attempts}")
        
        guess = input("Введите букву: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву!")
            continue
        
        if guess in guessed_letters:
            print("Вы уже называли эту букву!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print("Верно! Эта буква есть в слове.")
        else:
            print("Такой буквы нет в слове.")
            attempts -= 1
        
        # Проверяем, угадано ли слово полностью
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nПоздравляем! Вы угадали слово: '{secret_word}'!")
            break
    
    if attempts == 0:
        print(f"\nИгра окончена. Загаданное слово было: '{secret_word}'.")

# Запуск игры
if __name__ == "__main__":
    hangman()