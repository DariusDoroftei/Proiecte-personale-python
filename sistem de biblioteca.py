class Book:
    def __init__(self, title, author, year):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.year = year
    borrowed_by=None

    def afisare(self):
        print(f"{book.title} scrisa de {book.author} in anul {book.year}")
class Members:
     borrow_max=2
     def __init__(self, nume, email):
        self.nume=nume.strip().title()
        self.email=email.strip().title()
carti=[]
membri=[]
while(True):
    decision_number=int(input("""=== Task list ===
1. Adauga o carte in Biblioteca
2. Adauga un membru
3. Vizualizeaza lista de carti si cele care sunt imprumutate
4. Sterge o carte din biblioteca
5. Sterge un membru din biblioteca
6.Imprumuta o carte unui membru
7.Exit
"""))
    if(decision_number<1 or decision_number>5):
        print("Introdu o valoare intre 1 si 5")
        continue
    if(decision_number==1):
         titlu=input("Alege titlul cartii: ")
         author=input("Alege autorul cartii: ")
         year=int(input("Alege anul in care a fost scrisa cartea:"))
         if year <1450 or year>2100:
             print("Ai introdus un an nepermis")
             continue
         else:
             pass
         carte=Book(titlu,author,year)
         carti.append(carte)
    if(decision_number==2):
            nume=input("Alege numele si prenumele membrului nou: ")
            email=input("Alege adresa de email: ")
            x=0
            for litera in email:
                if(litera=="@"):
                    x=1
            if(x==1):
                pass
            else:
                print("Nu ai introdus o adresa de email corecta")
                continue
            membru=Members(nume,email)
            membri.append(membru)
    if(decision_number==3):
        for book in carti:
            book.afisare()
            if(book.borrow_by==None):
                pass
            else:
                print(f"Imprumutata de {book.borrow_by})
    if(decision_number==7):
        print("Ai inchis programul.")
        break

    print(Members)
    print(Book)