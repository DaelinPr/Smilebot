from telebot import TeleBot

# Создаем объект бота
BOT_TOKEN = '7763882149:AAGfbhCDHyt0hCyBn6t0egen5T6W4hNDfjE'
bot = TeleBot(BOT_TOKEN)

# Справочник по смайликам
emoji_dict = {
    '😊': 'Улыбка - выражение радости и дружелюбия.',
    '😂': 'Смеющийся со слезами - выражение сильного смеха или шутки.',
    '❤️': 'Сердце - выражение любви и привязанности.',
    '😢': 'Слезы - выражение грусти или печали.',
    '😎': 'Круто - выражение уверенности или стиля.',
    '🤔': 'Думающий - выражение размышлений или сомнений.',
    '😉': 'Подмигивание - выражение дружелюбного заигрывания или согласия.',
    '😞': 'Грустный - выражение печали или разочарования.',
    '🤝': 'Рукопожатие - выражение приветствия или соглашения.',
    '🍀': 'Пожелание удачи - выражение пожелания удачи и успехов.',
    '🎉': 'Праздник - выражение празднования и радости.',
    '🙏': 'Сложенные руки - выражение благодарности или просьбы.',
    '👍': 'Большой палец вверх - выражение одобрения или согласия.',
    '👎': 'Большой палец вниз - выражение неодобрения или несогласия.',
    '😡': 'Злой - выражение гнева или раздражения.',
    '🤗': 'Объятие - выражение дружелюбия и поддержки.',
    '🤩': 'Восхищение - выражение восхищения или восторга.',
    '🥺': 'Печальные глаза - выражение просьбы или сожаления.',
    '😴': 'Спящий - выражение усталости или желания спать.',
    '🤯': 'Взорвавшийся мозг - выражение удивления или шока.',
    '😇': 'Ангел - выражение невинности или добродушия.',
    '😈': 'Чертенок - выражение игривости или озорства.',
    '🤓': 'Умник - выражение умности или сосредоточенности.',
    '🤐': 'Молчун - выражение необходимости молчания или секрета.',
    '🤢': 'Тошнота - выражение чувства отвращения или недомогания.',
    '🤮': 'Рвота - выражение сильного отвращения или недомогания.',
    '🤧': 'Чихание - выражение простуды или аллергии.',
    '🤬': 'Ругательство - выражение сильного гнева или раздражения.',
    '🥳': 'Праздник - выражение радости и веселья.',
    '😵': 'Головокружение - выражение сильной усталости или шока.',
    '😕': 'Смущение - выражение неуверенности или смущения.',
    '😟': 'Обеспокоенность - выражение беспокойства или тревоги.',
    '🙁': 'Грусть - выражение печали или разочарования.',
    '😬': 'Неловкость - выражение неловкости или смущения.',
    '🙄': 'Закатить глаза - выражение раздражения или разочарования.',
    '😮': 'Удивление - выражение сильного удивления.',
    '😯': 'Удивление - выражение легкого удивления.',
    '😲': 'Шок - выражение сильного удивления или шока.',
    '😳': 'Смущение - выражение сильного смущения или стыда.',
    '🤥': 'Лжец - выражение лжи или обмана.',
    '😋': 'Лакомство - выражение удовольствия от вкусной еды.',
    '😛': 'Шутка - выражение игривости или веселья.',
    '😜': 'Подмигивание - выражение игривости или заигрывания.',
    '🤪': 'Безумие - выражение игривого или сумасшедшего настроения.',
    '😝': 'Смеющийся с высунутым языком - выражение игривого веселья.',
    '🤨': 'Подозрение - выражение недоверия или сомнения.',
    '🧐': 'Исследование - выражение сосредоточенного внимания или любопытства.',
    '😐': 'Нейтральное лицо - выражение безразличия или спокойствия.',
    '😑': 'Безмолвие - выражение молчания или спокойствия.',
    '😶': 'Безречие - выражение отсутствия слов или молчания.',
    '😏': 'Самодовольство - выражение легкого самодовольства или сарказма.',
    '😒': 'Недовольство - выражение легкого недовольства или раздражения.',
    '🙃': 'Перевернутое лицо - выражение игривого настроения или сарказма.',
    '😔': 'Печаль - выражение грусти или сожаления.',
    '😪': 'Сонливость - выражение усталости или желания спать.',
    '🤤': 'Слюни - выражение желания или увлеченности.',
    '😷': 'Маска - выражение болезни или необходимости защиты.',
    '🤒': 'Температура - выражение болезни или недомогания.',
    '👻': 'Призрак - выражение озорства или игривости.',
    '👽': 'Инопланетянин - выражение чего-то необычного или странного.',
    '👾': 'Инопланетный монстр - выражение игривости или ретро-игр.',
    '🤖': 'Робот - выражение технологии или чего-то автоматического.',
    '😺': 'Улыбающаяся кошка - выражение радости или дружелюбия.',
    '🙀': 'Испуганная кошка - выражение страха или удивления.',
    '😽': 'Целующая кошка - выражение любви или привязанности.',
    '😿': 'Плачущая кошка - выражение грусти или печали.',
    '💀': 'Череп - выражение чего-то страшного или смертельного.',
    '👀': 'Глаза - выражение внимания или слежки.',
    '👅': 'Язык - выражение игривости или дразнящего поведения.',
    '👄': 'Губы - выражение поцелуя или чего-то романтичного.',
    '💋': 'Отпечаток губ - выражение поцелуя или любви.',
    '👓': 'Очки - выражение умственного труда или моды.',
    '🕶️': 'Солнцезащитные очки - выражение стиля или защиты от солнца.',
    '🎓': 'Выпускная шапка - выражение учебы или окончания учебного заведения.',
    '👑': 'Корона - выражение власти или величия.',
    '💼': 'Портфель - выражение работы или бизнеса.',
    '🎒': 'Рюкзак - выражение учебы или путешествий.',
    '🧳': 'Чемодан - выражение путешествий или поездок.',
    '📱': 'Смартфон - выражение связи или технологий.',
    '💻': 'Ноутбук - выражение работы или учебы с использованием компьютера.',
    '📷': 'Камера - выражение фотографии или съемки.',
    '🎥': 'Видеокамера - выражение видеосъемки или кино.',
    '📺': 'Телевизор - выражение просмотра телевидения или видео.',
    '📻': 'Радио - выражение прослушивания радиопередач или музыки.',
    '🎙️': 'Микрофон - выражение записи звука или выступления.',
    '🎚️': 'Ползунок - выражение настройки звука или параметров.',
    '🎛️': 'Микшер - выражение настройки звуковых эффектов или музыки.',
    '🎧': 'Наушники - выражение прослушивания музыки или аудио.',
    '📀': 'DVD - выражение хранения данных или видео.',
    '💿': 'CD - выражение хранения музыки или данных.',
    '📼': 'Видеокассета - выражение видеосъемки или ретро-формата.',
    '🕹️': 'Джойстик - выражение видеоигр или управления.',
    '🎮': 'Игровой контроллер - выражение видеоигр или гейминга.',
    '🖥️': 'Компьютер - выражение работы или учебы с использованием компьютера.',
    '🖨️': 'Принтер - выражение печати документов или изображений.',
    '⌨️': 'Клавиатура - выражение работы с текстом или данными.',
    '🖱️': 'Мышь - выражение управления компьютером или навигации.',
    '🖲️': 'Трекбол - выражение управления компьютером или специального оборудования.',
    '💡': 'Лампочка - выражение идей или освещения.',
    '🔦': 'Фонарик - выражение света или поиска.',
    '🕯️': 'Свеча - выражение света или романтической атмосферы.',
    '🗑️': 'Мусорное ведро - выражение удаления или уборки.',
    '🛢️': 'Бочка - выражение хранения жидкости или топлива.',
    '💸': 'Летающие деньги - выражение траты или получения денег.',
    '💵': 'Купюра долларов - выражение денег или богатства.',
    '💶': 'Купюра евро - выражение денег или богатства.',
    '💷': 'Купюра фунтов - выражение денег или богатства.',
    '💴': 'Купюра иен - выражение денег или богатства.',
    '💰': 'Мешок с деньгами - выражение богатства или прибыли.',
    '💳': 'Кредитная карта - выражение финансов или покупок.',
    '💎': 'Драгоценный камень - выражение богатства или роскоши.',
    '⚖️': 'Весы - выражение справедливости или баланса.',
    '🔧': 'Гаечный ключ - выражение ремонта или настройки.',
    '🔨': 'Молоток - выражение строительства или разрушения.',
    '🪓': 'Топор - выражение рубки дерева или работы.',
    '⛏️': 'Кирка - выражение копки или работы.',
    '🔩': 'Болт - выражение крепежа или механики.',
    '⚙️': 'Шестеренка - выражение механики или работы.',
    '🗜️': 'Тиски - выражение зажима или работы.',
    '⚗️': 'Алхимическая реторта - выражение науки или химии.',
    '🔬': 'Микроскоп - выражение науки или исследований.',
    '🔭': 'Телескоп - выражение астрономии или наблюдения.',
    '📡': 'Спутниковая антенна - выражение связи или технологии.',
    '💉': 'Шприц - выражение медицины или вакцинации.',
    '💊': 'Таблетка - выражение медицины или лечения.',
    '🚪': 'Дверь - выражение входа или выхода.',
    '🛏️': 'Кровать - выражение сна или отдыха.',
    '🛋️': 'Диван и лампа - выражение отдыха или домашнего уюта.',
    '🚽': 'Унитаз - выражение санитарии или уборной.',
    '🚿': 'Душ - выражение гигиены или очищения.',
    '🛁': 'Ванна - выражение отдыха или очищения.',
    '🔥': 'огонь - выражение знак одобрения,если только что-то на самом деле не горит',
    '🫂': 'обнимающиеся люди - выражение утешительное или грустное',
    '💔': 'разбитое сердце - печаль, разочарование или недовольство результатом чего-либо',
    '🙏🏻': 'сложенные руки - выражение спасибо или пожалуйста',
    '🙈': 'обезьяна - выражение не вижу зла',
    '🤭': 'лицо с рукой - подавление смеха, молчание или даже сохранение секрета',
    '😅': 'застенчивый -  выражение  нервный смех сквозь  слезы',
    '🤡': 'клоун - выражение никак иначе',
    '🥹': 'улыбка со слезами - выражение еле сдерживает слезы',
    '🫶🏻': 'руки в виде серцда - выражение способ выражения любви',
    '🥶': 'замерзшее лицо - выражение холодное лицо',
    '🩻': 'потрясенный - выражение вы шокированы, поражены или трепетны',
    '🖕🏻': 'средний палец - выражение оставить в покое',
    '🫡': 'приветствующее лицо - выражение приветствие перед солдатами',
    '🌹': 'роза - выражение прилив любви',
    '🫨': 'трясщующееся лицо - выражение дрожь или волнение',
    '😀': 'передает общее удовольствие и хорошее настроение или юмор',
    '😃': 'передает общее счастье и добродушное веселье',
    '😄': 'передает общее счастье и добродушное веселье',
    '😁': 'выражает сияющее, удовлетворенное счастье',
    '😆': 'передает волнение или искренний смех'
}


