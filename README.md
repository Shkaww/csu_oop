Паттерн Наблюдатель (Observer)

Паттерн Наблюдатель определяет отношение "один-ко-многим" между объектами, где один объект (Subject) хранит список зависимых объектов (Observers) и уведомляет их об изменениях своего состояния. Это полезно, когда изменение состояния одного объекта должно автоматически отражаться на других.

Пример из жизни: Новостной канал публикует новости, а подписчики (например, пользователи приложения или email-рассылки) получают уведомления о новых публикациях.

В данном проекте реализован пример, где NewsAgency (Subject) уведомляет подписчиков (EmailSubscriber, SMSSubscriber) о новостях.

Установка и запуск

pip install pytest pytest-mock

pytest tests_pattern.py -v

Пример использования

В pattern_impl.py реализован новостной канал (NewsAgency), который позволяет подписчикам (EmailSubscriber, SMSSubscriber) получать уведомления о новых новостях. Подписчики могут подписываться и отписываться от канала. Пример кода:

from pattern_impl import NewsAgency, EmailSubscriber, SMSSubscriber

agency = NewsAgency()
email_sub = EmailSubscriber("user@example.com")
sms_sub = SMSSubscriber("+123456789")
agency.add_observer(email_sub)
agency.add_observer(sms_sub)
agency.add_news("Breaking News: Python 4.0 released!")
# Вывод:
# Email sent to user@example.com: Breaking News: Python 4.0 released!
# SMS sent to +123456789: Breaking News: Python 4.0 released!

Запуск тестов

Тесты проверяют:

Позитивные сценарии: добавление/удаление подписчиков, уведомление о новостях.

Негативные сценарии: попытка передать некорректные параметры (например, пустую новость).

Мок-тесты: подмена метода уведомления подписчика для проверки корректности вызова.

Для запуска тестов:

pytest tests_pattern.py -v