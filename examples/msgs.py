from email import message
from aiogram import Bot, Dispatcher, executor, types
import logging, os

""" HERE IS DEFAULTS MESSAGES """

hellomsg = '👋Приветствую тебя, {0.first_name}!'
botname = 'Меня зовут <b>{1.first_name}<b>!'

# -- trigger words --
morning_trigger = ['MORNING', 'УТРЕЧКА', 'ДОБРОЕ УТРО', 'УТРО', 'УТРО ДОБРОЕ', 'УТРЕЧКО']
laugh_trigger = ['ХАХ', 'АЗА', 'АЗАЗАЗ', 'ХАЭААЖАХХАЖА', 'ХЕХ', 'ХЕХЕХЕ', 'AHAHAHHAHAHA', 'HAHAHAHAHA', 'HEHEHE']
#   GAMES
dice_cmd = ['🎲 DICE', 'DICE', 'дайс', 'Кубик']
casino_cmd = ['🎰 CASINO', '🎰 Casino' , 'Казино', 'Казик']
dart_cmd = ['🎯 DART', 'Dart' , '🎯 ДАРТ', 'Дарт', '🎯']
football_cmd = ['⚽ FOOTBALL', 'FOOTBALL', 'Футбик', 'Футболл', 'Футбол']
basketball_cmd = ['🏀 BASKETBALL', 'BASKETBALL', 'Баскетбол', 'Баскетболл', 'Баскет', '🏀']
bowling_cmd = ['🎳 BOWLING', '🎳 БОУЛИНГ', 'БОУЛИНГ','Кегли']
gn_cmd = ['УГАДАЙ ЧИСЛО', 'GUESS THE NUMBER', 'GN']
sheesh_cmd = ['sheesh', 'sheeesh', 'sheeeesh', 'sheeeeesh', 'shish', 'shiish', 'shiiish', 'шиш', 'шииш', 'шиииш', 'шииииш', 'шиииииш', 'шииииииииш']
#   Sport screems
csk_cmd = ['ЦСК', 'ЦСКА', 'CSK', 'CSKA']
spartak_cmd = ['СПАРТАК', 'SPARTAK']

# -- Answers --
laugh_answers = ['Аха-хах да, ржомба!', 'Аха-хах да, ржомба!😂', 'Аха-хах да, ржомба!', 'Аха-хах да, ржомба!🤣', '🤣', 'Хех 😅']
# -- Smiles --
smiles_list = ['😀','😃','😄','😁','😆','😅','😂','🤣','🥲','☺️','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🥸','🤩','🥳','😏','😒','😞','😔','😟','😕','🙁','☹️','😣','😖','😫','😩','🥺','😢','😭','😤','😠','😡','🤬','🤯','😳','🥵','🥶','😶‍🌫️','😱','😨','😰','😥','😓','🤗','🤔','🤭','🤫','🤥','😶','😐','😑','😬','🙄','😯','😦','😧','😮','😲','🥱','😴','🤤','😪','😮‍💨','😵''😵‍💫''🤐','🥴','🤢','🤮','🤧','😷','🤒','🤕','🤑','🤠','😈','👿','👹','👺','🤡','💩','👻','☠️','👽','👾','🤖','🎃','😺','😸','😹','😻','😼','😽','🙀','😿','😾','🤝','👍','👎','👊','✊','🤛','🤜','🤞','✌️','🤟','🤘','👌','🤌','🤏','👈','👉🏻','👆','👇','☝️','✋','🤚','🖐','🖖','👋','🤙','💪','🦾','🖕','✍️','🙏','🦶','🦵','🦿','💄','💋','👄','🦷','👅','👃','👣','👁','👀','🧠','🗣','👤','👥','🫂','👶','👧','🧒','👦','🦱','👱‍♀️','👱','👱‍♂️','🧔‍♀️','🧔','👵','🧓','👴','👲'',👳‍♀️','👳','👳‍♂️','🧕','👮‍♀️','👮','👮‍♂️','👷‍♀️','👷','👷‍♂️','💂‍♀️','💂','💂‍♂️','🕵️‍♀️','🕵️','🕵️‍♂️','🧙','🧝‍♂️','🥷','🧜‍♂️','🙆','🙆‍♀️','🙆‍♂️','🙋','🙋‍♂️','💃','🕺','👯‍♀️','🚶','🧎‍♂️','🏃‍♀️','🏃','🏃‍♂️','🧍‍♀️','👬','🪡','🧥','🥼','🧶','👚','👕','👖','🎩','🧣','🧤','🧢','👒','🎓','⛑','🪖','👑','💍','👝','👛','👜','💼','🎒','🧳','👓','🕶','🥽','🌂', '❤️']

