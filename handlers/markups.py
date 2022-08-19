from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# back button
back_btn = KeyboardButton('◀️ НАЗАД')
back_games_btn = KeyboardButton('◀️ GAMES')

# --- Main menu ---
games_btn = KeyboardButton('🕹️ GAMES')
info_btn = KeyboardButton('ℹ️ INFO')
main_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(games_btn, info_btn)

""" 🎲🎰🎯⚽🏀🎳 """
# --- SPORT MENU ---
sport_btn = KeyboardButton('🏅 SPORT GAMES')
dart_btn = KeyboardButton('🎯 DART')
football_btn = KeyboardButton('⚽ FOOTBALL')
basketball_btn = KeyboardButton('🏀 BASKETBALL')
bowling_btn = KeyboardButton('🎳 BOWLING')
sport_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(dart_btn, basketball_btn, football_btn,
 bowling_btn, back_games_btn)

# --- CASINO MENU ---
dice_btn = KeyboardButton('🎲 DICE')
casino_btn = KeyboardButton('🎰 CASINO')
luck_btn = KeyboardButton('🎰 LUCK')
casino_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(dice_btn, casino_btn, back_games_btn)

# --- GEANES menu ---
games_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(sport_btn, luck_btn, back_btn)