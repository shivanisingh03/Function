# -----------------------------bug----------------------#

# def greet(names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender")


# -----------------------------debug--------------------------------#

def greet(*names):
    for name in names:
        print("Welcome", name)

greet("Rinki", "Vishal", "Kartik", "Bijender")