import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('7230393087:AAG2U9TdORx93ZkN0IIf3Fxx3tkVgAEIo3g')

id = None
Name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('ORDERS.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), application varchar(50),status varchar(50),userid varchar(50))')

    conn.commit()
    cur.close()
    conn.close()

    conn = sqlite3.connect('ORDERS.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        global Name, id
        print(el[3])

        id = el[4]
        Name = el[1]

        info = f'ID: {id} \n\n  Имя: {Name} \n Вид заказа: {el[2]} '

        print(id)
        print(Name)

        markup = types.InlineKeyboardMarkup()
        write = types.InlineKeyboardButton('Написать', url=f'https://web.telegram.org/k/#@{Name}')
        markup.row(write)
        delte = types.InlineKeyboardButton('Удалить', callback_data=f'{id}')
        markup.row(delte)

        bot.send_message(message.chat.id,info,reply_markup=markup)

    conn = sqlite3.connect('ORDERS.sql')
    cur = conn.cursor()

    cur.execute("SELECT userid FROM users")

    if cur.fetchone() is None:
        bot.send_message(message.chat.id, 'заказов нет')

    cur.close()
    conn.close()


@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    conn = sqlite3.connect('ORDERS.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    for el in users:
        id = el[4]
        if call.data == id:
            print(call.data)
            print(id)
            cur.execute(f"DELETE FROM users WHERE userid = '{call.data}'")
            conn.commit()
            cur.close()
            conn.close()



bot.polling(none_stop=True, interval=0)
