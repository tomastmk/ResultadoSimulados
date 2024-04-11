import csv

from modules.sendmail import *
from modules.converter import *
from modules.progress import *

def main():

    # Spliting test results
    split_pdf("files\\relatorio.pdf")

    # List with names, emails and ids
    path: str = "files\\lista.csv"
    
    # Email user and password
    login: tuple = "user@gmail.com","password"

    # Test type and date    
    info: tuple = 'UNESP',"23/05/2999"
    
    # Reading student list
    students: list = []
    with open(path,"r",encoding="utf-8") as file:
        file = csv.reader(file)
        for student in file:
            students.append(student)
    
    total: int = len(students)    # progress
    erro: bool = False
    
    for index, student in enumerate(students[1:]):
        
        print_progress(index, total)    # progress
        
        arq = f'files\\save\\id{student[0]}.pdf'    # path to student result through its id
        
        # Sending email and checking for error
        if send_email(login,student,arq,info):
            erro = True
        
    print_progress(total,total) # Completion
    
    if erro is True:
        print(bcolors.WARNING+bcolors.BOLD+"\n Erro no envio de um ou mais certificados. Um documento chamado \"erro.txt\" com mais detalhes foi gerado."+bcolors.ENDC)


if __name__=="__main__":
    main()