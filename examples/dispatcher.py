from email.policy import default
from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv
from handlers import *

import logging, random, time, asyncio, os
# bot keybords

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
    await bot.send_message(message.from_user.id, f"Я <b><a href='https://t.me/{me.username}'>{me.first_name}</a></b>.\nМой автор - <a href='https://github.com/avdushin'>ITDOBRO</a>!".format(bot.get_me()), parse_mode="html")

@dp.message_handler()
async def bot_message(message: types.Message):
    """ GAMES """
    # 🎲 DICE
    for s in msgs.dice_cmd:
        if message.text.lower().find(s.lower()) != -1:
            # await bot.send_dice(message.chat.id, emoji="🎲")
            msg=await message.reply_dice(emoji='🎲')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            # sleep(3), await  bot.send_message(message.chat.id, alert)
            break
    # 🎰 CASINO
    for s in msgs.casino_cmd:
        if message.text.lower().find(s.lower()) != -1:
            msg=await message.reply_dice(emoji='🎰')
            match msg.dice.value:
                case 1 | 22 | 43 | 64:
                    sleep(3), await bot.send_sticker(message.from_user.id, f'{random.choice(msgs.green_lizard_cool)}')
                    await  bot.send_message(message.chat.id, 'Хорош!')
                case _:
                    pass
            break
        
        """ SPORT GAMES """
    # 🎯 DART
    for s in msgs.dart_cmd:
        if message.text.lower().find(s.lower()) != -1:
            msg=await message.reply_dice(emoji='🎯')
            match msg.dice.value:
                case 1:
                    sleep(3), await  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFisZi9nXjPwEHZiGaUWxAL1S4Qy5GZgACwQAD9wLID2JmDHNJYyc5KQQ')
                    await  bot.send_message(message.chat.id, 'Мимо!')
                case 2 | 3 | 4 | 5:
                    alert = f'ОЧКИ: <b>{msg.dice.value}</b>'
                    sleep(3), await bot.send_message(message.chat.id, alert)
                case 6:
                    sleep(3), await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFiqhi9nMrmJ3FXRtFhanmQEDHtqcZOwACywAD9wLID6AkdNt7g-RaKQQ')
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
            break
    # 🏀 BASKETBALL
    loop = asyncio.get_event_loop()
    delay = 3
    for s in msgs.basketball_cmd:
        if message.text.lower().find(s.lower()) != -1:
            msg=await message.reply_dice(emoji='🏀')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            match msg.dice.value:
                case 4 | 5 | 6:
                    time.sleep(3), await  bot.send_message(message.chat.id, 'ПОПАЛ!')
                case 1 | 2:
                    time.sleep(3), await  bot.send_message(message.chat.id, 'МИМО!')
            break
    # ---🎳 BOWLING ---
    for s in msgs.bowling_cmd:
        if message.text.lower().find(s.lower()) != -1:
            msg=await message.reply_dice(emoji='🎳')
            alert = f'Ты выбил: <b>{msg.dice.value}</b>'
            if msg.dice.value == 6:
                time.sleep(3), await  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFiqhi9nMrmJ3FXRtFhanmQEDHtqcZOwACywAD9wLID6AkdNt7g-RaKQQ')
                await  bot.send_message(message.chat.id, 'STRIKE!!!💯')
            else:
                time.sleep(3), await  bot.send_message(message.chat.id, 'Теперь я:')
                bp = await bot.send_dice(message.chat.id, emoji="🎳")
                if bp.dice.value ==6:
                    time.sleep(3), await  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFiqhi9nMrmJ3FXRtFhanmQEDHtqcZOwACywAD9wLID6AkdNt7g-RaKQQ')
                    await  bot.send_message(message.chat.id, 'STRIKE!!!💯')
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
    # -- BRUUH --
    for s in msgs.bruh:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_photo(message.from_user.id, photo='https://c.tenor.com/lTtsDp9dZ34AAAAC/biruh-bruh.gif')
            break
    # --- SHEESH ---
    for s in msgs.sheesh_cmd:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_photo(message.from_user.id, photo=f'{random.choice(msgs.sheesh_answers_img)}')
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.sheesh_answers_text)}')
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
    # -- SMILES BATTLES --
    for s in msgs.smiles_list:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.smiles_answers)}'.format(message.from_user))
            break
    # -- LIZARD STIKERS BATTLE --
    # for s in msgs.green_lizard_stikers:
    #     # if message.text.send_stiker.find(s.lower()) != -1:
    #     if bot.get_file.find(s.lower()) != -1:
    #         await bot.send_sticker(message.from_user.id, f'{random.choice(msgs.green_lizard_stikers)}'.format(message.from_user))
    #         break
    
    # --- Morning ---
    for s in msgs.morning_trigger:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_sticker(message.from_user.id, f'{random.choice(msgs.green_lizard_morning)}'.format(message.from_user))
            await bot.send_message(message.from_user.id, f'{random.choice(msgs.morning_answers)}') 
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
    # --- LAUGH ---
    for s in msgs.laugh_trigger:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_sticker(message.from_user.id, f'{random.choice(msgs.green_lizard_laugh)}')
            break

    match message.text:
        # --- General --- #
        case "◀️ НАЗАД":
            await bot.send_message(message.from_user.id, '☑️ Главное меню'.format(message.from_user),
        reply_markup = markups.main_menu, parse_mode='html')
        # --- INFO --- #
        case "ℹ️ INFO":
            me = await bot.get_me()
            await bot.send_message(message.from_user.id, f"Я <b><a href='https://t.me/{me.username}'>{me.first_name}</a></b>.\nМой автор - <a href='https://github.com/avdushin'>ITDOBRO</a>!".format(bot.get_me()), parse_mode="html")
        case "info":
            me = await bot.get_me()
            await bot.send_message(message.from_user.id, f"Я <b>{me.first_name}</b>.\nМой автор - <a href='https://github.com/avdushin'>ITDOBRO</a>!".format(bot.get_me()), parse_mode="html")
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