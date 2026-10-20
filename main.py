from pyscript import display, document

Grade_7 = {'Zoey Ledres', 'Therese Reyes'}
Grade_8 = {'Elise Ramos', 'Cheree Mendoza'}
Grade_9 = {'Princess Schwab','Jericho Magsalin'}
Grade_10 ={'Tyler Sales', 'Savanna Bautista'}
master_set = (Grade_7 | Grade_8 | Grade_9 | Grade_10 | )


def new(e): 
    first_name = document.getElementById("fname").value #grabs the input for first name
    last_name = document.getElementById("lname").value #grabs the input for last name

    full_name = first_name + " " + last_name #combines both first and last name

    messages = f"{full_name} is now added to the club. "

    document.getElementById("output")
    display(f"{messages} + {master_set}")