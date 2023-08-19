# Реферальная система

### Описание
●	Авторизация по номеру телефона. Первый запрос на ввод номера телефона. Второй запрос на ввод кода \
●	Если пользователь ранее не авторизовывался, то записать его в бд \
●	Запрос на профиль пользователя \
●	Пользователю при первой авторизации присваивается рандомно сгенерированный 6-значный инвайт-код \
●	В профиле у пользователя есть возможность ввести чужой инвайт-код(при вводе проверять на существование). В своем профиле можно активировать только 1 инвайт код, если пользователь уже когда-то активировал инвайт код, то нужно выводить его в соответсвующем поле в запросе на профиль пользователя \
●	В API профиля должен выводиться список пользователей(номеров телефона), которые ввели инвайт код текущего пользователя. 
### Как пользоватся
устанавливаем зависимости

```
pip install -r requirements.txt
```
В директорий referal создайте файл .env и заполните следующим образом:

```
DEBUG = True
SECRET_KEY = 'django-insecure-4523yw%i7547a-zrd5f2qzk_b-e!1f+nw(4)p!w+xr(zi*%sv8'
ALLOWED_HOSTS = '*'
```
### API комманды и эндпоинты

Регистрация
```
http://127.0.0.1:8000/api/v1/signup/

{
    "phone": "номер телефона",
    "username": "имя пользователя"
}
```
Получаем токен
```
http://127.0.0.1:8000/api/v1/token/

{
    "phone": "номер телефона",
    "auth_code": "Код для авторизаций"
}
```
GET запрос - список тех,кто вас пригласил\
POST запрос - пригласить кого-то по чужому инват коду\
Этот эндпоинт не доступен без токена
```
http://127.0.0.1:8000/api/v1/profile/

{
    "invite_code": "чужой инвайт код",
}
```
