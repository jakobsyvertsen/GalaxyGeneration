import random
import json
import math
import string
import itertools
from alive_progress import alive_bar

myFile = open("starInfo.json", "w")
sapFile = open("sapientSpecies.json", "w")
specFile = open("speciesInfo.json", "w")

'''
To do at some point:
Add Asteroid Belt class so people can live in da asteroid belt
I can't be fucked to do it
'''
class Species:
    def __init__(self):
        self.biochemistry = ''
        self.tail_features = []
        self.manipulator_features = []
        self.special_senses = []
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    home_planet = ''
    biochemistry = ''
    land_dwelling = False
    water_dwelling = False
    habitat_type = ''
    trophic_level = ''
    primary_locomotion = ''
    secondary_locomotion = 'None'
    tertiary_locomotion = 'None'
    wingspan = 0
    size_category = ''
    size = 0
    mass = 0
    weight = 0
    strength = 0
    lifespan = ''
    symmetry = ''
    number_of_segments = 0
    number_of_limbs = 0
    number_of_sides = 0
    tail = False
    tail_features = []
    number_of_manipulators = 0
    manipulator_features = []
    skeleton_type = ''
    outer_covering_type = ''
    skin_type = ''
    breathing_method = ''
    temperature_regulation = ''
    growth_pattern = ''
    number_of_sexes = ''
    gestation_method = ''
    special_gestation_method = 'None'
    reproductive_strategy = ''
    number_of_offspring = 0
    primary_sense = ''
    vision = ''
    hearing = ''
    touch = ''
    taste_smell = ''
    special_senses = []
    primary_communication_channel = ''
    secondary_communication_channel = ''
    intelligence = ''
    iq = 0
    mating_behaviour = ''
    social_organisation = ''
    chauvinism = ''
    concentration = ''
    curiosity = ''
    egoism = ''
    empathy = ''
    gregariousness = ''
    imagination = ''
    suspicion = ''
    playfulness = ''
    sapient = False
    psionic = False

class Galaxy:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    num_stars = 123892
    system_list = []

class StarSystem:

    def toJSON(self):
        for starx in self.star_list:
                try:
                    starx.parent_star = starx.parent_star.name
                    starx.main_world = starx.main_world.name
                except AttributeError:
                    starx.parent_star = starx.parent_star
                    starx.main_world = starx.main_world.name
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    star_list = []
    sys_type = ''
    sys_age = 0
    sys_pop = ''
    sys_name = ''
    num_planets = 0
    inhabited_system = False
    sapient_home_system = False
    
class Star:

    def __init__(self, bool_val=False, par_star=''):
        self.is_companion = bool_val
        self.parent_star = par_star
        self.separation = ''
        self.orbit_sep_mult = 0.0
        self.orbit_separation_radius = 0.0
        self.orbit_eccentricity = 0.0
        self.inner_limit_radius = 0.0
        self.outer_limit_radius = 0.0
        self.snow_line_radius = 0.0
        self.min_separation = 0.0
        self.max_separation = 0.0
        self.forbidden_zone_min = 0.0
        self.forbidden_zone_max = 0.0
        self.star_mass = 0.0
        self.star_class = ''
        self.temp = 0
        self.l_min = 0.0
        self.l_max = 0.0
        self.m_span = 0.0
        self.s_span = 0.0
        self.g_span = 0.0
        self.star_sequence = ''
        self.effective_temp = 0
        self.luminosity_class = ''
        self.luminosity = 0.0
        self.radius = 0.0
        self.planet_list = []
        self.gas_giant_arrangement = ''
        self.orbital_spacing = []
        self.orbital_period = 0.0
        self.installations = []

    def toJSON(self):
        #if len(self.companions) > 0:
        for star in self.companions:
            star.parent_star = star.parent_star.name
            star.main_world = star.main_world.name
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        else:
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    name = ''
    is_companion = False
    star_age = 0
    parent_star = ''
    companions = []
    separation = ''
    orbit_sep_mult = 0.0
    orbit_separation_radius = 0.0
    orbit_eccentricity = 0.0
    inner_limit_radius = 0.0
    outer_limit_radius = 0.0
    snow_line_radius = 0.0
    min_separation = 0.0
    max_separation = 0.0
    forbidden_zone_min = 0.0
    forbidden_zone_max = 0.0
    star_mass = 0.0
    star_class = ''
    temp = 0
    l_min = 0.0
    l_max = 0.0
    m_span = 0.0
    s_span = 0.0
    g_span = 0.0
    star_sequence = ''
    effective_temp = 0
    luminosity_class = ''
    luminosity = 0.0
    radius = 0.0
    planet_list = []
    gas_giant_arrangement = ''
    orbital_spacing = []
    orbital_period = 0.0
    main_world = ''
    installations = []
    diameter = ''

class Planet:
    def __init__(self):
        self.companions = []
        self.tide_locked = False
        self.atmospheric_composition = []
        self.atmospheric_gases = []
        self.installations = []
    distance_from_parent = 0.0
    name = ''
    size = ''
    world_type = ''
    planet_type = ''
    companions = []
    num_moons = 0
    blackbody_temperature = 0.0
    atmospheric_pressure = 0.0
    pressure_category = ''
    atmospheric_mass = 0.0
    atmospheric_composition = []
    atmospheric_gases = []
    hydrographic_coverage_percent = 0
    blackbody_correction = 0.0
    surface_temperature = 0.0
    climate_type = ''
    world_density = 0.0
    core_type = ''
    world_mass = 0
    world_diameter = 0.0
    surface_gravity = 0.0
    orbital_period = 0.0
    orbital_eccentricity = 0.0
    min_separation = 0.0
    max_separation = 0.0
    tidal_braking = 0.0
    tide_locked = False
    rotation_period = 0
    retrograde_orbit = False
    day_length = 0
    moon_cycle_length = 0
    axial_tilt = 0
    volcanic_activity_level = ''
    tectonic_activity_level = ''
    resource_value_level = ''
    resource_value_modifier = 0
    habitability_modifier = 0
    affinity_modifier = 0
    main_world = False
    homeworld = False
    colony = False
    outpost = False
    inhabited_world = False
    tech_level = 0
    carrying_capacity = 0
    population = 0
    population_rating = 0
    world_unity = ''
    society_type = ''
    parent_power = ''
    control_rating = 0
    per_capita_income = 0
    wealth_level = ''
    spaceport_type = ''
    installations = []

class GasGiant(Planet):
    def __init__(self):
        self.world_type = 'Gas Giant'
        self.planet_type = 'Gas Giant'
        self.close_moonlets = []
        self.companions = []
        self.far_moonlets = []
        self.blackbody_temperature = 0
        self.tide_locked = False
        self.installations = []
    close_moonlets = []
    num_close_moonlets = 0
    far_moonlets = []
    num_far_moonlets = 0
    ring_status = ''
    cloud_top_gravity = 0

class TerrestrialPlanet(Planet):
    def __init__(self):
        self.planet_type = 'Terrestrial'
        self.companions = []
        self.blackbody_temperature = 0
        self.hydrographic_coverage_percent = 0
        self.atmospheric_gases = []
        self.atmospheric_composition = []
        self.tide_locked = False
        self.installations = []
    complete_world_type = ''

class Moon(TerrestrialPlanet):
    def __init__(self):
        self.planet_type = 'Moon'
        self.blackbody_temperature = 0
        self.hydrographic_coverage_percent = 0
        self.atmospheric_gases = []
        self.atmospheric_composition = []
        self.tide_locked = False
        self.installations = []
    parent_name = ''
    
class Moonlet(Moon):
    def __init__(self):
        self.planet_type = 'Moonlet'
        self.tide_locked = False
    distance_from_planet = 0
    family = ''

def gen_sys_name(letter=3, digits=3):
    alpha = string.ascii_uppercase
    digit = string.digits
    alpha_list = [alpha]*letter
    digit_list = [digit]*digits
    for i in itertools.product(*alpha_list):
        for j in itertools.product(*digit_list):
            yield "".join(i + j)

def gen_planet_name():
    alpha = string.ascii_uppercase
    digit = string.digits
    alpha_list = [alpha]
    digit_list = [digit]*2
    for i in itertools.product(*digit_list):
        for j in itertools.product(*alpha_list):
            yield "".join(i + j)

def gen_moon_name():
    alpha = string.ascii_lowercase
    digit = string.digits
    alpha_list = [alpha]
    digit_list = [digit]*2
    for i in itertools.product(*digit_list):
        for j in itertools.product(*alpha_list):
            yield "".join(i + j)

def write_to_file(the_system, the_file=myFile):
    the_file = open("starInfo.json", "a")
    the_file.write(the_system.toJSON() + ",")
    the_file.close()


sysname = gen_sys_name()

def galaxy_gen():
    myFile = open("starInfo.json", "w")
    myFile.write("[{")
    specFile = open('speciesInfo.json', "w")
    specFile.write("[{")
    sapFile = open('sapientSpecies.json', "w")
    sapFile.write("[{")
    print("enter random seed:")
    seed = input()
    print("enter number of stars")
    stars = input()
    print("\n")
    random.seed(seed)

    the_galaxy = Galaxy()
    the_galaxy.num_stars = int(stars)
    numSingle = 0
    numBinary = 0
    numTrinary = 0
    numStars = the_galaxy.num_stars
    with alive_bar(numStars) as bar:
        while numStars > 0:
            roll = roll_dice(3)
            if roll <= 10 or numStars == 1:
                #StarSystem.star_list.extend(star_gen('Solitary'))
                temp_system = system_gen('Solitary')
                numSingle += 1
                numStars -= 1
            elif (roll <= 15) or numStars == 2:
                #StarSystem.star_list.extend(star_gen('Binary'))
                temp_system = system_gen('Binary')
                numBinary += 1
                numStars -= 2
            else:
                #StarSystem.star_list.extend(star_gen('Trinary'))
                temp_system = system_gen('Trinary')
                numTrinary += 1
                numStars -= 3
            if temp_system.sys_type == 'Solitary':
                bar(1)
            elif temp_system.sys_type == 'Binary':
                bar(2)
            elif temp_system.sys_type == 'Trinary':
                bar(3)
            else:
                bar(3)
            the_galaxy.system_list.append(temp_system)


    #TO DO — write a goofy ass function right here that iterates through stars and converts parent stars to the names

    myFile.close()
    lines = []
    with open("starInfo.json", "r") as myFile:
        lines = myFile.readlines()
    myFile.close()
    with open("starInfo.json", "w") as myFile:
        myFile.writelines(lines[:-1])
        myFile.write("}]")
    myFile.close()

    spec_lines = []
    with open("speciesInfo.json", "r") as specFile:
        spec_lines = specFile.readlines()
    specFile.close()
    with open("speciesInfo.json", "w") as specFile:
        specFile.writelines(spec_lines[:-1])
        specFile.write("}]")
    specFile.close()

    sap_lines = []
    with open("sapientSpecies.json", "r") as sapFile:
        sap_lines = sapFile.readlines()
    sapFile.close()
    with open("sapientSpecies.json", "w") as sapFile:
        sapFile.writelines(sap_lines[:-1])
        sapFile.write("}]")
    sapFile.close()


def system_gen(system_type):
    the_system = StarSystem()
    the_system.star_list = []
    the_system.sys_type = system_type
    the_system.sys_name = next(sysname)
    generate_system_age(the_system)
    
    the_system.star_list.extend(star_gen(system_type, the_system.sys_age, the_system.sys_name))
    if len(the_system.star_list) == 4:
        the_system.sys_type = 'Quaternary'
        the_system.star_list[3].name = the_system.sys_name + ' IV'
    if len(the_system.star_list) == 5:
        the_system.sys_type = 'Quinary'
        the_system.star_list[3].name = the_system.sys_name + ' IV'
        the_system.star_list[4].name = the_system.sys_name + ' V'

    if len(the_system.star_list) > 1:
        generate_stellar_orbital_period(the_system.star_list, the_system.sys_type)
    for star in the_system.star_list:
        generate_gas_giant_arrangement(star)
        generate_orbital_spacing(star)
        fill_orbits(star)
        generate_moons(star)
        determine_blackbody_temperature(star)
        #The mother of all functions...
        assign_world_types(star)
        determine_atmosphere(star)
        determine_hydrographic_coverage(star)
        determine_climate(star)
        determine_world_size(star)
        determine_surface_atmospheric_pressure(star)
        generate_planet_dynamic_parameters(star)
        generate_volcanism(star)
        determine_resources(star)
        determine_habitability(star)
        determine_affinity(star)
        determine_main_world(star)
        name_worlds(star)
        check_sapient_species(the_system, star)
        
        if len(star.planet_list) < 1:
            if roll_dice(3) <= 8:
                star.installations.append('Dyson Swarm')
            elif roll_dice(3) >= 18:
                star.installations.append('Dyson Sphere')
    
    write_to_file(the_system)

    return the_system
       
def star_gen(sysType, sys_age, sys_name):
    if(sysType == 'Solitary'):
        star1 = Star()
        star1.name = sys_name + ' I'
        starlist = [star1]
    elif(sysType == 'Binary'):
        star1 = Star()
        star1.name = sys_name + ' I'
        star2 = Star(True, star1)
        star2.name = sys_name + ' II'
        starlist = [star1, star2]
    else:
        star1 = Star()
        star1.name = sys_name + ' I'
        star2 = Star(True, star1)
        star2.name = sys_name + ' II'
        star3 = Star(True, star1)
        star3.name = sys_name + ' III'
        star1.companions.append(star2)
        star1.companions.append(star3)
        starlist = [star1, star2, star3]
#generate size of star1
    generate_star_size(star1)
    
#if in a multistar system, generate their masses.
    for x in starlist:
        x.star_age = sys_age
        if x.is_companion == True:
            roll = roll_dice(1) - 1
            if roll == 0:
                x.star_mass = star1.star_mass
            else:
                totRoll = 0
                for _ in range(roll):
                    totRoll += roll_dice(1)
                if totRoll > 5:    
                    x.star_mass = round(star1.star_mass - (5 * 0.1) - ((totRoll - 5) * 0.05), 2)
                else:
                    x.star_mass = round(star1.star_mass - (totRoll * 0.1), 2)
                if x.star_mass < 0.10:
                    x.star_mass = 0.10
                
    #I'm going to krill myself if I keep having to write this many fucking if statements. Fuck you python, make a switch statement you quivering pussy.
    for star_to_define in starlist:
        classify_spectral_type(star_to_define)
        classify_star_sequence(star_to_define, sys_age)
        define_stellar_characteristics(star_to_define, sys_age)
        
    #we are out of the above for loop and about to do step 19: companion star orbits.
    if len(starlist) > 1:
        generate_companion_orbits(star1, starlist, sys_age)
        #check that 2nd star in trinary system has a wider orbital separation than the orbital separation of first star
        if len(starlist) > 2:
            check_trinary_orbit_radius(starlist[1], starlist[2])
        calculate_orbital_eccentricity(starlist)

    #generate inner and outer planet formation radii
    generate_orbital_zones(starlist)

    return starlist




#Functions used above
def generate_system_age(the_system):
    roll = roll_dice(3)
    if roll_dice(3) >= 16:
        roll += 3
    if roll == 3:
        the_system.sys_pop = 'Extreme Population I'
        the_system.sys_age = 0.01
    elif roll <= 6:
        the_system.sys_pop = 'Young Population I'
        roll1 = roll_dice(1) - 1
        roll2 = roll_dice(1) - 1
        the_system.sys_age = 0.1 + (roll1 * 0.3) + (roll2 * 0.05)
    elif roll <= 10:
        the_system.sys_pop = 'Intermediate Population I'
        roll1 = roll_dice(1) - 1
        roll2 = roll_dice(1) - 1
        the_system.sys_age = 2 + (roll1 * 0.6) + (roll2 * 0.1)
    elif roll <= 14:
        the_system.sys_pop = 'Old Population I'
        roll1 = roll_dice(1) - 1
        roll2 = roll_dice(1) - 1
        the_system.sys_age = 5.6 + (roll1 * 0.6) + (roll2 * 0.1)
    elif roll <= 17:
        the_system.sys_pop = 'Intermediate Population II'
        roll1 = roll_dice(1) - 1
        roll2 = roll_dice(1) - 1
        the_system.sys_age = 8 + (roll1 * 0.6) + (roll2 * 0.1)
    else:
        the_system.sys_pop = 'Extreme Population II'
        roll1 = roll_dice(1) - 1
        roll2 = roll_dice(1) - 1
        the_system.sys_age = 10 + (roll1 * 0.6) + (roll2 * 0.1)

def generate_star_size(star_to_define):
    roll = roll_dice(3) - 4
    if roll <= 3:
        roll = 3
    if roll == 3:
        roll = roll_dice(3)
        if roll <=10:
            star_to_define.star_mass = 2.0
        else:
            star_to_define.star_mass = 1.90
    elif roll == 4:
        roll = roll_dice(3)
        if roll <=8:
            star_to_define.star_mass = 1.80
        elif roll <= 11:
            star_to_define.star_mass = 1.70
        else:
            star_to_define.star_mass = 1.60
    elif roll == 5:
        roll = roll_dice(3)
        if roll <=7:
            star_to_define.star_mass = 1.50
        elif roll <= 10:
            star_to_define.star_mass = 1.45
        elif roll <= 12:
            star_to_define.star_mass = 1.40
        else:
            star_to_define.star_mass = 1.35
    elif roll == 6:
        roll = roll_dice(3)
        if roll <=7:
            star_to_define.star_mass = 1.30
        elif roll <= 9:
            star_to_define.star_mass = 1.25
        elif roll <= 10:
            star_to_define.star_mass = 1.20
        elif roll <= 12:
            star_to_define.star_mass = 1.15
        else:
            star_to_define.star_mass = 1.10
    elif roll == 7:
        roll = roll_dice(3)
        if roll <=7:
            star_to_define.star_mass = 1.05
        elif roll <= 9:
            star_to_define.star_mass = 1.0
        elif roll <= 10:
            star_to_define.star_mass = 0.95
        elif roll <= 12:
            star_to_define.star_mass = 0.90
        else:
            star_to_define.star_mass = 0.85
    elif roll == 8:
        roll = roll_dice(3)
        if roll <=7:
            star_to_define.star_mass = 0.80
        elif roll <= 9:
            star_to_define.star_mass = 0.75
        elif roll <= 10:
            star_to_define.star_mass = 0.70
        elif roll <= 12:
            star_to_define.star_mass = 0.65
        else:
            star_to_define.star_mass = 0.60
    elif roll == 9:
        roll = roll_dice(3)
        if roll <=8:
            star_to_define.star_mass = 0.55
        elif roll <= 11:
            star_to_define.star_mass = 0.50
        else:
            star_to_define.star_mass = 0.45
    elif roll == 10:
        roll = roll_dice(3)
        if roll <=8:
            star_to_define.star_mass = 0.40
        elif roll <= 11:
            star_to_define.star_mass = 0.35
        else:
            star_to_define.star_mass = 0.30
    elif roll == 11:
        roll = roll_dice(3)
        star_to_define.star_mass = 0.25
    elif roll == 12:
        roll = roll_dice(3)
        star_to_define.star_mass = 0.20
    elif roll == 13:
        roll = roll_dice(3)
        star_to_define.star_mass = 0.15
    else:
        roll = roll_dice(3)
        star_to_define.star_mass = 0.10

def classify_spectral_type(star_to_define):
    if star_to_define.star_mass == 0.10:
        star_to_define.star_class = 'M7'
        star_to_define.temp = 3100
        star_to_define.l_min = 0.0012
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'L7'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.15:
        star_to_define.star_class = 'M6'
        star_to_define.temp = 3200
        star_to_define.l_min = 0.0036
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'L6'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.20:
        star_to_define.star_class = 'M5'
        star_to_define.temp = 3200
        star_to_define.l_min = 0.0079
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'M5'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.25:
        star_to_define.star_class = 'M4'
        star_to_define.temp = 3300
        star_to_define.l_min = 0.015
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'M4'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.30:
        star_to_define.star_class = 'M4'
        star_to_define.temp = 3300
        star_to_define.l_min = 0.024
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'M4'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.35:
        star_to_define.star_class = 'M3'
        star_to_define.temp = 3400
        star_to_define.l_min = 0.037
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'M3'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.40:
        star_to_define.star_class = 'M2'
        star_to_define.temp = 3500
        star_to_define.l_min = 0.054
        star_to_define.l_max = 0
        star_to_define.m_span = 0
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'M2'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.45:
        star_to_define.star_class = 'M1'
        star_to_define.temp = 3600
        star_to_define.l_min = 0.07
        star_to_define.l_max = 0.08
        star_to_define.m_span = 70
        star_to_define.s_span = 0
        star_to_define.g_span = 0
        if roll_dice(3) <= 7:
            star_to_define.star_sequence = 'Brown Dwarf'
            star_to_define.luminosity_class = 'Luminosity Class VII'
            star_to_define.star_class = 'M1'
            roll = roll_dice(3)
            if roll <= 8:
                star_to_define.star_mass = 0.015
            elif roll <= 10:
                star_to_define.star_mass = 0.02
            elif roll <= 12:
                star_to_define.star_mass = 0.03
            elif roll <= 14:
                star_to_define.star_mass = 0.04
            elif roll <= 15:
                star_to_define.star_mass = 0.05
            elif roll <= 16:
                star_to_define.star_mass = 0.06
            else:
                star_to_define.star_mass = 0.07
    elif star_to_define.star_mass == 0.50:
        star_to_define.star_class = 'M0'
        star_to_define.temp = 3800
        star_to_define.l_min = 0.09
        star_to_define.l_max = 0.11
        star_to_define.m_span = 59
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.55:
        star_to_define.star_class = 'K8'
        star_to_define.temp = 4000
        star_to_define.l_min = 0.11
        star_to_define.l_max = 0.15
        star_to_define.m_span = 50
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.60:
        star_to_define.star_class = 'K6'
        star_to_define.temp = 4200
        star_to_define.l_min = 0.13
        star_to_define.l_max = 0.20
        star_to_define.m_span = 42
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.65:
        star_to_define.star_class = 'K5'
        star_to_define.temp = 4400
        star_to_define.l_min = 0.15
        star_to_define.l_max = 0.25
        star_to_define.m_span = 37
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.70:
        star_to_define.star_class = 'K4'
        star_to_define.temp = 4600
        star_to_define.l_min = 0.19
        star_to_define.l_max = 0.35
        star_to_define.m_span = 30
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.75:
        star_to_define.star_class = 'K2'
        star_to_define.temp = 4900
        star_to_define.l_min = 0.23
        star_to_define.l_max = 0.48
        star_to_define.m_span = 24
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.80:
        star_to_define.star_class = 'K0'
        star_to_define.temp = 5200
        star_to_define.l_min = 0.28
        star_to_define.l_max = 0.65
        star_to_define.m_span = 20
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.85:
        star_to_define.star_class = 'G8'
        star_to_define.temp = 5400
        star_to_define.l_min = 0.36
        star_to_define.l_max = 0.84
        star_to_define.m_span = 17
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.90:
        star_to_define.star_class = 'G6'
        star_to_define.temp = 5500
        star_to_define.l_min = 0.45
        star_to_define.l_max = 1.0
        star_to_define.m_span = 14
        star_to_define.s_span = 0
        star_to_define.g_span = 0
    elif star_to_define.star_mass == 0.95:
        star_to_define.star_class = 'G4'
        star_to_define.temp = 5700
        star_to_define.l_min = 0.56
        star_to_define.l_max = 1.3
        star_to_define.m_span = 12
        star_to_define.s_span = 1.8
        star_to_define.g_span = 1.1
    elif star_to_define.star_mass == 1.0:
        star_to_define.star_class = 'G2'
        star_to_define.temp = 5800
        star_to_define.l_min = 0.68
        star_to_define.l_max = 1.6
        star_to_define.m_span = 10
        star_to_define.s_span = 1.6
        star_to_define.g_span = 1.0
    elif star_to_define.star_mass == 1.05:
        star_to_define.star_class = 'G1'
        star_to_define.temp = 5900
        star_to_define.l_min = 0.87
        star_to_define.l_max = 1.9
        star_to_define.m_span = 8.8
        star_to_define.s_span = 1.4
        star_to_define.g_span = 0.8
    elif star_to_define.star_mass == 1.10:
        star_to_define.star_class = 'G0'
        star_to_define.temp = 6000
        star_to_define.l_min = 1.1
        star_to_define.l_max =  2.2
        star_to_define.m_span = 7.7
        star_to_define.s_span = 1.2
        star_to_define.g_span = 0.7
    elif star_to_define.star_mass == 1.15:
        star_to_define.star_class = 'F9'
        star_to_define.temp = 6100
        star_to_define.l_min = 1.4
        star_to_define.l_max = 2.6
        star_to_define.m_span = 6.7
        star_to_define.s_span = 1.0
        star_to_define.g_span = 0.6
    elif star_to_define.star_mass == 1.20:
        star_to_define.star_class = 'F8'
        star_to_define.temp = 6300
        star_to_define.l_min = 1.7
        star_to_define.l_max = 3.0
        star_to_define.m_span = 5.9
        star_to_define.s_span = 0.9
        star_to_define.g_span = 0.6
    elif star_to_define.star_mass == 1.25:
        star_to_define.star_class = 'F7'
        star_to_define.temp = 6400
        star_to_define.l_min = 2.1
        star_to_define.l_max = 3.5
        star_to_define.m_span = 5.2
        star_to_define.s_span = 0.8
        star_to_define.g_span = 0.5
    elif star_to_define.star_mass == 1.30:
        star_to_define.star_class = 'F6'
        star_to_define.temp = 6500
        star_to_define.l_min = 2.5
        star_to_define.l_max = 3.9
        star_to_define.m_span = 4.6
        star_to_define.s_span = 0.7
        star_to_define.g_span = 0.4
    elif star_to_define.star_mass == 1.35:
        star_to_define.star_class = 'F5'
        star_to_define.temp = 6600
        star_to_define.l_min = 3.1
        star_to_define.l_max = 4.5
        star_to_define.m_span = 4.1
        star_to_define.s_span = 0.6
        star_to_define.g_span = 0.4
    elif star_to_define.star_mass == 1.40:
        star_to_define.star_class = 'F4'
        star_to_define.temp = 6700
        star_to_define.l_min = 3.7
        star_to_define.l_max = 5.1
        star_to_define.m_span = 3.7
        star_to_define.s_span = 0.6
        star_to_define.g_span = 0.4
    elif star_to_define.star_mass == 1.45:
        star_to_define.star_class = 'F3'
        star_to_define.temp = 6900
        star_to_define.l_min = 4.3
        star_to_define.l_max = 5.7
        star_to_define.m_span = 3.3
        star_to_define.s_span = 0.5
        star_to_define.g_span = 0.3
    elif star_to_define.star_mass == 1.50:
        star_to_define.star_class = 'F2'
        star_to_define.temp = 7000
        star_to_define.l_min = 5.1
        star_to_define.l_max = 6.5
        star_to_define.m_span = 3.0
        star_to_define.s_span = 0.5
        star_to_define.g_span = 0.3
    elif star_to_define.star_mass == 1.60:
        star_to_define.star_class = 'F0'
        star_to_define.temp = 7300
        star_to_define.l_min = 6.7
        star_to_define.l_max =  8.2
        star_to_define.m_span = 2.5
        star_to_define.s_span = 0.4
        star_to_define.g_span = 0.2
    elif star_to_define.star_mass == 1.70:
        star_to_define.star_class = 'A9'
        star_to_define.temp = 7500
        star_to_define.l_min = 8.6
        star_to_define.l_max = 10.0
        star_to_define.m_span = 2.1
        star_to_define.s_span = 0.3
        star_to_define.g_span = 0.2
    elif star_to_define.star_mass == 1.80:
        star_to_define.star_class = 'A7'
        star_to_define.temp = 7800
        star_to_define.l_min = 11.0
        star_to_define.l_max = 13.0
        star_to_define.m_span = 1.8
        star_to_define.s_span = 0.3
        star_to_define.g_span = 0.2
    elif star_to_define.star_mass == 1.90:
        star_to_define.star_class = 'A6'
        star_to_define.temp = 8000
        star_to_define.l_min = 13.0
        star_to_define.l_max =  16.0
        star_to_define.m_span = 1.5
        star_to_define.s_span = 0.2
        star_to_define.g_span = 0.1
    else:
        star_to_define.star_class = 'A5'
        star_to_define.temp = 8200
        star_to_define.l_min = 16.0
        star_to_define.l_max = 20.0
        star_to_define.m_span = 1.3
        star_to_define.s_span = 0.2
        star_to_define.g_span = 0.1

