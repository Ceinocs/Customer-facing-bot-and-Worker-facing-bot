import sqlite3
import telebot
from telebot import types
import random

bot = telebot.TeleBot('7114153737:AAHpiisMQkKy8v5H-XBPZHUmGRefky2_6Bg')

pat = None
pre = None
txt = None
name = None
task = None
status = None
userid = 0
username = None

# Главные кнопки
markup = types.InlineKeyboardMarkup()
presentation_and_text = types.InlineKeyboardButton('👩‍💻Презенетация и текст📑', callback_data='pat')
markup.row(presentation_and_text)
presentation = types.InlineKeyboardButton('👩‍💻Презенетация👩‍💻', callback_data='prepresentation')
text = types.InlineKeyboardButton('📑Текст к презентации📑', callback_data='text')
markup.row(presentation, text)
stat = types.InlineKeyboardButton('⚙️Статус заказа⚙️', callback_data='stat')
markup.row(stat)

# кнопки для Презенетация и текст
Pat = types.InlineKeyboardMarkup()
application = types.InlineKeyboardButton('✔️Отправить заявку✔️', callback_data='application')
back = types.InlineKeyboardButton('Назад', callback_data='back')
Pat.add(application, back)
Bacend = types.InlineKeyboardMarkup()
Bacend.add(back)


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('ORDERS.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), application varchar(50),status varchar(50),userid varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,f"Привет, {message.from_user.username}🖐️ \n\n Я бот от компании WWS \n\n 🔥Вы можите заказать 3 вида услуга🔥",reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    global pat, lolo, pre, txt, task, name, status, userid, username

    task = ""
    name = call.from_user.username


    if call.data == 'pat':
        pat = 1
        print(1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Хорошо👍 \n\n Стоимость за 5 слайдов и текст к ним \n (это слайды без предстовления и спасибо за внимание) \n 300 рублей",
                              reply_markup=Pat)
    if call.data == 'prepresentation':
        pre = 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Замечателно👍 \n\n Стоимость за 5 слайдов \n (это слайды без предстовления и спасибо за внимание) \n 150 рублей",
                              reply_markup=Pat)
    if call.data == 'text':
        txt = 1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Отлично👍 \n\n Стоимость за текст к 5 слайдам \n (это слайды без предстовления и спасибо за внимание) \n 150 рублей",
                              reply_markup=Pat)
    if call.data == 'back':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"Привет, {name}🖐️ \n\n Я бот от компании WWS \n\n 🔥Вы можите заказать 3 вида услуга🔥",
                              reply_markup=markup)
    if call.data == 'application':
        userid=random.randint(1,50)
        print(pat)

        if pat == 1:

            conn = sqlite3.connect('ORDERS.sql')
            cur = conn.cursor()

            cur.execute("SELECT name FROM users")


            if cur.fetchone() is None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="💥Все отлично💥",
                                      reply_markup=Bacend)
                status = "Ожидает"
                task = "Презентация и тектс"

                conn = sqlite3.connect('ORDERS.sql')
                cur = conn.cursor()

                cur.execute("INSERT INTO users (name,application,status,userid) VALUES ('%s','%s','%s','%s')" % (name, task, status, userid))

            else:bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                       text="Вы уже сделали заказ😼 \n\n Если хотите закозать чтото еще вернитесь в мень👇 \n\n 💥Если хотите узнать статус заказ (нажмите на кнопку стату заказа в главном мень)💥",
                                       reply_markup=Bacend)

            conn.commit()
            cur.close()
            conn.close()

        if pre == 1:

            conn = sqlite3.connect('ORDERS.sql')
            cur = conn.cursor()

            cur.execute("SELECT name FROM users")

            if cur.fetchone() is None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="💥Все отлично💥",
                                      reply_markup=Bacend)
                status = "Ожидает"
                task = "Презентация"

                conn = sqlite3.connect('ORDERS.sql')
                cur = conn.cursor()

                cur.execute("INSERT INTO users (name,application,status,userid) VALUES ('%s','%s','%s','%s')" % (
                name, task, status, userid))

            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="Вы уже сделали заказ😼\n\n Если хотите закозать чтото еще вернитесь в мень👇 \n\n 💥Если хотите узнать статус заказ (нажмите на кнопку стату заказа в главном мень)💥",
                                      reply_markup=Bacend)

            conn.commit()
            cur.close()
            conn.close()


        if txt == 1:

            conn = sqlite3.connect('ORDERS.sql')
            cur = conn.cursor()

            cur.execute("SELECT name FROM users")

            if cur.fetchone() is None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="Все отлично😁",
                                      reply_markup=Bacend)
                status = "Ожидает"
                task = "Текст к презентации"

                conn = sqlite3.connect('ORDERS.sql')
                cur = conn.cursor()

                cur.execute("INSERT INTO users (name,application,status,userid) VALUES ('%s','%s','%s','%s')" % (
                name, task, status, userid))

            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text="Вы уже сделали заказ.\n\n Если хотите закозать чтото еще вернитесь в мень.\n\nЕсли хотите узнать статус заказ нажмите на кнопку стату заказа в главном мень",
                                      reply_markup=Bacend)

            conn.commit()
            cur.close()
            conn.close()

    if call.data == "stat":
        conn = sqlite3.connect('ORDERS.sql')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users')
        users = cur.fetchall()

        info = ''
        for el in users:
            if el[1] == name:
                username = el[1]
                info = f'ID заказа: {el[4]} \n\n Вид заказа: {el[2]} \n'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=info, reply_markup=Bacend)

            elif username != name:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='На даный момент у вас нет активных зазаов🥺',reply_markup=Bacend)

        cur.close()
        conn.close()


bot.polling(none_stop=True, interval=0)
