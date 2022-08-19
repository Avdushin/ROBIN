import pwinput, pyfiglet, platform, os

# Robin_SETUP - application to setup the ROBIN Telegram bot
# AUTHOR: github.com/Avdushin <ITDOBRO@TUTA.IO>
# DATE: 14.08.2022

VERSION = '1.0' # App version
APP_NAME = 'Robin_SETUP' # App name
ENV = '.env' # File to write environment variable
MAIL = 'ITDOBRO@TUTA.IO'

def logo():
    clear()
    setup_text = pyfiglet.figlet_format("Setup_")    
    rob_text = pyfiglet.figlet_format("ROBIN")    
    # print(f'\033[1;33;40m{setup_text}\033[1;31;40m{rob_text}\033[0;37;40m')
    print(f'\033[1;31;40m{rob_text}\033[1;33;40m{setup_text}\033[0;37;40m\n\033[1;33;40mAUTHOR: \033[1;0;37;40mITDOBRO \033[1;31;40mVERSION: \033[1;37;40m{VERSION}\033[0;37;40m')

def clear():
    # What OS is running check
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def setup():

    print(f'\nYou can get a BOT TOKEN from \033[1;37;40m@BotFather - https://t.me/BotFather\033[0;37;40m')
    token = pwinput.pwinput('\nEnter your bot TOKEN: ')

    match token:
        case '' | ' ' | 'exit' | '0' | 'quit' | 'выход' | 'выйти' | 'нет' | 'нету' | 'no' | 'none':
            print(f'\nAUTHOR MAIL: <{MAIL}>\n')
            quit()

    # Write the TOKEN
    with open(ENV, "w") as file:
        file.write(f'BOT_TOKEN={token.strip()}')

    print('\n\033[1;37;40mIf you entered the bot TOKEN correctly, you\'re done!\n\033[0;37;40m')
    print(f'\nAUTHOR MAIL: <{MAIL}>\n')

def main():
    logo()
    setup()

if __name__ == "__main__":
    main()