#! /usr/bin/python3
# notes.py

"""
This program was created by to make in a most quick way a correction of tests of math
"""

import sys, shelve

#Constants

CLRS = {
        "b": "\033[m",
        "g": "\033[32m",
        "r": "\033[31m"
        }

ANSW = {
        "q4": "c",
        "q5": "c",
        "q6": "a",
        "q7": "c",
        "q8": "b",
        "q9": "a",
        "q10": "e"
        }

alunos = shelve.open('data')

# -------------------------------------- MAIN CLASS DEFINITION -------------------------------------------
#
# Here its defined the principal class reposable to storage all informatios about the pupil
#
# --------------------------------------------------------------------------------------------------------

class Aluno:
    def __init__(self, name, notes, answers=[]):
        self.notes = notes
        self.name = name
        self.answers = answers

    def set_args(self, args):
        self.answers = []
        self.answers.append("notes.py")
        for c in range(3, 10):
            #print(f"adding note {args[c]}") #debug
            self.answers.append(args[c])

    def show_answ(self):
        for key, answ in enumerate(self.answers):
            if key == 0: continue

            state = self.notes[key - 1]
            #print(f"state: {state}") #degub 

            print("Answer: ", end='')
            if state == f"{CLRS['g']} Correct {CLRS['b']}":
                print(f"{CLRS['g']} {answ} {CLRS['b']}")
            else:
                print(f"{CLRS['r']} {answ} {CLRS['b']}")

    def show_details(self):
        index = 4
        for c in self.notes:
            print(f'Question {index}: {c}')
            index += 1

    def contability(self, notes):
        cont = dict()
        wrong = 0
        correct = 0
        for c in notes:
            if c == f"{CLRS['g']} Correct {CLRS['b']}":
                correct += 1
            else:
                wrong += 1
        cont["corrects"] = correct
        cont["wrongs"] = wrong
        return cont

    def __str__(self):
        aux = self.contability(self.notes)
        return "\nName:           ---> " + self.name + "\nCorrect answers ---> " + CLRS['g'] + str(aux["corrects"]) + CLRS['b'] + "\nWrong answers:  ---> " + CLRS['r'] + str(aux["wrongs"]) + CLRS['b'] + "\n"

    def set_name(self, name):
        self.name = name

    def set_notes(self, notes):
        self.notes = notes

def print_alunos(alunos, args):
    if not alunos.items():
        print("===Empty===")
        exit()

    print("\n===PUPIL INFORMTATION===\n")
    for aluno in alunos.values():
        print(aluno)
        if len(args) > 2:
            if args[2] == "detail":
                aluno.show_details()
            if args[2] == "answ":
                aluno.show_answ()



def print_keys(key):
    print(f"No client {key} on system")
    print("The pupils avaliable are:\n")
    for c in alunos.keys():
        print(c)

def clear_trash():
    index = 1
    for k in alunos.keys():
        if index == 14:
            print(f"Pupil {k} deleted")
            del(alunos[k])
        index += 1

# --------------------------------------- INPUT CONCERN --------------------------------------------------
#
# In this concern the only responsibilty is capture the input of the user and send it for the next concern
#
# --------------------------------------------------------------------------------------------------------

args = sys.argv

if len(args) >= 2 and args[1] == "ls":
    print_alunos(alunos, args);
    exit()

if len(args) >= 3:
    if args[1] == "del":
        try:
            #clear_trash()
            del(alunos[args[2]])
            print("Deleted")
        except KeyError:
            print_keys(args[2])
        exit()

    if args[1] == "name":
        try:
            aux = alunos[args[2]]
            aux.set_name(args[3])
            del(alunos[args[2]])
            alunos[args[3]] = aux
            print(f"Name of {args[2]} changed to {args[3]}")
        except KeyError:
            print_keys(args[2])
        exit()

if args[1] == "arg":
    try:
        aux = alunos[args[2]]
        aux.set_args(args)
        alunos[args[2]] = aux

        print("Notes updateds")
    except KeyError:
        print_keys(args[2])
    exit()

elif len(args) != 8:
    print("Invalid qtde of args!")
    exit()

# ----------------------------- CALC NOT CONCERN ----------------------------------------------------------
#
# That layers will calculate the question wrong and questions correct
#
# ---------------------------------------------------------------------------------------------------------

notes = []

def calc_notes(args):
    for n, c in enumerate(args):
        if(n == 0): continue

        index = n + 3
        if ANSW[f'q{index}'] == c:
            notes.append(f"{CLRS['g']} Correct {CLRS['b']}")
        else:
            notes.append(f"{CLRS['r']} Wrong {CLRS['b']}")

        #print(f'Note {c} copied')

# --------------------------------- OPERATION CONCERN -------------------------------------------------------
#
# This concern is responsable to do the principal tasks on the system as deletion or adding new pupils
#
# -----------------------------------------------------------------------------------------------------------

def addAluno(alunos, aluno):
    opt = str(input("\nAdd pupil on the system? [y/n]? ")).strip().lower()
    if opt != 'y': exit()
    name = input('Type the name of the pupil: ')
    aluno.set_name(name)
    alunos[name] = aluno

    print(aluno)
    alunos.close()

if __name__ == '__main__':
    calc_notes()
    aluno = Aluno("None", notes, args)
    aluno.show_details()
    addAluno(alunos, aluno)
