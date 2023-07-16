def individual_serial(info) ->dict:
    return{
        "firstName": str(info["firstName"]),
        "lastName": str(info["lastName"]),
        "cin": str(info["cin"]),
      
    }

def list_serial(infos) -> list:
    return[individual_serial(info) for info in infos]
    
# individual_serial, prend un dictionnaire (info) en entrée et retourne un autre dictionnaire qui contient les mêmes clés que le dictionnaire d'entrée, 
# list_serial, prend une liste de dictionnaires (infos) en entrée et retourne une liste de dictionnaires en appliquant la fonction individual_serial à chaque élément de la liste d'entrée.