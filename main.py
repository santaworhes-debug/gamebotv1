#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers.battle_handlers import battle_handler, attack, defend, flee
from handlers.profile_handlers import start_handler, profile_handler
from database import Database

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class GameBot:
    def __init__(self):
        self.db = Database()
        self.app = ApplicationBuilder().token("8981547481:AAGkcLgc8bJ9DnPby56CtMsHiP-y0UMg86Y").build()
        self._register_handlers()

    def _register_handlers(self):
        self.app.add_handler(CommandHandler("start", start_handler))
        self.app.add_handler(CommandHandler("profile", profile_handler))
        self.app.add_handler(CommandHandler("battle", battle_handler))
        self.app.add_handler(CallbackQueryHandler(attack, pattern="attack"))
        self.app.add_handler(CallbackQueryHandler(defend, pattern="defend"))
        self.app.add_handler(CallbackQueryHandler(flee, pattern="flee"))

    def run(self):
        logger.info("GameBot запущен")
        self.app.run_polling()

if __name__ == "__main__":
    bot = GameBot()
    bot.run()