def classify_star_sequence(star_to_define, sys_age):
    #figure out star sequence and luminosity class
    if star_to_define.m_span == 0:
        star_to_define.star_sequence = 'Main Sequence Star'
        star_to_define.luminosity_class = 'Luminosity Class V'
    elif sys_age <= star_to_define.m_span:
        star_to_define.star_sequence = 'Main Sequence Star'
        star_to_define.luminosity_class = 'Luminosity Class V'
    elif sys_age <= (star_to_define.s_span + star_to_define.m_span):
        star_to_define.star_sequence = 'Subgiant Star'
        star_to_define.luminosity_class = 'Luminosity Class IV'
    elif sys_age <= (star_to_define.g_span + star_to_define.s_span + star_to_define.m_span):
        star_to_define.star_sequence = 'Giant Star'
        star_to_define.luminosity_class = 'Luminosity Class III'
    else:
        star_to_define.star_sequence = 'White Dwarf'
        star_to_define.luminosity_class = 'Luminosity Class D'

def define_stellar_characteristics(star_to_define, sys_age):
        #time to fill out variables oh fuuuuuuuck
    if star_to_define.star_sequence == 'Main Sequence Star':
        if star_to_define.star_mass > 0.4:
            star_to_define.luminosity = star_to_define.l_min + ((sys_age/star_to_define.m_span) * (star_to_define.l_max - star_to_define.l_min))
        else:
            star_to_define.luminosity = star_to_define.l_min
        star_to_define.effective_temp = star_to_define.temp
        star_to_define.radius = round((155000 * math.sqrt(star_to_define.luminosity)/(star_to_define.effective_temp * star_to_define.effective_temp)), 4)
    elif star_to_define.star_sequence == 'Brown Dwarf':
        temp_age = star_to_define.star_age
        if temp_age <= 1:
            temp_age = 1
        temp_age = round(temp_age) // 1
        brown_dict = {
            0.015 : (0.00073, '17.5 Earths'),
            0.020 : (0.0016, '16.8 Earths'),
            0.030 : (0.0045, '15.9 Earths'),
            0.040 : (0.0097, '15.3 Earths'),
            0.050 : (0.017, '14.8 Earths'),
            0.060 : (0.028, '14.5 Earths'),
            0.070 : (0.042, '14.2 Earths')
        }
        age_dict = {
            1 : (1.0, 1.0),
            2 : (0.41, 0.96),
            3 : (0.24, 0.94),
            4 : (0.16, 0.93),
            5 : (0.12, 0.91),
            6 : (0.097, 0.90),
            7 : (0.080, 0.90),
            8 : (0.067, 0.89),
            9 : (0.057, 0.88),
            10 : (0.050, 0.88),
            11 : (0.044, 0.87),
            12 : (0.040, 0.87),
            13 : (0.036, 0.87),
            14 : (0.032, 0.86)
        }
        
        star_to_define.luminosity = brown_dict[star_to_define.star_mass][0] * age_dict[temp_age][0]
        star_to_define.diameter = brown_dict[star_to_define.star_mass][1] * age_dict[temp_age][1]
        star_to_define.l_min = brown_dict[star_to_define.star_mass][0]
        star_to_define.l_max = brown_dict[star_to_define.star_mass][0]

    #time to redo that whole fucking spectral type calculation yippee!
    elif star_to_define.star_sequence == 'Subgiant Star':
        star_to_define.luminosity = star_to_define.l_max * round(random.uniform(0.90, 1.11), 2)
        star_to_define.effective_temp = star_to_define.temp - ((sys_age/star_to_define.s_span) * (star_to_define.temp - 4800))
        if star_to_define.effective_temp <= 3100:
            star_to_define.star_class = 'M7'
        elif star_to_define.effective_temp <= 3200:
            if roll_dice(1,3) == 1:
                star_to_define.star_class = 'M6'
            else:
                star_to_define.star_class = 'M5'
        elif star_to_define.effective_temp <= 3300:
            star_to_define.star_class = 'M4'
        elif star_to_define.effective_temp <= 3400:
            star_to_define.star_class = 'M3'
        elif star_to_define.effective_temp <= 3500:
            star_to_define.star_class = 'M2'
        elif star_to_define.effective_temp <= 3600:
            star_to_define.star_class = 'M1'
        elif star_to_define.effective_temp <= 3800:
            star_to_define.star_class = 'M0'
        elif star_to_define.effective_temp <= 4000:
            star_to_define.star_class = 'K8'
        elif star_to_define.effective_temp <= 4200:
            star_to_define.star_class = 'K6'
        elif star_to_define.effective_temp <= 4400:
            star_to_define.star_class = 'K5'
        elif star_to_define.effective_temp <= 4600:
            star_to_define.star_class = 'K4'
        elif star_to_define.effective_temp <= 4900:
            star_to_define.star_class = 'K2'
        elif star_to_define.effective_temp <= 5200:
            star_to_define.star_class = 'K0'
        elif star_to_define.effective_temp <= 5400:
            star_to_define.star_class = 'G8'
        elif star_to_define.effective_temp <= 5500:
            star_to_define.star_class = 'G6'
        elif star_to_define.effective_temp <= 5700:
            star_to_define.star_class = 'G4'
        elif star_to_define.effective_temp <= 5800:
            star_to_define.star_class = 'G2'
        elif star_to_define.effective_temp <= 5900:
            star_to_define.star_class = 'G1'
        elif star_to_define.effective_temp <= 6000:
            star_to_define.star_class = 'G0'
        elif star_to_define.effective_temp <= 6100:
            star_to_define.star_class = 'F9'
        elif star_to_define.effective_temp <= 6300:
            star_to_define.star_class = 'F8'
        elif star_to_define.effective_temp <= 6400:
            star_to_define.star_class = 'F7'
        elif star_to_define.effective_temp <= 6500:
            star_to_define.star_class = 'F6'
        elif star_to_define.effective_temp <= 6600:
            star_to_define.star_class = 'F5'
        elif star_to_define.effective_temp <= 6700:
            star_to_define.star_class = 'F4'
        elif star_to_define.effective_temp <= 6900:
            star_to_define.star_class = 'F3'
        elif star_to_define.effective_temp <= 7000:
            star_to_define.star_class = 'F2'
        elif star_to_define.effective_temp <= 7300:
            star_to_define.star_class = 'F0'
        elif star_to_define.effective_temp <= 7500:
            star_to_define.star_class = 'A9'
        elif star_to_define.effective_temp <= 7800:
            star_to_define.star_class = 'A7'
        elif star_to_define.effective_temp <= 8000:
            star_to_define.star_class = 'A6'
        else:
            star_to_define.star_class = 'A5'

        star_to_define.radius = round((155000 * math.sqrt(star_to_define.luminosity)/(star_to_define.effective_temp * star_to_define.effective_temp)), 4)
    elif star_to_define.star_sequence == 'Giant Star':
        star_to_define.effective_temp = ((roll_dice(2) - 2) * 200) + 3000
        star_to_define.luminosity = (25 * star_to_define.l_max) * round(random.uniform(0.90, 1.11), 2)
        star_to_define.radius = round((155000 * math.sqrt(star_to_define.luminosity)/(star_to_define.effective_temp * star_to_define.effective_temp)), 4)
    else:
        star_to_define.star_mass = round(((roll_dice(2) - 2) * 0.05) + 0.9, 2)
        star_to_define.luminosity = 0.001
        star_to_define.radius = round(random.uniform(0.0008, 0.0021), 4)

def generate_companion_orbits(star1, starlist, sys_age):
    star1.separation = 'Primary'
    for x in starlist:
        if x.is_companion == True:
            if x.parent_star.is_companion == True:
                roll = roll_dice(3) - 6
            elif starlist.index(x) == 2:
                roll = roll_dice(3) + 6
            else:
                roll = roll_dice(3)
            
            if roll <= 6:
                x.separation = 'Very Close'
                x.orbit_sep_mult = 0.05
            elif roll <= 9:
                x.separation = 'Close'
                x.orbit_sep_mult = 0.5
            elif roll <= 11:
                x.separation = 'Moderate'
                x.orbit_sep_mult = 2.0
            elif roll <= 14:
                x.separation = 'Wide'
                x.orbit_sep_mult = 10.0
            else:
                x.separation = 'Distant'
                x.orbit_sep_mult = 50.0
                if roll_dice(3) >= 11:
                    #this is where distant companion stars having their own companion stars will go.
                    new_star = Star(True, x)
                    new_star.star_age = sys_age
                    if new_star.is_companion == True:
                        roll = roll_dice(1) - 1
                        if roll == 0:
                            new_star.star_mass = x.star_mass
                        else:
                            totRoll = 0
                            for _ in range(roll):
                                totRoll += roll_dice(1)
                            if totRoll > 5:    
                                new_star.star_mass = round(x.star_mass - (5 * 0.1) - ((totRoll - 5) * 0.05), 2)
                            else:
                                new_star.star_mass = round(x.star_mass - (totRoll * 0.1), 2)
                            if new_star.star_mass < 0.10:
                                new_star.star_mass = 0.10
                        classify_spectral_type(new_star)
                        classify_star_sequence(new_star, sys_age)
                        define_stellar_characteristics(new_star, sys_age)
                    x.companions.append(new_star)
                    starlist.append(new_star)
        x.orbit_separation_radius = round(roll_dice(2) * x.orbit_sep_mult, 2)

def check_trinary_orbit_radius(first_companion, second_companion):
    while first_companion.orbit_separation_radius > second_companion.orbit_separation_radius:
        roll = roll_dice(3) + 6
        if roll <= 6:
            second_companion.separation = 'Very Close'
            second_companion.orbit_sep_mult = 0.05
        elif roll <= 9:
            second_companion.separation = 'Close'
            second_companion.orbit_sep_mult = 0.5
        elif roll <= 11:
            second_companion.separation = 'Moderate'
            second_companion.orbit_sep_mult = 2.0
        elif roll <= 14:
            second_companion.separation = 'Wide'
            second_companion.orbit_sep_mult = 10.0
        else:
            second_companion.separation = 'Distant'
            second_companion.orbit_sep_mult = 50.0

        second_companion.orbit_separation_radius = round(roll_dice(2) * second_companion.orbit_sep_mult, 2)

def calculate_orbital_eccentricity(starlist):
    for x in starlist:
        if x.is_companion == True:
            #get roll for star
            if x.separation == 'Very Close':
                roll = roll_dice(3) - 6
            elif x.separation == 'Close':
                roll = roll_dice(3) - 4
            elif x.separation == 'Moderate':
                roll = roll_dice(3) - 2
            else:
                roll = roll_dice(3)
            #find eccentricity
            if roll <= 3:
                x.orbit_eccentricity = 0.0
            elif roll <= 4:
                x.orbit_eccentricity = 0.1
            elif roll <= 5:
                x.orbit_eccentricity = 0.2
            elif roll <= 6:
                x.orbit_eccentricity = 0.3
            elif roll <= 8:
                x.orbit_eccentricity = 0.4
            elif roll <= 11:
                x.orbit_eccentricity = 0.5
            elif roll <= 13:
                x.orbit_eccentricity = 0.6
            elif roll <= 15:
                x.orbit_eccentricity = 0.7
            elif roll <= 16:
                x.orbit_eccentricity = 0.8
            elif roll <= 17:
                x.orbit_eccentricity = 0.9
            else:
                x.orbit_eccentricity = 0.95

            x.min_separation = round((1 - x.orbit_eccentricity) * x.orbit_separation_radius, 2)
            x.max_separation = round((1 + x.orbit_eccentricity) * x.orbit_separation_radius, 2)

def generate_orbital_zones(starlist):
    for x in starlist:
        #closest planets will form
        inner_calc1 = 0.1 * x.star_mass
        inner_calc2 = 0.01 * math.sqrt(x.luminosity)
        if inner_calc1 >= inner_calc2:
            x.inner_limit_radius = round(inner_calc1, 3)
        else:
            x.inner_limit_radius = round(inner_calc2, 3)
        #furthest planets will form
        x.outer_limit_radius = round(40 * x.star_mass, 3)

        #distance where water ice can exist, most likely region of largest gas giant.
        x.snow_line_radius = round(4.85 * math.sqrt(x.l_min), 3)

        
        if x.is_companion == True:
            x.forbidden_zone_min = round(x.min_separation / 3, 2)
            x.forbidden_zone_max = round(x.max_separation * 3, 2)

def generate_gas_giant_arrangement(star, roll=0):
    if roll == 0:
        roll = roll_dice(3)

    if star.star_sequence == 'Brown Dwarf':
        roll -= 4
    
    if (star.snow_line_radius > star.forbidden_zone_min and star.snow_line_radius < star.forbidden_zone_max) or roll <= 10:
        star.gas_giant_arrangement = 'No Gas Giant'
        orbit_radius = 0
    elif roll <= 12:
        star.gas_giant_arrangement = 'Conventional Gas Giant'
        orbit_radius = (((roll_dice(2) - 2) * 0.05) + 1) * star.snow_line_radius
        in_snow = False
    elif roll <= 14:
        star.gas_giant_arrangement = 'Eccentric Gas Giant'
        orbit_radius = roll_dice(1) * 0.125 * star.snow_line_radius
        while orbit_radius < star.inner_limit_radius:
            orbit_radius = roll_dice(1) * 0.125 * star.snow_line_radius
        in_snow = False
    else:
        star.gas_giant_arrangement = 'Epistellar Gas Giant'
        orbit_radius = roll_dice(3) * 0.1 * star.inner_limit_radius
        in_snow = True

    if check_forbidden_zones(orbit_radius, star):
        try:
            generate_gas_giant_arrangement(star, roll)
        except:
            star.gas_giant_arrangement = 'No Gas Giant'
            orbit_radius = 0
    if star.gas_giant_arrangement != 'No Gas Giant':
        star.orbital_spacing.append(orbit_radius)
        temp_giant = GasGiant()
        temp_giant.distance_from_parent = round(orbit_radius, 4)
        temp_giant.size = assign_gas_giant_size(in_snow)
        orbit_tuple = (orbit_radius, temp_giant)
        star.planet_list.append(orbit_tuple)
        
def check_forbidden_zones(orbit, star_to_check):
    if orbit > star_to_check.forbidden_zone_min and orbit < star_to_check.forbidden_zone_max:
        return True
    else:
        return False

def generate_orbital_spacing(star):
    if len(star.orbital_spacing) > 0:
        first_spacing = star.orbital_spacing[0]
    else:
        first_spacing = (roll_dice(1) * 0.05 + 1)/star.outer_limit_radius
        while check_forbidden_zones(first_spacing, star) == True:
            first_spacing = (roll_dice(1) * 0.05 + 1)/star.outer_limit_radius
            if (1.05/star.outer_limit_radius) > star.forbidden_zone_min and (1.3/star.outer_limit_radius) < star.forbidden_zone_max:
                first_spacing = star.forbidden_zone_max 
    
    #sequence down until hit forbidden zone or inner limit
    ratio = pick_orbit_ratio()
    next_spacing = first_spacing / ratio
    while next_spacing >= star.inner_limit_radius:
        if check_forbidden_zones(next_spacing, star):
            break
        else:
            spacing_to_add = round(next_spacing, 3)
            if next_spacing < 0.15:
                spacing_to_add = 0.15
            star.orbital_spacing.append(spacing_to_add)
            ratio = pick_orbit_ratio()
            next_spacing = next_spacing / ratio
    
    #sequence up until hit forbidden zone or outer limit
    ratio = pick_orbit_ratio()
    next_spacing = first_spacing * ratio
    while next_spacing <= star.outer_limit_radius:
        if check_forbidden_zones(next_spacing, star):
            break
        else:
            if next_spacing < 0.15:
                next_spacing = 0.15
            spacing_to_add = round(next_spacing, 3)
            star.orbital_spacing.append(spacing_to_add)
            ratio = pick_orbit_ratio()
            next_spacing = next_spacing * ratio

def pick_orbit_ratio():
    roll = roll_dice(3)
    if roll <= 4:
        ratio = 1.4
    elif roll <= 6:
        ratio = 1.5
    elif roll <= 8:
        ratio = 1.6
    elif roll <= 12:
        ratio = 1.7
    elif roll <= 14:
        ratio = 1.8
    elif roll <= 16:
        ratio = 1.9
    else:
        ratio = 2.0
    
    return ratio

def fill_orbits(star_to_fill):
    #Place Gas Giants
    temp_orbit_list = star_to_fill.orbital_spacing
    if len(temp_orbit_list) > 0:
        temp_orbit_list.pop(0)
    temp_orbit_list.sort()
    if star_to_fill.gas_giant_arrangement == 'Conventional Gas Giant':
        count = 0
        for orbit in star_to_fill.orbital_spacing:
            roll = roll_dice(3)
            if orbit >= star_to_fill.snow_line_radius:
                if check_forbidden_zones(orbit, star_to_fill):
                    if roll <= 15:
                        in_snow = False
                        if temp_orbit_list[count-1] <= star_to_fill.snow_line_radius and orbit >= star_to_fill.snow_line_radius:
                            in_snow = True
                        temp_giant = GasGiant()
                        temp_giant.size = assign_gas_giant_size(in_snow)
                        temp_giant.distance_from_parent = round(orbit, 2)
                        orbit_tuple = (orbit, temp_giant)
                        star_to_fill.planet_list.append(orbit_tuple)
                        temp_orbit_list.pop(count)
            count += 1
    elif star_to_fill.gas_giant_arrangement == 'Eccentric Gas Giant':
        count = 0
        for orbit in star_to_fill.orbital_spacing:
            roll = roll_dice(3)
            if orbit < star_to_fill.snow_line_radius:
                if check_forbidden_zones(orbit, star_to_fill):
                    if roll <= 8:
                        in_snow = True
                        temp_giant = GasGiant()
                        temp_giant.size = assign_gas_giant_size(in_snow)
                        temp_giant.distance_from_parent = round(orbit, 2)
                        orbit_tuple = (orbit, temp_giant)
                        star_to_fill.planet_list.append(orbit_tuple)
                        temp_orbit_list.pop(count)
            elif orbit >= star_to_fill.snow_line_radius:
                if check_forbidden_zones(orbit, star_to_fill):
                    if roll <= 14:
                        in_snow = False
                        if temp_orbit_list[count-1] <= star_to_fill.snow_line_radius and orbit >= star_to_fill.snow_line_radius:
                            in_snow = True
                        temp_giant = GasGiant()
                        temp_giant.size = assign_gas_giant_size(in_snow)
                        temp_giant.distance_from_parent = round(orbit, 2)
                        orbit_tuple = (orbit, temp_giant)
                        star_to_fill.planet_list.append(orbit_tuple)
                        temp_orbit_list.pop(count)
            count += 1
    elif star_to_fill.gas_giant_arrangement == 'Epistellar Gas Giant':
        count = 0
        for orbit in star_to_fill.orbital_spacing:
            roll = roll_dice(3)
            if orbit < star_to_fill.snow_line_radius:
                if check_forbidden_zones(orbit, star_to_fill):
                    if roll <= 6:
                        in_snow = True
                        temp_giant = GasGiant()
                        temp_giant.distance_from_parent = round(orbit, 2)
                        temp_giant.size = assign_gas_giant_size(in_snow)
                        orbit_tuple = (orbit, temp_giant)
                        star_to_fill.planet_list.append(orbit_tuple)
                        temp_orbit_list.pop(count)
            elif orbit >= star_to_fill.snow_line_radius:
                if check_forbidden_zones(orbit, star_to_fill):
                    if roll <= 14:
                        in_snow = False
                        if temp_orbit_list[count-1] <= star_to_fill.snow_line_radius and orbit >= star_to_fill.snow_line_radius:
                            in_snow = True
                        temp_giant = GasGiant()
                        temp_giant.distance_from_parent = round(orbit, 2)
                        temp_giant.size = assign_gas_giant_size(in_snow)
                        orbit_tuple = (orbit, temp_giant)
                        star_to_fill.planet_list.append(orbit_tuple)
                        temp_orbit_list.pop(count)
            count += 1
    
    count = 0
    for orbit in temp_orbit_list:
        roll = roll_dice(3)
        if count == 0:
            roll -= 3
        if count == len(temp_orbit_list) - 1:
            roll -= 3
        if len(star_to_fill.planet_list) > count and count + 1 < len(temp_orbit_list) and temp_orbit_list[count+1] > star_to_fill.planet_list[count][0] and isinstance(star_to_fill.planet_list[count][1], GasGiant):
            roll -= 6
        if len(star_to_fill.planet_list) > count and len(temp_orbit_list) > 1 and temp_orbit_list[count-1] > star_to_fill.planet_list[count][0] and isinstance(star_to_fill.planet_list[count][1], GasGiant):
            roll -= 3
        if count == len(temp_orbit_list) - 1 and orbit < star_to_fill.forbidden_zone_min and star_to_fill.forbidden_zone_min <= star_to_fill.outer_limit_radius:
            roll -= 6
        if count == 0 and orbit > star_to_fill.forbidden_zone_max and star_to_fill.forbidden_zone_max <= star_to_fill.outer_limit_radius:
            roll -=6
        
        if roll <= 3:
            orbit_tuple = (orbit, 'Empty Orbit')
            star_to_fill.planet_list.append(orbit_tuple)
            temp_orbit_list.pop(count)
        elif roll <= 6:
            orbit_tuple = (orbit, 'Asteroid Belt')
            star_to_fill.planet_list.append(orbit_tuple)
            temp_orbit_list.pop(count)
        elif roll <= 8:
            temp_planet = TerrestrialPlanet()
            temp_planet.distance_from_parent = round(orbit, 4)
            temp_planet.size = 'Tiny'
            orbit_tuple = (orbit, temp_planet)
            star_to_fill.planet_list.append(orbit_tuple)
            temp_orbit_list.pop(count)
        elif roll <= 11:
            temp_planet = TerrestrialPlanet()
            temp_planet.distance_from_parent = round(orbit, 4)
            temp_planet.size = 'Small'
            orbit_tuple = (orbit, temp_planet)
            star_to_fill.planet_list.append(orbit_tuple)
            temp_orbit_list.pop(count)
        elif roll <= 15:
            temp_planet = TerrestrialPlanet()
            temp_planet.distance_from_parent = round(orbit, 4)
            temp_planet.size = 'Standard'
            orbit_tuple = (orbit, temp_planet)
            star_to_fill.planet_list.append(orbit_tuple)
            temp_orbit_list.pop(count)
        else:
            temp_planet = TerrestrialPlanet()
            temp_planet.distance_from_parent = round(orbit, 4)
            temp_planet.size = 'Large'
            orbit_tuple = (orbit, temp_planet)
            star_to_fill.planet_list.append(orbit_tuple)
            temp_orbit_list.pop(count)
        count += 1

def assign_gas_giant_size(inside):
    roll = roll_dice(3)
    if inside == True:
        roll += 4
    if roll <= 10:
        return 'Small'
    elif roll <=16:
        return 'Medium'
    else:
        return 'Large'

def generate_moons(star):
    generate_gas_giant_moons(star)
    generate_terrestrial_moons(star)

def generate_terrestrial_moons(star):
    for planet in star.planet_list:
        if isinstance(planet[1],TerrestrialPlanet):
            determine_terrestrial_moons(planet)

def generate_gas_giant_moons(star):
    for planet in star.planet_list:
        if isinstance(planet[1],GasGiant):
            determine_close_moonlets(planet)
            determine_major_moons(planet)
            determine_far_moonlets(planet)

def determine_close_moonlets(planet):
    roll = roll_dice(2)
    if planet[1].distance_from_parent <= 0.1:
        roll -= 10
    elif planet[1].distance_from_parent <= 0.5:
        roll -= 8
    elif planet[1].distance_from_parent <= 0.75:
        roll -= 6
    elif planet[1].distance_from_parent <= 1.5:
        roll -= 3
    
    for _ in range(roll):
        temp_moonlet = Moonlet()
        temp_moonlet.family = 'Close Moonlets'
        temp_moonlet.distance_from_planet = 1
        planet[1].close_moonlets.append(temp_moonlet)
        planet[1].num_close_moonlets += 1

    if len(planet[1].close_moonlets) <= 2:
        planet[1].ring_status = 'Faint'
    if len(planet[1].close_moonlets) <= 6:
        planet[1].ring_status = 'Visible'
    elif len(planet[1].close_moonlets) <= 10:
        planet[1].ring_status = 'Extremely Visible'
    else:
        planet[1].ring_status = 'Nonexistent'            

def determine_major_moons(planet):
    roll = roll_dice(1)
    if planet[1].distance_from_parent <= 0.1:
        roll = 0
    elif planet[1].distance_from_parent <= 0.5:
        roll -= 5
    elif planet[1].distance_from_parent <= 0.75:
        roll -= 4
    elif planet[1].distance_from_parent <= 1.5:
        roll -= 1
    
    for _ in range(roll):
        temp_moon = Moon()
        if isinstance(planet[1], GasGiant):
            temp_moon.size = determine_moon_size('Large')
        else:
            temp_moon.size = determine_moon_size(planet[1].size)
        planet[1].companions.append(temp_moon)
        planet[1].num_moons += 1

def determine_far_moonlets(planet):
    roll = roll_dice(2)
    if planet[1].distance_from_parent <= 0.5:
        roll = 0
    elif planet[1].distance_from_parent <= 0.75:
        roll -= 5
    elif planet[1].distance_from_parent <= 1.5:
        roll -= 4
    elif planet[1].distance_from_parent <= 3:
        roll -= 1
    
    for _ in range(roll):
        temp_moonlet = Moonlet()
        temp_moonlet.family = 'Far Moonlets'
        temp_moonlet.distance_from_planet = 3
        planet[1].far_moonlets.append(temp_moonlet)
        planet[1].num_far_moonlets += 1

def determine_terrestrial_moons(planet):
    roll = roll_dice(1) - 4
    moonlet_roll = roll_dice(1) - 2
    if planet[1].distance_from_parent <= 0.5:
        roll = 0
        moonlet_roll = 0
    elif planet[1].distance_from_parent <= 0.75:
        roll -= 3
        moonlet_roll -= 3
    elif planet[1].distance_from_parent <= 1.5:
        roll -= 1
        moonlet_roll -= 1
    if planet[1].size == 'Tiny':
        roll -= 2
        moonlet_roll -= 2
    elif planet[1].size == 'Small':
        roll -= 1
        moonlet_roll -= 1
    elif planet[1].size == 'Large':
        roll += 1
        moonlet_roll += 1
    
    if roll <= 0:
        for _ in range(moonlet_roll):
            temp_moonlet = Moonlet()
            planet[1].companions.append(temp_moonlet)
            planet[1].num_moons += 1
    else:
        for _ in range(roll):
            temp_moon = Moon()
            temp_moon.size = determine_moon_size(planet[1].size)
            planet[1].companions.append(temp_moon)
            planet[1].num_moons += 1

def determine_moon_size(size):
    size_dict = {
       '-3' : 'Tiny',
       '-2' : 'Tiny',
       '-1' : 'Tiny',
       '0' : 'Tiny',
       '1' : 'Small',
       '2' : 'Standard',
       '3' : 'Large' 
    }

    size_mod = int(list(size_dict.keys())[list(size_dict.values()).index(size)])
    roll = roll_dice(3)
    if roll <= 11:
        size_mod -= 3
    elif roll <= 14:
        size_mod -= 2
    else:
        size_mod -= 1
    
    return size_dict[str(size_mod)]

