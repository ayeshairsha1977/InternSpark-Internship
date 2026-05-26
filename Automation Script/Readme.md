# 📂 File Organizer Automation Script

A Python automation project that automatically organizes messy files into separate folders based on their file types.  
This project helps keep folders clean and structured by sorting files like images, documents, music, and videos automatically.

---

## 🚀 Features

- Automatically organizes files into folders
- Creates folders if they do not exist
- Supports multiple file types
- Uses logging to track file movements
- Simple menu-driven interface
- Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python
- `os` module
- `shutil` module
- `logging` module

---

## 📁 Supported File Types

| Folder Name | Supported Extensions   |
|-------------|------------------------|
| Images      | `.jpg`, `.jpeg`, `.png`|
| Documents   | `.pdf`, `.docx`, `.txt`|
| Music       | `.mp3`                 |
| Movies      | `.mp4`, `.mkv`         |

---

## 📌 How It Works

### Before Organizing

```text
Downloads/
│
├── photo.jpg
├── song.mp3
├── movie.mp4
├── notes.pdf
├── project.docx
```

### After Organizing

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Music/
│   └── song.mp3
│
├── Movies/
│   └── movie.mp4
│
└── Documents/
    ├── notes.pdf
    └── project.docx
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ayeshairsha1977/InternSpark-Task.git
```

### 2. Open the Project Folder

```bash
cd InternSpark-Task
```

### 3. Run the Python Script

```bash
python file_organizer.py
```

---

## 📜 Example Output

```text
Enter the folder name: downloads

Moving photo.jpg → Images
Moving song.mp3 → Music
Moving movie.mp4 → Movies
Moving notes.pdf → Documents

Files organized successfully!
```

---

## 🧠 Concepts Used

- File handling
- Directory management
- Python dictionaries
- Logging
- Automation scripting

---

## 📈 Future Improvements

- GUI version using Tkinter
- Drag and drop support
- Duplicate file detection
- Custom folder categories

---

## 👩‍💻 Author

### Mohammed Ayesha Firdouse  
🎓 AI & ML Student  
💻 Python Automation Enthusiast  
🚀 Interested in Technology, Problem Solving, and Building Real-World Projects

## ⭐ Project Goal

This project was built to practice Python automation and improve problem-solving skills using real-world file management tasks.