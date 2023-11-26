## Написать функции для выполнения в pytest:

### Напишите тестовую фунцию test_check_sensor_ram_v40(), которая должна:

1) Открыть https://support.kaspersky.com/help/
2) Найти на странице Industrial CyberSecurity for Networks
3) Открыть версию 4.0
4) В справке открыть "About Kaspersky Industrial CyberSecurity for Networks"
5) Открыть "Hardware and software requirements"
6) Найти текст "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"
7) Проверить, что найденный текст соответствует тексту "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"
    
### Напишите тестовую фунцию test_check_sensor_ram_v30() которая должна:

1) Открыть https://support.kaspersky.com/help/
2) Найти на странице Industrial CyberSecurity for Networks
3) Открыть версию 3.0
4) В справке открыть "About Kaspersky Industrial CyberSecurity for Networks"
5) Открыть Hardware and software requirements
6) Найти текст "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."
7) Проверить, что найденный текст соответствует тексту "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."

### Напишите тестовую фунцию t	test_check_sensor_ram_v40_rus() которая должна:

1) Открыть https://support.kaspersky.com/help/
2) Найти на странице Industrial CyberSecurity for Networks
3) Открыть версию 4.0
4) В справке открыть "О Kaspersky Industrial CyberSecurity for Networks"
5) Открыть "Аппаратные и программные требования"
6) Найти текст "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"
7) Проверить, что найденный текст соответствует тексту "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"

#### Примечание:
Данная реализация подразумевает возможность непосредственного запуска и через pytest