def determine_blackbody_temperature(star):
    for planet in star.planet_list:
        if isinstance(planet[1], GasGiant) or isinstance(planet[1], TerrestrialPlanet):
            planet[1].blackbody_temperature = round((278 * (math.sqrt(math.sqrt(star.luminosity)) / math.sqrt(planet[1].distance_from_parent))))
            for moon in planet[1].companions:
                if isinstance(moon,Moon):
                    moon.blackbody_temperature = planet[1].blackbody_temperature

def assign_world_types(star):
    for planet in star.planet_list:
        if isinstance(planet[1],TerrestrialPlanet):
            if planet[1].size == 'Tiny':
                if planet[1].blackbody_temperature <= 140:
                    planet[1].world_type = 'Ice'
                    planet[1].complete_world_type = 'Tiny (Ice)'
                else:
                    planet[1].world_type = 'Rock'
                    planet[1].complete_world_type = 'Tiny (Rock)'
            elif planet[1].size == 'Small':
                if planet[1].blackbody_temperature <= 80:
                    planet[1].world_type = 'Hadean'
                    planet[1].complete_world_type = 'Small (Hadean)'
                elif planet[1].blackbody_temperature <= 140:
                    planet[1].world_type = 'Ice'
                    planet[1].complete_world_type = 'Small (Ice)'
                else:
                    planet[1].world_type = 'Rock'
                    planet[1].complete_world_type = 'Small (Rock)'
            elif planet[1].size == 'Standard':
                if planet[1].blackbody_temperature <= 80:
                    planet[1].world_type = 'Hadean'
                    planet[1].complete_world_type = 'Standard (Hadean)'
                elif planet[1].blackbody_temperature <= 150:
                    planet[1].world_type = 'Ice'
                    planet[1].complete_world_type = 'Standard (Ice)'
                elif planet[1].blackbody_temperature <= 230:
                    if star.star_mass <= 0.65:
                        planet[1].world_type = 'Ammonia'
                        planet[1].complete_world_type = 'Standard (Ammonia)'
                    else: 
                        planet[1].world_type = 'Ice'
                        planet[1].complete_world_type = 'Standard (Ice)'
                elif planet[1].blackbody_temperature <= 240:
                    planet[1].world_type = 'Ice'
                    planet[1].complete_world_type = 'Standard (Ice)'
                elif planet[1].blackbody_temperature <= 320:
                    roll = roll_dice(3) + round((star.star_age * 2))
                    if roll >= 18:
                        planet[1].world_type = 'Garden'
                        planet[1].complete_world_type = 'Standard (Garden)'
                    else:
                        planet[1].world_type = 'Ocean'
                        planet[1].complete_world_type = 'Standard (Ocean)'
                elif planet[1].blackbody_temperature <= 500:
                    planet[1].world_type = 'Greenhouse'
                    planet[1].complete_world_type = 'Standard (Greenhouse)' 
                else:
                    planet[1].world_type = 'Chthonian'
                    planet[1].complete_world_type = 'Standard (Chthonian)' 
            elif planet[1].size == 'Large':
                if planet[1].blackbody_temperature <= 150:
                    planet[1].world_type = 'Ice'
                    planet[1].complete_world_type = 'Large (Ice)'
                elif planet[1].blackbody_temperature <= 230:
                    if star.star_mass <= 0.65:
                        planet[1].world_type = 'Ammonia'
                        planet[1].complete_world_type = 'Large (Ammonia)'
                    else: 
                        planet[1].world_type = 'Ice'
                        planet[1].complete_world_type = 'Large (Ice)'
                elif planet[1].blackbody_temperature <= 240:
                    planet[1].world_type = 'Ice'
                    planet[1].complete_world_type = 'Large (Ice)'
                elif planet[1].blackbody_temperature <= 320:
                    roll = roll_dice(3) + round((star.star_age * 2))
                    if roll >= 18:
                        planet[1].world_type = 'Garden'
                        planet[1].complete_world_type = 'Large (Garden)'
                    else:
                        planet[1].world_type = 'Ocean'
                        planet[1].complete_world_type = 'Large (Ocean)'
                elif planet[1].blackbody_temperature <= 500:
                    planet[1].world_type = 'Greenhouse'
                    planet[1].complete_world_type = 'Large (Greenhouse)' 
                else:
                    planet[1].world_type = 'Chthonian'
                    planet[1].complete_world_type = 'Large (Chthonian)'
        if isinstance(planet[1], TerrestrialPlanet) or isinstance(planet[1], GasGiant):
            for moon in planet[1].companions:
                if isinstance(moon,Moon):
                    if moon.size == 'Tiny':
                        if moon.blackbody_temperature <= 140:
                            if isinstance(planet[1],GasGiant):
                                if roll_dice(1) <= 3:
                                    moon.world_type = 'Sulfur'
                                    moon.complete_world_type = 'Tiny (Sulfur)'
                                else:
                                    moon.world_type = 'Ice'
                                    moon.complete_world_type = 'Tiny (Ice)'
                            else:
                                moon.world_type = 'Ice'
                                moon.complete_world_type = 'Tiny (Ice)'
                        else:
                            moon.world_type = 'Rock'
                            moon.complete_world_type = 'Tiny (Rock)'
                    elif moon.size == 'Small':
                        if moon.blackbody_temperature <= 80:
                            moon.world_type = 'Hadean'
                            moon.complete_world_type = 'Small (Hadean)'
                        elif moon.blackbody_temperature <= 140:
                            moon.world_type = 'Ice'
                            moon.complete_world_type = 'Small (Ice)'
                        else:
                            moon.world_type = 'Rock'
                            moon.complete_world_type = 'Small (Rock)'
                    elif moon.size == 'Standard':
                        if moon.blackbody_temperature <= 80:
                            moon.world_type = 'Hadean'
                            moon.complete_world_type = 'Standard (Hadean)'
                        elif moon.blackbody_temperature <= 150:
                            moon.world_type = 'Ice'
                            moon.complete_world_type = 'Standard (Ice)'
                        elif moon.blackbody_temperature <= 230:
                            if star.star_mass <= 0.65:
                                moon.world_type = 'Ammonia'
                                moon.complete_world_type = 'Standard (Ammonia)'
                            else: 
                                moon.world_type = 'Ice'
                                moon.complete_world_type = 'Standard (Ice)'
                        elif moon.blackbody_temperature <= 240:
                            moon.world_type = 'Ice'
                            moon.complete_world_type = 'Standard (Ice)'
                        elif moon.blackbody_temperature <= 320:
                            roll = roll_dice(3) + round((star.star_age * 2))
                            if roll >= 18:
                                moon.world_type = 'Garden'
                                moon.complete_world_type = 'Standard (Garden)'
                            else:
                                moon.world_type = 'Ocean'
                                moon.complete_world_type = 'Standard (Ocean)'
                        elif moon.blackbody_temperature <= 500:
                            moon.world_type = 'Greenhouse'
                            moon.complete_world_type = 'Standard (Greenhouse)' 
                        else:
                            moon.world_type = 'Chthonian'
                            moon.complete_world_type = 'Standard (Chthonian)' 

def determine_atmosphere(star):
    for planet in star.planet_list:
        if isinstance(planet[1], TerrestrialPlanet):
            assign_atmosphere_traits(planet[1])
        if isinstance(planet, TerrestrialPlanet) or isinstance(planet, GasGiant):
            for moon in planet[1].companions:
                if isinstance(moon, Moon):
                    assign_atmosphere_traits(moon)  

def assign_atmosphere_traits(planet):
        
        planet.atmospheric_mass = roll_dice(3) / 10

        if planet.complete_world_type == 'Small (Ice)':
            planet.atmospheric_gases.append('Nitrogen')
            planet.atmospheric_gases.append('Methane')
            if roll_dice(3) <= 15:
                planet.atmospheric_composition.append('Suffocating')
                planet.atmospheric_composition.append('Mildly Toxic')
            else:
                planet.atmospheric_composition.append('Suffocating')
                planet.atmospheric_composition.append('Highly Toxic')
                
        elif planet.complete_world_type == 'Standard (Ammonia)':
            planet.atmospheric_gases.append('Nitrogen')
            planet.atmospheric_gases.append('Abundant Ammonia')
            planet.atmospheric_gases.append('Abundant Methane')
            planet.atmospheric_composition.append('Suffocating')
            planet.atmospheric_composition.append('Lethally Toxic')
            planet.atmospheric_composition.append('Corrosive')

        elif planet.complete_world_type == 'Standard (Ice)':
            planet.atmospheric_gases.append('Nitrogen')
            planet.atmospheric_gases.append('Carbon Dioxide')
            if roll_dice(3) <= 12:
                planet.atmospheric_composition.append('Suffocating')
            else:
                planet.atmospheric_gases.append('Trace Toxic Substances')
                planet.atmospheric_composition.append('Suffocating')
                planet.atmospheric_composition.append('Mildly Toxic')

        elif planet.complete_world_type == 'Standard (Ocean)':
            planet.atmospheric_gases.append('Nitrogen')
            planet.atmospheric_gases.append('Carbon Dioxide')
            if roll_dice(3) <= 12:
                planet.atmospheric_composition.append('Suffocating')
            else:
                planet.atmospheric_gases.append('Trace Toxic Substances')
                planet.atmospheric_composition.append('Suffocating')
                planet.atmospheric_composition.append('Mildly Toxic')

        elif planet.complete_world_type == 'Standard (Garden)':
            planet.atmospheric_gases.append('Predominantly Nitrogen')
            planet.atmospheric_gases.append('Abundant Oxygen')
            if roll_dice(3) <= 11:
                planet.atmospheric_composition.append('No Special Properties')
            else:
                planet.atmospheric_composition.append('Marginal Atmosphere')
                determine_marginal_atmosphere(planet)

        elif planet.complete_world_type == 'Standard (Greenhouse)':
            if random.randrange(1,3) <= 1:
                planet.atmospheric_gases.append('Majority Carbon Dioxide')
                planet.atmospheric_gases.append('Trace Nitrogen')
            else:
                planet.atmospheric_gases.append('Abundant Nitrogen')
                planet.atmospheric_gases.append('Abundent Water Vapour')
                planet.atmospheric_gases.append('Trace Oxygen')
            planet.atmospheric_composition.append('Suffocating')
            planet.atmospheric_composition.append('Lethally Toxic')
            planet.atmospheric_composition.append('Corrosive')

        elif planet.complete_world_type == 'Large (Ammonia)':
            planet.atmospheric_gases.append('Predominantly Helium')
            planet.atmospheric_gases.append('Abundant Ammonia')
            planet.atmospheric_gases.append('Abundant Methane')
            planet.atmospheric_composition.append('Suffocating')
            planet.atmospheric_composition.append('Lethally Toxic')
            planet.atmospheric_composition.append('Corrosive')
        
        elif planet.complete_world_type == 'Large (Ice)':
            planet.atmospheric_gases.append('Abundant Helium')
            planet.atmospheric_gases.append('Abundant Nitrogen')
            if roll_dice(3) <= 13:
                planet.atmospheric_gases.append('Moderate Toxic Substances')
                planet.atmospheric_composition.append('Highly Toxic')
            else:
                planet.atmospheric_gases.append('Trace Toxic Substances')
                planet.atmospheric_composition.append('Mildly Toxic')
            planet.atmospheric_composition.append('Suffocating')
        
        elif planet.complete_world_type == 'Large (Ocean)':
            planet.atmospheric_gases.append('Abundant Helium')
            planet.atmospheric_gases.append('Abundant Nitrogen')
            if roll_dice(3) <= 13:
                planet.atmospheric_gases.append('Moderate Toxic Substances')
                planet.atmospheric_composition.append('Highly Toxic')
            else:
                planet.atmospheric_gases.append('Trace Toxic Substances')
                planet.atmospheric_composition.append('Mildly Toxic')
            planet.atmospheric_composition.append('Suffocating')
        
        elif planet.complete_world_type == 'Large (Garden)':
            planet.atmospheric_gases.append('Abundant Nitrogen')
            planet.atmospheric_gases.append('Abundant Noble Gases')
            planet.atmospheric_gases.append('Significant Oxygen')
            if roll_dice(3) <= 11:
                planet.atmospheric_composition.append('No Special Properties')
            else:
                planet.atmospheric_composition.append('Marginal Atmosphere')
                determine_marginal_atmosphere(planet)
        
        elif planet.complete_world_type == 'Large (Greenhouse)':
            if random.randrange(1,3) <= 1:
                planet.atmospheric_gases.append('Majority Carbon Dioxide')
                planet.atmospheric_gases.append('Trace Nitrogen')
            else:
                planet.atmospheric_gases.append('Abundant Nitrogen')
                planet.atmospheric_gases.append('Abundent Water Vapour')
                planet.atmospheric_gases.append('Trace Oxygen')
            planet.atmospheric_composition.append('Suffocating')
            planet.atmospheric_composition.append('Lethally Toxic')
            planet.atmospheric_composition.append('Corrosive')

def determine_marginal_atmosphere(planet):
    num_traits = 1
    roll = roll_dice(3)
    if roll >= 18:
        num_traits += 2
    elif roll >= 17:
        num_traits += 1
    else:
        num_traits += 0
    
    for _ in range(num_traits):
        roll = roll_dice(3)
        if roll <= 4:
            if roll_dice(3) >= 18:
                planet.atmospheric_gases.append('Significant Fluorine')
                planet.atmospheric_composition.append('Highly Toxic')
            else:
                planet.atmospheric_gases.append('Significant Chlorine')
                planet.atmospheric_composition.append('Highly Toxic')
        elif roll <= 6:
            planet.atmospheric_gases.append('Significant Sulfur Compounds')
            planet.atmospheric_composition.append('Mildly Toxic')
        elif roll <= 7:
            planet.atmospheric_gases.append('Significant Nitrogen Compounds')
            planet.atmospheric_composition.append('Mildly Toxic')
        elif roll <= 9:
            planet.atmospheric_gases.append('Significant Organic Toxins')
            roll = roll_dice(3)
            if roll <= 14:
                planet.atmospheric_composition.append('Mildly Toxic')
            elif roll <= 17:
                planet.atmospheric_composition.append('Highly Toxic')
            else:
                planet.atmospheric_composition.append('Lethally Toxic')
        elif roll <= 11:
            planet.atmospheric_composition.append('Low Oxygen Environment')
        elif roll <= 13:
            planet.atmospheric_gases.append('Significant Non-Organic Pollutants')
            planet.atmospheric_composition.append('Mildly Toxic')
        elif roll <= 14:
            planet.atmospheric_gases.append('Significant Carbon Dioxide')
            planet.atmospheric_composition.append('Mildly Toxic')
        elif roll <= 16:
            planet.atmospheric_gases.append('High Oxygen Environment')
            planet.atmospheric_composition.append('Mildly Toxic')
            planet.atmospheric_composition.append('Increased Flammability')
        else:
            planet.atmospheric_gases.append('Significant Inert Gases')
            planet.atmospheric_composition.append('Inert Gas Narcosis')

def determine_hydrographic_coverage(star):
    for planet_tup in star.planet_list:
        if isinstance(planet_tup[1], TerrestrialPlanet):
            planet = planet_tup[1]
            if (
            planet.complete_world_type == 'Tiny (Ice)' or
            planet.complete_world_type == 'Tiny (Rock)' or
            planet.complete_world_type == 'Tiny (Sulfur)' or
            planet.complete_world_type == 'Small (Hadean)' or
            planet.complete_world_type == 'Small (Rock)' or
            planet.complete_world_type == 'Standard (Hadean)' or
            planet.complete_world_type == 'Standard (Chthonian)' or
            planet.complete_world_type == 'Large (Chthonian)'
            ):
                planet.hydrographic_coverage_percent = 0
            else:
                if planet.complete_world_type == 'Small (Ice)':
                    planet.hydrographic_coverage_percent = (roll_dice(1) * 10) + random.randrange(-5, 5)

                elif planet.world_type == 'Ammonia':
                    planet.hydrographic_coverage_percent = (roll_dice(2) * 10) + random.randrange(-5, 5)
                    if planet.hydrographic_coverage_percent > 100:
                        planet.hydrographic_coverage_percent = 100

                elif planet.world_type == 'Ice':
                    planet.hydrographic_coverage_percent = ((roll_dice(2) - 10) * 10) + random.randrange(-5, 5)
                    if planet.hydrographic_coverage_percent < 0:
                        planet.hydrographic_coverage_percent = 0

                elif planet.world_type == 'Ocean':
                    if planet.size == 'Large':
                        roll = roll_dice(1) + 7
                    else:
                        roll = roll_dice(1) + 6
                    planet.hydrographic_coverage_percent = roll * 10 + random.randrange(-5, 5)
                    if planet.hydrographic_coverage_percent > 100:
                        planet.hydrographic_coverage_percent = 100
                
                elif planet.world_type == 'Garden':
                    if planet.size == 'Large':
                        roll = roll_dice(1) + 5
                    else:
                        roll = roll_dice(1) + 4
                    planet.hydrographic_coverage_percent = roll * 10 + random.randrange(-5, 5)
                    if planet.hydrographic_coverage_percent > 100:
                        planet.hydrographic_coverage_percent = 100

                elif planet.world_type == 'Greenhouse':
                    planet.hydrographic_coverage_percent = ((roll_dice(2) - 7) * 10) + random.randrange(-5, 5)
                    if planet.hydrographic_coverage_percent < 0:
                        planet.hydrographic_coverage_percent = 0

def determine_climate(star):
    temp_fact_dict = {
        'Asteroid Belt' : (0.97, 0),
        'Tiny (Ice)' : (0.86, 0),
        'Tiny (Rock)' : (0.97, 0),
        'Tiny (Sulfur)' : (0.77, 0),
        'Small (Hadean)' : (0.67, 0),
        'Small (Ice)' : (0.93, 0.10),
        'Small (Rock)' : (0.96, 0),
        'Standard (Hadean)' : (0.67, 0),
        'Standard (Ammonia)' : (0.84, 0.20),
        'Large (Ammonia)' : (0.84, 0.20),
        'Standard (Ice)' : (0.86, 0.20),
        'Large (Ice)' : (0.86, 0.20),
        'Standard (Greenhouse)' : (0.77, 2.0),
        'Large (Greenhouse)' : (0.77, 2.0),
        'Standard (Chthonian)' : (0.97, 0),
        'Large (Chthonian)' : (0.97, 0)
    }

    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        absorption_factor = 0
        greenhouse_factor = 0
        if planet == 'Asteroid Belt':
            factor_tup = temp_fact_dict['Asteroid Belt']
            absorption_factor = factor_tup[0]
            greenhouse_factor = factor_tup[1]
            continue
        elif planet == 'Empty Orbit':
            absorption_factor = 0
            greenhouse_factor = 0
            continue
        else:
            if isinstance(planet, TerrestrialPlanet):
                if (planet.world_type == 'Ocean' or planet.world_type == 'Garden') and planet.hydrographic_coverage_percent <= 20:
                    absorption_factor = 0.95
                    greenhouse_factor = 0.16
                elif (planet.world_type == 'Ocean' or planet.world_type == 'Garden') and planet.hydrographic_coverage_percent <= 50:
                    absorption_factor = 0.92
                    greenhouse_factor = 0.16
                elif (planet.world_type == 'Ocean' or planet.world_type == 'Garden') and planet.hydrographic_coverage_percent <= 90:
                    absorption_factor = 0.88
                    greenhouse_factor = 0.16
                elif (planet.world_type == 'Ocean' or planet.world_type == 'Garden') and planet.hydrographic_coverage_percent <= 100:
                    absorption_factor = 0.84
                    greenhouse_factor = 0.16
                else:
                    factor_tup = temp_fact_dict[planet.complete_world_type]
                    absorption_factor = factor_tup[0]
                    greenhouse_factor = factor_tup[1]

                greenhouse_factor += random.randrange(-5,6) * 0.01
                absorption_factor += random.randrange(-5,6) * 0.01
                if greenhouse_factor <= 0:
                    greenhouse_factor = 0
                if greenhouse_factor >= 1:
                    greenhouse_factor = 1
                if absorption_factor <= 0:
                    absorption_factor = 0
                if absorption_factor >= 1:
                    absorption_factor = 1
                planet.blackbody_correction = absorption_factor * (1 + (planet.atmospheric_mass * greenhouse_factor))
                planet.surface_temperature = round(planet.blackbody_correction * planet.blackbody_temperature)
                planet.blackbody_correction = round(planet.blackbody_correction, 2)

                if planet.complete_world_type == 'Tiny (Ice)' or planet.complete_world_type == 'Tiny (Sulfur)':
                    if planet.surface_temperature > 140:
                        planet.surface_temperature = 140
                elif planet.complete_world_type == 'Tiny (Rock)':
                    if planet.surface_temperature < 140:
                        planet.surface_temperature = 140
                elif planet.complete_world_type == 'Small (Hadean)':
                    if planet.surface_temperature < 50:
                        planet.surface_temperature = 50
                    elif planet.surface_temperature > 80:
                        planet.surface_temperature = 80
                elif planet.complete_world_type == 'Small (Ice)':
                    if planet.surface_temperature < 80:
                        planet.surface_temperature = 80
                    elif planet.surface_temperature > 140:
                        planet.surface_temperature = 140
                elif planet.complete_world_type == 'Small (Rock)':
                    if planet.surface_temperature < 140:
                        planet.surface_temperature = 140
                elif planet.complete_world_type == 'Standard (Hadean)':
                    if planet.surface_temperature < 50:
                        planet.surface_temperature = 50
                    elif planet.surface_temperature > 80:
                        planet.surface_temperature = 80
                elif planet.complete_world_type == 'Standard (Ammonia)':
                    if planet.surface_temperature < 140:
                        planet.surface_temperature = 140
                    elif planet.surface_temperature > 215:
                        planet.surface_temperature = 215
                elif planet.complete_world_type == 'Standard (Ice)':
                    if planet.surface_temperature < 80:
                        planet.surface_temperature = 80
                    elif planet.surface_temperature > 230:
                        planet.surface_temperature = 230
                elif planet.complete_world_type == 'Standard (Ocean)' or planet.complete_world_type == 'Standard (Garden)':
                    if planet.surface_temperature < 250:
                        planet.surface_temperature = 250
                    elif planet.surface_temperature > 340:
                        planet.surface_temperature = 340
                elif planet.complete_world_type == 'Standard (Greenhouse)' or planet.complete_world_type == 'Standard (Chthonian)':
                    if planet.surface_temperature < 500:
                        planet.surface_temperature = 500
                elif planet.complete_world_type == 'Large (Ammonia)':
                    if planet.surface_temperature < 140:
                        planet.surface_temperature = 140
                    elif planet.surface_temperature > 215:
                        planet.surface_temperature = 215
                elif planet.complete_world_type == 'Large (Ice)':
                    if planet.surface_temperature < 80:
                        planet.surface_temperature = 80
                    elif planet.surface_temperature > 230:
                        planet.surface_temperature = 230
                elif planet.complete_world_type == 'Large (Ocean)' or planet.complete_world_type == 'Large (Garden)':
                    if planet.surface_temperature < 250:
                        planet.surface_temperature = 250
                    elif planet.surface_temperature > 340:
                        planet.surface_temperature = 340
                elif planet.complete_world_type == 'Large (Greenhouse)' or planet.complete_world_type == 'Large (Chthonian)':
                    if planet.surface_temperature < 500:
                        planet.surface_temperature = 500

            if planet.surface_temperature <= 244:
                planet.climate_type = 'Frozen'
            elif planet.surface_temperature <= 255:
                planet.climate_type = 'Very Cold'
            elif planet.surface_temperature <= 266:
                planet.climate_type = 'Cold'
            elif planet.surface_temperature <= 278:
                planet.climate_type = 'Chilly'
            elif planet.surface_temperature <= 289:
                planet.climate_type = 'Cool'
            elif planet.surface_temperature <= 300:
                planet.climate_type = 'Normal'
            elif planet.surface_temperature <= 311:
                planet.climate_type = 'Warm'
            elif planet.surface_temperature <= 322:
                planet.climate_type = 'Tropical'
            elif planet.surface_temperature <= 333:
                planet.climate_type = 'Hot'
            elif planet.surface_temperature <= 344:
                planet.climate_type = 'Very Hot'
            elif planet.surface_temperature > 344:
                planet.climate_type = 'Infernal'
        for moon in planet.companions:
            if isinstance(moon, Moonlet):
                continue
            if (moon.world_type == 'Ocean' or moon.world_type == 'Garden') and moon.hydrographic_coverage_percent <= 20:
                absorption_factor = 0.95
                greenhouse_factor = 0.16
            elif (moon.world_type == 'Ocean' or moon.world_type == 'Garden') and moon.hydrographic_coverage_percent <= 50:
                absorption_factor = 0.92
                greenhouse_factor = 0.16
            elif (moon.world_type == 'Ocean' or moon.world_type == 'Garden') and moon.hydrographic_coverage_percent <= 90:
                absorption_factor = 0.88
                greenhouse_factor = 0.16
            elif (moon.world_type == 'Ocean' or moon.world_type == 'Garden') and moon.hydrographic_coverage_percent <= 100:
                absorption_factor = 0.84
                greenhouse_factor = 0.16
            else:
                factor_tup = temp_fact_dict[moon.complete_world_type]
                absorption_factor = factor_tup[0]
                greenhouse_factor = factor_tup[1]

            greenhouse_factor += random.randrange(-5,6) * 0.01
            absorption_factor += random.randrange(-5,6) * 0.01
            if greenhouse_factor <= 0:
                greenhouse_factor = 0
            if greenhouse_factor >= 1:
                greenhouse_factor = 1
            if absorption_factor <= 0:
                absorption_factor = 0
            if absorption_factor >= 1:
                absorption_factor = 1
            moon.blackbody_correction = absorption_factor * (1 + (moon.atmospheric_mass * greenhouse_factor))
            moon.surface_temperature = round(moon.blackbody_correction * moon.blackbody_temperature)

            if moon.complete_world_type == 'Tiny (Ice)' or moon.complete_world_type == 'Tiny (Sulfur)':
                if moon.surface_temperature > 140:
                    moon.surface_temperature = 140
            elif moon.complete_world_type == 'Tiny (Rock)':
                if moon.surface_temperature < 140:
                    moon.surface_temperature = 140
            elif moon.complete_world_type == 'Small (Hadean)':
                if moon.surface_temperature < 50:
                    moon.surface_temperature = 50
                elif moon.surface_temperature > 80:
                    moon.surface_temperature = 80
            elif moon.complete_world_type == 'Small (Ice)':
                if moon.surface_temperature < 80:
                    moon.surface_temperature = 80
                elif moon.surface_temperature > 140:
                    moon.surface_temperature = 140
            elif moon.complete_world_type == 'Small (Rock)':
                if moon.surface_temperature < 140:
                    moon.surface_temperature = 140
            elif moon.complete_world_type == 'Standard (Hadean)':
                if moon.surface_temperature < 50:
                    moon.surface_temperature = 50
                elif moon.surface_temperature > 80:
                    moon.surface_temperature = 80
            elif moon.complete_world_type == 'Standard (Ammonia)':
                if moon.surface_temperature < 140:
                    moon.surface_temperature = 140
                elif moon.surface_temperature > 215:
                    moon.surface_temperature = 215
            elif moon.complete_world_type == 'Standard (Ice)':
                if moon.surface_temperature < 80:
                    moon.surface_temperature = 80
                elif moon.surface_temperature > 230:
                    moon.surface_temperature = 230
            elif moon.complete_world_type == 'Standard (Ocean)' or moon.complete_world_type == 'Standard (Garden)':
                if moon.surface_temperature < 250:
                    moon.surface_temperature = 250
                elif moon.surface_temperature > 340:
                    moon.surface_temperature = 340
            elif moon.complete_world_type == 'Standard (Greenhouse)' or moon.complete_world_type == 'Standard (Chthonian)':
                if moon.surface_temperature < 500:
                    moon.surface_temperature = 500
            elif moon.complete_world_type == 'Large (Ammonia)':
                if moon.surface_temperature < 140:
                    moon.surface_temperature = 140
                elif moon.surface_temperature > 215:
                    moon.surface_temperature = 215
            elif moon.complete_world_type == 'Large (Ice)':
                if moon.surface_temperature < 80:
                    moon.surface_temperature = 80
                elif moon.surface_temperature > 230:
                    moon.surface_temperature = 230
            elif moon.complete_world_type == 'Large (Ocean)' or moon.complete_world_type == 'Large (Garden)':
                if moon.surface_temperature < 250:
                    moon.surface_temperature = 250
                elif moon.surface_temperature > 340:
                    moon.surface_temperature = 340
            elif moon.complete_world_type == 'Large (Greenhouse)' or moon.complete_world_type == 'Large (Chthonian)':
                if moon.surface_temperature < 500:
                    moon.surface_temperature = 500

            if moon.surface_temperature <= 244:
                moon.climate_type = 'Frozen'
            elif moon.surface_temperature <= 255:
                moon.climate_type = 'Very Cold'
            elif moon.surface_temperature <= 266:
                moon.climate_type = 'Cold'
            elif moon.surface_temperature <= 278:
                moon.climate_type = 'Chilly'
            elif moon.surface_temperature <= 289:
                moon.climate_type = 'Cool'
            elif moon.surface_temperature <= 300:
                moon.climate_type = 'Normal'
            elif moon.surface_temperature <= 311:
                moon.climate_type = 'Warm'
            elif moon.surface_temperature <= 322:
                moon.climate_type = 'Tropical'
            elif moon.surface_temperature <= 333:
                moon.climate_type = 'Hot'
            elif moon.surface_temperature <= 344:
                moon.climate_type = 'Very Hot'
            elif moon.surface_temperature > 344:
                moon.climate_type = 'Infernal'

