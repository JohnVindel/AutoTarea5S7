#Tarea 5 - Foto y Video
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['foto', 'photo'])
def foto(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('/Users/gurdianux/Downloads/logo ucrish.png', 'rb')
    bot.send_photo(id, photo)
    print("Ubicacion")

@bot.message_handler(commands=['video', 'mp4'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    video = open('/Users/gurdianux/Downloads/video1.mp4', 'rb')
    bot.send_video(id, video)
    print("Ubicacion")

bot.polling()