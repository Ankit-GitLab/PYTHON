Dict= {
        "name" : "Ankit sharma",
        "subject" : {
            "phy" : 97,
            "math" : 98,
            "chem" : 92
    }
}
print(list[Dict.keys()])#return all key

print(Dict.values())#return all values

print(Dict.items())#return all(key, val) pair as tuple

print(Dict.get("name"))#return the key according to value

print(Dict.update({"Topic" : "math"}))#insert the specified items to the dictionary

print(Dict)