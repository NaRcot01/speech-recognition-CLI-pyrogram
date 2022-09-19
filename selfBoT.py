from pyrogram import Client,filters
import speech
import configparser

config=configparser.ConfigParser()
config.read("config.ini")
api_id = config.get("default",'api_id')
api_hash=config.get("default",'api_hash')

bot=Client("speech-self", api_id, api_hash)
@bot.on_message(filters.command('v2t',prefixes=['']))
def main(client,message):

    client.download_media(message.reply_to_message.voice.file_id,file_name='audio_file.ogg')
    speach_res=speech.speachR("audio_file.ogg")
    client.send_message(chat_id=message.chat.id,text=speach_res,reply_to_message_id=message.reply_to_message.id)   
    message.delete()
    
            

bot.run()
