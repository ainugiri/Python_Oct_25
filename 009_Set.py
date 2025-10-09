Team1 = {"Rohit", "Virat", "Dhoni", "Jadeja", "Steve", "Bumrah"}
Team2 = {"james", "Rohit",  "Warner"}
Team3 = {"Dhoni", "Rohit", "Warner"}

print(Team1 | Team2)  # union
print(Team1 & Team2)  # intersection
print(Team1 - Team2)  # difference who is playing for Team1 but not in Team2
print(Team2 - Team1)  # difference who is playing for Team2 but not in Team1