def log_user_id(user_id):
    try:
        with open("user_ids.txt", "a+") as file:
            file.seek(0)
            users = file.read().splitlines()
            if str(user_id) not in users:
                file.write(f"{user_id}\n")
    except Exception as e:
        print(f"Произошла ошибка при записи ID: {str(e)}")


# Обработчик команды /start и /help
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    log_user_id(message.from_user.id)
    bot.reply_to(message, f"Привет, {message.from_user.first_name}. Я справочник по эмодзи. "
                          f"Напиши мне любой эмодзи, и если я его знаю, я расскажу, что он обозначает!")


# Обработчик на любое текстовое сообщение
@bot.message_handler(func=lambda message: True)
def respond_to_text(message):
    log_user_id(message.from_user.id)
    if message.text.lower() == 'привет':
        bot.reply_to(message,
                     f"Привет, {message.from_user.first_name}! Напиши мне любой эмодзи и узнаешь, "
                     f"что он обозначает.")
    else:
        handle_emoji(message)


# Функция для обработки эмодзи
def handle_emoji(message):
    try:
        smileys = message.text.strip()
        if not smileys:
            bot.reply_to(message, "Сообщение не должно быть пустым. Пожалуйста, отправьте эмодзи.")
            return
        response = ""
        for smiley in smileys:
            smiley_info = emoji_dict.get(smiley)
            if smiley_info:
                response += f"{smiley}: {smiley_info}\n"
            else:
                response += f"{smiley}: К сожалению, я не знаю этот эмодзи.\n"
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")


# Запуск бота
if __name__ == "__main__":
    bot.infinity_polling()
