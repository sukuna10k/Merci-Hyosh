from pyrogram import Client, filters
from pypdf import PdfWriter
import hashlib

async def encode_user_id(user_id):
    hashed_user_id = hashlib.sha256(str(user_id).encode()).hexdigest()
    encoded_id = int(hashed_user_id, 16)
    return encoded_id
    
docs = {}

@Client.on_message(filters.private & filters.document)
async def on_pdf(bot, message):
    usr = message.from_user
    user = await encode_user_id(usr.id)
    
    if message.document.file_name.endswith(".pdf"):
        await message.reply_text("Téléchargement du PDF, veuillez patienter..!!")
        file = await message.download()
        
        if user not in docs:
            docs[user] = []
        
        docs[user].append(file)
        
        await message.reply_text("PDF téléchargé avec succès. Vous pouvez envoyer plus de PDFs ou taper /merge pour les fusionner.")
        
@Client.on_message(filters.command("merge") & filters.private & filters.incoming)
async def merge(bot, message):
    usr = message.from_user
    user = await encode_user_id(usr.id)
    
    if user in docs and len(docs[user]) >= 2:
        merger = PdfWriter()
        
        for doc in docs[user]:
            merger.append(doc)
        
        merged_pdf = f"merged.pdf"
        
        with open(merged_pdf, "wb") as pdf:
            merger.write(pdf)
        
        await message.reply_document(document=merged_pdf)
        docs[user].clear()
    else:
        await message.reply_text("Envoyez au moins deux PDFs d'abord, puis envoyez /merge pour les fusionner.")
