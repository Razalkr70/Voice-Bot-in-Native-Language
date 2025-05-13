import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import speech_recognition as sr
from gtts import gTTS
import os
import random
from playsound import playsound
import pygame
import threading

# Load hospital dataset
data = pd.read_csv("hospital_info.csv")
pygame.mixer.init()

# Voice recognition + bot logic
def voice_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        update_status("🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        # Speech-to-text in Malayalam
        text = recognizer.recognize_google(audio, language="ml-IN")
        update_query(f"Query: {text}")
        print("🔊 You said:", text)

        # Get bot response
        response = find_response(text)
        update_response(f"Bot: {response}")
        print("🤖 Bot:", response)

        # Convert response to audio and play it using a new thread
        tts = gTTS(response, lang='ml')
        filename = f"response_{random.randint(1000, 9999)}.mp3"
        tts.save(filename)

        # Use a separate thread to play audio
        threading.Thread(target=play_audio, args=(filename,)).start()

        update_status("✅ Done.")
    except Exception as e:
        error_msg = "❌ പ്രശ്നം ഉണ്ടായി, വീണ്ടും ശ്രമിക്കൂ."
        update_response(error_msg)
        print("❌ Error:", e)
        update_status(error_msg)

# Play the MP3 file
def play_audio(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Polling the status of music
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Check every 10ms if the music is still playing

        os.remove(filename)  # Delete the temporary file after playing
    except Exception as e:
        print(f"Error playing audio: {e}")

# Find a reply from the CSV
def find_response(query):
    for _, row in data.iterrows():
        if row['Doctor Name'].split()[1].lower() in query.lower():
            return f"{row['Doctor Name']} {row['Department']} വിഭാഗത്തിൽ ആണ്. കൗണ്ടർ നമ്പർ {row['Room No']}."
        if row['Department'].lower() in query.lower():
            return f"{row['Doctor Name']} {row['Department']} വിഭാഗത്തിൽ ആണ്. കൗണ്ടർ നമ്പർ {row['Room No']}."
    return "ക്ഷമിക്കണം, വിവരങ്ങൾ കണ്ടെത്താനായില്ല."

# Update functions for GUI
def update_status(text):
    status_var.set(text)

def update_query(text):
    query_var.set(text)  # Update the query label with the user input text

def update_response(text):
    response_var.set(text)

# Function to trigger the voice query from the button
def on_mic_click():
    threading.Thread(target=voice_query).start()  # Start the voice query function in a new thread

# Initialize main window
root = tk.Tk()
root.title("Malayalam Voice Bot")
root.geometry("600x400")

# ✅ Set background image
bg_image = Image.open("background.jpg")  # Use your background image
bg_image = bg_image.resize((600, 400))   # Match the window size
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ✅ Load and resize mic image
mic_image = Image.open("music_16518482.png")  # Use your mic icon
mic_image = mic_image.resize((60, 60))  # Resize to smaller size
mic_photo = ImageTk.PhotoImage(mic_image)

# ✅ Mic Button
mic_button = tk.Button(root, image=mic_photo, command=on_mic_click, borderwidth=0, bg="white")
mic_button.place(x=270, y=300)  # Centered near bottom

# ✅ Label to show the user's query (this is where the user's input will be displayed)
query_var = tk.StringVar()
query_label = tk.Label(root, textvariable=query_var, bg="white", fg="black", font=("Arial", 12))
query_label.place(x=150, y=150)

# ✅ Label to show output text
response_var = tk.StringVar()
response_label = tk.Label(root, textvariable=response_var, bg="white", fg="black", font=("Arial", 12))
response_label.place(x=150, y=200)

# ✅ Label for status updates
status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var, bg="white", fg="black", font=("Arial", 12))
status_label.place(x=150, y=250)


root.mainloop()

