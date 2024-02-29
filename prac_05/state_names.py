CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

for code, name in CODE_TO_NAME.items():
    try:
        print(f"{code} is {name}")
    except KeyError:
        print("Invalid state code")


while True:
    state_code = input("Enter short state: ").upper()
    if not state_code:
        break
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
