from client.cli import add_files, list_files, remove_file, word_count
import os

def test_add_files():
    with open('test_add.txt', 'w') as f:
        f.write("Test file for adding")
    add_files(['test_add.txt'])
    assert os.path.exists('test_add.txt')
    os.remove('test_add.txt')

def test_list_files():
    
    files = list_files()
    assert isinstance(files, list)

def test_remove_file():
    with open('test_remove_cli.txt', 'w') as f:
        f.write("Test file for removal")
    add_files(['test_remove_cli.txt'])
    remove_file('test_remove_cli.txt')
    assert not os.path.exists('test_remove_cli.txt')

def test_word_count():
    with open('test_wc_cli.txt', 'w') as f:
        f.write("This is a word count test")
    add_files(['test_wc_cli.txt'])
    count = word_count()
    assert count > 0
    os.remove('test_wc_cli.txt')
