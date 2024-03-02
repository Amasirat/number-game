import os
import src.core.file_handling as file

DB_DIR = "./tests/database/"
DB_NAME = "question.csv"
def test_create_database() -> None:
    directory = DB_DIR
    file.create_database(directory, DB_NAME)
    assert(os.path.exists(directory))
    
def test_row_count() -> None:
    pass

def test_add_input_to_database() -> None:
    pass  

def test_add_question_to_database() -> None:
    directory = os.path.join(DB_DIR, DB_NAME)
    file.add_question_to_database("age",directory)
    iterator = 0
    while iterator < 10:
        file.add_question_to_database("age",directory)
        iterator += 1
    