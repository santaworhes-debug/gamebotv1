from telegram import Update
from telegram.ext import ContextTypes
from database import Database

db = Database()

async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = await db.get_player(user.id)
    if not player:
        await update.message.reply_text("Персонаж не создан. Используйте /start")
        return

    profile_text = (
        f"📊 **ПРОФИЛЬ ИГРОКА** 📊\n\n"
        f"🆔 ID: `{user.id}`\n"
        f"👤 Имя: {user.username}\n"
        f"📈 Уровень: {player['level']}/{100}\n"
        f"⭐ Опыт: {player['xp']}/{int(100 * (player['level'] ** 1.5))}\n"
        f"❤️ HP: {player['hp']}/{player['max_hp']}\n"
        f"⚔️ Атака: {player['attack']}\n"
        f"🛡️ Защита: {player['defense']}\n"
        f"💰 Золото: {player['gold']}"
    )
    await update.message.reply_text(profile_text, parse_mode="Markdown")
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = await db.get_player(user.id)
    if not player:
        await db.create_player(user.id, user.username)
        await update.message.reply_text(
            "🎮 Добро пожаловать в игру!\n\n"
            "Твой персонаж создан:\n"
            "❤️ HP: 100 | ⚔️ Атака: 10 | 🛡️ Защита: 5 | 💰 Золото: 100\n\n"
            "Команды:\n"
            "/profile — профиль\n"
            "/battle — начать бой"
        )
    else:
        await update.message.reply_text("Ты уже в игре! Используй /profile или /battle")
