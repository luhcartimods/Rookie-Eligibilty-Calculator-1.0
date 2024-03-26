import pandas as pd
#make sure to run (pip install pandas) in the terminal
#data from bbref (idk how to source)
#this data is from 2023 season

data = {
    'Jake Alu': 175,
    'Francisco Alvarez': 437,
    'Miguel Amaya': 156,
    'Gabriel Arias': 402,
    'Ji Hwan Bae': 408,
    'Patrick Bailey': 353,
    'Luken Baker': 99,
    'Brett Baty': 431,
    'Dairon Blanco': 145,
    'Will Brennan': 500,
    'Alec Burleson': 400,
    'Jose Caballero': 280,
    'Dominic Canzone': 182,
    'Conner Capel': 145,
    'Corbin Carroll': 760,
    'Triston Casas': 597,
    'Oscar Colas': 263,
    'Henry Davis': 255,
    'Elly De La Cruz': 427,
    'Jonny DeLuca': 45,
    'Jordan Diaz': 344,
    'Yainer Diaz': 386,
    'Brenton Doyle': 431,
    'Christian Encarnacion-Strand': 241,
    'Freddy Fermin': 242,
    'Sal Frelick': 223,
    'David Fry': 113,
    'Maikel Garcia': 538,
    'Zack Gelof': 300,
    'Dalton Guthrie': 56,
    'Gunnar Henderson': 754,
    'Bryce Johnson': 67,
    'Nolan Jones': 518,
    'Edouard Julien': 408,
    'Corey Julks': 323,
    'Josh Jung': 617,
    'Grae Kessinger': 45,
    'Royce Lewis': 280,
    'Nathan Lukes': 31,
    'Miles Mastrobuoni': 166,
    'Luis Matos': 253,
    'Matt McLain': 403,
    'Garrett Mitchell': 141,
    'Andruw Monasterio': 315,
    'Bo Naylor': 238,
    'Zach Neto': 329,
    'Ryan Noda': 495,
    'Logan OHoppe': 215,
    'James Outman': 593,
    'Oswald Peraza': 248,
    'Carlos Perez': 71,
    'Blake Perkins': 168,
    'Israel Pineda': 14,
    'Heliot Ramos': 82,
    'Henry Ramos': 141,
    'Zach Remillard': 160,
    'Endy Rodriguez': 204,
    'Johan Rojas': 164,
    'Eguy Rosario': 46,
    'Esteury Ruiz': 533,
    'Blake Sabol': 344,
    'Cesar Salazar': 19,
    'Casey Schmitt': 277,
    'Tyler Soderstrom': 138,
    'Lenyn Sosa': 209,
    'Spencer Steer': 773,
    'Brett Sullivan': 86,
    'Cody Thomas': 78,
    'Michael Toglia': 272,
    'Ezequiel Tovar': 650,
    'Jared Triolo': 209,
    'Brice Turang': 448,
    'Enmanuel Valdez': 149,
    'Miguel Vargas': 354,
    'Mark Vientos': 274,
    'Anthony Volpe': 601,
    'Jordan Walker': 465,
    'Matt Wallner': 319,
    'Jordan Westburg': 228,
    'Joey Wiemer': 410,
    'Masataka Yoshida': 580,
}

def is_rookie(pa):
    return pa <= 130

def get_pa(player_name):
    return data.get(player_name, "Player not found")

def check_rookie_eligibility(player_name):
    pa = get_pa(player_name)
    if pa == "Player not found":
        print("Player not found in the data.")
    else:
        rookie_status = is_rookie(pa)
        if rookie_status:
            print(f"{player_name} is eligible as a rookie, {player_name} has {pa} plate apperances! The cuttoff is 130 Plate Apperances!")
        else:
            print(f"{player_name} is not eligible as a rookie. {player_name} has {pa} plate apperances!")

player_name = input("Enter the player's name: ")
check_rookie_eligibility(player_name)