def determine_world_size(star):

    size_const_dict = {
        'Large' : (0.065, 0.091),
        'Standard' : (0.030, 0.065),
        'Small' : (0.024, 0.030),
        'Tiny' : (0.009, 0.024)
    }


    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if isinstance (planet, str):
            continue
        if isinstance(planet, GasGiant):
            roll = roll_dice(3)
            if roll <= 8:
                if planet.size == 'Small':
                    planet.world_mass = 10
                    planet.world_density = 0.42 
                elif planet.size == 'Medium':
                    planet.world_mass = 100
                    planet.world_density = 0.18
                elif planet.size == 'Large':
                    planet.world_mass = 600
                    planet.world_density = 0.31
            elif roll <= 10:
                    if planet.size == 'Small':
                        planet.world_mass = 15
                        planet.world_density = 0.26
                    elif planet.size == 'Medium':
                        planet.world_mass = 150
                        planet.world_density = 0.19
                    elif planet.size == 'Large':
                        planet.world_mass = 800
                        planet.world_density = 0.35
            elif roll <= 11:
                    if planet.size == 'Small':
                        planet.world_mass = 20
                        planet.world_density = 0.22
                    elif planet.size == 'Medium':
                        planet.world_mass = 200
                        planet.world_density = 0.20
                    elif planet.size == 'Large':
                        planet.world_mass = 1000
                        planet.world_density = 0.4
            elif roll <= 12:
                    if planet.size == 'Small':
                        planet.world_mass = 30
                        planet.world_density = 0.19
                    elif planet.size == 'Medium':
                        planet.world_mass = 250
                        planet.world_density = 0.22
                    elif planet.size == 'Large':
                        planet.world_mass = 1500
                        planet.world_density = 0.6
            elif roll <= 13:
                    if planet.size == 'Small':
                        planet.world_mass = 40
                        planet.world_density = 0.17 
                    elif planet.size == 'Medium':
                        planet.world_mass = 300
                        planet.world_density = 0.24
                    elif planet.size == 'Large':
                        planet.world_mass = 2000
                        planet.world_density = 0.8
            elif roll <= 14:
                    if planet.size == 'Small':
                        planet.world_mass = 50
                        planet.world_density = 0.17
                    elif planet.size == 'Medium':
                        planet.world_mass = 350
                        planet.world_density = 0.25
                    elif planet.size == 'Large':
                        planet.world_mass = 2500
                        planet.world_density = 1.0
            elif roll <= 15:
                    if planet.size == 'Small':
                        planet.world_mass = 60
                        planet.world_density = 0.17
                    elif planet.size == 'Medium':
                        planet.world_mass = 400
                        planet.world_density = 0.26
                    elif planet.size == 'Large':
                        planet.world_mass = 3000
                        planet.world_density = 1.2
            elif roll <= 16:
                    if planet.size == 'Small':
                        planet.world_mass = 70
                        planet.world_density = 0.17
                    elif planet.size == 'Medium':
                        planet.world_mass = 450
                        planet.world_density = 0.27
                    elif planet.size == 'Large':
                        planet.world_mass = 3500
                        planet.world_density = 1.4
            else:
                    if planet.size == 'Small':
                        planet.world_mass = 80
                        planet.world_density = 0.17
                    elif planet.size == 'Medium':
                        planet.world_mass = 500
                        planet.world_density = 0.29
                    elif planet.size == 'Large':
                        planet.world_mass = 4000
                        planet.world_density = 1.6
        
            planet.world_diameter = round((planet.world_mass/planet.world_density)**(1.0/3.0), 3)
            planet.cloud_top_gravity = round(planet.world_diameter * planet.world_density, 3)
                    
        elif isinstance(planet, TerrestrialPlanet):
            if (
                planet.complete_world_type == 'Tiny (Ice)' or
                planet.complete_world_type == 'Tiny (Sulfur)' or
                planet.complete_world_type == 'Small (Hadean)' or
                planet.complete_world_type == 'Small (Ice)' or
                planet.complete_world_type == 'Standard (Hadean)' or
                planet.complete_world_type == 'Standard (Ammonia)' or
                planet.complete_world_type == 'Large(Ammonia)'
            ):
                planet.core_type = 'Icy Core'
                roll = roll_dice(3)
                if roll <= 6:
                    planet.world_density = 0.3
                elif roll <= 10:
                    planet.world_density = 0.4
                elif roll <= 14:
                    planet.world_density = 0.5
                elif roll <= 17:
                    planet.world_density = 0.6
                else:
                    planet.world_density = 0.7
            elif planet.complete_world_type == 'Tiny (Rock)' or planet.complete_world_type == 'Small (Rock)':
                planet.core_type = 'Small Iron Core'
                roll = roll_dice(3)
                if roll <= 6:
                    planet.world_density = 0.6
                elif roll <= 10:
                    planet.world_density = 0.7
                elif roll <= 14:
                    planet.world_density = 0.8
                elif roll <= 17:
                    planet.world_density = 0.9
                else:
                    planet.world_density = 1.0
            else:
                planet.core_type = 'Large Iron Core'
                roll = roll_dice(3)
                if roll <= 6:
                    planet.world_density = 0.8
                elif roll <= 10:
                    planet.world_density = 0.9
                elif roll <= 14:
                    planet.world_density = 1.0
                elif roll <= 17:
                    planet.world_density = 1.1
                else:
                    planet.world_density = 1.2

            planet.world_density += random.randrange(-5,6) * 0.01
            planet.world_density = round(planet.world_density, 3)
            constraint_tup = size_const_dict[planet.size]
            min_diameter = math.sqrt(planet.blackbody_temperature/planet.world_density) * constraint_tup[0]
            max_diameter = math.sqrt(planet.blackbody_temperature/planet.world_density) * constraint_tup[1]
            diam_roll = roll_dice(2) + 2
            if diam_roll >= 6:
                diam_roll = 5 + roll_dice(1) - 1
            else:
                diam_roll = 5 - roll_dice(1) + 1
            diameter = min_diameter + (diam_roll * (0.1 * (max_diameter - min_diameter)))
            diameter += random.randrange(-5,6) * 0.01 * diameter
            planet.world_diameter = round(diameter, 3)
            planet.surface_gravity = round(diameter * planet.world_density, 3)
            planet.world_mass = round(planet.world_density * (planet.world_diameter ** 3), 5)

        for moon in planet.companions:
            if isinstance(moon, Moonlet):
                continue
            if (
                moon.complete_world_type == 'Tiny (Ice)' or
                moon.complete_world_type == 'Tiny (Sulfur)' or
                moon.complete_world_type == 'Small (Hadean)' or
                moon.complete_world_type == 'Small (Ice)' or
                moon.complete_world_type == 'Standard (Hadean)' or
                moon.complete_world_type == 'Standard (Ammonia)' or
                moon.complete_world_type == 'Large(Ammonia)'
            ):
                moon.core_type = 'Icy Core'
                roll = roll_dice(3)
                if roll <= 6:
                    moon.world_density = 0.3
                elif roll <= 10:
                    moon.world_density = 0.4
                elif roll <= 14:
                    moon.world_density = 0.5
                elif roll <= 17:
                    moon.world_density = 0.6
                else:
                    moon.world_density = 0.7
            elif moon.complete_world_type == 'Tiny (Rock)' or moon.complete_world_type == 'Small (Rock)':
                moon.core_type = 'Small Iron Core'
                roll = roll_dice(3)
                if roll <= 6:
                    moon.world_density = 0.6
                elif roll <= 10:
                    moon.world_density = 0.7
                elif roll <= 14:
                    moon.world_density = 0.8
                elif roll <= 17:
                    moon.world_density = 0.9
                else:
                    moon.world_density = 1.0
            else:
                moon.core_type = 'Large Iron Core'
                roll = roll_dice(3)
                if roll <= 6:
                    moon.world_density = 0.8
                elif roll <= 10:
                    moon.world_density = 0.9
                elif roll <= 14:
                    moon.world_density = 1.0
                elif roll <= 17:
                    moon.world_density = 1.1
                else:
                    moon.world_density = 1.2

            moon.world_density += random.randrange(-5,6) * 0.01
            moon.world_density = round(moon.world_density, 3)
            constraint_tup = size_const_dict[moon.size]
            min_diameter = math.sqrt(moon.blackbody_temperature/moon.world_density) * constraint_tup[0]
            max_diameter = math.sqrt(moon.blackbody_temperature/moon.world_density) * constraint_tup[1]
            diameter = min_diameter + ((roll_dice(2) - 2) * (0.1 * (max_diameter - min_diameter)))
            diameter += random.randrange(-5,6) * 0.01 * diameter
            moon.world_diameter = round(diameter, 4)
            moon.surface_gravity = round(diameter * moon.world_density, 4)
            moon.world_mass = round(moon.world_density * (moon.world_diameter ** 3), 5)
            
def determine_surface_atmospheric_pressure(star):
    
    atm_dict = {
        'Small (Ice)' : 10,
        'Standard (Ammonia)' : 1,
        'Standard (Ice)' : 1,
        'Standard (Ocean)' : 1,
        'Standard (Garden)' : 1,
        'Standard (Greenhouse)' : 100,
        'Large (Ammonia)' : 5,
        'Large (Ice)' : 5,
        'Large (Ocean)' : 5,
        'Large (Garden)' : 5,
        'Large (Greenhouse)' : 500,
        'Small' : 1,
        'Medium' : 2,
        'Large' : 5
    }

    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if isinstance(planet, str):
            continue
        if isinstance(planet, TerrestrialPlanet):
            if (
            planet.complete_world_type == 'Tiny (Ice)' or
            planet.complete_world_type == 'Tiny (Rock)' or
            planet.complete_world_type == 'Tiny (Sulfur)' or
            planet.complete_world_type == 'Small (Hadean)' or
            planet.complete_world_type == 'Small (Rock)' or
            planet.complete_world_type == 'Standard (Hadean)' or
            planet.complete_world_type == 'Standard (Chthonian)' or
            planet.complete_world_type == 'Large (Chthonian)'
            ):
                planet.atmospheric_pressure = 0.0
            else:
                planet.atmospheric_pressure = planet.atmospheric_mass * planet.surface_gravity * atm_dict[planet.complete_world_type]
        elif isinstance(planet, GasGiant):
            planet.atmospheric_pressure = planet.atmospheric_mass * planet.surface_gravity * atm_dict[planet.size]

        if planet.atmospheric_pressure == 0:
            planet.pressure_category = 'Nonexistent Atmosphere'
            planet.atmospheric_mass = 0.0
            planet.atmospheric_composition.append('Nonexistent Atmosphere')
        elif planet.atmospheric_pressure <= 0.01:
            planet.pressure_category = 'Trace Atmosphere'
        elif planet.atmospheric_pressure <= 0.5:
            planet.pressure_category = 'Very Thin Atmosphere'
        elif planet.atmospheric_pressure <= 0.8:
            planet.pressure_category = 'Thin Atmosphere'
        elif planet.atmospheric_pressure <= 1.2:
            planet.pressure_category = 'Standard Atmosphere'
        elif planet.atmospheric_pressure <= 1.5:
            planet.pressure_category = 'Dense Atmosphere'
        elif planet.atmospheric_pressure <= 10:
            planet.pressure_category = 'Very Dense Atmosphere'
        else:
            planet.pressure_category = 'Superdense Atmosphere'

        for moon in planet.companions:
            if isinstance(moon, Moonlet):
                continue
            
            if (
            moon.complete_world_type == 'Tiny (Ice)' or
            moon.complete_world_type == 'Tiny (Rock)' or
            moon.complete_world_type == 'Tiny (Sulfur)' or
            moon.complete_world_type == 'Small (Hadean)' or
            moon.complete_world_type == 'Small (Rock)' or
            moon.complete_world_type == 'Standard (Hadean)' or
            moon.complete_world_type == 'Standard (Chthonian)' or
            moon.complete_world_type == 'Large (Chthonian)'
            ):
                moon.atmospheric_pressure = 0.0
            else:
                moon.atmospheric_pressure = moon.atmospheric_mass * moon.surface_gravity * atm_dict[moon.complete_world_type]

            if moon.atmospheric_pressure == 0:
                moon.pressure_category = 'Nonexistent Atmosphere'
                moon.atmospheric_mass = 0.0
                moon.atmospheric_composition.append('Nonexistent Atmosphere')
            elif moon.atmospheric_pressure <= 0.01:
                moon.pressure_category = 'Trace Atmosphere'
            elif moon.atmospheric_pressure <= 0.5:
                moon.pressure_category = 'Very Thin Atmosphere'
            elif moon.atmospheric_pressure <= 0.8:
                moon.pressure_category = 'Thin Atmosphere'
            elif moon.atmospheric_pressure <= 1.2:
                moon.pressure_category = 'Standard Atmosphere'
            elif moon.atmospheric_pressure <= 1.5:
                moon.pressure_category = 'Dense Atmosphere'
            elif moon.atmospheric_pressure <= 10:
                moon.pressure_category = 'Very Dense Atmosphere'
            else:
                moon.pressure_category = 'Superdense Atmosphere'
            
            if (
                moon.complete_world_type == 'Small (Rock)' or
                moon.complete_world_type == 'Standard (Chthonian)' or
                moon.complete_world_type == 'Large (Chthonian)'
            ):
                moon.pressure_category = 'Trace Atmosphere'


        if isinstance(planet, GasGiant):
            continue
        if (
                planet.complete_world_type == 'Small (Rock)' or
                planet.complete_world_type == 'Standard (Chthonian)' or
                planet.complete_world_type == 'Large (Chthonian)'
            ):
                planet.pressure_category = 'Trace Atmosphere'

def generate_stellar_orbital_period(starlist, system_type):
    if system_type == 'Binary':
        period = math.sqrt((starlist[1].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass))
        for star in starlist:
            star.orbital_period = round(period, 3)
    elif system_type == 'Trinary':
        ab_period = math.sqrt((starlist[1].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass))
        starlist[0].orbital_period = round(ab_period, 3)
        starlist[1].orbital_period = round(ab_period, 3)
        c_period = math.sqrt((starlist[2].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass + starlist[2].star_mass))
        starlist[2].orbital_period = round(c_period, 3)
    elif system_type == 'Quaternary':
        if len(starlist[1].companions) > 0:
            bd_period = math.sqrt((starlist[3].orbit_separation_radius ** 3)/(starlist[1].star_mass + starlist[3].star_mass))
            starlist[3].orbital_period = round(bd_period, 2)
        elif len(starlist[2].companions) > 0:
            cd_period = period = math.sqrt((starlist[3].orbit_separation_radius ** 3)/(starlist[2].star_mass + starlist[3].star_mass))
            starlist[3].orbital_period = round(cd_period, 3)
        ab_period = math.sqrt((starlist[1].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass))
        starlist[0].orbital_period = round(ab_period, 3)
        starlist[1].orbital_period = round(ab_period, 3)
        c_period = math.sqrt((starlist[2].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass + starlist[2].star_mass))
        starlist[2].orbital_period = round(c_period, 3)
    elif system_type == 'Quinary':
        bd_period = math.sqrt((starlist[3].orbit_separation_radius ** 3)/(starlist[1].star_mass + starlist[3].star_mass))
        starlist[3].orbital_period = round(bd_period, 3)
        cd_period = period = math.sqrt((starlist[4].orbit_separation_radius ** 3)/(starlist[2].star_mass + starlist[4].star_mass))
        starlist[4].orbital_period = round(cd_period, 3)
        ab_period = math.sqrt((starlist[1].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass))
        starlist[0].orbital_period = round(ab_period, 3)
        starlist[1].orbital_period = round(ab_period, 3)
        c_period = math.sqrt((starlist[2].orbit_separation_radius ** 3)/(starlist[0].star_mass + starlist[1].star_mass + starlist[2].star_mass))
        starlist[2].orbital_period = round(c_period, 3)

def generate_planet_dynamic_parameters(star):
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        #set up for later
        if isinstance(planet, str):
            continue
        else:
            #orbital period
            planet.orbital_period = round(math.sqrt((planet.distance_from_parent ** 3) / (star.star_mass + (planet.world_mass * 0.000003))), 3)
        
        #orbit eccentricity
        roll = roll_dice(3)
        if star.gas_giant_arrangement == 'Eccentric Gas Giant' and planet.distance_from_parent <= star.snow_line_radius:
            roll += 4
        if star.gas_giant_arrangement == 'Epistellar Gas Giant' and star.planet_list[0] == planet:
            roll -= 6
        if star.gas_giant_arrangement == 'Conventional Gas Giant':
            roll -= 6
        
        if roll <= 3:
            planet.eccentricity = 0
        elif roll <= 6:
            planet.eccentricity = 0.05
        elif roll <= 9:
            planet.eccentricity = 0.1
        elif roll <= 11:
            planet.eccentricity = 0.15
        elif roll <= 12:
            planet.eccentricity = 0.2
        elif roll <= 13:
            planet.eccentricity = 0.3
        elif roll <= 14:
            planet.eccentricity = 0.4
        elif roll <= 15:
            planet.eccentricity = 0.5
        elif roll <= 16:
            planet.eccentricity = 0.6
        elif roll <= 17:
            planet.eccentricity = 0.7
        else:
            planet.eccentricity = 0.8
        
        

        #furthest and closest point of separation from star
        planet.min_separation = round((1 - planet.eccentricity) * planet.distance_from_parent, 2)
        planet.max_separation = round((1 + planet.eccentricity) * planet.distance_from_parent, 2)

        #moon radii
        if isinstance(planet, GasGiant):
            for moonlet in planet.close_moonlets:
                moonlet.distance_from_parent = round(((roll_dice(1) + 4) / 4) * planet.world_diameter, 3)
            for moonlet in planet.far_moonlets:
                moonlet.distance_from_parent = round(((roll_dice(1) + 4) * 4) * planet.world_diameter, 3)
            for moon in planet.companions:
                orbit_lists = []
                roll = roll_dice(3) + 3
                if roll >= 15:
                    roll += roll_dice(2)
                moon.distance_from_parent = round((roll / 2) * planet.world_diameter, 3)

                while moon.distance_from_parent in orbit_lists == False:
                    
                    too_close = False
                    for radius in orbit_lists:
                        if radius - 5 <= moon.distance_from_parent <= radius + 5:
                            too_close = True

                    if too_close == False:
                        orbit_lists.append(moon.distance_from_parent)
                    else:
                        roll = roll_dice(3) + 3
                        if roll >= 15:
                            roll += roll_dice(2)
                        moon.distance_from_parent = round((roll / 2) * planet.world_diameter, 3)


        if isinstance(planet, TerrestrialPlanet):
            for moon in planet.companions:
                orbit_lists = []
                if isinstance(moon, Moonlet):
                    roll = ((roll_dice(1) + 4) / 4) * planet.world_diameter
                else:
                    roll = roll_dice(2)
                    if (
                        (moon.size == 'Small' and planet.size == 'Large') or
                        (moon.size == 'Tiny' and planet.size == 'Standard')
                    ):
                        roll += 2
                    if (
                        (moon.size == 'Standard' and planet.size == 'Large') or
                        (moon.size == 'Small' and planet.size == 'Standard') or
                        (moon.size == 'Tiny' and planet.size == 'Small')   
                    ):
                        roll += 4
                    
                moon.distance_from_parent = round((roll * 2.5) * planet.world_diameter, 2)

                while moon.distance_from_parent in orbit_lists == False:
                
                    too_close = False
                    for radius in orbit_lists:
                        if radius - 5 <= moon.distance_from_parent <= radius + 5:
                            too_close = True

                    if too_close == False:
                        orbit_lists.append(moon.distance_from_parent)
                    else:
                        roll = roll_dice(3) + 3
                        if roll >= 15:
                            roll += roll_dice(2)
                        moon.distance_from_parent = round((roll / 2) * planet.world_diameter, 3)
        #moon orbital period
        total_braking = 0
        for moon in planet.companions:
            moon.orbital_period = 0.166 * math.sqrt((moon.distance_from_parent ** 3) / (moon.world_mass + planet.world_mass))
            #tidal braking
            if isinstance(moon, Moonlet):
                continue
            moon_braking = (2230000 * planet.world_mass * moon.world_diameter)/(moon.distance_from_parent ** 3)
            moon.tidal_braking = round((moon_braking * star.star_age)/moon.world_mass)
            total_braking += (2230000 * moon.world_mass * planet.world_diameter)/(moon.distance_from_parent ** 3)
            if moon.tidal_braking >= 50:
                moon.tide_locked = True
                moon.rotation_period = moon.orbital_period
            #rotation period
            if moon.tide_locked == False:
                roll = roll_dice(3)
                mod_roll = roll
                if moon.size == 'Standard':
                    mod_roll += 10
                elif moon.size == 'Small':
                    mod_roll += 14
                elif moon.size == 'Tiny':
                    mod_roll += 18
                else:
                    mod_roll += 22
                if roll >= 16 or mod_roll > 36:
                    roll = roll_dice(2)
                    if roll <= 6:
                        moon.rotation_period = mod_roll / 24
                    elif roll <= 7:
                        moon.rotation_period = roll_dice(1) * 2
                    elif roll <= 8:
                        moon.rotation_period = roll_dice(1) * 5
                    elif roll <= 9:
                        moon.rotation_period = roll_dice(1) * 10
                    elif roll <= 10:
                        moon.rotation_period = roll_dice(1) * 20
                    elif roll <= 11:
                        moon.rotation_period = roll_dice(1) * 50
                    else:
                        moon.rotation_period = roll_dice(1) * 100
                else:
                    moon.rotation_period = mod_roll / 24
                
                if moon.rotation_period > moon.distance_from_parent:
                    moon.tide_locked = True
                    moon.rotation_period = moon.distance_from_parent
                
                if roll_dice(3) >= 17:
                    moon.retrograde_orbit = True
                
                moon.rotation_period = round(moon.rotation_period, 3)
                

        #rotation period
        total_braking += (0.46 * star.star_mass * planet.world_diameter)/(planet.distance_from_parent ** 3)
        planet.tidal_braking = round((total_braking * star.star_age)/planet.world_mass)
        if planet.tidal_braking >= 50:
            planet.tide_locked = True
        if planet.tide_locked == False:
            roll = roll_dice(3)
            mod_roll = roll
            if planet.size == 'Small' and isinstance(planet, GasGiant):
                mod_roll += 6
            elif planet.size == 'Large' and isinstance(planet, TerrestrialPlanet):
                mod_roll += 6
            elif planet.size == 'Standard':
                mod_roll += 10
            elif planet.size == 'Small':
                mod_roll += 14
            elif planet.size == 'Tiny':
                mod_roll += 18
            else:
                mod_roll += 0
            if roll >= 16 or mod_roll > 36:
                roll = roll_dice(2)
                if roll <= 6:
                    planet.rotation_period = mod_roll / 24
                elif roll <= 7:
                    planet.rotation_period = roll_dice(1) * 2
                elif roll <= 8:
                    planet.rotation_period = roll_dice(1) * 5
                elif roll <= 9:
                    planet.rotation_period = roll_dice(1) * 10
                elif roll <= 10:
                    planet.rotation_period = roll_dice(1) * 20
                elif roll <= 11:
                    planet.rotation_period = roll_dice(1) * 50
                else:
                    planet.rotation_period = roll_dice(1) * 100
            else:
                planet.rotation_period = mod_roll / 24
            
            if planet.rotation_period > planet.distance_from_parent:
                planet.tide_locked = True
                planet.rotation_period = planet.distance_from_parent

            if roll_dice(3) >= 13:
                planet.retrograde_orbit = True
        else:
            planet.rotation_period = planet.orbital_period

        planet.rotation_period = round(planet.rotation_period, 3)


            
        #local calendar stuff
        for moon in planet.companions:
            if moon.retrograde_orbit == False:
                moon.day_length = round((planet.orbital_period * moon.rotation_period) / (planet.orbital_period - moon.rotation_period), 2)
                moon.moon_cycle_length = round((moon.orbital_period * planet.rotation_period) / (moon.orbital_period - planet.rotation_period), 2)
            else:
                moon.day_length = round((planet.orbital_period * (moon.rotation_period * -1)) / (planet.orbital_period + moon.rotation_period), 2)
                moon.moon_cycle_length = round((moon.orbital_period * (planet.rotation_period * -1)) / (moon.orbital_period + planet.rotation_period), 2)
        
        if planet.orbital_period - planet.rotation_period == 0:
            planet.day_length = 'Perpetually Day'
        else:
            planet.day_length = round((planet.orbital_period * planet.rotation_period) / (planet.orbital_period - planet.rotation_period), 2)

        #axial tilt - TO DO
        roll = roll_dice(3)
        if roll <= 6:
            planet.axial_tilt = roll_dice(2) - 2
        elif roll <= 9:
            planet.axial_tilt = 10 + roll_dice(2) - 2
        elif roll <= 12:
            planet.axial_tilt = 20 + roll_dice(2) - 2
        elif roll <= 14:
            planet.axial_tilt = 30 + roll_dice(2) - 2
        elif roll <= 16:
            planet.axial_tilt = 40 + roll_dice(2) - 2
        else:
            roll = roll_dice(1)
            if roll <= 2:
                planet.axial_tilt = 50 + roll_dice(2) - 2
            elif roll <= 4:
                planet.axial_tilt = 60 + roll_dice(2) - 2
            elif roll <= 5:
                planet.axial_tilt = 70 + roll_dice(2) - 2
            else:
                planet.axial_tilt = 80 + roll_dice(2) - 2
        
