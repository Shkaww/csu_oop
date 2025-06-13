import pytest
from unittest.mock import Mock
from pattern_impl import NewsAgency, EmailSubscriber, SMSSubscriber, Observer

def test_add_and_notify_observer(capsys):
    """Проверяет, что подписчики добавляются и получают уведомления."""
    agency = NewsAgency()
    email_sub = EmailSubscriber("test@example.com")
    sms_sub = SMSSubscriber("+123456789")
    
    agency.add_observer(email_sub)
    agency.add_observer(sms_sub)
    
    agency.add_news("Test news")
    captured = capsys.readouterr().out
    assert "Email sent to test@example.com: Test news" in captured
    assert "SMS sent to +123456789: Test news" in captured

def test_remove_observer(capsys):
    """Проверяет, что удаленный подписчик не получает уведомления."""
    agency = NewsAgency()
    email_sub = EmailSubscriber("test@example.com")
    
    agency.add_observer(email_sub)
    agency.remove_observer(email_sub)
    
    agency.add_news("Test news")
    captured = capsys.readouterr().out
    assert "Email sent" not in captured

def test_empty_news_raises_error():
    """Проверяет, что пустая новость вызывает ошибку."""
    agency = NewsAgency()
    with pytest.raises(ValueError, match="News message cannot be empty"):
        agency.add_news("")

def test_invalid_email_raises_error():
    """Проверяет, что некорректный email вызывает ошибку."""
    with pytest.raises(ValueError, match="Invalid email address"):
        EmailSubscriber("invalid_email")

def test_invalid_phone_raises_error():
    """Проверяет, что некорректный номер телефона вызывает ошибку."""
    with pytest.raises(ValueError, match="Invalid phone number"):
        SMSSubscriber("123456789")

def test_mock_observer_update():
    """Проверяет, что метод update наблюдателя вызывается с правильным аргументом."""
    agency = NewsAgency()
    mock_observer = Mock(spec=Observer)
    
    agency.add_observer(mock_observer)
    agency.add_news("Test news")
    
    mock_observer.update.assert_called_once_with("Test news")