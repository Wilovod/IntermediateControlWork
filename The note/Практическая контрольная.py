import json
import datetime

filename = 'notes.json'

def load_notes():
    try:
        with open(filename, 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(filename, 'w') as f:
        json.dump(notes, f)

def get_notes(query=None):
    notes = load_notes()
    if query:
        notes = [note for note in notes if note['date'] == query]
    if not notes:
        print("Заметки отсутствуют!")
    return notes


def view_note(note_id):
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        return note
    else:
        return None

def add_note():
    notes = load_notes()
    note_title = input("Введите заголовок заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    note_id = len(notes) + 1
    notes.append({'id': note_id, 'title': note_title, 'text': note_text, 'date': note_date})
    save_notes(notes)

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите номер заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note_title = input("Введите новый заголовок заметки: ")
        note_text = input("Введите новый текст заметки: ")
        note_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        note['title'] = note_title
        note['text'] = note_text
        note['date'] = note_date
        save_notes(notes)
    else:
        print("\nЗаметка не найдена!")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите номер заметки для удаления: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("\nЗаметка удалена!")
    else:
        print("\nЗаметка не найдена!")

print("\nПриветствую Вас в моей системе заметок.")

while True:
    print("\nВыберите действие:")
    print("1 - просмотреть список заметок")
    print("2 - просмотреть заметку")
    print("3 - добавить заметку")
    print("4 - редактировать заметку")
    print("5 - удалить заметку")
    print("0 - выход")

    choice = input("\nВаш выбор: ")

    if choice == '1':
        query = input("Введите дату для выборки (dd-mm-yyyy) или нажмите Enter для вывода всех заметок: " '\n')
        notes = get_notes(query)
        for note in notes:
            print(note['id'], note['title'], note['date'])


    elif choice == '2':
        note_id = int(input("Введите номер заметки для просмотра: "))
        note = view_note(note_id)
        if note:
            print()
            print(note['title'], note['date'])
            print(note['text'])
        else:
            print("\nЗаметка не найдена!")

    elif choice == '3':
        add_note()

    elif choice == '4':
        edit_note()

    elif choice == '5':
        delete_note()

    elif choice == '0':
        print("\n!")
        break