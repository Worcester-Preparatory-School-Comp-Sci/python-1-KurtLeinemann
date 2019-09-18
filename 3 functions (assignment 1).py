#Kurt Leinemann 9/17/19 Three Functions

#function 1 must take the volume of the great lakes, divide by area of the 48 contiguous states, and find the depth of the water
def howDeep():
	lakesVolume = 22810 #cubic kilometers
	statesArea = 8080464 #square kilometers
	depthWater= (lakesVolume/statesArea)*1000 #in meters
	print(depthWater,"meters deep")

def gasInfo(gasGallons):
	#rules : one barrel produces 19.5 gallons of gasoline, one gallon of gas produces 20 lbs of CO2 gas when burned, gas costs $3.35/gallon)
	numLiters = gasGallons * 3.785
	numBarrels = gasGallons/19.5
	numCarbon = gasGallons*20
	price = gasGallons*3.35
	print("Liters:",numLiters,"\nBarrels:",numBarrels,"\nPounds CO2 when burned:",numCarbon,"\nThe price is $",price)
	
def population(years):
	#rules : There is a birth every 7 seconds There is a death every 13 seconds There is a new immigrant every 35 seconds
	initialPopulation = 307357870
	newPopulation = (years*365*60*24*60/7)-(years*365*24*60*60/13)+(years*365*24*60*60/35)+initialPopulation
	newPopulation=int(newPopulation)
	print("The population after",years,"years is ",newPopulation,"people")
howDeep()
population(20)
gasInfo(11)
