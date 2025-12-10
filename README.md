# Project1_Andrey_Bykov_DPO
Проект консольной игровой программы 'Лабиринт Сокровищ'
Программа выполнена на трех модуля main player_actions utils.
Управление в игре производится за счет ввода команд в консоль.
Список всех команд с описанием выводится по использованию команды 
show_help.

Установка программы прозводится через команду Make build  далее Make 
install. Запуск через команду poetry run project


asciinema
=======================

Last login: Thu Dec 11 00:19:24 on ttys034
andrey@Andreys-Air ~ % ls -a
.				.zsh_history
..				.zsh_sessions
.CFUserTextEncoding		Applications
.DS_Store			Desktop
.Trash				Documents
.com.drweb.quarantine		Downloads
.config				Library
.cups				Movies
.easyeda			Music
.git				Pictures
.gitconfig			Public
.idlerc				README.md
.lesshst			Yandex.Disk.localized
.oracle_jre_usage		lab-0-3
.pgadmin			php_test
.ssh				python_test
.viminfo			pytonproject
.vscode				test .py
.yandex				user-git
.zprofile			Дистрибутивы
.zprofile.pysave
andrey@Andreys-Air ~ % cd pytonproject
andrey@Andreys-Air pytonproject % 
andrey@Andreys-Air pytonproject % ls -a
.				.git
..				Project1_Andrey_Bykov_DPO
andrey@Andreys-Air pytonproject % cd Project1_Andrey_Bykov_DPO
andrey@Andreys-Air Project1_Andrey_Bykov_DPO % 
andrey@Andreys-Air Project1_Andrey_Bykov_DPO % 
andrey@Andreys-Air Project1_Andrey_Bykov_DPO % 
andrey@Andreys-Air Project1_Andrey_Bykov_DPO % ls -a
.		.gitignore	Makefile	labyrinth_game
..		.ruff_cache	README.md	poetry.lock
.git		.venv		dist		pyproject.toml
andrey@Andreys-Air Project1_Andrey_Bykov_DPO % cd labyrinth_game
andrey@Andreys-Air labyrinth_game % 
andrey@Andreys-Air labyrinth_game % 
andrey@Andreys-Air labyrinth_game % ls -a
.			constants.py		player_actions.py
..			labyrinth.cast		utils.py
__init__.py		main.py
andrey@Andreys-Air labyrinth_game % nano labyrinth.cast

  UW PICO 5.09                                                                                    
File: labyrinth.cast                                                                                      

