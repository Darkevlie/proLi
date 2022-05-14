from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

# код спонсирован ужасом, спешкой и непониманием

ost1 = 0
ost2 = 0
ost3 = 0


def echo(update, context):
    update.message.reply_text("Отправьте команду /start, чтобы получить список доступных команд")


def main():
    updater = Updater('5357846814:AAGq4Uzy3fQ0n-oSQn0fMaA1J7yPdoZFGpQ', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("budget", budget))
    dp.add_handler(CommandHandler("1", first))
    dp.add_handler(CommandHandler("2", second))
    dp.add_handler(CommandHandler("3", third))
    dp.add_handler(CommandHandler("back", start))
    dp.add_handler(CommandHandler("clear1", clear1))
    dp.add_handler(CommandHandler("clear2", clear2))
    dp.add_handler(CommandHandler("clear3", clear3))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('refill1', refill1)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, refill12)]},
        fallbacks=[CommandHandler('budget', budget)])
    dp.add_handler(conv_handler)

    conv_handler2 = ConversationHandler(
        entry_points=[CommandHandler('withdrawal1', withdrawal1)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, withdrawal12)]},
        fallbacks=[CommandHandler('budget', budget)])
    dp.add_handler(conv_handler2)

    conv_handler3 = ConversationHandler(
        entry_points=[CommandHandler('refill2', refill2)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, refill22)]},
        fallbacks=[CommandHandler('budget', budget)])
    dp.add_handler(conv_handler3)

    conv_handler4 = ConversationHandler(
        entry_points=[CommandHandler('withdrawal2', withdrawal2)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, withdrawal22)]},
        fallbacks=[CommandHandler('budget', budget)])
    dp.add_handler(conv_handler4)

    conv_handler5 = ConversationHandler(
        entry_points=[CommandHandler('refill3', refill3)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, refill32)]},
        fallbacks=[CommandHandler('budget', budget)])
    dp.add_handler(conv_handler5)

    conv_handler6 = ConversationHandler(
        entry_points=[CommandHandler('withdrawal3', withdrawal3)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, withdrawal32)]},
        fallbacks=[CommandHandler('budget', budget)])
    dp.add_handler(conv_handler6)

    text_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


