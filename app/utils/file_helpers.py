# app/utils/file_helpers.py
import os
import json

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def append_file(path, content):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        pass  # Just creates an empty file