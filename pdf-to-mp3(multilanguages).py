import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from gtts import gTTS
import os
from googletrans import Translator

def pdf_to_text(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    return text

def translate_to_hindi(text, choose):
    translator = Translator()
    translate = translator.translate(text, dest = choose).text
    return translate

def speak_in_hindi(text):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

def main():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        original_text = pdf_to_text(file_path)
        choose = input("Choose in which language notes you need (Telugu/English/Malayalam/Hindi/Tamil/French/Italian/Chinese/German/Japanese/Arabic/Russian/urdu): ")
        translated_text = translate_to_hindi(original_text, choose)
        print(translated_text)
        speak_in_hindi(translated_text)

if __name__ == "__main__":
    main()
