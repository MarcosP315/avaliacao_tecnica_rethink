# Python 3.10
pessoas = [
    {"name":"Fabiana Araújo", "age":33},
    {"name":"Gabriel Gomes", "age":25},
    {"name":"Fernando Henrique", "age":17},
    {"name":"Ana Luiza", "age":2},
    {"name":"Geralda do Nascimento", "age":93},
    {"name":"Miguel Souza", "age":70},
    {"name":"Antonio Miguel", "age":69}
]

def get_person_by_name(name:str) -> list:
    return [x for x in pessoas if x["name"] == name]

def get_people_names() -> list:
    return [x["name"] for x in pessoas]

def get_people_first_names() -> list:
    return [x["name"].split(" ")[0] for x in pessoas]

def get_people_with_id():
    aux_list = []
    for x,y in enumerate(pessoas, 1):
        y["id"] = x
        aux_list.append(y)
    
    return aux_list

def get_overages():
    return [x for x in pessoas if x["age"] >= 18]

def get_ages_average():
    return sum([x["age"] for x in pessoas])/len(pessoas)
