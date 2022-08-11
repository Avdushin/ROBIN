from email import message
from email.policy import default
from time import sleep
from turtle import delay
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv

import logging, random, time, asyncio, os
import msgs
# bot keybords
import markups

# Find .env file
load_dotenv(find_dotenv())

# init
bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)

""" HEANDLERS """
# /start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                            sticker=r"CAACAgIAAxkBAAEFg5li8qnCAwn8afnP9H1xPgVgxgEmZgACuAAD9wLID0YLnLTiTgs4KQQ")
    await bot.send_message(message.from_user.id, 'Приветствую тебя, {0.first_name}!'.format(message.from_user),
    reply_markup = markups.main_menu, parse_mode='html')

# /info
@dp.message_handler(commands=['info'])
async def command_start(message: types.Message):
    me = await bot.get_me()
    await bot.send_message(message.from_user.id, f"Я <b><a href='https://t.me/{me.username}'>{me.first_name}</a></b>.\nМой автор - <a href='https://github.com/avdushin'>Ananazz</a>!".format(bot.get_me()), parse_mode="html")

@dp.message_handler()
async def bot_message(message: types.Message):
    """ GAMES """
    # 🎲 DICE
    for s in msgs.dice_cmd:
        if message.text.lower().find(s.lower()) != -1:
            # await bot.send_dice(message.chat.id, emoji="🎲")
            msg=await message.reply_dice(emoji='🎲')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            sleep(3), await  bot.send_message(message.chat.id, alert)
            break
    # 🎰 CASINO
    for s in msgs.casino_cmd:
        if message.text.lower().find(s.lower()) != -1:
            # await bot.send_dice(message.chat.id, emoji="🎰")
            msg=await message.reply_dice(emoji='🎰')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            sleep(3), await  bot.send_message(message.chat.id, alert)
            break
        """ SPORT GAMES """
    # 🎯 DART
    for s in msgs.dart_cmd:
        if message.text.lower().find(s.lower()) != -1:
            # await bot.send_dice(message.chat.id, emoji="🎯")
            msg=await message.reply_dice(emoji='🎯')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            sleep(3), await  bot.send_message(message.chat.id, alert)
            break
    # ⚽ FOOTBALL
    for s in msgs.football_cmd:
        if message.text.lower().find(s.lower()) != -1:
            # await bot.send_dice(message.chat.id, emoji="⚽")
            msg=await message.reply_dice(emoji='⚽')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            match msg.dice.value:
                case 3 | 4 | 5:
                    sleep(3), await  bot.send_message(message.chat.id, 'ГОЛ!!!')
                case _:
                    sleep(3), await  bot.send_message(message.chat.id, 'МИМО =(')
            sleep(3), await  bot.send_message(message.chat.id, alert)
            break
    # 🏀 BASKETBALL
    for s in msgs.basketball_cmd:
        if message.text.lower().find(s.lower()) != -1:
            msg=await message.reply_dice(emoji='🏀')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            if msg.dice.value == 4 | 5:
                sleep(4), await  bot.send_message(message.chat.id, 'ПОПАЛ!')
            else:
                sleep(4), await  bot.send_message(message.chat.id, 'МИМО!')
            await  bot.send_message(message.chat.id, alert)
            # await bot.send_dice(message.chat.id, emoji="🏀")
            break
    # ---🎳 BOWLING ---
    for s in msgs.bowling_cmd:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_dice(message.chat.id, emoji="🎳")
            break
    # ---GUESS THE NUMBER ---
    # if message.text == "GUESS THE NUMBER":
    #     r = random.randint(1, 100)
    #     await bot.send_message(message.chat.id, f'Я загадал число от 1 до 100. Теперь попробуйте отгадать его. Никаких подсказок!')
    #     if message.text == r:
    #         await message.reply(f'Поздравляю, ты угадал!\nЯ загадал число: {r}!')
    #     else:
    #         await message.reply('Не угадал!')

        """ MEMES """
    for s in msgs.bruh:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_photo(message.from_user.id, photo='https://c.tenor.com/lTtsDp9dZ34AAAAC/biruh-bruh.gif')
            break
        """"Кричалки"""
    # ЦСКА
    for s in msgs.csk_cmd:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_dice(await bot.send_message(message.from_user.id, random.choice(msgs.csk_screem).format(message.from_user),
        parse_mode='html'))
            break
    # Spartak
    for s in msgs.spartak_cmd:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_dice(await bot.send_message(message.from_user.id, random.choice(msgs.spartak_screem).format(message.from_user),
        parse_mode='html'))
            break
    
    """ RANDOM """
    for s in msgs.smiles_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.smiles_answers)}'.format(message.from_user))
            break
    
    """ BAD WORDS """
    # suka check
    for s in msgs.suka_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.suka_answers)()}'.format(message.from_user))
            break
    # churk check
    for s in msgs.churka_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.churka_answers)}'.format(message.from_user))
            break
    # mutter at hole check
    for s in msgs.mutterhole_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.mutterhole_answers)}'.format(message.from_user))
            break
    # fk check
    for s in msgs.fcku_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.fcku_answers)}'.format(message.from_user))
            break
    # rfk check
    for s in msgs.rfk_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.rfk_answers)}'.format(message.from_user))
            break
    # --- SORRY ---
    for s in msgs.sry_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.sry_answers)}'.format(message.from_user))
            break

    match message.text:
        # --- General --- #
        case "◀️ НАЗАД":
            await bot.send_message(message.from_user.id, '☑️ Главное меню'.format(message.from_user),
        reply_markup = markups.main_menu, parse_mode='html')
        # --- INFO --- #
        case "ℹ️ INFO":
            me = await bot.get_me()
            await bot.send_message(message.from_user.id, f"Я <b><a href='https://t.me/{me.username}'>{me.first_name}</a></b>.\nМой автор - <a href='https://github.com/avdushin'>Ananazz</a>!".format(bot.get_me()), parse_mode="html")
        case "info":
            me = await bot.get_me()
            await bot.send_message(message.from_user.id, f"Я <b>{me.first_name}</b>.\nМой автор - <a href='https://github.com/avdushin'>Ananazz</a>!".format(bot.get_me()), parse_mode="html")
        # --- GAMES --- 🎲🎰🎯🏀⚽🎳 # 
        case "🕹️ GAMES":
             await bot.send_message(message.from_user.id, '🕹️ Давай играть!!!'.format(message.from_user),
        reply_markup = markups.games_menu, parse_mode='html')
        case "◀️ GAMES":
             await bot.send_message(message.from_user.id, '🕹️ ИГРЫ'.format(message.from_user),
        reply_markup = markups.games_menu, parse_mode='html')
        # --- 🏅 SPORT GAMES ---
        case "🏅 SPORT GAMES":
             await bot.send_message(message.from_user.id, '🏅 SPORT GAMES'.format(message.from_user),
        reply_markup = markups.sport_menu, parse_mode='html')
        # --- 🎰 LUCK ---
        case "🎰 LUCK":
             await bot.send_message(message.from_user.id, '🎰 LUCK'.format(message.from_user),
        reply_markup = markups.casino_menu, parse_mode='html')
        
        # --- Оскорбления ---
        # case "Чурка" | "чурка" | "чуркаа" | "Ты чурка" | "ты чурка" :
        #      await bot.send_message(message.from_user.id, 'Сам ты чурка :('.format(message.from_user),
        # parse_mode='html')
        # case "Сука" | "сука" | "Ты Сука" | "ты Сука" | "ты сука":
        #      await bot.send_message(message.from_user.id, 'Я не сука, а кобель - хочешь ротиком проверь хахаха'.format(message.from_user),
        # parse_mode='html')
        # case "Ебать" | "ебать" | "Ептать" | "ептать" | "Ёптать" | "ёптать":
        # case words:
        #     await bot.send_message(message.from_user.id, 'Хух'.format(message.from_user))
        #      await bot.send_message(message.from_user.id, f'{random.choice(msgs.eps)}'.format(message.from_user),
        # parse_mode='html')
        # case "Иди на хуй" | "иди на хуй" | "Иди на хуй!" | "иди на хуй!" | "Пошел на хуй" | "пошел на хуй" | "Пошел на хуй!" | "пошел на хуй!":
        #     await bot.send_message(message.from_user.id, 'САМ ПОШЁЛ НА ХУЙ ЕБЛАН!'.format(message.from_user),
        # parse_mode='html')
        # case "Иди в жопу" | "иди в жопу":
        #     await bot.send_message(message.from_user.id, 'Шо, опять?!'.format(message.from_user),
        # parse_mode='html')
        case "Пошёл в жопу" | "пошёл в жопу" | "Иди в очко" | "иди в очко":
            await bot.send_message(message.from_user.id, 'А дорогу покажешь?))'.format(message.from_user),
        parse_mode='html')
        # case "Мать в канаве" | "мать в канаве" | "Твоя мать в канаве" | "твоя мать в канаве" | "У тебя мать в канаве" | "у тебя мать в канаве":
        #     await bot.send_message(message.from_user.id, 'У-у-у не повезло, не повезло... ну думаю батя то у тебя остался 😅'.format(message.from_user),
        # parse_mode='html')
        # --- SORRY ---
        # case "прости" | "всё прости" | "ну прости" | "извини" | "всё извини" | "ну извини":
        #     await bot.send_message(message.from_user.id, 'Ладно, бывет...'.format(message.from_user),
        # parse_mode='html')
        # --- Happy ---
        case 'ахаха' | 'аха' | 'ахахаха' | 'хех' | 'азаза':
            await bot.send_photo(message.from_user.id, photo='https://www.anime-internet.com/content/images/size/w2000/wordpress/2021/02/c2180b854c81945835d05aad85a6d89b.jpg')
            await bot.send_message(message.from_user.id, 'Аха-ха-ха шииииииш'.format(message.from_user),
        parse_mode='html')
        case "хех":
            await bot.send_message(message.from_user.id, 'АХАха да, ржомба!'.format(message.from_user),
        parse_mode='html')
        case 'sheesh' | 'sheeesh' | 'sheeeesh' | 'sheeeeesh' | 'shish' | 'shiish' | 'shiiish' | 'шиш' | 'шииш' | 'шиииш' | 'шииииш' | 'шиииииш' | 'шииииииииш':
            await bot.send_photo(message.from_user.id, photo='https://www.anime-internet.com/content/images/size/w2000/wordpress/2021/02/c2180b854c81945835d05aad85a6d89b.jpg')
            await bot.send_message(message.from_user.id, 'Аха-ха-ха шииииииш'.format(message.from_user),
        parse_mode='html')
        # case 'bruh' | 'bruuh' | 'bruuuh' | 'bruuuuuh' | 'bruuuuuuh' | 'bruuuuuuuh' | 'брух' | 'брах' | 'брааах':
        #     return await bot.send_photo(message.from_user.id, photo='https://c.tenor.com/lTtsDp9dZ34AAAAC/biruh-bruh.gif')

    # if  msgs.words in message.text:
    #     bot.send_message(message.from_user.id, f'{is_part_in_list(message.text.lower(), msgs.words)}'.format(message.from_user),
    # parse_mode='html')