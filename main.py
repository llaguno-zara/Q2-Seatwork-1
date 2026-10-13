from pyscript import document

def checkMem(e):

    mem_first = ["Zara", "Ysabel", "Cheree", "Therese"]
    mem_last = ["LLAGUNO", "VALERO", "MENDOZA", "REYES"]


    memf= document.getElementById("memf").value
    meml= document.getElementById("meml").value
    name= "Zara"

    first = memf.lower() in [name.lower() for name in mem_first]
    last = meml.lower() in [name.lower() for name in mem_last]

    confirm_mem = first and last

    message = (f'Sorry {name}, this member is not in the club.', f'Congratulations, {name}! this member is in the club.')

    document.getElementById("output1").innerHTML = message[int(confirm_mem)]

