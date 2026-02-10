import os
import telebot
from telebot import types
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread

# --- إعدادات البوت ---
API_TOKEN = '8414464648:AAEOPa54U1ZgZ8283KWCqFz24u1B8AE6Avw'
bot = telebot.TeleBot(API_TOKEN)

# إعداد المتصفح ليعمل في بيئة السيرفر (الوضع الخفي)
def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# --- لوحة التحكم (الأزرار) ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add('➕ ربط حساب واتساب', '🚨 بدء بلاغات جماعية')
    markup.add('📊 حالة السيرفر')
    return markup

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "✅ تم تشغيل نظام البلاغات السحابي بنجاح.", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == '🚨 بدء بلاغات جماعية')
def report_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("10 بلاغات (بدون حظر)", callback_data="rep_10_none"),
               types.InlineKeyboardButton("10 بلاغات (مع حظر المزعج)", callback_data="rep_10_block"))
    bot.send_message(message.chat.id, "اختر نوع العملية المطلوبة للرقم الهدف:", reply_markup=markup)

# تشغيل البوت بشكل دائم
if __name__ == "__main__":
    bot.polling(none_stop=True)
