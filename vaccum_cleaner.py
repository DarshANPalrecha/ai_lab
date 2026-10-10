# Robot Vacuum Cleaner Agent

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


# Environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

print("Initial Environment:", environment)

for step in range(5):
    status = environment[location]
    action = vacuum_agent(location, status)

    print(f"\nLocation: {location}")
    print(f"Status: {status}")
    print(f"Action: {action}")

    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

    print("Environment:", environment)

    if all(status == "Clean" for status in environment.values()):
        print("\nAll locations are clean!")
        break