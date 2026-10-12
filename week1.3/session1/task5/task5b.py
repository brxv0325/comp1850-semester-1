# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c, r in rivers.items():
    print(c, r)

for c in rivers.keys():
    print(c)

for _, r in rivers.items():
    print(r)

# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# hint: we looked at built in function for dicts last session

greeting = "restart"
match greeting:
  case "hi":
    print("hi was case 1")
  case "start" | "restart":
    print("greeting was case 2")
  case _:
    print("greeting was not case 1 or 2")

