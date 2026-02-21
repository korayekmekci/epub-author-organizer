# 📚 EPUB Author Organizer
## 🎬 Demo

![Demo](assets/demo.gif)

![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A powerful Python tool that automatically organizes your EPUB books into author-based folders.

Designed for developers and digital library enthusiasts who want clean and structured book collections.

---

## 🎯 Why This Project?

Managing large EPUB libraries manually is time-consuming and error-prone.

This project solves that problem by automatically:

- Detecting author metadata
- Creating structured author folders
- Organizing books safely
- Allowing preview mode before changes

It turns chaos into structure.

---

## ✨ Features

- 📖 Reads EPUB metadata (`dc:creator`)
- 👤 Automatically detects author name
- 📂 Creates author-based folders
- 🔁 Recursive folder scanning (subfolders supported)
- 🧪 Dry-run mode (preview changes safely)
- 🛟 Handles missing metadata (`Unknown_Author` fallback)

---

## 🧠 How It Works

- Uses `ebooklib` to read EPUB metadata
- Extracts `dc:creator` field
- Normalizes author names (safe folder format)
- Uses `os.walk()` for recursive scanning
- Moves files using `shutil`

---

## 🚀 Installation

```bash
git clone https://github.com/korayekmekci/epub-author-organizer.git
cd epub-author-organizer

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🛠 Usage

### Organize books

```bash
python main.py /path/to/your/books
```

### Preview changes (Dry Run)

```bash
python main.py /path/to/your/books --dry-run
```

---

## 🖥 Example Output

```
Scanning folder: /Users/username/Desktop/Books

[DRY RUN] Would move:
Book1.epub → George_Orwell/
Book2.epub → Stefan_Zweig/
Book3.epub → Unknown_Author/
```

---

## 📂 Project Structure

```
epub-author-organizer/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🗺 Roadmap

- [x] EPUB metadata extraction
- [x] Recursive folder scanning
- [x] Dry-run mode
- [ ] PDF metadata support
- [ ] Convert into CLI tool
- [ ] Publish to PyPI

---

## 👨‍💻 Author

Developed by Koray Ekmekci  
GitHub: https://github.com/korayekmekci

---

## 📄 License

MIT License