def generate_volcanism(star):
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if isinstance(planet, str):
            continue
        if isinstance(planet, TerrestrialPlanet):
            roll = roll_dice(3)
            roll += round((planet.surface_gravity / star.star_age) * 40)
            if len(planet.companions) == 1 and isinstance(planet.companions[0], Moon):
                roll += 5
            if len(planet.companions) >= 2 and isinstance(planet.companions[0], Moon):
                roll += 10
            if planet.complete_world_type == 'Tiny (Sulfur)':
                roll += 60
            
            if roll <= 16:
                planet.volcanic_activity_level = 'None'
            elif roll <= 20:
                planet.volcanic_activity_level = 'Light'
            elif roll <= 26:
                planet.volcanic_activity_level = 'Moderate'
            elif roll <= 70:
                planet.volcanic_activity_level = 'Heavy'
            else:
                planet.volcanic_activity_level = 'Extreme'
            
            if planet.world_type == 'Garden':
                if planet.volcanic_activity_level == 'Heavy' and roll_dice(3) <= 8:
                    planet.atmospheric_composition.append('Marginal Atmosphere')
                    if roll_dice(1) <= 3:
                        planet.atmospheric_gases.append('Significant Non-Organic Pollutants')
                    else:
                        planet.atmospheric_gases.append('Significant Sulfur Compounds')
                elif planet.volcanic_activity_level == 'Extreme' and roll_dice(3) <= 14:
                    planet.atmospheric_composition.append('Marginal Atmosphere')
                    if roll_dice(1) <= 3:
                        planet.atmospheric_gases.append('Significant Non-Organic Pollutants')
                    else:
                        planet.atmospheric_gases.append('Significant Sulfur Compounds')
            
            if planet.size == 'Tiny' or planet.size == 'Small':
                planet.tectonic_activity_level = 'None'
            else:
                roll = roll_dice(3)
                if planet.volcanic_activity_level == 'None':
                    roll -= 8
                elif planet.volcanic_activity_level == 'Light':
                    roll -= 4
                elif planet.volcanic_activity_level == 'Heavy':
                    roll += 4
                elif planet.volcanic_activity_level == 'Extreme':
                    roll += 8
                if planet.hydrographic_coverage_percent <= 0:
                    roll -= 4
                elif planet.hydrographic_coverage_percent < 50:
                    roll -= 2
                if len(planet.companions) == 1 and isinstance(planet.companions[0], Moon):
                    roll += 2
                elif len(planet.companions) >= 2 and isinstance(planet.companions[0], Moon):
                    roll += 4
                
                if roll <= 6:
                    planet.tectonic_activity_level = 'None'
                elif roll <= 10:
                    planet.tectonic_activity_level = 'Light'
                elif roll <= 14:
                    planet.tectonic_activity_level = 'Moderate'
                elif roll <= 18:
                    planet.tectonic_activity_level = 'Heavy'
                else:
                    planet.tectonic_activity_level = 'Extreme'
        
        for moon in planet.companions:
            if isinstance(moon, Moonlet):
                continue
            roll = roll_dice(3)
            roll += round((moon.surface_gravity / star.star_age) * 40)
            if moon.complete_world_type == 'Tiny (Sulfur)':
                roll += 60
            elif isinstance(planet, GasGiant):
                roll += 5
            
            if roll <= 16:
                moon.volcanic_activity_level = 'None'
            elif roll <= 20:
                moon.volcanic_activity_level = 'Light'
            elif roll <= 26:
                moon.volcanic_activity_level = 'Moderate'
            elif roll <= 70:
                moon.volcanic_activity_level = 'Heavy'
            else:
                moon.volcanic_activity_level = 'Extreme'
            
            if moon.world_type == 'Garden':
                if moon.volcanic_activity_level == 'Heavy' and roll_dice(3) <= 8:
                    moon.atmospheric_composition.append('Marginal Atmosphere')
                    if roll_dice(1) <= 3:
                        moon.atmospheric_gases.append('Significant Non-Organic Pollutants')
                    else:
                        moon.atmospheric_gases.append('Significant Sulfur Compounds')
                elif moon.volcanic_activity_level == 'Extreme' and roll_dice(3) <= 14:
                    moon.atmospheric_composition.append('Marginal Atmosphere')
                    if roll_dice(1) <= 3:
                        moon.atmospheric_gases.append('Significant Non-Organic Pollutants')
                    else:
                        moon.atmospheric_gases.append('Significant Sulfur Compounds')
            
            if moon.size == 'Tiny' or moon.size == 'Small':
                continue
            else:
                roll = roll_dice(3)
                if moon.volcanic_activity_level == 'None':
                    roll -= 8
                elif moon.volcanic_activity_level == 'Light':
                    roll -= 4
                elif moon.volcanic_activity_level == 'Heavy':
                    roll += 4
                elif moon.volcanic_activity_level == 'Extreme':
                    roll += 8
                if moon.hydrographic_coverage_percent <= 0:
                    roll -= 4
                elif moon.hydrographic_coverage_percent < 50:
                    roll -= 2
                if len(moon.companions) == 1 and isinstance(moon.companions[0], Moon):
                    roll += 2
                elif len(moon.companions) >= 2 and isinstance(moon.companions[0], Moon):
                    roll += 4
                
                if roll <= 6:
                    moon.tectonic_activity_level = 'None'
                elif roll <= 10:
                    moon.tectonic_activity_level = 'Light'
                elif roll <= 14:
                    moon.tectonic_activity_level = 'Moderate'
                elif roll <= 18:
                    moon.tectonic_activity_level = 'Heavy'
                else:
                    moon.tectonic_activity_level = 'Extreme'

def determine_resources(star):
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        roll = roll_dice(3)
        if isinstance(planet, str):
            if planet == 'Asteroid Belt':
                ast_list = list(planet_tup)
                if roll <= 3:
                    planet = 'Asteroid Belt (Worthless)'
                elif roll <= 4:
                    planet = 'Asteroid Belt (Very Scant)'
                elif roll <= 5:
                    planet = 'Asteroid Belt (Scant)'
                elif roll <= 7:
                    planet = 'Asteroid Belt (Very Poor)'
                elif roll <= 9:
                    planet = 'Asteroid Belt (Poor)'
                elif roll <= 11:
                    planet = 'Asteroid Belt (Average)'
                elif roll <= 13:
                    planet = 'Asteroid Belt (Abundant)'
                elif roll <= 15:
                    planet = 'Asteroid Belt (Very Abundant)'
                elif roll <= 16:
                    planet = 'Asteroid Belt (Rich)'
                elif roll <= 17:
                    planet = 'Asteroid Belt (Very Rich)'
                elif roll <= 18:
                    planet = 'Asteroid Belt (Motherlode)'
                
                ast_list[1] = planet
                i = star.planet_list.index(planet_tup)
                star.planet_list[i] = tuple(ast_list)
                
                continue
            else:
                continue
        elif isinstance(planet, TerrestrialPlanet):
            if planet.volcanic_activity_level == 'None':
                roll -= 2
            elif planet.volcanic_activity_level == 'Light':
                roll -= 1
            elif planet.volcanic_activity_level == 'Heavy':
                roll += 1
            elif planet.volcanic_activity_level == 'Extreme':
                roll += 2

            if roll <= 2:
                planet.resource_value_level = 'Scant'
                planet.resource_value_modifier = -3
            elif roll <= 4:
                planet.resource_value_level = 'Very Poor'
                planet.resource_value_modifier = -2
            elif roll <= 7:
                planet.resource_value_level = 'Poor'
                planet.resource_value_modifier = -1
            elif roll <= 13:
                planet.resource_value_level = 'Average'
                planet.resource_value_modifier = 0
            elif roll <= 16:
                planet.resource_value_level = 'Abundant'
                planet.resource_value_modifier = 1
            elif roll <= 18:
                planet.resource_value_level = 'Very Abundant'
                planet.resource_value_modifier = 2
            else:
                planet.resource_value_level = 'Rich'
                planet.resource_value_modifier = 3
        elif isinstance(planet, GasGiant):
            if roll <= 2:
                planet.resource_value_level = 'Scant'
                planet.resource_value_modifier = -3
            elif roll <= 4:
                planet.resource_value_level = 'Very Poor'
                planet.resource_value_modifier = -2
            elif roll <= 7:
                planet.resource_value_level = 'Poor'
                planet.resource_value_modifier = -1
            elif roll <= 13:
                planet.resource_value_level = 'Average'
                planet.resource_value_modifier = 0
            elif roll <= 16:
                planet.resource_value_level = 'Abundant'
                planet.resource_value_modifier = 1
            elif roll <= 18:
                planet.resource_value_level = 'Very Abundant'
                planet.resource_value_modifier = 2
            else:
                planet.resource_value_level = 'Rich'
                planet.resource_value_modifier = 3
        
        for moon in planet.companions:
            if isinstance(moon, Moonlet):
                continue
            if moon.volcanic_activity_level == 'None':
                roll -= 2
            elif moon.volcanic_activity_level == 'Light':
                roll -= 1
            elif moon.volcanic_activity_level == 'Heavy':
                roll += 1
            elif moon.volcanic_activity_level == 'Extreme':
                roll += 2

            if roll <= 2:
                moon.resource_value_level = 'Scant'
                moon.resource_value_modifier = -3
            elif roll <= 4:
                moon.resource_value_level = 'Very Poor'
                moon.resource_value_modifier = -2
            elif roll <= 7:
                moon.resource_value_level = 'Poor'
                moon.resource_value_modifier = -1
            elif roll <= 13:
                moon.resource_value_level = 'Average'
                moon.resource_value_modifier = 0
            elif roll <= 16:
                moon.resource_value_level = 'Abundant'
                moon.resource_value_modifier = 1
            elif roll <= 18:
                moon.resource_value_level = 'Very Abundant'
                moon.resource_value_modifier = 2
            else:
                moon.resource_value_level = 'Rich'
                moon.resource_value_modifier = 3

def determine_habitability(star):
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        hab_mod = 0
        if isinstance(planet, str):
            continue
        
        if isinstance(planet, TerrestrialPlanet):
            if planet.volcanic_activity_level == 'Heavy' or planet.tectonic_activity_level == 'Heavy':
                if planet.volcanic_activity_level == 'Heavy':
                    hab_mod -= 1
                if planet.tectonic_activity_level == 'Heavy':
                    hab_mod -= 1
            if planet.volcanic_activity_level == 'Extreme' or planet.tectonic_activity_level == 'Extreme':
                if planet.volcanic_activity_level == 'Extreme':
                    hab_mod -= 2
                if planet.tectonic_activity_level == 'Extreme':
                    hab_mod -= 2
            
            if (
                ('Suffocating' in planet.atmospheric_composition) and ('Corrosive' in planet.atmospheric_composition) and
                (
                    'Mildy Toxic' in planet.atmospheric_composition or
                    'Highly Toxic' in planet.atmospheric_composition or
                    'Lethally Toxic' in planet.atmospheric_composition
                )
            ):
                hab_mod -= 2
            elif (
                ('Suffocating' in planet.atmospheric_composition) and
                (
                    'Mildy Toxic' in planet.atmospheric_composition or
                    'Highly Toxic' in planet.atmospheric_composition or
                    'Lethally Toxic' in planet.atmospheric_composition
                )
            ):
                hab_mod -= 1
            elif not (('Suffocating' in planet.atmospheric_composition) and ('Corrosive' in planet.atmospheric_composition) and
                (
                    'Highly Toxic' in planet.atmospheric_composition or
                    'Lethally Toxic' in planet.atmospheric_composition
            )):
                if planet.pressure_category == 'Very Thin Atmosphere':
                    hab_mod += 1
                elif planet.pressure_category == 'Thin Atmosphere':
                    hab_mod += 2
                elif planet.pressure_category == 'Standard Atmosphere' or planet.pressure_category == 'Dense Atmosphere':
                    hab_mod += 3
                elif planet.pressure_category == 'Very Dense Atmosphere' or planet.pressure_category == 'Superdense Atmosphere':
                    hab_mod += 1
                
                if not ('Marginal Atmosphere' in planet.atmospheric_composition) and not (planet.pressure_category == 'Trace Atmosphere' or planet.pressure_category == 'Nonexistent Atmosphere'):
                    hab_mod += 1

                if planet.climate_type == 'Cold':
                    hab_mod += 1
                elif (
                    planet.climate_type == 'Chilly' or
                    planet.climate_type == 'Cool' or
                    planet.climate_type == 'Normal' or
                    planet.climate_type == 'Warm' or
                    planet.climate_type == 'Tropical'
                ):
                    hab_mod += 2
                elif planet.climate_type == 'Hot':
                    hab_mod += 1
            
            if 1 <= planet.hydrographic_coverage_percent <= 59:
                hab_mod += 1
            elif 59 < planet.hydrographic_coverage_percent <= 90:
                hab_mod += 2
            elif 90 < planet.hydrographic_coverage_percent <= 99:
                hab_mod += 1
            
            if hab_mod <= -2:
                hab_mod = -2
            elif hab_mod >= 8:
                hab_mod = 8
            
            planet.habitability_modifier = hab_mod

        for moon in planet.companions:
            hab_mod = 0
            if isinstance(moon, Moonlet):
                continue
            if moon.volcanic_activity_level == 'Heavy' or moon.tectonic_activity_level == 'Heavy':
                if moon.volcanic_activity_level == 'Heavy':
                    hab_mod -= 1
                if moon.tectonic_activity_level == 'Heavy':
                    hab_mod -= 1
            if moon.volcanic_activity_level == 'Extreme' or moon.tectonic_activity_level == 'Extreme':
                if moon.volcanic_activity_level == 'Extreme':
                    hab_mod -= 2
                if moon.tectonic_activity_level == 'Extreme':
                    hab_mod -= 2
            
            if (
                ('Suffocating' in moon.atmospheric_composition) and ('Corrosive' in moon.atmospheric_composition) and
                (
                    'Mildy Toxic' in moon.atmospheric_composition or
                    'Highly Toxic' in moon.atmospheric_composition or
                    'Lethally Toxic' in moon.atmospheric_composition
                )
            ):
                hab_mod -= 2
            elif (
                ('Suffocating' in moon.atmospheric_composition) and
                (
                    'Mildy Toxic' in moon.atmospheric_composition or
                    'Highly Toxic' in moon.atmospheric_composition or
                    'Lethally Toxic' in moon.atmospheric_composition
                )
            ):
                hab_mod -= 1
            elif not (('Suffocating' in moon.atmospheric_composition) and ('Corrosive' in moon.atmospheric_composition) and
                (
                    'Mildy Toxic' in moon.atmospheric_composition or
                    'Highly Toxic' in moon.atmospheric_composition or
                    'Lethally Toxic' in moon.atmospheric_composition
            )):
                if moon.pressure_category == 'Very Thin Atmosphere':
                    hab_mod += 1
                elif moon.pressure_category == 'Thin Atmosphere':
                    hab_mod += 2
                elif moon.pressure_category == 'Standard Atmosphere' or moon.pressure_category == 'Dense Atmosphere':
                    hab_mod += 3
                elif moon.pressure_category == 'Very Dense Atmosphere' or moon.pressure_category == 'Superdense Atmosphere':
                    hab_mod += 1
                
                if not ('Marginal Atmosphere' in moon.atmospheric_composition):
                    hab_mod += 1

                if moon.climate_type == 'Cold':
                    hab_mod += 1
                elif (
                    moon.climate_type == 'Chilly' or
                    moon.climate_type == 'Cool' or
                    moon.climate_type == 'Normal' or
                    moon.climate_type == 'Warm' or
                    moon.climate_type == 'Tropical'
                ):
                    hab_mod += 2
                elif moon.climate_type == 'Hot':
                    hab_mod += 1
            
            if 1 <= moon.hydrographic_coverage_percent <= 59:
                hab_mod += 1
            elif moon.hydrographic_coverage_percent <= 90:
                hab_mod += 2
            elif moon.hydrographic_coverage_percent <= 99:
                hab_mod += 1
            
            if hab_mod < -2:
                hab_mod = -2
            elif hab_mod > 8:
                hab_mod = 8
            
            moon.habitability_modifier = hab_mod

def determine_affinity(star):
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if isinstance(planet, str):
            continue
        
        planet.affinity_modifier = planet.resource_value_modifier + planet.habitability_modifier

        for moon in planet.companions:
            if isinstance(moon, Moonlet):
                continue

            moon.affinity_modifier = moon.resource_value_modifier + moon.habitability_modifier

def determine_main_world(star):
    mainworld = TerrestrialPlanet()
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if isinstance(planet, str):
            continue

        if planet.affinity_modifier > mainworld.affinity_modifier:
            mainworld = planet
        
        for moon in planet.companions:
            if moon.affinity_modifier > mainworld.affinity_modifier:
                mainworld = moon
        
    mainworld.main_world = True
    star.main_world = mainworld

def name_worlds(star):
    plan_name = gen_planet_name()
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if isinstance(planet, str):
            continue
        
        planet.name = star.name + ' ' + next(plan_name)
        
        moon_name = gen_moon_name()
        for moon in planet.companions:
            moon.name = planet.name + next(moon_name)

def check_sapient_species(system, star):
    # To Do — Check with 1/10,000 chance for sapient species. Garden worlds are rolled twice OR 1/1000, depending on results.
    for planet_tup in star.planet_list:
        planet = planet_tup[1]
        if not isinstance(planet, str):
            if (planet.world_type == 'Garden' or planet.world_type == 'Ocean') and system.sapient_home_system == False:
                for _ in range(0, roll_dice(1) + 1):
                    create_species(planet)
                if planet.homeworld == True:
                    system.sapient_home_system = True
                    system.inhabited_system = True
                    generate_homeworld(planet)
            elif planet.main_world == True and system.sapient_home_system == False:
                if roll_dice(1) >= 4:
                    for _ in range(0, roll_dice(1) - 1):
                        create_species(planet)
                    if planet.homeworld == True:
                        system.sapient_home_system = True
                        system.inhabited_system = True
                        generate_homeworld(planet)

            if planet.main_world == True and system.sapient_home_system == False and planet.affinity_modifier > 0:
                #Generate a colony for a system without a homeworld
                system.inhabited_system = True
                planet.inhabited_world = True
                generate_main_world_colony(planet)
                planet.colony = True
            elif system.inhabited_system == True and planet.homeworld == False and planet.affinity_modifier > 0:
                #Generate a colony for an inhabited system if the affinity modifier > 0
                planet.inhabited_world = True
                if planet.habitability_modifier > 0:
                    if roll_dice(1) >= 4:
                        create_species(planet)
                        create_species(planet)
                    else:
                        create_species(planet)
                generate_secondary_colony(planet, star.main_world)
                planet.colony = True
            elif system.inhabited_system == True and planet.homeworld == False:
                if roll_dice(3) >= 16:
                    create_species(planet)
                roll = roll_dice(3) + planet.habitability_modifier
                if roll >= 9:
                    generate_outpost(planet, star.main_world)
                    planet.outpost = True
            elif planet.homeworld == False:
                if planet.habitability_modifier > 0:
                    if roll_dice(3) >= 16:
                        create_species(planet)
                        create_species(planet)
                    else:
                        create_species(planet)
                roll = roll_dice(3) + planet.affinity_modifier
                if roll >= 9:
                    generate_outpost(planet, star.main_world)
                    planet.outpost = True
        
            for moon in planet.companions:
                if not isinstance(moon, Moonlet):
                    if (moon.world_type == 'Garden' or moon.world_type == 'Ocean') and system.sapient_home_system == False:
                        for _ in range(0, roll_dice(1) + 1):
                            create_species(moon)
                        if moon.homeworld == True:
                            system.sapient_home_system = True
                            system.inhabited_system = True
                            generate_homeworld(moon)
                    elif moon.main_world == True and system.sapient_home_system == False:
                        if roll_dice(1) >= 4:
                            for _ in range(0, roll_dice(1) - 1):
                                create_species(moon)
                            if moon.homeworld == True:
                                system.sapient_home_system = True
                                system.inhabited_system = True
                                generate_homeworld(moon)

                    if moon.main_world == True and system.sapient_home_system == False and moon.affinity_modifier > 0:
                        #Generate a colony for a system without a homeworld
                        system.inhabited_system = True
                        moon.inhabited_world = True
                        generate_main_world_colony(moon)
                        moon.colony = True
                    elif system.inhabited_system == True and moon.homeworld == False and moon.affinity_modifier > 0:
                        #Generate a colony for an inhabited system if the affinity modifier > 0
                        moon.inhabited_world = True
                        if moon.habitability_modifier > 0:
                            if roll_dice(1) >= 4:
                                create_species(moon)
                                create_species(moon)
                            else:
                                create_species(moon)
                        generate_secondary_colony(moon, star.main_world)
                        moon.colony = True
                    elif system.inhabited_system == True and moon.homeworld == False:
                        if roll_dice(3) >= 16:
                            create_species(moon)
                        roll = roll_dice(3) + moon.habitability_modifier
                        if roll >= 9:
                            generate_outpost(moon, star.main_world)
                            moon.outpost = True
                    elif moon.homeworld == False:
                        if moon.habitability_modifier > 0:
                            if roll_dice(3) >= 16:
                                create_species(moon)
                                create_species(moon)
                            else:
                                create_species(moon)
                        roll = roll_dice(3) + moon.affinity_modifier
                        if roll >= 9:
                            generate_outpost(moon, star.main_world)
                            moon.outpost = True

def generate_homeworld(planet):
    generate_tech_level(planet)
    determine_carrying_capacity(planet)
    planet.population = (planet.carrying_capacity * 10) / roll_dice(2)
    determine_world_unity(planet)
    determine_society_type(planet)
    determine_control_rating(planet)
    determine_economics(planet)
    determine_installations(planet)

def generate_main_world_colony(planet):
    generate_tech_level(planet)
    determine_carrying_capacity(planet)
    determine_mainworld_colony_population(planet)
    determine_world_unity(planet)
    determine_society_type(planet)
    determine_control_rating(planet)
    determine_economics(planet)
    determine_installations(planet)

def generate_secondary_colony(planet, mainworld):
    generate_tech_level(planet)
    determine_carrying_capacity(planet)
    determine_secondary_colony_population(planet, mainworld)
    if roll_dice(3) + planet.population_rating >= 20:
        determine_world_unity(planet)
        determine_society_type(planet)
        determine_control_rating(planet)
    else:
        if len(mainworld.world_unity) > 16:
            planet.world_unity = 'World Government (Colony)'
            planet.society_type = mainworld.society_type
            planet.control_rating = mainworld.control_rating
        else:
            planet.world_unity = mainworld.world_unity + ' (Colony)'
            planet.society_type = mainworld.society_type
            planet.control_rating = mainworld.control_rating
    determine_economics(planet)
    determine_installations(planet)

def generate_outpost(planet, mainworld):
    generate_tech_level(planet)
    determine_carrying_capacity(planet)
    determine_outpost_population(planet)
    if roll_dice(3) + planet.population_rating >= 20:
        determine_world_unity(planet)
        determine_society_type(planet)
        determine_control_rating(planet)
    else:
        if len(mainworld.world_unity) > 16:
            planet.world_unity = 'World Government (Colony)'
            planet.society_type = mainworld.society_type
            planet.control_rating = mainworld.control_rating
        else:
            if mainworld.inhabited_world == True:
                planet.world_unity = mainworld.world_unity + ' (Colony)'
                planet.society_type = mainworld.society_type
                planet.control_rating = mainworld.control_rating
            else:
                planet.world_unity = 'System Outpost'
                determine_society_type(planet)
                determine_control_rating(planet)
    determine_economics(planet)
    determine_installations(planet)

def generate_tech_level(planet):
    roll = roll_dice(3)
    if (planet.homeworld == True or planet.colony == True) and 4 <= planet.habitability_modifier <= 6:
        roll += 1
    elif (planet.homeworld == True or planet.colony == True) and planet.habitability_modifier <= 3:
        roll += 2
    elif planet.outpost == True:
        roll += 3
    
    if roll <= 7:
        planet.tech_level = '10'
    elif roll <= 11:
        planet.tech_level = '11 (Delayed)'
    elif roll <= 15:
        planet.tech_level = '11'
    else:
        planet.tech_level = '11 (Advanced)'

def determine_carrying_capacity(planet):
    cap_dict = {
        10 : 1000,
        9 : 500,
        8 : 250,
        7 : 130,
        6 : 60,
        5 : 30,
        4 : 15,
        3 : 8,
        2 : 4,
        1 : 2,
        0 : 1,
        -1 : 0.5,
        -2 : 0.25,
        -3 : 0.13,
        -4 : 0.06,
        -5 : 0.03
    }

    planet.carrying_capacity = round(25000000 * cap_dict[planet.affinity_modifier] * (planet.world_diameter ** 2))

    #Figure out asteroid belt bullshit later, but multiply by 50 instead of world_diameter^2

def determine_mainworld_colony_population(planet):
    roll = roll_dice(3) + (3 * planet.affinity_modifier) + 45 #I can't be fucked to figure out time scale, this planet has been settled.
    if roll <= 35:
        planet.population = 10000 * (random.randrange(1, 101) / 10)
    elif roll <= 45:
        planet.population = 100000 * (random.randrange(1, 101) / 10)
    elif roll <= 55:
        planet.population = 1000000 * (random.randrange(1, 101) / 10)
    elif roll <= 65:
        planet.population = 10000000 * (random.randrange(1, 101) / 10)
    elif roll <= 75:
        planet.population = 100000000 * (random.randrange(1, 101) / 10)
    elif roll <= 85:
        planet.population = 1000000000 * (random.randrange(1, 101) / 10)
    else:
        planet.population = 10000000000 * (random.randrange(1, 101) / 10)

    planet.population_rating = math.log10(planet.population) // 1
    
def determine_secondary_colony_population(planet, mainworld):
    total_to_add = planet.affinity_modifier - mainworld.affinity_modifier - roll_dice(3)
    #lower bound: 10 - -5 - 3 = 12
    #upper bound: -5 - 10 - 18 = -33
    #get remainder after dividing out the multiplier as a whole number
    log_pop = planet.population / 10000000000
    if 1 <= log_pop <= 10:
        log_pop = 85 + log_pop
    elif 0.1 <= log_pop < 1:
        log_pop = 75 + log_pop * 10
    elif 0.01 <= log_pop < 1:
        log_pop = 65 + log_pop * 100
    elif 0.001 <= log_pop < 0.01:
        log_pop = 55 + log_pop * 1000
    elif 0.0001 <= log_pop < 0.001:
        log_pop = 45 + log_pop * 10000
    elif 0.00001 <= log_pop < 0.0001:
        log_pop = 35 + log_pop * 100000
    elif 0.000001 <= log_pop < 0.00001:
        log_pop = 25 + log_pop * 1000000
    
    log_pop = round(log_pop)

    roll = log_pop + total_to_add

    if roll <= 35:
        planet.population = 10000 * (random.randrange(1, 101) / 10)
    elif roll <= 45:
        planet.population = 100000 * (random.randrange(1, 101) / 10)
    elif roll <= 55:
        planet.population = 1000000 * (random.randrange(1, 101) / 10)
    elif roll <= 65:
        planet.population = 10000000 * (random.randrange(1, 101) / 10)
    elif roll <= 75:
        planet.population = 100000000 * (random.randrange(1, 101) / 10)
    elif roll <= 85:
        planet.population = 1000000000 * (random.randrange(1, 101) / 10)
    else:
        planet.population = 10000000000 * (random.randrange(1, 101) / 10)

def determine_outpost_population(planet):
    pop_dict = {
        3 : 100,
        4 : 150,
        5 : 250,
        6 : 400,
        7 : 600,
        8 : 1000,
        9 : 1500,
        10 : 2500,
        11 : 4000,
        12 : 6000,
        13 : 10000,
        14 : 15000,
        15 : 25000,
        16 : 40000,
        17 : 60000,
        18 : 100000
    }

    out_pop = pop_dict[roll_dice(3)]
    out_pop += round(out_pop * (random.randrange(-25, 26) / 100))
    planet.population = out_pop

def determine_world_unity(planet):
    roll = roll_dice(2)
    if planet.population_rating <= 4:
        roll += 4
    elif planet.population_rating <= 5:
        roll += 3
    elif planet.population_rating <= 6:
        roll += 2
    elif planet.population_rating <= 7:
        roll += 1

    if roll <= 5:
        planet.world_unity = 'Diffuse'
    elif roll <= 6:
        planet.world_unity = 'Factionalised'
    elif roll <= 7:
        planet.world_unity = 'Coalition'
    elif roll <= 8:
        determine_special_conditions(planet)
    else:
        planet.world_unity = 'World Government'

