#!/bin/bash
echo "2022 (с) Давыдов Д.Э., support@easyastra.ru"
echo "Установка СУБД FireBird-4 в Astra Linux SE 1.7"

VERSION=$(</etc/astra_version)
SUB="1.7"

if [[ ! "$VERSION" =~ .*"$SUB".* ]]; then
    echo "Необходима ОС Astra Linux SE 1.7! Завершение..."
    exit
else
    echo "1 - Установить СУБД FireBird-4"
    echo "2 - Выйти"
    read ACTION
fi;

case $ACTION in
1) if [[ ! -f /opt/firebird/bin/firebird ]]; then
    sudo apt install libtommath1;
    wget https://easyastra.ru/files/soft/fb/Firebird-4.0.1.2692-0.amd64.tar.gz;
    tar xvzf Firebird-4.0.1.2692-0.amd64.tar.gz;
    cd Firebird-4.0.1.2692-0.amd64/;
    sudo ./install.sh;
    cd ..;
    wget https://easyastra.ru/files/soft/fb/firebird.conf;
    sudo mv firebird.conf /opt/firebird/;
    rm -r Firebird-4.0.1.2692-0.amd64/;
    rm Firebird-4.0.1.2692-0.amd64.tar.gz;
    echo "Установка СУБД FireBird-4 успешно выполнена!";
    echo "Нажмите ENTER для перезагрузки компьютера...";
    read;
    sudo reboot;
    else echo "СУБД FireBird-4 уже установлен в системе!";
  fi;;
2) exit;;
esac
