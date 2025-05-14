# 🏥 Malayalam Voice Bot for Hospital Information

This project is a simple voice assistant built using Python and Tkinter that helps users find hospital-related information using voice queries in **Malayalam**. It uses **Google Speech Recognition** for voice input and **gTTS** for Malayalam speech synthesis.

---

## 🧠 Features

- 🎙️ Voice recognition in Malayalam
- 🧑‍⚕️ Responds with doctor and department info
- 📂 Reads hospital data from a CSV file
- 🎧 Malayalam speech output using gTTS and playsound
- 🖼️ GUI interface built with Tkinter
- 📈 Threading used for non-blocking voice and playback operations
- 🌄 Custom background and microphone icons

---

## 🛠️ Technologies Used

- Python
- Tkinter (GUI)
- `speech_recognition`
- `gTTS` (Google Text-to-Speech)
- `pygame` (audio playback)
- `PIL` (for image handling)
- `pandas` (for reading the hospital dataset)

---

## 🗂️ Files and Folders
```
project/
│
├── hospital_info.csv # Hospital dataset
├── background.jpg # Background image
├── music_16518482.png # Mic icon image
├── voice_bot.py # Main Python script
├── README.md # Documentation

```
## 📋 CSV Format (hospital_info.csv)

Make sure your CSV has the following columns:

```csv
Doctor Name,Department,Room No
Dr. Anil Kumar,Cardiology,101
Dr. Meera Varma,Dermatology,102
```
...
### 🚀 How to Run

- **Install dependencies:**

  ```bash
  pip install pandas speechrecognition gTTS pygame pillow
  ```

- **Make sure microphone access is enabled.**

- **Run the script:**

  ```bash
  python bot.py
  ```

  - Speak in **Malayalam** to ask for:
    - A doctor's name (e.g., "ഡോക്ടർ മീര")
    - A department (e.g., "ഡർമറ്റോളജി")

---

### 🌐 Example Query

> **"ഡോക്ടർ അനിൽ കുമാർ എവിടെയാണ്?"**

---

### 🧠 Bot will reply

> **"ഡോക്ടർ അനിൽ കുമാർ, കാർഡിയോളജി വിഭാഗത്തിൽ ആണ്. കൗണ്ടർ നമ്പർ 101."**

### 💡 Future Improvements
- Add more hospital locations and branches

- Integrate text-based queries via keyboard

- Add chatbot logging feature

- Support English + Malayalam hybrid queries
