# Простой бот для демонстрации подключения и работы с коллекцией данных в MongoDB - Atlas
## Тестовое задание компании RLT

Полный список команд для установки MongoDB на Ubuntu 22.04:
```
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list 
sudo apt update 
sudo apt install libssl1.1
curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt update
sudo apt install -y mongodb-org
```
А также MongoDB Compas

```
wget https://downloads.mongodb.com/compass/mongodb-compass_1.32.3_amd64.deb
sudo apt install ./mongodb-compass_1.32.3_amd64.deb
```

Переменные окружения 
```
URI="" данные для подлючения к кластеру в MongoDB Atlas
DB_NAME='' имя базы данных
COLLECTION='' имя коллекции
TOKEN="" телеграм бот токен
```