def start(update, context):
    reply_keyboard = [['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Я могу помочь вам с контролем вашего бюджета. Выберите /budget, чтобы перейти к работе",
        reply_markup=markup
    )


def budget(update, context):
    reply_keyboard = [['/1'], ['/2'], ['/3'], ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Выберите счёт:", reply_markup=markup)
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    return ConversationHandler.END
    # я вообще 0 понятия, зачем мне столько одинаковых строчек, но поверьте мне, оно ТОЛЬКО ТАК РАБОТАЕТ
    # но на всякий случай не перепроверяйте, а то вдруг работает и без них


def first(update, context):
    reply_keyboard = [['/refill1'], ['/withdrawal1'], ['/clear1'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    global ost1
    d = ost1
    update.message.reply_text(
        f"Первый счёт \nОстаток:{d} \n \nВыберите действие: \n/refill1 - пополнение \n/withdrawal1 - снятие "
        f"\n/clear1 - очистить данные счёта \n/budget - назад",
        reply_markup=markup)


def second(update, context):
    reply_keyboard = [['/refill2'], ['/withdrawal2'], ['/clear2'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    global ost2
    d = ost2
    update.message.reply_text(
        f"Второй счёт \nОстаток:{d} \n \nВыберите действие: \n/refill2 - пополнение \n/withdrawal2 - снятие "
        f"\n/clear2 - очистить данные счёта \n/budget - назад",
        reply_markup=markup)


def third(update, context):
    reply_keyboard = [['/refill3'], ['/withdrawal3'], ['/clear3'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    global ost3
    d = ost3
    update.message.reply_text(
        f"Третий счёт \nОстаток:{d} \n \nВыберите действие: \n/refill3 - пополнение \n/withdrawal3 - снятие "
        f"\n/clear3 - очистить данные счёта \n/budget - назад",
        reply_markup=markup)


def refill1(update, context):
    update.message.reply_text('Введите сумму пополнения в рублях', reply_markup=ReplyKeyboardRemove())
    return 1


def refill12(update, context):
    a = update.message.text
    reply_keyboard = [['/1'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if a.isnumeric():
        a = int(a)
        update.message.reply_text(f'Счёт успешно пополнен на {a} руб', reply_markup=markup)
        global ost1
        ost1 += a
    else:
        update.message.reply_text(f'Ошибка формата. Повторите попытку', reply_markup=markup)

    return ConversationHandler.END


def withdrawal1(update, context):
    update.message.reply_text('Введите сумму снятия в рублях', reply_markup=ReplyKeyboardRemove())
    return 1


def withdrawal12(update, context):
    a = update.message.text
    reply_keyboard = [['/1'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if a.isnumeric():
        a = int(a)
        update.message.reply_text(f'Сумма в размере {a} успешно снята', reply_markup=markup)
        global ost1
        ost1 -= a
    else:
        update.message.reply_text(f'Ошибка формата. Повторите попытку', reply_markup=markup)

    return ConversationHandler.END


def clear1(update, context):
    reply_keyboard = [['/1']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('Информация о счёте успешно удалена', reply_markup=markup)
    global ost1
    ost1 = 0


def refill2(update, context):
    update.message.reply_text('Введите сумму пополнения в рублях', reply_markup=ReplyKeyboardRemove())
    return 1


def refill22(update, context):
    a = update.message.text
    reply_keyboard = [['/2'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if a.isnumeric():
        a = int(a)
        update.message.reply_text(f'Счёт успешно пополнен на {a} руб', reply_markup=markup)
        global ost2
        ost2 += a
    else:
        update.message.reply_text(f'Ошибка формата. Повторите попытку', reply_markup=markup)

    return ConversationHandler.END


def withdrawal2(update, context):
    update.message.reply_text('Введите сумму снятия в рублях', reply_markup=ReplyKeyboardRemove())
    return 1


def withdrawal22(update, context):
    a = update.message.text
    reply_keyboard = [['/2'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if a.isnumeric():
        a = int(a)
        update.message.reply_text(f'Сумма в размере {a} успешно снята', reply_markup=markup)
        global ost2
        ost2 -= a
    else:
        update.message.reply_text(f'Ошибка формата. Повторите попытку', reply_markup=markup)

    return ConversationHandler.END


def clear2(update, context):
    reply_keyboard = [['/2']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('Информация о счёте успешно удалена', reply_markup=markup)
    global ost2
    ost2 = 0


def refill3(update, context):
    update.message.reply_text('Введите сумму пополнения в рублях', reply_markup=ReplyKeyboardRemove())
    return 1


def refill32(update, context):
    a = update.message.text
    reply_keyboard = [['/3'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if a.isnumeric():
        a = int(a)
        update.message.reply_text(f'Счёт успешно пополнен на {a} руб', reply_markup=markup)
        global ost3
        ost3 += a
    else:
        update.message.reply_text(f'Ошибка формата. Повторите попытку', reply_markup=markup)

    return ConversationHandler.END


def withdrawal3(update, context):
    update.message.reply_text('Введите сумму снятия в рублях', reply_markup=ReplyKeyboardRemove())
    return 1


def withdrawal32(update, context):
    a = update.message.text
    reply_keyboard = [['/3'], ['/budget']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    if a.isnumeric():
        a = int(a)
        update.message.reply_text(f'Сумма в размере {a} успешно снята', reply_markup=markup)
        global ost3
        ost3 -= a
    else:
        update.message.reply_text(f'Ошибка формата. Повторите попытку', reply_markup=markup)

    return ConversationHandler.END


def clear3(update, context):
    reply_keyboard = [['/3']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text('Информация о счёте успешно удалена', reply_markup=markup)
    global ost3
    ost3 = 0


if __name__ == '__main__':
    main()

