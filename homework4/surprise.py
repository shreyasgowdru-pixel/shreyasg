# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

def name_star(targets):
	for name in targets:
		print(name)

def name_and_type(targets):
	for name in targets:
		print(name, targets[name])


#1
def name_stars(targets):
    for star in targets:
        print(star)
name_stars(targets)

#2
def name_and_spectral_type(targets):
	for star in targets:
		print(star, targets[star]["Spectral Type"])
name_and_spectral_type(targets)

#3
def find_bright_stars(targets):
	for star in targets:
		if targets[star]["Magnitude"] > 0.1:
			print(star, targets[star]["Magnitude"])
find_bright_stars(targets)

#4
def add_target(targets, name, ra, dec, magnitude, spectral_type):
    targets[name] = {
        "RA": ra,
        "Dec": dec,
        "Magnitude": magnitude,
        "Spectral Type": spectral_type
    }
add_target(targets, "Canopus", "06h 23m 57.11s", "-52° 41′ 44.38″", -0.72, "A9II")

#5
def find_star_decl(targets):
	closest_star = None
	minimum_diff = float("1000000") #some arbitrary difference so that the first one doesnt become minimum
	for star in targets:
		dec = targets[star]["Dec"]
		dec_minus = dec.replace("−", "-") #replace the minus sign with a regular minus sign so that it reads as a negative number rather than a string
		dec_getnumbers = float(dec_minus.split("°")[0])
		diff = abs(dec_getnumbers - 20)
		if diff < minimum_diff:
			minimum_diff = diff
			closest_star = star
	return closest_star
print(find_star_decl(targets))

#6: my favorite constellation is Orion since it is the easiest to find due to the three stars in a row on the belt.



# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?
