import os
import shutil
from ebooklib import epub

BOOKS_FOLDER = "/Users/kuzum/Documents/E-Kitaplar"  # BURAYI değiştir

def get_author(epub_path):
    try:
        book = epub.read_epub(epub_path)
        authors = book.get_metadata('DC', 'creator')
        if authors:
            return authors[0][0]
        else:
            return "Unknown_Author"
    except Exception as e:
        print(f"Hata: {epub_path} okunamadı -> {e}")
        return "Unknown_Author"

def organize_books():
    for file in os.listdir(BOOKS_FOLDER):
        if file.endswith(".epub"):
            full_path = os.path.join(BOOKS_FOLDER, file)
            author = get_author(full_path)

            author_folder = os.path.join(BOOKS_FOLDER, author)
            os.makedirs(author_folder, exist_ok=True)

            shutil.move(full_path, os.path.join(author_folder, file))
            print(f"Taşındı: {file} → {author}")

if __name__ == "__main__":
    organize_books()