# ansible_hw
Ansible Homework: create and configure simple infrastructure uses Ansible, VBox, Docker, Nginx, Python ( Django, Flask, Gunicorn ) MariaDB.

Данный проект выполнен в рамках изучения Ansible.

Для корректной работы проекта необходимо:
 - на хосте с которого будет осуществляться запуск должен быть установлен Python и Ansible
 - в inventories/production/group_vars/all/all.yml прописать перемененную main_path таким образом, что б она указывала на каталог содержащий корень проекта.
 - в inventories/production/group_vars/all/  в файл id_rsa.pub положить публичный ключ с которым Ansible будет осуществлять подключение к хостам.
 - при запуске использовать файл ssk для раскодирования vault:  ansible-playbook site.yml --vault-password-file ssk
 
Описание содержимого файлов*:
 * - приведено только описание файлов необходимых для запуска отлаженого проекта на с nginx+gunicorn+flask+mariadb. 
 * - по аналогии можно собрать инфраструктуру с использованием  nginx+gunicorn+django+mariadb (нет готовой app django)
 * - по аналогии можно собрать инфраструктуру с использованием  nginx+nginx on hosts+mariadb (нет готовой app php)
 
Для запуска проекта полностью используйте:
 - site.yml
 
Для отдельного запуска сборки контейнеров:
 - build_co.yml - сборка образа контейнера CentOS
 - build_ub.yml - сборка образа контейнера Ubuntu
 - build_all.yml - сборка образов контейнера CentOS и Ubuntu
 
Для поднятия инфраструктуры (ДжампБох+Хост Апп на ЦентОС+Хост Апп на Убунту+База Данных):
 - run_infrastructure.yml
 
Для поднятия хостов отдельно есть роли, и файлы которые начинаются на run_, 
использовались в самом начале для отладки - запуск на свой страх и риск =)

Для конфигурирования всех серверов используются файлы:
 - config_all_flask.yml - nginx+2x(gunicorn+flask)+mariadb
 - config_all_django.yml - nginx+2x(gunicorn+django)+mariadb
 - config_all_nginx.yml - nginx+2x(nginx on hosts)+mariadb
 
Для конфигурирования серверов по отдельности используются файлы*:
* расписывать буду позже, назначение есть внутри файлов =)
 - config_*.yml
 - django_*.yml
 - flask_*.yml
 
 все что не описано было сделано для проверок работоспособности тех или иных функций Ansible
 и оставлено как примеры для последующих работ.
 
 Проект стремится к структуре лучших практик Ansible.
 в Свободное время будет дорабатываться, добавляться новые конфигурации, исправляться старые недочеты.
 
