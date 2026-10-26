# Мій сайт — WESTY

Окремий Django-проєкт для персональної сторінки посилань WESTY. Інші сайти та
магазин у сусідніх папках не змінюються.

## Запуск на Windows

```powershell
cd "C:\Users\Admin\Desktop\сайт\мій сайт"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Сторінка: <http://127.0.0.1:8000/>  
Адмін-панель: <http://127.0.0.1:8000/admin/>

Після входу в адмінку відкрийте **Profile and links**. Додайте повні URL-адреси
із `https://` для кнопок My Telegram, TikTok, Info, Stars, Telegram Premium,
Price та Contact me. Тут можна змінювати назву, нік, цитату, адресу аватара,
назви, порядок і видимість кнопок. Якщо URL кнопки ще не вказаний, вона
відображається неактивною, а не веде на вигадане посилання.

## Публікація в інтернеті

Для постійної роботи розмістіть проєкт на хостингу з підтримкою Django. Перед
публікацією задайте секретний `DJANGO_SECRET_KEY`, встановіть `DJANGO_DEBUG=0`
і вкажіть домен у `DJANGO_ALLOWED_HOSTS`. `runserver` призначений лише для
локальної розробки.
