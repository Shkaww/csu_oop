import sys
import pytest
from pattern_impl import NewsAgency, EmailSubscriber, SMSSubscriber

def run_example():
    print("=== Демонстрация паттерна Наблюдатель ===")
    
    # Создаем новостной канал
    agency = NewsAgency()
    
    # Создаем подписчиков
    email_sub = EmailSubscriber("alice@example.com")
    sms_sub = SMSSubscriber("+123456789")
    
    # Добавляем подписчиков в канал
    print("\nДобавляем подписчиков...")
    agency.add_observer(email_sub)
    agency.add_observer(sms_sub)
    
    # Публикуем новость
    print("\nПубликуем первую новость...")
    agency.add_news("Новость: Запущен новый спутник!")
    
    # Удаляем одного подписчика
    print("\nУдаляем email-подписчика...")
    agency.remove_observer(email_sub)
    
    # Публикуем еще одну новость
    print("\nПубликуем вторую новость...")
    agency.add_news("Новость: Новый рекорд скорости!")
    
    print("\n=== Демонстрация завершена ===")

def run_tests():
    print("=== Запуск тестов ===")
    # Запускаем pytest с файлом тестов
    pytest_args = ["tests_pattern.py", "-v"]
    sys.exit(pytest.main(pytest_args))

if __name__ == "__main__":
    # Проверяем, передан ли аргумент --run-tests
    if "--run-tests" in sys.argv:
        run_tests()
    else:
        run_example()