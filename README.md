# Трансляция VK Музыки в статус Telegram
[![Made with Python 3.10.4](https://img.shields.io/badge/Made_with-Python_3.10.4-336E9E?style=flat-square)][1]  
[![Beautiful Soup](https://img.shields.io/badge/Beautiful_Soup-1C4E63?style=flat-square)][2]
[![Telethon](https://img.shields.io/badge/Telethon-FFD750?style=flat-square)][3]

Транслируй музыку, которая играет у тебя VK Музыке в информацию о твоём профиле Telegram.

<img src="https://user-images.githubusercontent.com/22418658/172883534-9dc82cc4-7f69-4741-bf00-1e156309a1bc.png" alt="Скриншот профиля Telegram, демонстрирующий работу скрипта" height="350">

## Как настроить:
1. **[Скачай][4]** репозиторий на своё устройство
2. Открой терминал в папке репозитория
3. Установи зависимости: `pip install -r requirements.txt`
4. Запусти **setup.py** и следуй инструкциям: `python3 setup.py`
5. Запусти скрипт в первый раз для входа в Telegram: `python3 main.py`
6. Введи номер телефона и пароль (сессия хранится локально в файле **anon.session**, данные не пересылаются)
7. Настройка завершена! Скрипт уже начал работу 🚀

## Как запустить:
1. Повтори ш.5 из настройки скрипта: `python3 main.py`  
Входить повторно не придётся — модуль Telethon используется сессию из **anon.session**.

#### Спасибо [XuliGan4eg2006][5] за базу для написания скрипта ✊🏻

[1]: https://python.org
[2]: https://www.crummy.com/software/BeautifulSoup/
[3]: https://github.com/LonamiWebs/Telethon
[4]: https://github.com/PaveTranquil/vk-tg-music-broadcaster/archive/refs/heads/main.zip
[5]: https://github.com/XuliGan4eg2006
