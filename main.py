from pyscript import document

def checkMem(e):

    mem_first = ["Zara", "Ysabel", "Cheree", "Therese"]
    mem_last = ["LLAGUNO", "VALERO", "MENDOZA", "REYES"]
    

    memf= document.getElementById("memf").value
    meml= document.getElementById("meml").value
    name= "Zara"

    confirm_mem = memf in mem_first
    confirm_mem = meml in mem_last

    message = (f'Sorry {name}, this member is not in the club.', f'Congratulations {name}!, this member is in the club.')

    document.getElementById("output1").innerHTML = message[confirm_mem]