stikers_list = ['CAACAgIAAxkBAAEFiati9YZz7TZakbkynCKzPARiu1Pb-AACbRQAAvh48Ev_35tLbqKxRykE', 'AACAgIAAxkBAAEFia1i9YZ07HCZsaFgbRA-sf4u3VymSQAC6yMAAj_lAUl35ZIodwxRkykE']
green_lizard_stikers = ['CAACAgIAAxkBAAEFiqpi9nWoJW4FrRULEUFI5TbzHBNuAgACwgAD9wLID96foOapLgziKQQ', 'CAACAgIAAxkBAAEFiqxi9nWrPchHSO1R2DzhuH7Jb3hROQACtQAD9wLIDzOvqyodfzZvKQQ', 'CAACAgIAAxkBAAEFiq5i9nWu6JkSb7YVC7YxkHcY4JnnZgACugAD9wLID_0MODzqmFe5KQQ', 'CAACAgIAAxkBAAEFirBi9nWxTngscnAY5BNWAAE5Ef2KM84AArwAA_cCyA8zr8vPYniagSkE', 'CAACAgIAAxkBAAEFirJi9nWz8n5yCCtNYPnG9tdPA1ESmgACvAAD9wLIDzOvy89ieJqBKQQ', 'CAACAgIAAxkBAAEFirRi9nXC5qLvP5ugTGEizsxCQzZr3wACuAAD9wLID0YLnLTiTgs4KQQ', 'CAACAgIAAxkBAAEFirZi9nXFDAdOMWUyFUkwestFLF5yogACtwAD9wLID5Dxtgc7IUgdKQQ', 'CAACAgIAAxkBAAEFirhi9nXJUOz41sVTSo59m4qIJjNrRQACuQAD9wLID5Ahqvg5d0bYKQQ', 'CAACAgIAAxkBAAEFirpi9nXNzh8tnatCIlAcmunSyVWbjAAC0AAD9wLIDyZtRF2ev7O_KQQ', 'CAACAgIAAxkBAAEFirxi9nXQ4FYjr50rDyYsKqSzu5-vTQACvQAD9wLIDx2aqkRb2DeaKQQ', 'CAACAgIAAxkBAAEFir5i9nXVAAFbsELc9t5CEp3ldiLHESAAAsMAA_cCyA-ScOAAAWuXY2UpBA', 'CAACAgIAAxkBAAEFisBi9nXYMY2BivnSlG3fQHa9q6zIhgACvgAD9wLID2NpaQGUlw4kKQQ', 'CAACAgIAAxkBAAEFisJi9nXbMtGm9jzNm2opf5sj-InIVQACvwAD9wLID8qXLow7_RMvKQQ', 'CAACAgIAAxkBAAEFisRi9nXfrfAB-77O-0jk17HeOSo0sAACwAAD9wLID1T13GCuDbNaKQQ', 'CAACAgIAAxkBAAEFisZi9nXjPwEHZiGaUWxAL1S4Qy5GZgACwQAD9wLID2JmDHNJYyc5KQQ', 'CAACAgIAAxkBAAEFishi9nXpiY-yRJQHdg0BlljyV4uE7gACuwAD9wLID2SXQZNlMBzAKQQ', 'CAACAgIAAxkBAAEFispi9nXtA9W0MKHFsCaH-B2vPBlvfwACxAAD9wLIDwxl0XWs1Rg9KQQ', 'CAACAgIAAxkBAAEFisxi9nXyzb4qDgsjk7g-a3-0XPr3KAACxQAD9wLID7s40cGklXikKQQ', 'CAACAgIAAxkBAAEFis5i9nX4X92CQWBDdaFDHhxQuZ9r2gACyQAD9wLID4KSRkmwBpN8KQQ', 'CAACAgIAAxkBAAEFitBi9nX8cKBDZLU9EAdTARc-39Nv3gACygAD9wLIDwQk_4gT6LTDKQQ', 'CAACAgIAAxkBAAEFitJi9nX_xmi2x9puI-uAT4EIi7SV0QACywAD9wLID6AkdNt7g-RaKQQ', 'CAACAgIAAxkBAAEFitRi9nYDWOTJ2Se8xFNW1UcsMY-CsQACzAAD9wLID0v7TB_rXdKjKQQ', 'CAACAgIAAxkBAAEFitZi9nYGXAcoelqn1kbRH36tY2Xt0AACzgAD9wLID1yYR-DMq26KKQQ', 'CAACAgIAAxkBAAEFithi9nYLYSqujIztrTVQTM8lPCECugACzQAD9wLIDxCD-C_rPlmDKQQ', 'CAACAgIAAxkBAAEFitpi9nYPhz8ikDEmXTtw6MU5udkW3AACzwAD9wLID7n4OPunGK79KQQ', 'CAACAgIAAxkBAAEFitxi9nYTEmhChfHPNZPWGBI_WYu_EQAC0QAD9wLID7DVFiL6IbHMKQQ']
green_lizard_birthday = ['CAACAgIAAxkBAAEFitxi9nYTEmhChfHPNZPWGBI_WYu_EQAC0QAD9wLID7DVFiL6IbHMKQQ']
green_lizard_morning = ['CAACAgIAAxkBAAEFitRi9nYDWOTJ2Se8xFNW1UcsMY-CsQACzAAD9wLID0v7TB_rXdKjKQQ', 'CAACAgIAAxkBAAEFitJi9nX_xmi2x9puI-uAT4EIi7SV0QACywAD9wLID6AkdNt7g-RaKQQ']
green_lizard_night = ['CAACAgIAAxkBAAEFisRi9nXfrfAB-77O-0jk17HeOSo0sAACwAAD9wLID1T13GCuDbNaKQQ']
green_lizard_love = ['CAACAgIAAxkBAAEFitpi9nYPhz8ikDEmXTtw6MU5udkW3AACzwAD9wLID7n4OPunGK79KQQ', 'CAACAgIAAxkBAAEFiqxi9nWrPchHSO1R2DzhuH7Jb3hROQACtQAD9wLIDzOvqyodfzZvKQQ']
green_lizard_cool = ['CAACAgIAAxkBAAEFitJi9nX_xmi2x9puI-uAT4EIi7SV0QACywAD9wLID6AkdNt7g-RaKQQ', 'CAACAgIAAxkBAAEFitBi9nX8cKBDZLU9EAdTARc-39Nv3gACygAD9wLIDwQk_4gT6LTDKQQ', 'CAACAgIAAxkBAAEFiq5i9nWu6JkSb7YVC7YxkHcY4JnnZgACugAD9wLID_0MODzqmFe5KQQ']
green_lizard_thx = ['CAACAgIAAxkBAAEFisxi9nXyzb4qDgsjk7g-a3-0XPr3KAACxQAD9wLID7s40cGklXikKQQ']
green_lizard_laugh = ['CAACAgIAAxkBAAEFiqpi9nWoJW4FrRULEUFI5TbzHBNuAgACwgAD9wLID96foOapLgziKQQ', 'CAACAgIAAxkBAAEFi11i9qvvMc9t6CUpZ2CWaLLyOk7gNQACJAMAArVx2gafiis85FHPvSkE', 'CAACAgIAAxkBAAEFi1ti9qvprhdQmFTozuyFFYT6NbYRqQACRRMAAuIsqEsuvmavuVAG_SkE', 'CAACAgIAAxkBAAEFi1Vi9qvT02DkLZ9NcE31S54ZQUp_7QACOhAAAjGBaEvATKmNS4D52SkE']
green_lizard_omg = ['CAACAgIAAxkBAAEFisBi9nXYMY2BivnSlG3fQHa9q6zIhgACvgAD9wLID2NpaQGUlw4kKQQ']
green_lizard_smoke = ['CAACAgIAAxkBAAEFispi9nXtA9W0MKHFsCaH-B2vPBlvfwACxAAD9wLIDwxl0XWs1Rg9KQQ']
# -- ANSWERS WORDS --
morning_answers = ['Утро доброе блять! 😎', 'Доброе утро 😌', 'Утречка...', 'Саламалекум!']
# -- BAD WORDS --
suka_list = ['Сука', 'сука', 'Ты Сука', 'ты Сука', 'ты сука']
suka_answers = ['Я не сука, а кобель - хочешь ротиком проверь хахаха', 'Сам сука', 'Заткнись сученышь :3']
churka_list =['ЧУРКА']
churka_answers =['Сам ты чурка ;(', 'Я вообще-то на Российских серверах живу 🧐', 'Сам чурка, иди на хуй =)', 'От всех чурок тебе большой "САЛАМАЛЕКУМ"!', 'Кумыс буш?']
rfk_list = ['ЕДРИТЬ', 'ЕБАТЬ', 'ЕБААТЬ', 'ЕБАААТЬ', 'ЕБААААТЬ', 'ЕБАААААТЬ', 'ЕБААААААТЬ',  'ЕБАААААААТЬ', 'ЕБААААААААТЬ',  'ЕБААААТь']
rfk_answers = ['КОПАТЬ', 'Шатать', 'Колотить']
fcku_list = ['ИДИ НА ХУЙ','ИДИ НАХУЙ', 'ПОШЁЛ В ЖОПУ', 'ИДИ В ЖОПУ', 'ИДИ В ОЧКО']
fcku_answers = ['Шо, опять?!', 'А дорогу покажешь?😎', 'Ладно...', 'Ладно 😒', 'Ладна 😐', 'Та за что?!😭', 'САМ ПОШЁЛ НА ХУЙ ЕБЛАН!🖕']
mutterhole_list = ['Мать в канаве', 'мать в канаве', 'Твоя мать в канаве', 'твоя мать в канаве', 'У тебя мать в канаве', 'у тебя мать в канаве']
mutterhole_answers = ['У-у-у не повезло, не повезло... ну думаю батя то у тебя остался 😅', 'Ох...как же ты без матери теперь?😢', 'Тогда найду тебя в приюте ☺️']
sry_list = ['ПРОСТИ', 'ВСЁ ПРОСТИ', 'НУ ПРОСТИ', 'ИЗВИНИ', 'ВСЁ ИЗВИНИ', 'НУ ИЗВИНИ']
sry_answers = ['Ладно, бывает...😁', 'Я подумаю...🧐', 'Да ничего, я привык.', 'Да пошёл ты!😡']
# -- MEMES --
bruh = ['bruh', 'bruuh', 'bruuuh', 'bruuuuuh', 'bruuuuuuh', 'bruuuuuuuh', 'bruuuuuuuuh', 'bruuuuuuuuuh', 'bruuuuuuuuuuuuuuuuuuh', 'брух', 'брах', 'брааах']
sheesh_answers_text = ['Аха-ха-ха шииииииш', 'Аха-ха-ха SHEEEEESH', 'ШИИИИИИИИИИИИИИИИИИИИИИИИИШ', 'SHEEEEEEEEEEESH']
sheesh_answers_img = ['https://www.anime-internet.com/content/images/size/w2000/wordpress/2021/02/c2180b854c81945835d05aad85a6d89b.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8Pm7Q9ABiG9DcQvAA2H1YPMOr867bnSNX3g&usqp=CAU']

