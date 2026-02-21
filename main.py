import os
import shutil
import argparse
from ebooklib import epub


def get_author_epub(epub_path):
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


def organize_books(folder_path, dry_run=False):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".epub"):
                full_path = os.path.join(root, file)
                author = get_author_epub(full_path)

                author_folder = os.path.join(folder_path, author)
                destination = os.path.join(author_folder, file)

                if dry_run:
                    print(f"[DRY RUN] {file} → {author}")
                else:
                    os.makedirs(author_folder, exist_ok=True)
                    shutil.move(full_path, destination)
                    print(f"Taşındı: {file} → {author}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organize EPUB books into author-based folders."
    )
    parser.add_argument("folder", help="Path to the folder containing EPUB files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving files",
    )

    args = parser.parse_args()

    organize_books(args.folder, args.dry_run)