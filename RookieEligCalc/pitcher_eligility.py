import pandas as pd

#data from bbref (idk how to source)
#make sure to run pip install pandas in the terminal
#data from 2023 season

data = {
    'Andrew Abbott': 109.1,
    'Logan Allen': 125.1,
    'Grant Anderson': 35.2,
    'Javier Assad': 147.0,
    'Pedro Avila': 63.2,
    'Sam Bachman': 17.0,
    'Peyton Battenfield': 34.2,
    'Tristan Beck': 85.0,
    'Brennan Bernardino': 53.0,
    'Tanner Bibee': 142.0,
    'Osvaldo Bido': 50.2,
    'Ronel Blanco': 58.1,
    'Cody Bradford': 56.0,
    'Taj Bradley': 104.2,
    'Jhony Brito': 90.2,
    'Hunter Brown': 176.0,
    'Alec Burleson': 1.2,
    'Isaiah Campbell': 28.2,
    'Yennier Cano': 90.2,
    'Drew Carlton': 33.0,
    'Cade Cavalli': 4.1,
    'Tom Cosgrove': 52.1,
    'Austin Cox': 35.2,
    'Fernando Cruz': 80.2,
    'Xzavion Curry': 104.1,
    'Tyler Cyr': 15.0,
    'Davis Daniel': 12.1,
    'Noah Davis': 31.0,
    'Jhonathan Diaz': 35.1,
    'Mason Englert': 56.0,
    'Lucas Erceg': 55.0,
    'Jeremiah Estrada': 17.1,
    'Angel Felipe': 15.0,
    'Jose Ferrer': 34.0,
    'J.P. France': 136.1,
    'Bowden Francis': 37.0,
    'David Fry': 5.0,
    'Shintaro Fujinami': 79.0,
    'Deivi Garcia': 57.2,
    'Robert Garcia': 32.0,
    'Luis Gil': 33.1,
    'Michael Grove': 100.1,
    'Ian Hamilton': 72.2,
    'Hogan Harris': 63.0,
    'Grant Hartwig': 35.1,
    'Jose Hernandez': 50.2,
    'Sean Hjelle': 54.0,
    'Bryan Hoeing': 83.1,
    'Gavin Hollowell': 40.2,
    'Tyler Holton': 94.1,
    'Brent Honeywell Jr.': 56.2,
    'Jake Irvin': 121.0,
    'Andre Jackson': 82.2,
    'Alek Jacob': 3.0,
    'Joe Jacques': 26.2,
    'Drey Jameson': 65.0,
    'Ben Joyce': 10.0,
    'Kevin Kelly': 67.0,
    'Michael Kelly': 20.2,
    'Zack Kelly': 23.0,
    'Ray Kerr': 32.0,
    'Joe La Sorsa': 32.2,
    'Casey Legumina': 12.2,
    'Matthew Liberatore': 96.1,
    'Alec Marsh': 74.1,
    'Miles Mastrobuoni': 0.1,
    'James McArthur': 23.1,
    'Easton McGee': 9.2,
    'Scott McGough': 77.0,
    'Luis Medina': 109.2,
    'Bobby Miller': 124.1,
    'Bryce Miller': 131.1,
    'Mason Miller': 33.1,
    'Tyson Miller': 31.0,
    'Carmen Mlodzinski': 36.0,
    'Bryce Montes de Oca': 3.1,
    'Kyle Muller': 126.0,
    'Chris Murphy': 47.2,
    'Parker Mushinski': 22.0,
    'James Naile': 24.1,
    'Ryne Nelson': 162.1,
    'Reese Olson': 103.2,
    'Luis Ortiz': 33.1,
    'Daniel Palencia': 28.1,
    'Ryan Pepiot': 78.1,
    'Eury Perez': 91.1,
    'Brandon Pfaadt': 96.0,
    'Grayson Rodriguez': 122.0,
    'Cole Sands': 52.1,
    'Gregory Santos': 72.0,
    'Jesse Scholtens': 85.0,
    'Connor Seabold': 108.2,
    'Kodai Senga': 166.1,
    'Emmet Sheehan': 60.1,
    'Jared Shuster': 52.2,
    'Chase Silseth': 81.0,
    'George Soriano': 52.0,
    'Jose Soriano': 42.0,
    'Thomas Szapucki': 18.2,
    'Freddy Tarnok': 15.1,
    'Justin Topa': 87.1,
    'Abner Uribe': 30.2,
    'Carlos Vargas': 4.2,
    'Gus Varland': 20.2,
    'Louie Varland': 94.0,
    'Cole Waites': 8.0,
    'Ken Waldichuk': 175.2,
    'Josh Walker': 10.0,
    'Ryan Walker': 61.1,
    'Thaddeus Ward': 35.1,
    'Zack Weiss': 27.1,
    'Greg Weissert': 31.1,
    'Joey Wentz': 138.1,
    'Hayden Wesneski': 122.1,
    'Brendan White': 40.2,
    'Gavin Williams': 82.0,
    'Brandon Williamson': 117.0,
    'Bryan Woo': 87.2,
    'Angel Zerpa': 58.2
}

def is_rookie(ip):
    return ip <= 50

def get_ip(player_name):
    return data.get(player_name, "Player not found")

def check_rookie_eligibility(player_name):
    ip = get_ip(player_name)
    if ip == "Player not found":
        print("Player not found, check here for all 2023 rookies: https://www.baseball-reference.com/leagues/majors/2023-rookies.shtml")
    else:
        rookie_status = is_rookie(ip)
        if rookie_status:
            print(f"{player_name} is eligible as a rookie, {player_name} has {ip}/50 innings pitched!")
        else:
            print(f"{player_name} is not eligible as a rookie. {player_name} has {ip}/50")

while True:
    player_name = input("Enter the player's name (type 'exit' to quit): ")
    if player_name.lower() == 'exit':
        break
    check_rookie_eligibility(player_name)
