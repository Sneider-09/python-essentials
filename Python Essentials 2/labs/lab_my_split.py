def mysplit(str):
    new_list = []
    aux = ""
    if str == "":
        return new_list

    for ch in str:
        if ch != " ":
            aux += ch
        else:
            if aux != "":
                new_list.append(aux)
                aux = ""
            
    if aux != "":
        new_list.append(aux)
        
    return new_list
    


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))