def determine_special_conditions(planet):
    count = 0
    num_times = 1
    up_count = False
    conditions_list = []
    spec_dict = {
        5 : 'Subjugated',
        6 : 'Sanctuary',
        8 : 'Military Government',
        9 : 'Socialist',
        10 : 'Bureaucracy',
        12 : 'Colony',
        14 : 'Oligarchy',
        15 : 'Meritocracy',
        16 : 'Hypercapitalist',
        17 : 'Utopia',
        18 : 'Cybercracy'
    }
    while count < num_times:
        roll = roll_dice(3)

        if roll <= 5:
            roll = 5
            up_count = True
        elif 7 <= roll <= 8:
            roll = 8
        elif roll <= 9:
            up_count = True
        elif 11 <= roll <= 12:
            roll = 12
        elif 13 <= roll <= 14:
            roll = 14
            up_count = True
        elif roll <= 15:
            up_count = True

        if up_count == True and num_times < 2:
            num_times = 2
        
        conditions_list.append(spec_dict[roll])
        count += 1
    
    if len(conditions_list) == 1:
        planet.world_unity = 'World Government (' + conditions_list[0] + ')'
    else:
        if conditions_list[0] != conditions_list[1]:
            planet.world_unity = 'World Government (' + conditions_list[0] + ', ' + conditions_list[1] + ')'
        else:
            planet.world_unity = 'World Government (' + conditions_list[0] + ')'
    
def determine_society_type(planet):
    emp_dict = {
        6: 'Anarchy',
        8: 'Clan Society',
        9: 'Caste Society',
        10: 'Feudal Society',
        11: 'Feudal Society',
        12: 'Feudal Society',
        13: 'Theocracy',
        14: 'Dictatorship',
        15: 'Dictatorship',
        16: 'Dictatorship',
        17: 'Dictatorship',
        18: 'Representative Democracy',
        19: 'Representative Democracy',
        20: 'Corpocracy',
        21: 'Corpocracy',
        22: 'Corpocracy',
        23: 'Technocracy',
        25: 'Technocracy',
        27: 'Caste Society',
        28: 'Anarchy'
    }
    corp_dict = {
        6: 'Anarchy',
        8: 'Clan Society',
        9: 'Caste Society',
        10: 'Theocracy',
        11: 'Feudal Society',
        12: 'Feudal Society',
        13: 'Dictatorship',
        14: 'Dictatorship',
        15: 'Dictatorship',
        16: 'Representative Democracy',
        17: 'Representative Democracy',
        18: 'Athenian Democracy',
        19: 'Corpocracy',
        20: 'Corpocracy',
        21: 'Corpocracy',
        22: 'Technocracy',
        23: 'Technocracy',
        25: 'Technocracy',
        27: 'Caste Society',
        28: 'Anarchy'
    }
    fed_dict = {
        6: 'Anarchy',
        8: 'Clan Society',
        9: 'Caste Society',
        10: 'Feudal Society',
        11: 'Theocracy',
        12: 'Dictatorship',
        13: 'Dictatorship',
        14: 'Dictatorship',
        15: 'Representative Democracy',
        16: 'Representative Democracy',
        17: 'Representative Democracy',
        18: 'Representative Democracy',
        19: 'Representative Democracy',
        20: 'Athenian Democracy',
        21: 'Athenian Democracy',
        22: 'Athenian Democracy',
        23: 'Corpocracy',
        25: 'Technocracy',
        27: 'Caste Society',
        28: 'Anarchy'
    }

    roll = roll_dice(3)
    roll2 = roll_dice(3) + 10
    if 3 <= roll2 <= 6:
        roll2 = 6
    elif 7 <= roll2 <= 8:
        roll2 = 8
    elif 24 <= roll2 <= 25:
        roll2 = 25
    elif 26 <= roll2 <= 27:
        roll2 = 27
    elif roll2 >= 28:
        roll2 = 28


    if roll <= 4 or roll >= 17:
        planet.parent_power = 'Minor Power 1'
        planet.society_type = fed_dict[roll2]
    elif roll <= 6:
        planet.parent_power = 'Minor Power 2'
        planet.society_type = fed_dict[roll2]
    elif 7 <= roll <= 10:
        planet.parent_power = 'Major Power 1'
        planet.society_type = emp_dict[roll2]
    elif 11 <= roll <= 14:
        planet.parent_power = 'Major Power 2'
        planet.society_type = corp_dict[roll2]
    elif  roll >= 15:
        planet.parent_power = 'Minor Power 3'
        planet.society_type = corp_dict[roll2]

def determine_control_rating(planet):
    if planet.society_type == 'Anarchy':
        planet.control_rating = 0
    elif planet.society_type == 'Athenian Democracy':
        planet.control_rating = random.randrange(2,5)
    elif planet.society_type == 'Representative Democracy':
        planet.control_rating = random.randrange(2,5)
    elif planet.society_type == 'Clan Society':
        planet.control_rating = random.randrange(3,6)
    elif planet.society_type == 'Caste Society':
        planet.control_rating = random.randrange(3,6)
    elif planet.society_type == 'Dictatorship':
        planet.control_rating = random.randrange(3,7)
    elif planet.society_type == 'Technocracy':
        planet.control_rating = random.randrange(3,7)
    elif planet.society_type == 'Theocracy':
        planet.control_rating = random.randrange(3,7)
    elif planet.society_type == 'Corpocracy':
        planet.control_rating = random.randrange(4,7)
    elif planet.society_type == 'Feudal Society':
        planet.control_rating = random.randrange(4,7)

def determine_economics(planet):
    total_modifier = 0
    
    if planet.affinity_modifier >= 10:
        total_modifier += 0.40
    elif planet.affinity_modifier >= 9:
        total_modifier += 0.20
    elif 4 <= planet.affinity_modifier <= 6:
        total_modifier -= 0.10
    elif 1 <= planet.affinity_modifier <= 3:
        total_modifier -= 0.20
    elif planet.affinity_modifier <= 0:
        total_modifier -= 0.30
    
    if planet.population_rating == 5:
        total_modifier -= 0.10
    elif planet.population_rating <= 4:
        total_modifier -= 0.20
    
    planet.per_capita_income = 97000 + (97000 * total_modifier)

    if planet.carrying_capacity < planet.population:
        planet.per_capita_income = (planet.per_capita_income * planet.carrying_capacity) / planet.population
    
    planet.per_capita_income = round(planet.per_capita_income, 2)

    wt_lookup = planet.per_capita_income / 97000

    if wt_lookup <= 0.09:
        planet.wealth_level = 'Dead Broke'
    elif wt_lookup <= 0.31:
        planet.wealth_level = 'Poor'
    elif wt_lookup <= 0.72:
        planet.wealth_level = 'Struggling'
    elif wt_lookup <= 1.39:
        planet.wealth_level = 'Average'
    else:
        planet.wealth_level = 'Comfortable'

