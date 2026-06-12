name = input("What's your name ?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    
    case "Draco" | "Utkarsh":
        print("slytherin")
    
    case _:
        print("who are you?")                  



