from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8730845046:AAHK0RpwnkIPAV9Mu7GutKMZ7wp8N60fufk"

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users:
        users[user_id] = {
            "referrals": 0
        }

    referral_link = f"https://t.me/bostic_marbot?start={user_id}"

    text = f"""
Welcome!

Invite 4 friends to unlock private videos.

Your referrals: {users[user_id]['referrals']}/4

Your invite link:
{referral_link}
"""

    if users[user_id]["referrals"] >= 4:
        text += "\nUnlocked!\nPrivate Channel:\nhttps://t.me/+NkmPmz3E6mQ1MWY1"

    await update.message.reply_text(text)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Running...")

app.run_polling()