# -- Sport screems --
csk_screem = [""" <b>ЦСКА - ЧЕМПИОН!!!</b>\n
Атомная бомба нет!
Нейтронная бомба,
Водородная бомба,
Шариковая бомба,
Шарикоподшипниковая бомба,
Пластиковая бомба,
Резиновая бомба,
Каучуковая бомба,
Бомба, которая взорвётся,
Бомба, которая не взорвётся,
Бомба, которая везде продаётся,
Бомба, которую боится народ,
Бомба, которая упадёт в огород,
Бомба, которой играют дети,
Бомба, которой нет на белом свете,
Бомба с дырочкой в правом боку,
Бомба с дырочкой в левом боку,
Мужик в шляпе,
Мужик без шляпы,
Голый мужик,
Женщина, которая поёт,
Женщина, которая даёт,
Женщина, которая р*ком встаёт,
Алла Пугачёва,
Раиса Горбачёва,
Катя Лычёва,
Сраные кошки Куклачёва,
Режим Тори,
Режим Бори,
Режим Миши,
Режим Гриши,
Чеченский абрек,
Дом, который построил Джек,
Обрывки матраса,
Команда Гондураса,
Лысина Филимонова - п*дораса,
Берёзовая роща,
Злая тёща,
Тифозные вши,
Болотные камыши,
Спокойной ночи, малыши,
Жи - ши пиши через «и»,
Побеги бамбука,
Бяка и Бука,
Ворона Каркуша,
Розовый поросёнок Хрюша,
Заяц Степашка,
Бандит Промокашка,
Лохматый Чебурашка,
Молдавский портвейн,
Садам Хусейн,
Проститутка Бронштейн,
Титов - мясной наркоман,
Глюкоза и её доберман,
Монетизация льгот,
Шарикоподшипниковый завод,
Да и просто сами знаете что,
Жанна Фриски,
Её обвисшие сиськи,
Утренние капли из пиписьки,
Девочка Лена,
Х*й по колено,
Мыльная пена,
Телевизионная антенна,
Крокодил Гена,
Рыба мурена,
Повязка аборигена,
Диагноз алигофрена,
Динамо московское,
Динамо хохловское,
Динамо минское,
Динамо грузинское,
Шахтёр,
Пахтакор,
Кайрат,
Арарат,
Нефтчи,
Спартачи,
Верона,
Барселона,
Обладатель кубка УЕФА!
Центральный, Одена Ленина,
Красносинезнаменный,
Всемогущий,
Всех в рот е*ущий,
Спортивный клуб Армии -
Да...
<a href='https://www.youtube.com/watch?v=Z8p9ybtuz5c'>Видео версия</a>""", 'В сердце клуб всегда один – ЦСКА непобедим!']

spartak_screem = ['В мире нет еще пока Команды лучше ЦСКА!', 'В мире нет еще пока Команды лучше Спартака =(', 'Пошёл на хуй, ЦСКА - ЧЕМПЕОН!!!🤩']