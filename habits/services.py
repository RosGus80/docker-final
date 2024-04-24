import os

import requests


class TGBot:
    """Класс для взаимодействия с интерфейсом телеграм бота"""
    BASE_URL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('BOT_KEY')
    MY_CHAT_ID = os.getenv('TELEGRAM_ID')

    def send_message(self, chat_id=None, text=''):
        """Метод для отправки сообщения пользователю.
        Принимает: айди чата или по умолчанию - отправляет сообщение мне
        текст - текст сообщения"""
        chat_id = chat_id or self.MY_CHAT_ID
        requests.post(
            url=f'{self.BASE_URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