def determine_installations(planet):
    
    if planet.population_rating >= 6:
        if roll_dice(3) <= planet.population_rating + 2:
            planet.spaceport_type = 'Class V - Full Facilities'
        elif roll_dice(3) <= planet.population_rating + 5:
            planet.spaceport_type = 'Class IV - Standard Facilities'
        elif roll_dice(3) <= planet.population_rating + 8:
            planet.spaceport_type = 'Class III - Local Facilities'
        elif roll_dice(3) <= planet.population_rating + 7:
            planet.spaceport_type = 'Class II - Frontier Facilities'
        elif roll_dice(3) <= 14:
            planet.spaceport_type = 'Class I - Emergency Facilities'
        else:
            planet.spaceport_type = 'Class 0 - No Facilities'
    else:
        if roll_dice(3) <= planet.population_rating + 8:
            planet.spaceport_type = 'Class III - Local Facilities'
        elif roll_dice(3) <= planet.population_rating + 7:
            planet.spaceport_type = 'Class II - Frontier Facilities'
        elif roll_dice(3) <= 14:
            planet.spaceport_type = 'Class I - Emergency Facilities'
        else:
            planet.spaceport_type = 'Class 0 - No Facilities'

    if roll_dice(3) <= 6:
        planet.installations.append('Alien Enclave')
    if roll_dice(3) <= (9 - planet.control_rating):
        planet.installations.append('Black Market')
    if 3 <= roll_dice(3) <= planet.population_rating + 4:
        planet.installations.append('Colonial Office')
    if planet.population_rating >= 6 and roll_dice(3) <= planet.population_rating + 3:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Corporate Headquarters (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating + 3:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Criminal Base (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating + 6:
        roll = roll_dice(1)
        if roll <= 4:
            pr_rate = roll_dice(1) - 4
            if pr_rate <= 0:
                pr_rate = 1
            planet.installations.append('Civilian Espionage Facility (PR ' + str(pr_rate) + ')')
        if roll <= 5:
            pr_rate = roll_dice(1) - 2
            if pr_rate <= 0:
                pr_rate = 1
            planet.installations.append('Friendly Military Espionage Facility (PR ' + str(pr_rate) + ')')
        else:
            pr_rate = roll_dice(1) - 2
            if pr_rate <= 0:
                pr_rate = 1
            planet.installations.append('Hostile Military Espionage Facility (PR ' + str(pr_rate) + ')')
        
        keep_going = True
        while keep_going == True:
            if roll_dice(3) <= planet.population_rating + 6:
                roll = roll_dice(1)
                if roll <= 4:
                    pr_rate = roll_dice(1) - 4
                    if pr_rate <= 0:
                        pr_rate = 1
                    planet.installations.append('Civilian Espionage Facility (PR ' + str(pr_rate) + ')')
                if roll <= 5:
                    pr_rate = roll_dice(1) - 2
                    if pr_rate <= 0:
                        pr_rate = 1
                    planet.installations.append('Friendly Military Espionage Facility (PR ' + str(pr_rate) + ')')
                else:
                    pr_rate = roll_dice(1) - 2
                    if pr_rate <= 0:
                        pr_rate = 1
                    planet.installations.append('Hostile Military Espionage Facility (PR ' + str(pr_rate) + ')')
            else:
                keep_going = False
    if roll_dice(3) <= 12:
        pr_rate = roll_dice(1) - 4
        if pr_rate <= 0:
            pr_rate = 1
        if roll_dice(1) <= 2:
            planet.installations.append('Secret Government Research Station (PR ' + str(pr_rate) + ')')
        else:
            planet.installations.append('Government Research Station (PR ' + str(pr_rate) + ')')
        if roll_dice(3) <= planet.population_rating:
            pr_rate = roll_dice(1) - 4
            if pr_rate <= 0:
                pr_rate = 1
            if roll_dice(1) <= 2:
                planet.installations.append('Secret Government Research Station (PR ' + str(pr_rate) + ')')
            else:
                planet.installations.append('Government Research Station (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating + 3:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Mercenary Base (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= 12 - planet.population_rating:
        planet.installations.append('Nature Preserve')
    if planet.spaceport_type == 'Class V — Full Facilities' or roll_dice(3) <= planet.population_rating + 4:
        pr_rate = roll_dice(1) - 2
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Naval Base (PR ' + str(pr_rate) + ')')
    if (planet.spaceport_type == 'Class V — Full Facilities' or 
        planet.spaceport_type == 'Class IV — Standard Facilities' or 
        roll_dice(3) <= planet.population_rating + 4):
        pr_rate = roll_dice(1) - 2
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Patrol Base (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= 8 - planet.control_rating:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Pirate Base (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating + 4:
        pr_rate = roll_dice(1) - 4
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Private Research Station (PR ' + str(pr_rate) + ')')
        if roll_dice(3) <= planet.population_rating + 4:
            pr_rate = roll_dice(1) - 4
            if pr_rate <= 0:
                pr_rate = 1
            planet.installations.append('Private Research Station (PR ' + str(pr_rate) + ')')
        if roll_dice(3) <= planet.population_rating + 4:
            pr_rate = roll_dice(1) - 4
            if pr_rate <= 0:
                pr_rate = 1
            planet.installations.append('Private Research Station (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= 9:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        if roll_dice(1) >= 4:
            planet.installations.append('Rebel Base (PR ' + str(pr_rate) + ')')
        else:
            planet.installations.append('Terrorist Base (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating - 3:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Refugee Camp (PR ' + str(pr_rate) + ')')
        
        keep_going = True
        while keep_going == True:
            if roll_dice(3) <= planet.population_rating - 3:
                pr_rate = roll_dice(1) - 3
                if pr_rate <= 0:
                    pr_rate = 1
                planet.installations.append('Refugee Camp (PR ' + str(pr_rate) + ')')
            else:
                keep_going = False
    if roll_dice(3) <= planet.population_rating - 3:
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Religious Centre (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating:
        pr_rate = roll_dice(1) - 4
        if pr_rate <= 0:
            pr_rate = 1
        if roll_dice(1) >= 4:
            planet.installations.append('Covert MUAGT Office (PR ' + str(pr_rate) + ')')
        else:
            planet.installations.append('MUAGT Office (PR ' + str(pr_rate) + ')')
    if (planet.spaceport_type == 'Class V — Full Facilities' or 
        planet.spaceport_type == 'Class IV — Standard Facilities' or 
        roll_dice(3) <= planet.population_rating + 3):
        pr_rate = roll_dice(1) - 3
        if pr_rate <= 0:
            pr_rate = 1
        planet.installations.append('Survey Base (PR ' + str(pr_rate) + ')')
    if roll_dice(3) <= planet.population_rating - 6:
        pr_rate = roll_dice(1)
        if pr_rate <= 2:
            pr_rate = 3
        elif pr_rate <= 4:
            pr_rate = 4
        else:
            pr_rate = 5
        planet.installations.append('University (PR ' + str(pr_rate) + ')')
    if (len(planet.installations) == 0 or
        len(planet.installations) == 1 and ('Naval Base' in planet.installations[0] or 'Patrol Base' in planet.installations[0]) or
        (len(planet.installations) == 2 and ('Naval Base' in planet.installations[0] or 'Patrol Base' in planet.installations[0]) and 
            ('Naval Base' in planet.installations[1] or 'Patrol Base' in planet.installations[1]))
    ):
        if roll_dice(3) <= 10 - planet.population_rating:
            pr_rate = roll_dice(1) - 3
            if pr_rate <= 0:
                pr_rate = 1
            planet.installations.append('Prison (PR ' + str(pr_rate) + ')')

def create_species(planet):
    species = Species()
    species.home_planet = planet.name
    if planet.planet_type == 'Gas Giant' or planet.surface_temperature <= 116.4:
        species.biochemistry = 'Hydrogen-Based Life'
    elif planet.world_type == 'Ammonia' or 199.8 <= planet.surface_temperature <= 238.7:
        species.biochemistry = 'Ammonia-Based Life'
    elif (planet.climate_type == 'Cold' or 
          planet.climate_type == 'Chilly' or
          planet.climate_type == 'Cool'
        ) and planet.world_type == 'Ice':
        species.biochemistry = 'Hydrocarbon-Based Life'
    elif (planet.climate_type == 'Cold' or
          planet.climate_type == 'Chilly' or
          planet.climate_type == 'Cool' or
          planet.climate_type == 'Normal' or
          planet.climate_type == 'Warm' or
          planet.climate_type == 'Tropical' or
          planet.climate_type == 'Hot'
          ) and (planet.world_type == 'Garden' or planet.world_type == 'Ocean'):
        species.biochemistry = 'Water-Based Life'
    elif (planet.climate_type == 'Cold' or
          planet.climate_type == 'Chilly' or
          planet.climate_type == 'Cool' or
          planet.climate_type == 'Normal' or
          planet.climate_type == 'Warm' or
          planet.climate_type == 'Tropical'
          ) and 'Significant Chlorine' in planet.atmospheric_gases:
            species.biochemistry = 'Chlorine-Based Life'
    elif (
          planet.climate_type == 'Warm' or
          planet.climate_type == 'Tropical' or
          planet.climate_type == 'Hot' or
          planet.climate_type == 'Very Hot' or
          planet.climate_type == 'Infernal'
          ) and 283 <= planet.surface_temperature <= 588.7 and (planet.world_type == 'Sulfur' or 'Significant Sulfur Compounds' in planet.atmospheric_gases):
        species.biochemistry = 'Silicon-Based Life (Sulfuric Acid)'
    elif (planet.climate_type == 'Infernal' and 
          394 <= planet.surface_temperature <= 672 and 
          (planet.world_type == 'Sulfur' or 'Significant Sulfur Compounds' in planet.atmospheric_gases)
         ):
        species.biochemistry = 'Silicon-Based Life (Liquid Sulfur)'
    else:
        return
    
    roll = roll_dice(1)
    if planet.hydrographic_coverage_percent <= 50:
        roll -= 1
    elif planet.hydrographic_coverage_percent >= 90:
        roll += 2
    elif planet.hydrographic_coverage_percent >= 80:
        roll += 1
    
    if roll <= 3:
        species.land_dwelling = True
    else:
        species.water_dwelling = True
    
    if species.land_dwelling == True:
        if planet.hydrographic_coverage_percent >= 100:
            species.habitat_type = 'Island/Beach'
        else:
            roll = roll_dice(3)
            if roll <= 7:
                species.habitat_type = 'Plains'
            elif roll <= 8:
                species.habitat_type = 'Desert'
            elif roll <= 9:
                species.habitat_type = 'Island/Beach'
            elif roll <= 10:
                species.habitat_type = 'Woodlands'
            elif roll <= 11:
                species.habitat_type = 'Swampland'
            elif roll <= 12:
                species.habitat_type = 'Mountain'
            elif roll <= 13:
                species.habitat_type = 'Arctic'
            else:
                species.habitat_type = 'Jungle'
    elif species.water_dwelling == True:
        if planet.hydrographic_coverage_percent <= 0:
            roll = roll_dice(1)
            if roll <= 2:
                species.habitat_type = 'Saltwater Sea'
            elif roll <= 4:
                species.habitat_type = 'Freshwater Lake'
            else:
                species.habitat_type = 'River/Stream'
        else:
            roll = roll_dice(3)
            if roll <= 7:
                species.habitat_type = 'Banks'
            elif roll <= 8:
                species.habitat_type = 'Opean Ocean'
            elif roll <= 9:
                species.habitat_type = 'Freshwater Lake'
            elif roll <= 10:
                species.habitat_type = 'River/Stream'
            elif roll <= 11:
                species.habitat_type = 'Tropical Lagoon'
            elif roll <= 12:
                species.habitat_type = 'Saltwater Sea'
            else:
                species.habitat_type = 'Reef'
    
    roll = roll_dice(3)
    if roll <= 4:
        roll = roll_dice(1)
        if roll <= 3:
            species.trophic_level = 'Autotroph (Photosynthesis)'
        elif roll <= 5:
            species.trophic_level = 'Autotroph (Chemosynthesis)'
        else:
            species.trophic_level = 'Autotroph (Other)'
    elif roll <= 5:
        species.trophic_level = 'Decomposer'
    elif roll <= 6:
        species.trophic_level = 'Scavenger'
    elif roll <= 7:
        species.trophic_level = 'Omnivore'           
    elif roll <= 9:
        species.trophic_level = 'Gathering Herbivore'
    elif roll <= 11:
        species.trophic_level = 'Grazing/Browsing Herbivore'
    elif roll <= 12:
        species.trophic_level = 'Pouncing Carnivore'
    elif roll <= 13:
        species.trophic_level = 'Chasing Carnivore'           
    elif roll <= 14:
        species.trophic_level = 'Trapping Carnivore'
    elif roll <= 15:
        species.trophic_level = 'Hijacking Carnivore'
    elif roll <= 16:
        if species.habitat_type == 'Arctic' or species.habitat_type == 'Desert':
            species.trophic_level = 'Trapping Carnivore'
        else:
            species.trophic_level = 'Filter-Feeder'
    else:
        species.trophic_level = 'Parasite/Symbiont'
    
        
    #Intelligence Check
                
    roll = roll_dice(2)
    if 'Autotroph' in species.trophic_level or species.trophic_level == 'Filter-Feeder' or species.trophic_level == 'Grazing Herbivore':
        roll -= 1
    elif species.trophic_level == 'Omnivore' or species.trophic_level == 'Gathering Herbivore':
        roll += 1
    
    if species.size_category == 'Small':
        roll -= 1
    if species.reproductive_strategy == 'Strong r-Strategy':
        roll -= 1
    elif species.reproductive_strategy == 'Strong K-Strategy':
        roll += 1
    
    if roll <= 3:
        species.intelligence = 'Mindless (IQ 0)'
        species.iq = 0
    elif roll <= 5:
        species.intelligence = 'Preprogrammed (IQ 1, Cannot Learn)'
        species.iq = 1
    elif roll <= 8:
        roll = random.randrange(1,4)
        species.intelligence = 'Low Intelligence (IQ ' + str(roll) + ', Bestial)'
        species.iq = roll
    elif roll <= 10:
        roll = random.randrange(3,6)
        species.intelligence = 'High Intelligence (IQ ' + str(roll) + ', Bestial)'
        species.iq = roll
    elif roll <= 12:
        species.intelligence = 'Presapient (IQ 5)'
        species.iq = 5
    else:
        if planet.world_type == 'Garden' or planet.world_type == 'Ocean':
            species.sapient = True
            planet.homeworld = True
            planet.inhabited_world = True
            roll = roll_dice(1) + 5
            if 'Autotroph' in species.trophic_level or species.trophic_level == 'Filter-Feeder' or species.trophic_level == 'Grazing Herbivore':
                roll -= 1
            elif species.trophic_level == 'Omnivore' or species.trophic_level == 'Gathering Herbivore':
                roll += 1

            if species.size_category == 'Small':
                roll -= 1
            if species.reproductive_strategy == 'Strong r-Strategy':
                roll -= 1
            elif species.reproductive_strategy == 'Strong K-Strategy':
                roll += 1
            
            species.intelligence = 'Sapient Intelligence (IQ ' + str(roll) + ')'
            species.iq = roll
        else:
            if roll_dice(3) >= 18:
                species.sapient = True
                planet.homeworld = True
                planet.inhabited_world = True
                roll = roll_dice(1) + 5
                if 'Autotroph' in species.trophic_level or species.trophic_level == 'Filter-Feeder' or species.trophic_level == 'Grazing Herbivore':
                    roll -= 1
                elif species.trophic_level == 'Omnivore' or species.trophic_level == 'Gathering Herbivore':
                    roll += 1

                if species.size_category == 'Small':
                    roll -= 1
                if species.reproductive_strategy == 'Strong r-Strategy':
                    roll -= 1
                elif species.reproductive_strategy == 'Strong K-Strategy':
                    roll += 1
                
                species.intelligence = 'Sapient Intelligence (IQ ' + str(roll) + ')'
                species.iq = roll
            else:
                species.intelligence = 'Presapient (IQ 5)'
                species.iq = 5

        
    roll = roll_dice(2)
    if (species.trophic_level == 'Pouncing Carnivore' or
        species.trophic_level == 'Chasing Carnivore' or
        species.trophic_level == 'Omnivore' or
        species.trophic_level == 'Gathering Herbivore' or
        species.trophic_level == 'Scavenger'
    ):
        roll += 1
    if species.habitat_type == 'Arctic':
        if roll <= 2:
            species.primary_locomotion = 'Immobile'
        elif roll <= 4:
            species.primary_locomotion = 'Slithering'
        elif roll <= 6:
            species.primary_locomotion = 'Swimming'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 9:
                species.secondary_locomotion = 'Walking'
        elif roll <= 7:
            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
        elif roll <= 9:
            species.primary_locomotion = 'Walking'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
        else:
            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Banks' or species.habitat_type == 'Open Ocean':
        if roll <= 3:
            species.primary_locomotion = 'Immobile'
        elif roll <= 4:
            species.primary_locomotion = 'Floating'
        elif roll <= 5:
            species.primary_locomotion = 'Sailing'
        elif roll <= 8:
            species.primary_locomotion = 'Swimming'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
                roll = roll_dice(2)
                if roll <= 10:
                    species.tertiary_locomotion = 'Swimming'
        else:
            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Reef':
        if roll <= 5:
            species.primary_locomotion = 'Immobile'
        elif roll <= 6:
            species.primary_locomotion = 'Floating'
        elif roll <= 7:
            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Slithering'
                roll = roll_dice(2)
                if roll <= 10:
                    species.tertiary_locomotion = 'Swimming'
            elif roll <= 7:
                species.secondary_locomotion = 'Walking'
                roll = roll_dice(2)
                if roll <= 8:
                    species.tertiary_locomotion = 'Swimming'
            elif roll <= 11:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 9:
            species.primary_locomotion = 'Walking'
            roll = roll_dice(2)
            if roll <= 8:
                species.secondary_locomotion = 'Swimming'
        else:
            species.primary_locomotion = 'Swimming'
    elif species.habitat_type == 'Desert':
        if roll <= 2:
            species.primary_locomotion = 'Immobile'
        elif roll <= 4:
            species.primary_locomotion = 'Slithering'
        elif roll <= 5:
            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
        elif roll <= 8:
            species.primary_locomotion = 'Walking'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
            else:
                species.primary_locomotion = 'Special'
    elif planet.planet_type == 'Gas Giant':
        if roll <= 5:
            species.primary_locomotion = 'Swimming'
        elif roll <= 8:
            species.primary_locomotion = 'Winged Flight'
        else:
            species.primary_locomotion = 'Special (Buoyant Flight)'
    elif species.habitat_type == 'Island/Beach':
        if roll <= 2:
            species.primary_locomotion = 'Immobile'
        elif roll <= 4:
            species.primary_locomotion = 'Slithering'
        elif roll <= 5:
            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
        elif roll <= 7:
            species.primary_locomotion = 'Walking'
        elif roll <= 8:
            species.primary_locomotion = 'Climbing'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
        elif roll <= 9:
            species.primary_locomotion = 'Swimming'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 9:
                species.secondary_locomotion = 'Walking'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
        else:
            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Tropical Lagoon':
        if roll <= 4:
            species.primary_locomotion = 'Immobile'
        elif roll <= 5:
            species.primary_locomotion = 'Floating'
        elif roll <= 6:
            species.primary_locomotion = 'Slithering'
            roll = roll_dice(2)
            if roll <= 10:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 7:
            species.primary_locomotion = 'Walking'
            roll = roll_dice(2)
            if roll <= 8:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 8:
            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Slithering'
                roll = roll_dice(2)
                if roll <= 10:
                    species.tertiary_locomotion = 'Swimming'
            elif roll <= 7:
                species.secondary_locomotion = 'Walking'
                roll = roll_dice(2)
                if roll <= 8:
                    species.tertiary_locomotion = 'Swimming'
            elif roll <= 11:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 9:
            species.primary_locomotion = 'Swimming'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
        else:
            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Freshwater Lake' or species.habitat_type == 'Saltwater Sea':
        if roll <= 3:
            species.primary_locomotion = 'Immobile'
        elif roll <= 4:
            species.primary_locomotion = 'Floating'
        elif roll <= 5:
            species.primary_locomotion = 'Walking'
            roll = roll_dice(2)
            if roll <= 8:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 6:
            species.primary_locomotion = 'Slithering'
            roll = roll_dice(2)
            if roll <= 10:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 9:
            species.primary_locomotion = 'Swimming'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
        else:
            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Mountain':
        if roll <= 2:

            species.primary_locomotion = 'Immobile'

        elif roll <= 4:

            species.primary_locomotion = 'Slithering'

        elif roll <= 5:

            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'

        elif roll <= 7:

            species.primary_locomotion = 'Walking'

        elif roll <= 8:

            species.primary_locomotion = 'Climbing'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
            
        elif roll <= 11:

            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'

        else:

            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Plains':
        if roll <= 2:

            species.primary_locomotion = 'Immobile'

        elif roll <= 4:

            species.primary_locomotion = 'Slithering'

        elif roll <= 5:

            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'

        elif roll <= 8:

            species.primary_locomotion = 'Walking'

        elif roll <= 11:

            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'

        else:

            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'River/Stream':
        if roll <= 3:
            species.primary_locomotion = 'Immobile'
        elif roll <= 4:
            species.primary_locomotion = 'Floating'
        elif roll <= 5:
            species.primary_locomotion = 'Slithering'
            roll = roll_dice(2)
            if roll <= 10:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 6:
            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Slithering'
                roll = roll_dice(2)
                if roll <= 10:
                    species.tertiary_locomotion = 'Swimming'
            elif roll <= 7:
                species.secondary_locomotion = 'Walking'
                roll = roll_dice(2)
                if roll <= 8:
                    species.tertiary_locomotion = 'Swimming'
            elif roll <= 11:
                species.secondary_locomotion = 'Swimming'
        elif roll <= 7:
            species.primary_locomotion = 'Walking'
            roll = roll_dice(2)
            if roll <= 8:
                species.secondary_locomotion = 'Swimming'            
        elif roll <= 9:
            species.primary_locomotion = 'Swimming'
        elif roll <= 11:
            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'
        else:
            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Swampland':
        if roll <= 2:

            species.primary_locomotion = 'Immobile'

        elif roll <= 5:

            species.primary_locomotion = 'Swimming'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 9:
                species.secondary_locomotion = 'Walking'

        elif roll <= 6:

            species.primary_locomotion = 'Slithering'

        elif roll <= 7:

            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'

        elif roll <= 8:

            species.primary_locomotion = 'Walking'

        elif roll <= 9:

            species.primary_locomotion = 'Climbing'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
            
        elif roll <= 11:

            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'

        else:

            species.primary_locomotion = 'Special'
    elif species.habitat_type == 'Woodlands' or species.habitat_type == 'Jungle':
        if roll <= 2:

            species.primary_locomotion = 'Immobile'

        elif roll <= 4:

            species.primary_locomotion = 'Slithering'

        elif roll <= 5:

            species.primary_locomotion = 'Digging'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'

        elif roll <= 7:

            species.primary_locomotion = 'Walking'

        elif roll <= 9:

            species.primary_locomotion = 'Climbing'
            roll = roll_dice(2)
            if roll <= 6:
                species.secondary_locomotion = 'Slithering'
            elif roll <= 11:
                species.secondary_locomotion = 'Walking'
            
        elif roll <= 11:

            species.primary_locomotion = 'Winged Flight'
            roll = roll_dice(2)
            if roll <= 5:
                species.secondary_locomotion = 'Climbing'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 11:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 7:
                species.secondary_locomotion = 'Swimming'
                roll = roll_dice(2)
                if roll <= 6:
                    species.tertiary_locomotion = 'Slithering'
                elif roll <= 9:
                    species.tertiary_locomotion = 'Walking'
            elif roll <= 10:
                species.secondary_locomotion = 'Walking'
            elif roll <= 11:
                species.secondary_locomotion = 'Slithering'

        else:

            species.primary_locomotion = 'Special'

    if species.primary_locomotion == 'Special':
        roll = roll_dice(2)
        if roll <= 3:
            species.primary_locomotion = 'Special (Sliding)'
        elif roll <= 6:
            species.primary_locomotion = 'Special (Buoyant Flight)'
        elif roll <= 9:
            species.primary_locomotion = 'Special (Psionic)'
        else:
            species.primary_locomotion = 'Special (Other)'

    roll = roll_dice(1)
    if isinstance(planet, GasGiant):
        if planet.cloud_top_gravity <= 0.4:
            roll += 2
        elif planet.cloud_top_gravity <= 0.75:
            roll += 1
        elif 1.5 <= planet.cloud_top_gravity <= 2:
            roll -= 1
        elif planet.cloud_top_gravity > 2:
            roll -= 2
    else:
        if planet.surface_gravity <= 0.4:
            roll += 2
        elif planet.surface_gravity <= 0.75:
            roll += 1
        elif 1.5 <= planet.surface_gravity <= 2:
            roll -= 1
        elif planet.surface_gravity > 2:
            roll -= 2
    
    if species.water_dwelling == True:
        roll += 1
    if species.habitat_type == 'Open Ocean' or species.habitat_type == 'Banks' or species.habitat_type == 'Plains':
        roll += 1
    if (species.habitat_type == 'Tropical Lagoon' or 
        species.habitat_type == 'River/Stream' or 
        species.habitat_type == 'Island/Beach' or 
        species.habitat_type == 'Desert' or 
        species.habitat_type == 'Mountain'
    ):
        roll -= 1
    if species.trophic_level == 'Grazing Herbivore':
        roll += 1
    if species.trophic_level == 'Parasite/Symbiont':
        roll -= 4
    if species.primary_locomotion == 'Slithering':
        roll -= 1
    if species.primary_locomotion == 'Winged Flyer':
        roll -= 3
    
    if roll <= 2:
        species.size_category = 'Small'
    elif roll <= 4:
        species.size_category = 'Human-Scale'
    else:
        species.size_category = 'Large'
    
    if species.size_category == 'Small':
        roll = roll_dice(1)
        if roll == 1:
            species.size = 0.05
        elif roll == 2:
            species.size = 0.07
        elif roll == 3:
            species.size = 0.1
        elif roll == 4:
            species.size = 0.15
        elif roll == 5:
            species.size = 0.2
        else:
            species.size = 0.3
    elif species.size_category == 'Human-Scale':
        roll = roll_dice(1)
        if roll == 1:
            species.size = 0.5
        elif roll == 2:
            species.size = 0.7
        elif roll == 3:
            species.size = 1
        elif roll == 4:
            species.size = 1.5
        elif roll == 5:
            species.size = 2
        else:
            species.size = 3
    elif species.size_category == 'Large':
        roll = roll_dice(1)
        if roll == 1:
            species.size = 5
        elif roll == 2:
            species.size = 7
        elif roll == 3:
            species.size = 10
        elif roll == 4:
            species.size = 15
        elif roll == 5:
            species.size = 20
        else:
            species.size = roll_dice(2) * 10
        
    if isinstance(planet, GasGiant):
        if 5 <= planet.cloud_top_gravity:
            species.size = species.size * 0.3
        elif 3.5 <= planet.cloud_top_gravity:
            species.size = species.size * 0.4
        elif 2.5 <= planet.cloud_top_gravity:
            species.size = species.size * 0.5
        elif 2 <= planet.cloud_top_gravity:
            species.size = species.size * 0.6
        elif 1.5 <= planet.cloud_top_gravity:
            species.size = species.size * 0.75
        elif 1.25 <= planet.cloud_top_gravity:
            species.size = species.size * 0.9
        elif 1 <= planet.cloud_top_gravity:
            species.size = species.size * 1
        elif 0.9 <= planet.cloud_top_gravity:
            species.size = species.size * 1.1
        elif 0.8 <= planet.cloud_top_gravity:
            species.size = species.size * 1.2
        elif 0.7 <= planet.cloud_top_gravity:
            species.size = species.size * 1.3
        elif 0.6 <= planet.cloud_top_gravity:
            species.size = species.size * 1.4
        elif 0.5 <= planet.cloud_top_gravity:
            species.size = species.size * 1.6
        elif 0.4 <= planet.cloud_top_gravity:
            species.size = species.size * 1.8
        elif 0.3 <= planet.cloud_top_gravity:
            species.size = species.size * 2.2
        elif 0.2 <= planet.cloud_top_gravity:
            species.size = species.size * 2.9
        else:
            species.size = species.size * 4.6

        if species.biochemistry == 'Hydrogen-Based Life':
            species.mass = ((species.size / 2) ** 3) * 20
        else:
            species.mass = ((species.size / 2) ** 3) * 200

        if species.biochemistry == 'Silicon-Based Life (Sulfuric Acid)' or species.biochemistry == 'Silicon-Based Life (Liquid Sulfur)':
            species.mass *= 2
        
        species.weight = species.mass * planet.cloud_top_gravity
    else:
        if 5 <= planet.surface_gravity:
            species.size = species.size * 0.3
        elif 3.5 <= planet.surface_gravity:
            species.size = species.size * 0.4
        elif 2.5 <= planet.surface_gravity:
            species.size = species.size * 0.5
        elif 2 <= planet.surface_gravity:
            species.size = species.size * 0.6
        elif 1.5 <= planet.surface_gravity:
            species.size = species.size * 0.75
        elif 1.25 <= planet.surface_gravity:
            species.size = species.size * 0.9
        elif 1 <= planet.surface_gravity:
            species.size = species.size * 1
        elif 0.9 <= planet.surface_gravity:
            species.size = species.size * 1.1
        elif 0.8 <= planet.surface_gravity:
            species.size = species.size * 1.2
        elif 0.7 <= planet.surface_gravity:
            species.size = species.size * 1.3
        elif 0.6 <= planet.surface_gravity:
            species.size = species.size * 1.4
        elif 0.5 <= planet.surface_gravity:
            species.size = species.size * 1.6
        elif 0.4 <= planet.surface_gravity:
            species.size = species.size * 1.8
        elif 0.3 <= planet.surface_gravity:
            species.size = species.size * 2.2
        elif 0.2 <= planet.surface_gravity:
            species.size = species.size * 2.9
        else:
            species.size = species.size * 4.6

        if species.biochemistry == 'Hydrogen-Based Life':
            species.mass = ((species.size / 2) ** 3) * 20
        else:
            species.mass = ((species.size / 2) ** 3) * 200

        if species.biochemistry == 'Silicon-Based Life (Sulfuric Acid)' or species.biochemistry == 'Silicon-Based Life (Liquid Sulfur)':
            species.mass *= 2
        
        species.weight = species.mass * planet.surface_gravity
    
    species.strength = round(2 * math.cbrt(species.weight))
    if species.primary_locomotion == 'Winged Flight':
        species.wingspan = round(math.sqrt((species.weight / 30)) * 10, 2)
    
    #Lifespan
    
    life_dict = {
        0 : 'Short Lifespan 4',
        1 : 'Short Lifespan 4',
        2 : 'Short Lifespan 3',
        3 : 'Short Lifespan 2',
        4 : 'Short Lifespan 1',
        5 : 'Average Lifespan',
        6 : 'Extended Lifespan 1',
        7 : 'Extended Lifespan 2',
        8 : 'Extended Lifespan 3'
    }
    lifespan = 4
    if species.size <= 0.3:
        lifespan = 1
    elif species.size <= 0.56:
        lifespan = 2
    elif species.size <= 1.5:
        lifespan = 3
    elif species.size >= 6:
        lifespan = 6
    
    if species.sapient == True:
        lifespan += 1
    if 'Ammonia' in species.biochemistry or 'Hydrogen' in species.biochemistry:
        lifespan += 1
    if 'Silicon' in species.biochemistry or 'Hot' in planet.climate_type or planet.climate_type == 'Infernal':
        lifespan -= 1
    
    species.lifespan = life_dict[lifespan]

    #Alien Creation V onwards
    roll = roll_dice(2)
    if species.primary_locomotion == 'Immobile' or species.primary_locomotion == 'Special (Buoyant Flight)':
        roll += 1
    
    if roll <= 7:
        species.symmetry = 'Bilateral'
        species.number_of_sides = 2
    elif roll <= 8:
        species.symmetry = 'Trilateral'
        species.number_of_sides = 3
    elif roll <= 9:
        roll = roll_dice(1) + 3
        species.symmetry = str(roll) + '-Sided Radial'
        species.number_of_sides = roll
    elif roll <= 10:
        roll = roll_dice(1)
        spherical_dict = {
            1 : 4,
            2 : 6,
            3 : 6,
            4 : 8,
            5 : 12,
            6 : 20
        }
        species.symmetry = str(spherical_dict[roll]) + '-Sided Spherical'
        species.number_of_segments = 1
        species.number_of_sides = spherical_dict[roll]
        species.number_of_limbs = spherical_dict[roll]
    else:
        species.symmetry = 'Asymmetric'
        species.number_of_sides = roll_dice(2) - 2
        species.number_of_segments = roll_dice(2) - 2
        species.number_of_limbs = roll_dice(2) - 2
    
    if not 'Spherical' in species.symmetry and species.symmetry != 'Asymmetric':
        roll = roll_dice(1)
        if species.symmetry == 'Trilateral':
            roll -= 1
        elif species.symmetry == 'Radial':
            roll -= 2

        if roll <= 1:
            species.number_of_segments = 1
            species.number_of_limbs = 0
        elif roll <= 2:
            species.number_of_segments = 1
            species.number_of_limbs = species.number_of_sides
        elif roll <= 3:
            species.number_of_segments = 2
            species.number_of_limbs = species.number_of_sides * 2
        elif roll <= 4:
            species.number_of_segments = roll_dice(1)
            species.number_of_limbs = species.number_of_sides * species.number_of_segments
        elif roll <= 5:
            species.number_of_segments = roll_dice(2)
            species.number_of_limbs = species.number_of_sides * species.number_of_segments
        else:
            species.number_of_segments = roll_dice(3)
            species.number_of_limbs = species.number_of_sides * species.number_of_segments

    if not 'Spherical' in species.symmetry:
        roll = roll_dice(1)
        if (species.primary_locomotion == 'Swimming' or
            species.secondary_locomotion == 'Swimming' or
            species.tertiary_locomotion == 'Swimming'):
            roll += 1
        
        if roll >= 5:
            species.tail = True
            create_tail_features(species)

    roll = generate_manipulator_roll(species, planet)
    
    create_manipulators(species, planet, roll)
    
    roll = roll_dice(2)
    if species.size_category == 'Human-Scale':
        roll += 1
    elif species.size_category == 'Large':
        roll += 2
    
    if species.land_dwelling == True:
        roll += 1
    
    if species.primary_locomotion == 'Immobile' or species.primary_locomotion == 'Slithering':
        roll -= 1
    
    if species.symmetry == 'Asymmetric':
        roll -= 1
    
    if isinstance(planet, GasGiant) == True:
        if planet.cloud_top_gravity <= 0.5:
            roll -= 1
        elif planet.cloud_top_gravity >= 1.25:
            roll += 1
    else:
        if planet.surface_gravity <= 0.5:
            roll -= 1
        elif planet.surface_gravity >= 1.25:
            roll += 1

    if roll <= 3:
        species.skeleton_type = 'No Skeleton'
    if roll <= 5:
        species.skeleton_type = 'Hydrostatic Skeleton'
    elif roll <= 7:
        species.skeleton_type = 'External Skeleton'
    elif roll <= 10:
        species.skeleton_type = 'Internal Skeleton'
    else:
        roll = roll_dice(1)
        if roll <= 2:
            species.skeleton_type = 'Combination Hydrostatic-External Skeleton'
        elif roll <= 4:
            species.skeleton_type = 'Combination Hydrostatic-Internal Skeleton'
        else:
            species.skeleton_type = 'Combination External-Internal Skeleton'
    

    #To Do - Alien Creation VI
    if species.skeleton_type == 'External Skeleton' or species.skeleton_type == 'Combination Hydrostatic-External Skeleton':
        roll = roll_dice(2)
        if species.water_dwelling == True:
            roll += 1
        if species.primary_locomotion == 'Immobile':
            roll += 1
        elif species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
            roll -= 2

        species.outer_covering_type == 'Exoskeleton'
        if roll <= 2:
            species.skin_type = 'Light Exoskeleton (DR 0)'
        elif roll <= 4:
            species.skin_type = 'Tough Exoskeleton (DR 1)'
        elif roll <= 5:
            species.skin_type = 'Heavy Exoskeleton (DR 3)'
        else:
            species.skin_type = 'Armour Shell (DR 5)'
    else:
        if not species.skeleton_type == 'Combination External-Internal Skeleton':
            roll = random.randrange(1,6)
        else:
            roll = roll_dice(1)
        
        if roll <= 2:
            species.outer_covering_type = 'Skin'
            roll = roll_dice(2)
            if species.habitat_type == 'Arctic':
                roll += 1
            elif species.habitat_type == 'Desert':
                roll -= 1
            if species.water_dwelling == True:
                roll += 1

            if (species.trophic_level == 'Gathering Herbivore' or
                species.trophic_level == 'Grazing Herbivore' or
                species.trophic_level == 'Grazing/Browsing Herbivore'):
                roll += 1
            
            if species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
                roll -= 5
            
            if roll <= 4:
                species.skin_type = 'Soft Skin'
            elif roll <= 5:
                species.skin_type = 'Normal Skin'
            elif roll <= 7:
                species.skin_type = 'Hide (DR 1)'
            elif roll <= 8:
                species.skin_type = 'Thick Hide (DR 2)'
            elif roll <= 9:
                species.skin_type = 'Armour Shell (DR 5)'
            else:
                species.skin_type = 'Blubber (DR 4 and ' + str(roll_dice(1)) + ' levels Temperature Tolerance)'

        elif roll <= 3:
            species.outer_covering_type = 'Scales'
            roll = roll_dice(2)

            if species.habitat_type == 'Desert':
                roll += 1
            
            if (species.trophic_level == 'Gathering Herbivore' or
                species.trophic_level == 'Grazing Herbivore' or
                species.trophic_level == 'Grazing/Browsing Herbivore'):
                roll += 1
            
            if species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
                roll -= 2
            
            if species.primary_locomotion == 'Digging':
                roll -= 1
            
            if roll <= 3:
                species.skin_type = 'Normal Skin'
            elif roll <= 8:
                species.skin_type = 'Scales (DR 1)'
            elif roll <= 10:
                species.skin_type = 'Heavy Scales (DR 3)'
            elif roll <= 14:
                species.skin_type = 'Armour Shell (DR 5)'
               
        elif roll <= 4:
            species.outer_covering_type = 'Fur'
            roll = roll_dice(2)

            if species.habitat_type == 'Desert':
                roll -= 1
            elif species.habitat_type == 'Arctic':
                roll += 1
            
            if (species.trophic_level == 'Gathering Herbivore' or
                species.trophic_level == 'Grazing Herbivore' or
                species.trophic_level == 'Grazing/Browsing Herbivore'):
                roll += 1
            
            if species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
                roll -= 1
            
            if roll <= 5:
                species.skin_type = 'Normal Skin'
            elif roll <= 7:
                species.skin_type = 'Fur'
            elif roll <= 9:
                species.skin_type = 'Thick Fur (1 Level Temperature Tolerance)'
            elif roll <= 11:
                species.skin_type = 'Thick Fur Over Hide (DR 1 and 1 Level Temperature Tolerance)'
            else:
                species.skin_type = 'Spines'

        elif roll <= 5:
            species.outer_covering_type = 'Feathers'
            roll_dice(2)
            if species.habitat_type == 'Desert':
                roll -= 1
            elif species.habitat_type == 'Arctic':
                roll += 1
            
            if species.primary_locomotion == 'Winged Flight':
                roll += 1
            
            if roll <= 5:
                species.skin_type = 'Normal Skin'
            elif roll <= 8:
                species.skin_type = 'Feathers (1 Level Temperature Tolerance)'
            elif roll <= 10:
                species.skin_type = 'Thick Feathers (2 Levels Temperature Tolerance)'
            elif roll <= 11:
                species.skin_type = 'Feathers Over Hide (DR 1 and 1 Level Temperature Tolerance)'
            else:
                species.skin_type = 'Spines'

        else:
            species.outer_covering_type = 'Exoskeleton'
            roll = roll_dice(2)
            if species.water_dwelling == True:
                roll += 1
            if species.primary_locomotion == 'Immobile':
                roll += 1
            elif species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
                roll -= 2
                
            if roll <= 2:
                species.skin_type = 'Light Exoskeleton (DR 0)'
            elif roll <= 4:
                species.skin_type = 'Tough Exoskeleton (DR 1)'
            elif roll <= 5:
                species.skin_type = 'Heavy Exoskeleton (DR 3)'
            else:
                species.skin_type = 'Armour Shell (DR 5)'
        
    if species.water_dwelling == False and not (species.habitat_type == 'Arctic' or 
                                                species.habitat_type == 'Swampland' or 
                                                species.habitat_type == 'Island/Beach'):
        species.breathing_method = 'Lungs'
    else:
        roll = roll_dice(2)
        
        if (species.habitat_type == 'Arctic' or
            species.habitat_type == 'Swampland' or
            species.habitat_type == 'River/Stream' or
            species.habitat_type == 'Island/Beach' or
            species.habitat_type == 'Tropical Lagoon'
            ):
            roll += 1
        
        if species.primary_locomotion == 'Walking' or species.secondary_locomotion == 'Walking':
            roll += 1
        elif species.secondary_locomotion == 'Climbing':
            roll += 2

        if roll <= 6:
            species.breathing_method = 'Gills'
        elif roll <= 8:
            species.breathing_method = 'Lungs (Oxygen Storage)'
        elif roll <= 10:
            species.breathing_method = 'Gills and Lungs'
        else:
            species.breathing_method = 'Lungs'
        
    roll = roll_dice(2)

    if (species.breathing_method == 'Lungs' or
        species.breathing_method == 'Lungs (Oxygen Storage)'
        ):
        roll += 1
    elif species.breathing_method == 'Gills':
        roll -= 1
    
    if species.size_category == 'Human-Scale' or species.size_category == 'Large':
        roll += 1
    
    if species.land_dwelling == True:
        roll += 1
    
    if species.habitat_type == 'Woodlands' or species.habitat_type == 'Mountain':
        roll += 1
    elif species.habitat_type == 'Arctic':
        roll += 2

    if roll <= 4:
        species.temperature_regulation = 'Cold-Blooded (Cold-Blooded Disadvantage)'
    elif roll <= 6:
        species.temperature_regulation = 'Cold-Blooded (No Disadvantage)'
    elif roll <= 7:
        species.temperature_regulation = 'Partial Regulation (Temperature Variation Within Limits)'
    elif roll <= 9:
        species.temperature_regulation = 'Warm-Blooded'
    else:
        species.temperature_regulation = 'Warm-Blooded (Metabolism Control 2)'
    
    roll = roll_dice(2)
    if species.skeleton_type == 'External Skeleton' or species.skeleton_type == 'Combination Hydrostatic-External Skeleton':
        roll -= 2
    elif species.skeleton_type == 'Combination External-Internal Skeleton':
        roll -= 1
    
    if species.size_category == 'Large':
        roll += 1
    
    if species.primary_locomotion == 'Immobile':
        roll += 1
    
    if roll <= 4:
        species.growth_pattern = 'Metamorphosis'
    elif roll <= 6:
        species.growth_pattern = 'Molting'
    elif roll <= 11:
        species.growth_pattern = 'Continuous Growth'
    else:
        species.growth_pattern = 'Unusual Growth Pattern'
    

    #Alien Creation VII
        
    roll = roll_dice(2)

    if species.primary_locomotion == 'Immobile':
        roll -= 1
    if species.symmetry == 'Asymmetric':
        roll -= 1
    if (species.trophic_level == 'Autotroph (Chemosynthesis)' or 
        species.trophic_level == 'Autotroph (Other)' or 
        species.trophic_level == 'Autotroph (Photosynthesis)'
        ):
        roll -= 1
    
    if roll <= 4:
        if roll_dice(1) <= 3:
            species.number_of_sexes = 'Asexual Reproduction'
        else:
            species.number_of_sexes = 'Parthenogenesis'
    elif roll <= 6:
        species.number_of_sexes = 'Simultaneous Hermaphroditic Reproduction'
    elif roll <= 9:
        species.number_of_sexes = 'Sexual Reproduction (2 Sexes)'
    elif roll <= 10:
        species.number_of_sexes = 'Sequential Hermaphroditic Reproduction'
    elif roll <= 11:
        roll = roll_dice(1)
        if roll <= 3:
            species.number_of_sexes = 'Sexual Reproduction (3 Sexes)'
        elif roll <= 5:
            species.number_of_sexes = 'Sexual Reproduction (4 Sexes)'
        else:
            species.number_of_sexes = 'Sexual Reproduction (' + str(roll_dice(2)) + ' Sexes)'
    else:
        roll = random.randrange(1,10)
        
        if roll == 1:
            species.number_of_sexes = 'Asexual Reproduction/Simultaneous Hermaphroditic Reproduction'
        elif roll == 2:
            species.number_of_sexes = 'Parthenogenesis/Simultaneous Hermaphroditic Reproduction'
        elif roll == 3:
            species.number_of_sexes = 'Asexual Reproduction/Sequential Hermaphroditic Reproduction'
        elif roll == 4:
            species.number_of_sexes = 'Parthenogenesis/Sequential Hermaphroditic Reproduction'
        elif roll == 5:
            species.number_of_sexes = 'Simultaneous Hermaphroditic Reproduction/Sequential Hermaphroditic Reproduction'
        elif roll == 6:
            species.number_of_sexes = 'Asexual Reproduction/Sexual Reproduction (' + str(roll_dice(2)) + ' Sexes)'
        elif roll == 7:
            species.number_of_sexes = 'Parthenogenesis/Sexual Reproduction (' + str(roll_dice(2)) + ' Sexes)'
        elif roll == 8:
            species.number_of_sexes = 'Simultaneous Hermaphroditic Reproduction/Sexual Reproduction (' + str(roll_dice(2)) + ' Sexes)'
        else:
            species.number_of_sexes = 'Sequential Hermaphroditic Reproduction/Sexual Reproduction (' + str(roll_dice(2)) + ' Sexes)'
    
    roll = roll_dice(2)

    if species.water_dwelling == True or species.breathing_method == 'Gills and Lungs':
        roll -= 1
    
    if species.primary_locomotion == 'Immobile':
        roll -= 2

    if species.temperature_regulation == 'Warm-Blooded (Metabolism Control 2)' or species.temperature_regulation == 'Warm-Blooded':
        roll += 1

    if roll <= 6:
        species.gestation_method = 'Spawning/Pollinating'
    elif roll <= 8:
        species.gestation_method = 'Egg-Laying'
    elif roll <= 10:
        species.gestation_method = 'Live-Bearing'
    else:
        species.gestation_method = 'Live-Bearing With Pouch'
    
    if roll_dice(2) == 12:
        roll = roll_dice(1)
        
        if roll <= 1:
            species.special_gestation_method = 'Brood Parasite'
        elif roll <= 3:
            species.special_gestation_method = 'Parasitic Young'
        elif roll <= 5:
            species.special_gestation_method = 'Cannibalistic Young (Young Consume Parent)'
        else:
            species.special_gestation_method = 'Cannibalistic Young (Young Consume Each Other)'

    roll = roll_dice(2)
    if species.size_category == 'Large':
        roll -= 2
    elif species.size_category == 'Small':
        roll += 1
    
    if species.gestation_method == 'Spawning/Pollinating':
        roll += 2

    if roll <= 4:
        species.reproductive_strategy = 'Strong K-Strategy'
        species.number_of_offspring = 1
    elif roll <= 6:
        species.reproductive_strategy = 'Moderate K-Strategy'
        species.number_of_offspring = random.randrange(1,3)
    elif roll <= 7:
        species.reproductive_strategy = 'Median Strategy'
        species.number_of_offspring = roll_dice(1)
    elif roll <= 9:
        species.reproductive_strategy = 'Moderate r-Strategy'
        species.number_of_offspring = roll_dice(1) + 1
    else:
        species.reproductive_strategy = 'Strong r-Strategy'
        species.number_of_offspring = roll_dice(2)
    
    if species.gestation_method == 'Spawning/Pollinating':
        species.number_of_offspring *= (roll_dice(2) * 10)
    

    roll = roll_dice(3)
    if species.water_dwelling == True:
        roll -= 2
    if (species.trophic_level == 'Autotroph (Chemosynthesis)' or
        species.trophic_level == 'Autotroph (Other)' or
        species.trophic_level == 'Autotroph (Photosynthesis)'
    ):
        roll += 2
    
    if roll <= 7:
        species.primary_sense = 'Hearing'
    elif roll <= 12:
        species.primary_sense = 'Vision'
    else:
        species.primary_sense = 'Touch and Taste'
    

    high_communication_channel = 0
    low_communication_channel = 0
    roll = roll_dice(3)

    if species.primary_sense == 'Vision':
        roll += 4
    
    if species.primary_locomotion == 'Digging':
        roll -= 4
    if species.primary_locomotion == 'Climbing' or species.secondary_locomotion == 'Climbing':
        roll += 2
    if species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
        roll += 3
    if species.primary_locomotion == 'Immobile':
        roll -= 4
    if species.trophic_level == 'Filter-Feeder':
        roll -= 2
    if (species.trophic_level == 'Chasing Carnivore' or
        species.trophic_level == 'Pouncing Carnivore' or
        species.trophic_level == 'Scavenger' or
        species.trophic_level == 'Trapping Carnivore' or
        species.trophic_level == 'Hijacking Carnivore' or
        species.trophic_level == 'Gathering Herbivore'
        ):
        roll += 2
    
    if roll <= 6:
        species.vision = 'Completely Blind'
    elif roll <= 7:
        species.vision = 'Nearly Blind'
    elif roll <= 9:
        species.vision = 'Bad Sight and Colourblindness'
    elif roll <= 11:
        if roll_dice(1) <= 3:
            species.vision = 'Bad Sight'
        else:
            species.vision = 'Colourblindness'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Vision'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Vision'
    elif roll <= 14:   
        species.vision = 'Normal Vision'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Vision'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Vision'
    else:
        species.vision = 'Telescopic Vision 4'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Vision'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Vision'
    
    #Hearing
    
    roll = roll_dice(3)
    if species.primary_sense == 'Hearing':
        roll += 4
    if species.vision == 'Completely Blind' or species.vision == 'Nearly Blind':
        roll += 2
    if species.vision == 'Bad Sight' or species.vision == 'Bad Sight and Colourblindness':
        roll += 1
    if species.water_dwelling == True:
        roll += 1
    if species.primary_locomotion == 'Immobile':
        roll -= 4
    
    if roll <= 6:
        species.hearing = 'Deafness'
    elif roll <= 8:
        species.hearing = 'Hard of Hearing'
    elif roll <= 10:
        species.hearing = 'Normal Hearing'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Hearing'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Hearing'
    elif roll <= 11:
        if species.size_category == 'Large':
            species.hearing = 'Normal Hearing (Subsonic Hearing)'
        else:
            species.hearing = 'Normal Hearing (Ultrahearing)'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Hearing'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Hearing'
    elif roll <= 12:
        species.hearing = 'Acute Hearing 4'
        if roll + 1 > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Hearing'
        elif roll + 1 > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Hearing'
    elif roll <= 13:
        if species.size_category == 'Large':
            species.hearing = 'Acute Hearing 4 (Subsonic Hearing)'
        else:
            species.hearing = 'Acute Hearing 4 (Ultrahearing)'
        if roll + 1 > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Hearing'
        elif roll + 1 > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Hearing'
    else:
        species.hearing = 'Acute Hearing 4 (Ultrasonic Hearing, Sonar)'
        if roll + 1 > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Hearing'
        elif roll + 1 > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Hearing'
    
    #Touch
    roll = roll_dice(2)
    if species.primary_sense == 'Touch and Taste':
        roll += 4
    if (species.skeleton_type == 'External Skeleton' or 
        species.skeleton_type == 'Combination Hydrostatic-External Skeleton' or
        species.skeleton_type == 'Combination External-Internal Skeleton'
        ):
        roll -= 2
    if species.water_dwelling == True:
        roll += 2
    if species.primary_locomotion == 'Digging':
        roll += 2
    if species.primary_locomotion == 'Winged Flight' or species.primary_locomotion == 'Special (Buoyant Flight)':
        roll -= 2
    if species.vision == 'Completely Blind' or species.vision == 'Nearly Blind':
        roll += 2
    if species.trophic_level == 'Trapping Carnivore':
        roll += 1
    if species.size_category == 'Small':
        roll += 1
    
    if roll <= 2:
        species.touch = 'Numb'
    elif roll <= 4:
        species.touch = 'Poor Sense of Touch (-2 DX)'
    elif roll <= 6:
        species.touch = 'Poor Sense of Touch (-1 DX)'
    elif roll <= 8:
        species.touch = 'Human-Level Touch'
    elif roll <= 10:
        species.touch = 'Acute Touch 4'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Touch'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Touch'
    else:
        if roll_dice(1) <= 3:
            species.touch = 'Acute Touch 4 (Sensitive Touch)'
        else:
            species.touch = 'Acute Touch 4 (Vibration Sense)'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Touch'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Touch'
    
    roll = roll_dice(2)
    if species.trophic_level == 'Chasing Carnivore':
        roll += 2
    elif species.trophic_level == 'Gathering Herbivore':
        roll += 2
    elif species.trophic_level == 'Filter-Feeder' or 'Autotroph' in species.trophic_level or species.trophic_level == 'Trapping Carnivore':
        roll -= 2
    
    if 'Sexual Reproduction' in species.number_of_sexes:
        roll += 2
    
    if species.primary_locomotion == 'Immobile':
        roll -= 4
    
    if roll <= 3:
        species.taste_smell = 'No Sense of Taste or Smell'
    elif roll <= 5:
        species.taste_smell = 'No Sense of Smell'
    elif roll <= 8:
        species.taste_smell = 'Normal Sense of Taste and Smell'
    elif roll <= 10:
        if species.water_dwelling == True:
            species.taste_smell = 'Acute Sense of Taste 4 and Normal Sense of Smell'
        else:
            species.taste_smell = 'Acute Sense of Taste and Smell 4'
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Taste/Smell'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Taste/Smell'
    else:
        if species.water_dwelling == True:
            species.taste_smell = 'Acute Sense of Taste and Smell 4 (Discriminatory Taste)'
        else:
            species.taste_smell = 'Acute Sense of Taste and Smell 4 (Discriminatory Smell)'
    
    #Special Sense
    roll = roll_dice(2)
    if species.habitat_type == 'Plains' or species.habitat_type == 'Desert':
        roll += 1
    if 'Herbivore' in species.trophic_level:
        roll += 1
    if 'Spherical' in species.symmetry or 'Radial' in species.symmetry:
        roll += 1
    
    if roll >= 11:
        species.special_senses.append('360 Degree Vision')
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Vision'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Vision'

    roll = roll_dice(2)
    if species.habitat_type == 'Opean Ocean':
        roll += 1
    if 'Flight' in species.primary_locomotion:
        roll += 1
    if species.primary_locomotion == 'Digging':
        roll += 1
    
    if roll >= 11:
        species.special_senses.append('Absolute Direction')
    
    roll = roll_dice(2)
    if 'Sonar' in species.hearing:
        roll += 2
    if roll >= 11:
        species.special_senses.append('Discriminatory Hearing')
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Hearing'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Hearing'
    
    roll = roll_dice(2)
    if species.habitat_type == 'Plains' or species.habitat_type == 'Desert':
        roll += 1
    if 'Herbivore' in species.trophic_level:
        roll += 2
    if roll >= 10:
        species.special_senses.append('Peripheral Vision')
    
    roll = roll_dice(2)
    if species.water_dwelling == True:
        roll += 2
    if 'Carnivore' in species.trophic_level or species.trophic_level == 'Scavenger':
        roll += 2
    if roll >= 11:
        species.special_senses.append('Night Vision ' + str(roll_dice(1) + 3))
        if roll > high_communication_channel:
            high_communication_channel = roll
            species.primary_communication_channel = 'Vision'
        elif roll > low_communication_channel:
            low_communication_channel = roll
            species.secondary_communication_channel = 'Vision'
    
    roll = roll_dice(2)
    if not species.water_dwelling == True and not 'Ammonia' in species.biochemistry:
        if roll >= 11:
            species.special_senses.append('Ultravision')
            if roll > high_communication_channel:
                high_communication_channel = roll
                species.primary_communication_channel = 'Vision'
            elif roll > low_communication_channel:
                low_communication_channel = roll
                species.secondary_communication_channel = 'Vision'
    
    roll = roll_dice(2)
    if 'Carnivore' in species.trophic_level or species.trophic_level == 'Scavenger':
        roll += 1
    if species.habitat_type == 'Arctic':
        roll += 1
    
    if not species.water_dwelling == True:
        if roll >= 11:
            species.special_senses.append('Detect (Heat)')
            if roll > high_communication_channel:
                high_communication_channel = roll
                species.primary_communication_channel = 'Temperature'
            elif roll > low_communication_channel:
                low_communication_channel = roll
                species.secondary_communication_channel = 'Temperature'
    
    roll = roll_dice(2)
    if 'Carnivore' in species.trophic_level or species.trophic_level == 'Scavenger':
        roll += 1
    if species.water_dwelling == True:
        if roll >= 11:
            species.special_senses.append('Detect (Electric Fields)')
            if roll > high_communication_channel:
                high_communication_channel = roll
                species.primary_communication_channel = 'Electric Fields'
            elif roll > low_communication_channel:
                low_communication_channel = roll
                species.secondary_communication_channel = 'Electric Fields'

    roll = roll_dice(2)
    if species.primary_locomotion == 'Climbing' or species.secondary_locomotion == 'Cimbing':
        roll += 2
    if species.habitat_type == 'Mountain':
        roll += 1
    if planet.surface_gravity <= 0.5:
        roll -= 1
    if planet.surface_gravity >= 1.5:
        roll += 1
    
    if species.land_dwelling == True:
        if roll >= 11:
            species.special_senses.append('Perfect Balance')
    
    roll = roll_dice(2)
    if not species.size_category == 'Small' or not species.water_dwelling == True:
        if roll >= 11:
            species.special_senses.append('Scanning Sense (Radar)')
            if roll > high_communication_channel:
                high_communication_channel = roll
                species.primary_communication_channel = 'Radar'
            elif roll > low_communication_channel:
                low_communication_channel = roll
                species.secondary_communication_channel = 'Radar'


    if 'Psionic' in species.primary_locomotion:
        species.psionic = True
    else:
        if species.sapient == True:
            if random.randrange(1,6) == 5:
                species.psionic = True
        else:
            if random.randrange(1,5001) == 5000:
                species.psionic = True
    
    
    roll = roll_dice(2)
    if 'Hermaphroditic Reproduction' in species.number_of_sexes:
        roll -= 2
    
    if 'Spawning' in species.gestation_method:
        roll -= 1
    elif 'Live-Bearing' in species.gestation_method:
        roll += 1

    if species.reproductive_strategy == 'Strong r-Strategy':
        roll -= 1
    elif species.reproductive_strategy == 'Strong K-Strategy':
        roll += 1
    
    if roll <= 5:
        species.mating_behaviour = 'Mating Only, No Pair Bond'
    elif roll <= 7:
        species.mating_behaviour = 'Temporary Pair Bond'
    elif roll <= 8:
        species.mating_behaviour = 'Permanent Pair Bond'
    elif roll <= 10:
        species.mating_behaviour = 'Harem'
    else:
        species.mating_behaviour = 'Hive'
    
    roll = roll_dice(2)
    if 'Carnivore' in species.trophic_level or species.trophic_level == 'Scavenger':
        roll -= 1
    elif species.trophic_level == 'Grazing Herbivore':
        roll += 1
    if species.size_category == 'Large':
        roll -= 1
    if species.mating_behaviour == 'Harem':
        roll += 1
    elif 'No Pair Bond' in species.mating_behaviour:
        roll -= 1
    
    if species.mating_behaviour == 'Hive':
        species.social_organisation == 'Hive Mind'
    else:
        if roll <= 6:
            species.social_organisation = 'Solitary'
        elif roll <= 8:
            species.social_organisation = 'Pair-Bonded'
        elif roll <= 10:
            roll = roll_dice(1)
            if roll <= 2:
                species.social_organisation = 'Troop of ' + str(roll_dice(2)) + ' Members'
            elif roll <= 4:
                species.social_organisation = 'Small Pack of ' + str(roll_dice(2)) + ' Members'
            else:
                species.social_organisation = 'Small Herd of ' + str(roll_dice(2)) + ' Members'
        elif roll <= 11:
            roll = roll_dice(1)
            if roll <= 2:
                species.social_organisation = 'Pack of ' + str(roll_dice(4)) + ' Members'
            else:
                species.social_organisation = 'Herd of ' + str(roll_dice(4)) + ' Members'
        else:
            species.social_organisation = 'Large Herd of ' + str(roll_dice(1) * 10) + ' Members'


    #Chauvinism
    chauv = 0
    if 'Autotroph' in species.trophic_level or species.trophic_level == 'Filter-Feeder':
        chauv -= 1
    if 'Parasite' in species.trophic_level or species.trophic_level == 'Scavenger':
        chauv -= 2
    if ('Troop' in species.social_organisation or 
        ('Herd' in species.social_organisation and not 'Large' in species.social_organisation) or 
        species.social_organisation == 'Hive Mind'
        ):
        chauv += 2
    if 'Asexual' in species.number_of_sexes or 'Spawning' in species.gestation_method:
        chauv -= 1
    if species.social_organisation == 'Solitary' or species.social_organisation == 'Pair Bonded':
        chauv -= 1

    concen = 0
    if species.trophic_level == 'Pouncing Carnivore' or species.trophic_level == 'Chasing Carnivore':
        concen += 1
    if 'Herbivore' in species.trophic_level:
        concen -= 1
    if species.reproductive_strategy == 'Strong K-Strategy':
        roll += 1
    
    curio = 0
    if species.trophic_level == 'Omnivore':
        curio += 1
    elif species.trophic_level == 'Grazing Herbivore' or species.trophic_level == 'Filter-Feeder':
        curio -= 1
    if species.vision == 'Completely Blind' or species.vision == 'Nearly Blind':
        curio -= 1
    if species.reproductive_strategy == 'Strong r-Strategy':
        curio -= 1
    elif species.reproductive_strategy == 'Strong K-Strategy':
        curio += 1
    
    ego = 0
    if species.social_organisation == 'Solitary':
        ego += 1
    if species.mating_behaviour == 'Harem':
        ego += 1
    if species.mating_behaviour == 'Hive':
        ego -= 1
    if species.reproductive_strategy == 'Strong K-Strategy':
        ego += 1
    if species.reproductive_strategy == 'Strong r-Strategy':
        ego -= 1
    
    emp = 0
    if species.trophic_level == 'Chasing Carnivore':
        emp += 1
    elif ('Autotroph' in species.trophic_level or
          species.trophic_level == 'Filter-Feeder' or
          'Grazing' in species.trophic_level or
          species.trophic_level == 'Scavenger'
          ):
        emp -= 1
    if species.social_organisation == 'Solitary' or species.social_organisation == 'Pair-Bonded':
        emp -= 1
    if ('Troop' in species.social_organisation or 
        ('Herd' in species.social_organisation and not 'Large' in species.social_organisation)
        ):
        emp += 1
    if species.reproductive_strategy == 'Strong K-Strategy':
        emp += 1
    
    greg = 0
    if (species.trophic_level == 'Pouncing Carnivore' or
        species.trophic_level == 'Filter-Feeder' or
        'Autotroph' in species.trophic_level or
        'Herbivore' in species.trophic_level
    ):
        greg -= 1
    if species.social_organisation == 'Solitary' or species.social_organisation == 'Pair-Bonded':
        greg -= 1
    if ('Pack' in species.social_organisation or 'Herd' in species.social_organisation) and not 'Small' in species.social_organisation:
        greg += 1
    if species.social_organisation == 'Hive Mind':
        greg += 2
    if 'Asexual' in species.number_of_sexes or 'Hermaphroditic' in species.number_of_sexes:
        greg -= 1
    if 'Spawning' in species.gestation_method:
        greg -= 1
    
    imag = 0
    if (species.trophic_level == 'Pouncing Carnivore' or
        species.trophic_level == 'Omnivore' or
        species.trophic_level == 'Gathering Herbivore'
    ):
        imag += 1
    elif ('Autotroph' in species.trophic_level or
          species.trophic_level == 'Filter-Feeder' or
          'Grazing' in species.trophic_level
        ):
        imag -= 1
    if species.reproductive_strategy == 'Strong K-Strategy':
        imag += 1
    elif species.reproductive_strategy == 'Strong r-Strategy':
        imag -= 1
    
    sus = 0
    if 'Carnivore' in species.trophic_level:
        sus -= 1
    elif 'Grazing' in species.trophic_level:
        sus += 1
    if species.vision == 'Completely Blind' or species.vision == 'Nearly Blind':
        sus += 1
    if species.size_category == 'Large':
        sus -= 1
    elif species.size_category == 'Small':
        sus += 1
    if species.social_organisation == 'Solitary' or species.social_organisation == 'Pair-Bonded':
        sus += 1
    
    play = 0
    if 'K-Strategy' in species.reproductive_strategy:
        play += 1
    if species.reproductive_strategy == 'Strong K-Strategy':
        play += 2
    if species.iq >= 2:
        play += 1
    if species.social_organisation == 'Solitary':
        play -= 1
    if 'Cannot Learn' in species.intelligence:
        play -= 3

    if chauv >= 3:
        if emp < 1 or sus > -1:
            if sus > 1:
                species.chauvinism = 'Xenophobia'
            else:
                species.chauvinism = 'Racial Intolerance'
        else:
            species.chauvinism = 'Chauvinistic'
    elif chauv >= 2:
        if emp < 1 or sus > -1:
            species.chauvinism = 'Racial Intolerance'
        else:
            species.chauvinism = 'Chauvinistic'
    elif chauv >= 1:
        if emp < 0 or sus > 0:
            species.chauvinism = 'Racial Intolerance'
        else:
            species.chauvinism = 'Chauvinism'
    elif chauv >= 0:
        species.chauvinism = 'Normal'
    elif chauv >= -1:
        species.chauvinism = 'Broad-Minded'
    elif chauv >= -2:
        if sus < 0 and emp > 0:
            species.chauvinism = 'Xenophilia (15)'
        else:
            species.chauvinism = 'Broad-Minded'
    else:
        if sus < 0 or emp > 0:
            if sus < 0 and emp > 0:
                species.chauvinism = 'Xenophilia (9)'
            else:
                species.chauvinism = 'Xenophilia (12)'
        else:
            species.chauvinism = 'Undiscriminating'
    
    if concen >= 3:
        species.concentration = 'Single-Minded (High Pain Threshold)'
    elif concen >= 2:
        species.concentration = 'Single-Minded'
    elif concen >= 1:
        species.concentration = 'Attentive'
    elif concen >= 0:
        species.concentration = 'Normal'
    elif concen >= -1:
        species.concentration = 'Distractible'
    elif concen >= -2:
        species.concentration = 'Short Attention Span (12)'
    else:
        species.concentration = 'Short Attention Span (9)'
    
    if curio >= 3:
        if concen <= 0 or sus <= 0:
            species.curiosity = 'Curious (6)'
        else:
            species.curiosity = 'Curious (9)'
    elif curio >= 2:
        if concen <= 0:
            species.curiosity = 'Curious (9)'
        else:
            species.curiosity = 'Curious (12)'
    elif curio >= 1:
        if concen <= 0:
            species.curiosity = 'Curious (12)'
        else:
            species.curiosity = 'Nosy'
    elif curio >= 0:
        species.curiosity = 'Normal'
    elif curio >= -1:
        species.curiosity = 'Staid'
    elif curio >= -2:
        if sus < 0:
            species.curiosity = 'Incurious (9)'
        else:
            species.curiosity = 'Incurious (12)'
    else:
        species.curiosity = 'Incurious (12)'
    
    if ego >= 3:
        species.egoism = 'Selfish (9)'
    elif ego >= 2:
        if sus > 0 or emp < 0:
            species.egoism = 'Selfish (9)'
        else:
            species.egoism = 'Selfish (12)'
    elif ego >= 1:
        if sus > 0 or emp <= 2:
            if sus >= 2 or emp <= 2:
                species.egoism = 'Selfish (9)'
            else:
                species.egoism = 'Selfish (12)'
        else:
            species.egoism = 'Proud'
    elif ego >= 0:
        species.egoism = 'Normal'
    elif ego >= -1:
        species.egoism = 'Humble'
    elif ego >= -2:
        if chauv >= 2:
            species.egoism = 'Selfless (9)'
        else:
            species.egoism = 'Selfless (12)'
    else:
        species.egoism = 'Selfless (6)'

    if emp >= 3:
        if greg > 0:
            species.empathy = 'Empathy, Charitable (12)'
        else:
            species.empathy = 'Empathy (Sensitive)'
    elif emp >= 2:
        species.empathy = 'Empathy (Sensitive)'
    elif roll >= 1:
        if greg > 0 and sus < 0:
            species.empathy = 'Empathy (Sensitive)'
        else:
            species.empathy = 'Responsive'
    elif roll >= 0:
        species.empathy = 'Normal'
    elif roll >= -1:
        species.empathy = 'Oblivious'
    elif roll >= -2:
        species.empathy = 'Callous'
    else:
        if 'Carnivore' in species.trophic_level:
            species.empathy = 'Low Empathy, Bloodlust (12)'
        else:
            species.empathy = 'Low Empathy'
    
    if greg >= 3:
        species.gregariousness = 'Gregarious'
    elif greg >= 2:
        species.gregariousness = 'Chummy'
    elif greg >= 1:
        species.gregariousness = 'Congenial'
    elif greg >= 0:
        species.gregariousness = 'Normal'
    elif greg >= -1:
        species.gregariousness = 'Uncongenial'
    elif greg >= -2:
        species.gregariousness = 'Loner (12)'
    else:
        species.gregariousness = 'Loner (9)'
    
    if imag >= 3:
        if concen >= 0 and ego < 2:
            if ego > 0 or concen < 1:
                if emp < 1:
                    species.imagination = 'Imaginative, Versatile, Dreamer, Odious Racial Habit (Nonstop Idea Factory)'
                else:
                    species.imagination = 'Imaginative, Versatile, Dreamer'
            else:
                if emp < 1:
                    species.imagination = 'Imaginative, Versatile, Odious Racial Habit (Nonstop Idea Factory)'
                else:
                    species.imagination = 'Imaginative, Versatile'
        else:
            if emp < 1:
                species.imagination = 'Imaginative, Odious Racial Habit (Nonstop Idea Factory)'
            else:
                species.imagination = 'Imaginative'
    elif imag >= 2:
        if concen >= 0 and ego < 2:
            if ego > 0 or concen < 1:
                species.imagination = 'Imaginative, Versatile, Dreamer'
            else:
                species.imagination = 'Imaginative, Versatile'
        else:
                species.imagination = 'Imaginative'
    elif imag >= 1:
        if concen >= 0 and ego < 2:
            species.imagination = 'Imaginative, Versatile'
        else:
            species.imagination = 'Imaginative'
    elif imag >= 0:
        species.imagination = 'Normal'
    elif imag >= -1:
        species.imagination = 'Dull'
    elif imag >= -2:
        species.imagination = 'Hidebound'
    else:
        species.imagination = 'Hidebound'
        species.iq -= 1
    
    if sus >= 3:
        if 'Herbivore' in species.trophic_level:
            species.suspicion = 'Fearfulness 2, Cowardice'
        elif 'Carnivore' in species.trophic_level:
            species.suspicion = 'Fearfulness 2, Paranoia'
        else:
            species.suspicion = 'Fearfulness 2'
    elif sus >= 2:
        if curio <= -3:
            species.suspicion = 'Careful'
        else:
            species.suspicion = 'Fearfulness 1'
    elif sus >= 1:
        if curio <= -2:
            species.suspicion = 'Normal'
        else:
            species.suspicion = 'Careful'
    elif sus >= 0:
        species.suspicion = 'Normal'
    elif sus >= -1:
        species.suspicion = 'Fearlessness 1'
    elif sus >= -2:
        if ego >= 2:
            species.suspicion = 'Fearlessness 2, Overconfidence'
        else:
            species.suspicion = 'Fearlessness 2'
    else:
        if ego >= 1:
            if chauv <= -3:
                species.suspicion = 'Unfazeable, Overconfidence'
            else:
                species.suspicion = 'Fearlessness 3, Overconfidence'
        else:
            if chauv <= -3:
                species.suspicion = 'Unfazeable'
            else:
                species.suspicion = 'Fearlessness 3'
    
    if play >= 3:
        if (ego >= 2 and sus == -2) or (sus <= -3 and ego >= 1):
            species.playfulness = 'Trickster (12)'
        else:
            species.playfulness = 'Compulsive Playfulness (9)'
    elif play >= 2:
        species.playfulness = 'Compulsive Playfulness (12)'
    elif play >= 1:
        species.playfulness = 'Playful'
    elif play >= 0:
        species.playfulness = 'Normal'
    elif play >= -1:
        species.playfulness = 'Serious'
    elif play >= -2:
        species.playfulness = 'Odious Racial Habit (Wet Blanket)'
    else:
        species.playfulness = 'No Sense of Humour'


    if species.sapient == True:
        the_file = open("sapientSpecies.json", "a")
        the_file.write(species.toJSON() + ",")
        the_file.close()
    else:
        the_file = open("speciesInfo.json", "a")
        the_file.write(species.toJSON() + ",")
        the_file.close()

def create_tail_features(species, recursed=False):
    if recursed == False:
        roll = roll_dice(2)
    else:
        roll = roll_dice(1) + 5

    if roll <= 5:
        species.tail_features.append('No Special Features')
    elif roll <= 6:
        species.tail_features.append('Striker Tail')
    elif roll <= 7:
        species.tail_features.append('Long Tail')
    elif roll <= 8:
        species.tail_features.append('Constricting Tail')
    elif roll <= 9:
        species.tail_features.append('Barbed Striker Tail')
    elif roll <= 10:
        species.tail_features.append('Gripping Tail')
    elif roll <= 11:
        species.tail_features.append('Branching Tail')
    else:
        create_tail_features(species, True)
        create_tail_features(species, True)

def generate_manipulator_roll(species, planet):
    if  species.sapient == True:
        roll = roll_dice(1) + 6
    else:
        roll = roll_dice(2)

    if species.number_of_limbs == 2:
        roll -= 1
    elif species.number_of_limbs >= 6:
        roll += 2
    elif species.number_of_limbs >= 4:
        roll += 1
    
    if species.primary_locomotion == 'Winged Flight':
        roll -= 1
    
    if planet.planet_type == 'Gas Giant' or species.habitat_type == 'Open Ocean':
        roll -= 2
    
    if species.trophic_level == 'Gathering Herbivore':
        roll += 1
    
    if 'Gripping Tail' in species.tail_features and species.primary_locomotion == 'Climbing':
        roll += 2

    return roll

def create_manipulators(species, planet, roll):
    if roll <= 6:
        species.manipulator_features.append('No Limb Manipulators')
    elif roll <= 7:
        species.number_of_manipulators += species.number_of_sides
        species.manipulator_features.append('Bad Grip Manipulators')
    elif roll <= 8:
        if species.tail == True and not 'Prehensile Tail' in species.manipulator_features:
            species.manipulator_features.append('Prehensile Tail')
        else:
            species.manipulator_features.append('Prehensile Trunk')
        species.number_of_manipulators += 1

        if roll_dice(1) == 6:
            create_manipulators(species, planet, generate_manipulator_roll(species, planet))
    elif roll <= 9:
        species.number_of_manipulators += species.number_of_sides
        species.manipulator_features.append('Normal DX Manipulators')
    elif roll <= 10:

        species.number_of_manipulators += species.number_of_sides
        if roll_dice(1) <= 4:
            species.manipulator_features.append('Bad Grip Manipulators')
        else:
            species.manipulator_features.append('Normal DX Manipulators')
        
        species.number_of_manipulators += species.number_of_sides
        if roll_dice(1) <= 4:
            species.manipulator_features.append('Bad Grip Manipulators')
        else:
            species.manipulator_features.append('Normal DX Manipulators')

    elif roll <= 11:
        roll = roll_dice(1)
        species.number_of_manipulators += species.number_of_sides * roll
        for _ in range(0, roll):
            if roll_dice(1) <= 4:
                species.manipulator_features.append('Bad Grip Manipulators')
            else:
                species.manipulator_features.append('Normal DX Manipulators')
    
    else:
        roll = roll_dice(1)
        species.number_of_manipulators += species.number_of_sides * roll
        for _ in range(0, roll):
            if roll_dice(1) <= 4:
                species.manipulator_features.append('Normal DX Manipulators')
            else:
                species.manipulator_features.append('High Manual Dexterity 1 Manipulators')

#the method used for me being a fucking idiot and forgetting about probability distribution
def roll_dice(num1):
    num_sum = 0
    for _ in range(num1):
        num_sum += random.randrange(1,7)
    return num_sum

            



#Main Functions
galaxy_gen()
print("All done!")