{"version": 2, "width": 80, "height": 24, "timestamp": 1765401628, "env": 
{"SHELL": "/bin/zsh", "TERM": "xterm-256color"}}
[0.017247, "o", "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m                                                                               
\r \r"]
[0.018241, "o", 
"\u001b]7;file://Andreys-Air.lan/Users/andrey/pytonproject/Project1_Andrey_Bykov_DPO/labyrinth_game\u0007"]
[0.019608, "o", "\r\u001b[0m\u001b[27m\u001b[24m\u001b[Jandrey@Andreys-Air 
labyrinth_game % \u001b[K\u001b[?2004h"]
[1.13922, "o", "\u001b[?2004l\r\r\n"]
[1.139557, "o", "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m                                                                               
\r \r"]
[1.14156, "o", 
"\u001b]7;file://Andreys-Air.lan/Users/andrey/pytonproject/Project1_Andrey_Bykov_DPO/labyrinth_game\u0007"]
[1.141757, "o", "\r\u001b[0m\u001b[27m\u001b[24m\u001b[Jandrey@Andreys-Air 
labyrinth_game % \u001b[K\u001b[?2004h"]
[1.682659, "o", "\u001b[?2004l\r\r\n"]
[1.683118, "o", "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m                                                                               
\r \r"]
[1.685371, "o", 
"\u001b]7;file://Andreys-Air.lan/Users/andrey/pytonproject/Project1_Andrey_Bykov_DPO/labyrinth_game\u0007"]
[1.685657, "o", "\r\u001b[0m\u001b[27m\u001b[24m\u001b[Jandrey@Andreys-Air 
labyrinth_game % \u001b[K\u001b[?2004h"]
[1.837612, "o", "\u001b[?2004l\r\r\n"]
[1.837957, "o", "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m                                                                               
\r \r"]
[1.840256, "o", 
"\u001b]7;file://Andreys-Air.lan/Users/andrey/pytonproject/Project1_Andrey_Bykov_DPO/labyrinth_game\u0007"]
[1.840572, "o", "\r\u001b[0m\u001b[27m\u001b[24m\u001b[Jandrey@Andreys-Air 
labyrinth_game % \u001b[K\u001b[?2004h"]
[2.51735, "o", "/opt/homebrew/bin/python3.14 
/Users/andrey/pytonproject/Project1_Andrey_Bykov_DPO/labyrinth_game/main.py\u001b[K"]
[3.174615, "o", 
"\u001b[A\u001b[24D\u001b[K\u001b[1B\r\u001b[K\u001b[A\u001b[36C"]
[4.836308, "o", "p"]
[4.99681, "o", "\bpo"]
[5.492049, "o", "e"]
[5.938962, "o", "t"]
[6.041731, "o", "r"]
[6.244737, "o", "y"]
[6.634155, "o", " "]
[7.368852, "o", "r"]
[7.853931, "o", "u"]
[8.093746, "o", "n"]
[8.240104, "o", " "]
[8.72933, "o", "p"]
[9.084448, "o", "r"]
[9.664089, "o", "o"]
[10.573276, "o", "j"]
[11.008283, "o", "e"]
[11.309773, "o", "c"]
[11.60079, "o", "t"]
[12.265086, "o", "\u001b[?2004l"]
[12.265289, "o", "\u001b[1B\r"]
[12.803668, "o", "Добро пожаловать в Лабиринт!\r\nНазвание текущей 
комнаты: ENTRANCE\r\nОписание комнаты: Вы в темном входе лабиринта. Стены 
покрыты мхом. На полу лежит старый факел.\r\nЗаметные предметы$
[16.799962, "o", "t"]
[17.045457, "o", "a"]
[17.760025, "o", "k"]
[18.214706, "o", "e"]
[18.476006, "o", " "]
[20.06173, "o", "t"]
[20.639546, "o", "o"]
[21.046, "o", "r"]
[21.449124, "o", "c"]
[21.741826, "o", "h"]
[22.873439, "o", "\r\n"]
[22.87366, "o", "Вы подняли: torch\r\nДля выхода из игры введите Quit 
\r\nВведите команду > "]
[25.096197, "o", "l"]
[25.324217, "o", "o"]
[25.466228, "o", "o"]
[25.696053, "o", "k"]
[26.01971, "o", "\r\n"]
[26.019948, "o", "Название текущей комнаты: ENTRANCE\r\nОписание комнаты: 
Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый 
факел.\r\nЗаметные предметы: \r\nДоступные выходы:  north->$
[26.020067, "o", "Для выхода из игры введите Quit \r\nВведите команду > "]
26.020067, "o", "Для выхода из игры введите Quit \r\nВведите команду > "]
[29.529049, "o", "e"]
[29.837901, "o", "a"]
[30.037316, "o", "s"]   
[30.288488, "o", "t"]
[30.840028, "o", "\r\n"]
[30.840331, "o", "Название текущей комнаты: TRAP_ROOM\r\nОписание комнаты: 
Комната с хитрой плиточной поломкой. На стене видна надпись: \"Осторожно — 
ловушка\".\r\nЗаметные предметы:  rusty_key\r\nДоступ$
[32.98626, "o", "t"] 
[33.287307, "o", "a"]
[33.964503, "o", "k"]
[34.373111, "o", "e"]
[34.869269, "o", " "]
[37.630168, "o", "rusty_key"]
[38.247182, "o", "\r\n"]
[38.247454, "o", "Вы подняли: rusty_key\r\nДля выхода из игры введите Quit 
\r\nВведите команду > "]
[39.630998, "o", "l"]
[39.796824, "o", "o"]
[40.295395, "o", "o"]
[40.46092, "o", "k"]    
[41.030123, "o", "\r\n"]
[41.030352, "o", "Название текущей комнаты: TRAP_ROOM\r\nОписание комнаты: 
Комната с хитрой плиточной поломкой. На стене видна надпись: \"Осторожно — 
ловушка\".\r\nЗаметные предметы: \r\nДоступные выходы$
[58.32278, "o", "w"]
[58.476872, "o", "e"]
[58.684669, "o", "s"]
[58.967931, "o", "t"]   
[59.720851, "o", "\r\n"]
[59.721162, "o", "Я нашел монетку\r\nНазвание текущей комнаты: 
ENTRANCE\r\nОписание комнаты: Вы в темном входе лабиринта. Стены покрыты 
мхом. На полу лежит старый факел.\r\nЗаметные предметы: \r\nДоступн$
[59.721335, "o", "Для выхода из игры введите Quit \r\nВведите команду > "]
[64.584434, "o", "n"]
82.318763, "o", " "]
[84.756357, "o", "treasure_key"]
[85.403116, "o", "\r\n"]
[85.403343, "o", "Вы подняли: treasure_key\r\nДля выхода из игры введите 
Quit \r\nВведите команду > "]
[86.335132, "o", "l"]
[86.529463, "o", "o"]   
[86.679374, "o", "o"]
[86.92129, "o", "k"]
[87.204534, "o", "\r\n"]
[87.204872, "o", "Название текущей комнаты: DINNING_ROOM\r\nОписание 
комнаты: Комната, посредине комнаты большой стол. Накрыт ужин, горят 
свечи, но никого нет.\r\nЗаметные предметы: \r\nДоступные выходы:$
[87.204908, "o", "Для выхода из игры введите Quit \r\nВведите команду > "]
[89.987903, "o", "g"]
[90.404757, "o", "o"]
[90.720503, "o", " "]   
[91.392869, "o", "e"]
[91.682122, "o", "a"]
[91.894405, "o", "s"]
[92.183219, "o", "t"]
[93.399646, "o", "\r\n"]
[93.399953, "o", "Название текущей комнаты: LIVING_ROOM\r\nОписание 
комнаты: Комната, большая кровать, перед ней красная вуаль и никого ... 
.\r\nЗаметные предметы: \r\nДоступные выходы:  west->dinning_ro$
[96.585916, "o", "s"]
[97.313029, "o", "o"]
[97.627356, "o", "u"]
[98.03513, "o", "t"]
[98.41393, "o", "h"]
[98.839538, "o", "\r\n"]
[98.839759, "o", "Вы используете найденный ключ, чтобы открыть путь в 
комнату сокровищ.\r\nВы в сокровищнице, вы можете попытаться открыть 
сундук (используйте команду open)\r\nНазвание текущей комнаты: T$
[108.337219, "o", "o"]
[108.520464, "o", "p"]
[109.014499, "o", "e"]
[109.633792, "o", "n"]
[110.340111, "o", "\r\n"]
[110.340443, "o", "Вы применяете ключ, и замок щёлкает. Сундук 
открыт!\r\nВ сундуке сокровище! Вы победили!\r\n"]
[110.340493, "o", "Игра завершена\r\n"]
[110.352282, "o", "\u001b[1m\u001b[7m%\u001b[27m\u001b[1m\u001b[0m                                                                               
\r \r"]
[110.353407, "o", 
"\u001b]7;file://Andreys-Air.lan/Users/andrey/pytonproject/Project1_Andrey_Bykov_DPO/labyrinth_game\u0007"]
[110.353556, "o", 
"\r\u001b[0m\u001b[27m\u001b[24m\u001b[Jandrey@Andreys-Air labyrinth_game 
% \u001b[K\u001b[?2004h"]
[114.992274, "o", "\u001b[?2004l\r\r\n"]
[114.99594, "o", "\r\nSaving session..."]
[115.009122, "o", "\r\n...copying shared history..."]
[115.01311, "o", "\r\n...saving history..."]
[115.022283, "o", "truncating history files..."]
[115.031034, "o", "\r\n..."]
[115.031134, "o", "completed.\r\n"]




