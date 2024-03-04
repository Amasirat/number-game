import os
import src.core.file_handling as file
# use these defaults to validate function effects
DB_DIR = "./tests/database/"
DB_NAME = "question.csv"
FULL_DB_DIR = os.path.join(DB_DIR, DB_NAME)

def test_create_database() -> None:
    directory = DB_DIR
    file.create_database(directory, DB_NAME)
    assert(os.path.exists(directory))
    
def test_row_count() -> None:
    pass

def test_add_input_to_database() -> None:
    input_dir = "/home/amasirat/projects/number-game/tests/input.txt"
    file.add_input_to_database(input_dir, FULL_DB_DIR)  

def test_add_question_to_database() -> None:
    file.add_question_to_database("age",FULL_DB_DIR)
    iterator = 0
    while iterator < 10:
        file.add_question_to_database("age",FULL_DB_DIR)
        iterator += 1
    