d = {"name" : "Dylan",
     "age" : "24",
     "hobbies" : ["gaming", "football", "hockey"],
     "wake up" : {"Monday" : "11AM",
                  "Tuesday" : "10AM",
                  "Wednesday" : "8:30AM"
                  }
     }

print("Name: " + d["name"])
print("# of Hobbies: " + str(len(d["hobbies"])))
print("When I wake up (sometimes): " + d["wake up"]["Wednesday"])