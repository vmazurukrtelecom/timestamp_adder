import sys
from datetime import datetime

def add_timestamp(text):
    """Додає timestamp до вхідного тексту"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"{text} [Timestamp: {timestamp}]"

def add_timestamp_command():
    """Обробка команди з командного рядка"""
    if len(sys.argv) < 2:
        print("Помилка: Будь ласка, надайте текстовий аргумент")
        print("Використання: add-timestamp \"ваш текст\"")
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
    result = add_timestamp(text)
    print(result)

if __name__ == "__main__":
    add_timestamp_command()
