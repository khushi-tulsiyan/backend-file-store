import argparse
import requests
import os

BASE_URL = "http://127.0.0.1:5000"  

def add_files(files):
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"Error: {file_path} does not exist.")
            continue
        with open(file_path, 'rb') as f:
            response = requests.post(f"{BASE_URL}/add", files={'file': f})
            print(response.json())

def list_files():
    response = requests.get(f"{BASE_URL}/list")
    print(response.json())

def remove_file(filename):
    response = requests.delete(f"{BASE_URL}/remove/{filename}")
    print(response.json())

def update_file(filename, file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return
    with open(file_path, 'rb') as f:
        response = requests.put(f"{BASE_URL}/update/{filename}", files={'file': f})
        print(response.json())

def word_count():
    response = requests.get(f"{BASE_URL}/wordcount")
    print(response.json())

def freq_words(order, limit):
    response = requests.get(f"{BASE_URL}/freq-words", params={'order': order, 'limit': limit})
    print(response.json())

def main():
    parser = argparse.ArgumentParser(description="File Store Client")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add files to the store")
    add_parser.add_argument("files", nargs='+', help="Files to upload")

    list_parser = subparsers.add_parser("list", help="List files in the store")

    remove_parser = subparsers.add_parser("remove", help="Remove a file from the store")
    remove_parser.add_argument("filename", help="Name of the file to remove")

    update_parser = subparsers.add_parser("update", help="Update a file in the store")
    update_parser.add_argument("filename", help="Name of the file to update")
    update_parser.add_argument("file_path", help="Local path to the file")

    wc_parser = subparsers.add_parser("wordcount", help="Get word count of all files")

    freq_parser = subparsers.add_parser("freq-words", help="Get most/least frequent words")
    freq_parser.add_argument("--order", choices=["asc", "dsc"], default="dsc", help="Order of frequency (default: dsc)")
    freq_parser.add_argument("--limit", type=int, default=10, help="Number of frequent words to display (default: 10)")

    args = parser.parse_args()

    if args.command == "add":
        add_files(args.files)
    elif args.command == "list":
        list_files()
    elif args.command == "remove":
        remove_file(args.filename)
    elif args.command == "update":
        update_file(args.filename, args.file_path)
    elif args.command == "wordcount":
        word_count()
    elif args.command == "freq-words":
        freq_words(args.order, args.limit)

if __name__ == "__main__":
    main()