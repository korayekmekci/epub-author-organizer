# 📚 EPUB Author Organizer

A powerful Python tool that automatically organizes your EPUB books into author-based folders.

Perfect for large digital libraries.

---

## ✨ Features

- 📖 Reads EPUB metadata
- 👤 Automatically detects author name
- 📂 Creates author-based folders
- 🔁 Recursive folder scanning (subfolders supported)
- 🧪 Dry-run mode (preview changes safely)
- 🛟 Handles missing metadata (`Unknown_Author` fallback)

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

### Organize books:

```bash
python main.py /path/to/your/books
```

### Preview changes (Dry Run):

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