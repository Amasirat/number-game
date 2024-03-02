import os
import csv
import globals

DB_FIELDNAMES = ["id", "question"]
# outputs full directory to created database
def create_database(file_directory: str, file_name: str) -> str:
    if not os.path.exists(file_directory):
           os.makedirs(file_directory)
    
    full_directory: str = os.path.join(file_directory, file_name)
    with open(full_directory, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DB_FIELDNAMES)
        
        writer.writerow(
            {
                DB_FIELDNAMES[0]:DB_FIELDNAMES[0], 
                DB_FIELDNAMES[1]:DB_FIELDNAMES[1]
            }
        )
    return full_directory
# returns the count of rows in given csv file
def row_count(file_directory: str) -> int:
    if not os.path.isfile(file_directory):
        raise FileNotFoundError
    
    counter: int = 0
    with open(file_directory, "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=DB_FIELDNAMES)
        counter += sum(1 for _ in reader)
        
    return counter
        
def add_input_to_database(input_directory: str, db_directory: str) -> None:
    if not os.path.isfile(input_directory) or not os.path.isfile(db_directory):
        raise FileNotFoundError
    
    questions : list = list()
    
    with open(input_directory) as input_file:
        for row in input_file:
            questions.append(row)

def add_question_to_database(question: str, file_directory: str) -> None:
    if not os.path.isfile(file_directory):
        raise FileNotFoundError
    
    with open(file_directory, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DB_FIELDNAMES)
        writer.writerow(
            {
                DB_FIELDNAMES[0]:row_count(file_directory),
                DB_FIELDNAMES[1]:question
            }
        )