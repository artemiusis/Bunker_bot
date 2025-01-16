import random
import telebot
import numpy as np
API_TOKEN = '8030840729:AAHqLZmZLSFiYIJvdaJm-Lk6b6YdV_esdiI'

bot = telebot.TeleBot(API_TOKEN)
used_bunker_cards = set()
# Окремі списки для характеристик
# Separate lists for characteristics
def generate_bio():
    # Ймовірності для різних гендерів
    genders = {
        "male": 36,
        "female": 36,
        "bisexual": 7,
        "transgender": 7,
        "gay": 7,
        "lesbian": 7
    }
    
    # Вибір гендера на основі ймовірностей
    # Gender selection based on probabilities
    gender = random.choices(
        population=list(genders.keys()),
        weights=list(genders.values()),
        k=1
    )[0]
    mean_age_primary = 28
    mean_age_secondary = 70
    std_dev = 10  # Стандартне відхилення/Standard deviation
    while True:
        # 88% для основного піку, 12% для додаткового/88% for the main peak, 12% for the additional peak
        if random.random() < 0.88:
            age = np.random.normal(mean_age_primary, std_dev)
        else:
            age = np.random.normal(mean_age_secondary, std_dev *4)

        # Повторна генерація, якщо значення не в діапазоні
        # Re-generation if the value is not in the range
        if 17 <= age <= 99:
            age = round(age)
            break
    # Ймовірність бути childfree
    # Probability of being childfree
    childfree = random.choices(
        population=[True, False],
        weights=[30, 70],  # Наприклад, 30% шанс бути childfree/For example, a 30% chance of being childfree
        k=1
    )[0]

    # Створення біо
    # Creating a bio
    bio = f"{gender}, {age}, childfree: {childfree}"
        
    return bio

professions = [
    "Civil Engineer",
    "Soldier",
"Vet",
"IHT Physics professor",
"IHT Biology professor",
"IHT Chemistry professor",
"Cleaner",

    "High School Teacher",
    "Emergency Room Doctor",
    "Pediatric Nurse",
    "Freelance Graphic Artist",
    "Restaurant Head Chef",
    "Fire Captain",
    "Police Detective",
    "Research Scientist",
    "Investigative Journalist",
    "Software Developer",
    "Automotive Mechanic",
    "Landscaper",
    "Community Pharmacist",
    "Clinical Psychologist",
    "Small Animal Veterinarian",
    "Retail Sales Associate",
    "Construction Foreman",
    "Child Social Worker",
    "Indie Musician",
    "Adult Film Star",
    "Twitch Streamer",
    "YouTube Content Creator",
    "Social Media Influencer",
    "Cryptocurrency Trader",
    "Life Coach",
    "Pet Groomer",
    "Personal Trainer",
    "Escape Room Designer",
    "Professional Gamer",
    "Fashion Designer",
    "Event Planner",
    "Yoga Instructor",
    "Voice Actor",
    "Podcast Host",
    "Digital Marketer",
    "Real Estate Agent",
    "Travel Blogger",
    "App Developer",
    "Personal Chef",
    "Nail Technician",
    "Body Painter",
    "Street Performer",
    "Underwater Welder",
    "Sculptor",
    "Home Inspector",
    "Tax Consultant",
    "Wildlife Photographer"
]

health_statuses = [
    "Healthy, no known issues",
    "Allergy to pollen (mild - severe)",
    "Pet dander allergy (mild - severe)",
    "Headaches (occasional - chronic)",
    "Prone to colds (infrequent - frequent)",
    "Sensitive skin (mild - very sensitive)",
    "Lactose intolerance (slight - strong)",
    "Gluten sensitivity (mild - severe)",
    "Back pain (rare - chronic)",
    "Insomnia (occasional - chronic)",
    "Nosebleeds (occasional - frequent)",
    "Sore throat (occasional - recurring)",
    "Motion sickness (mild - severe)",
    "Bruising easily (mild - severe)",
    "Mild vision impairment (slight - significant, uses glasses)",
    "Near-sighted (mild - severe)",
    "Far-sighted (mild - severe)",
    "Asthma (mild - severe)",
    "Caffeine sensitivity (mild - severe)",
    "Prone to fainting (occasional - frequent)",
    "Dry skin (mild - chronic)",
    "Indigestion (occasional - frequent)",
    "Sensitive teeth (mild - severe)",
    "Vitamin D deficiency (mild - significant)",
    "Iron deficiency (mild - severe)",
    "Anemia (mild - severe)",
    "Altitude sensitivity (mild - severe)",
    "Limp (slight - noticeable)",
    "Eczema (mild - severe)",
    "Muscle cramps (occasional - chronic)",
    "Allergy to pollen (mild - strong)",
    "Scoliosis (mild - moderate)",
    "Sunburns easily (mild - severe)",
    "Sinus issues (occasional - chronic)",
    "Noise sensitivity (mild - severe)",
    "Cold sensitivity (mild - severe)",
    "Heat sensitivity (mild - severe)",
    "Spice sensitivity (mild - strong)",
    "Anxiety (occasional - severe)",
    "Stress-prone (mild - high)",
    "Heart murmur (mild - significant)",
    "Fatigue (occasional - chronic)",
    "Dizziness (occasional - frequent)",
    "Light sensitivity (mild - severe)",
    "Hay fever (mild - chronic)",
    "Insect bite sensitivity (mild - strong reaction)",
    "Dental issues (minor - frequent)",
    "Joint pain (mild - chronic)",
    "Skin irritation from synthetic fabrics (mild - severe)",
    "Dehydration-prone (mild - severe)",
    "Stomach aches (occasional - frequent)",
    "Acid reflux (occasional - chronic)",
    "Temperature sensitivity (mild - severe)",
    "Shortness of breath (mild - chronic)",
    "Hand tremor (slight - noticeable)",
    "Weakened immune system (mild - significant)",
    "Obsessive tendencies (mild - strong)",
    "Attention issues (mild - severe)",
    "Shellfish allergy (mild - severe)",
    "Sensitivity to perfumes (mild - strong)",
    "Frequent need for eye drops",
    "Mold sensitivity (mild - severe)",
    "History of minor surgeries",
    "Weak ankles (mild - weak)",
    "Poor night vision (mild - significant)",
    "Dry eyes (mild - chronic)",
    "Dust sensitivity (mild - severe)",
    "Prone to acne (mild - frequent)",
    "Carpal tunnel (mild - severe)",
    "Air pollution sensitivity (mild - strong)",
    "Frequent muscle stiffness",
    "Slow healing from minor cuts",
    "Blister-prone feet (mild - frequent)",
    "Recurring ear infections (mild - chronic)",
    "Weak nails",
    "Arthritis in knees (mild - severe)",
    "Gluten sensitivity (mild - severe)",
    "Jaw pain (occasional - frequent)",
    "Dairy sensitivity (mild - severe)",
    "Irritable bowel syndrome (mild - moderate)",
    "Hand numbness (occasional - frequent)",
    "Repetitive strain injury (mild - chronic)",
    "Dry mouth (occasional - frequent)",
    "Sensitivity to rapid weather changes (mild - severe)"
]
health_statuses += [
    "Heart disease (mild - advanced)",
    "Diabetes (Type I or II, managed - uncontrolled)",
    "Missing right hand",
    "Missing left leg below the knee",
    "Epilepsy (rare - frequent seizures)",
    "Cancer (in remission - active treatment)",
    "Organ transplant recipient (managed - potential rejection)",
    "Severe chronic pain (mildly - highly debilitating)",
    "Multiple sclerosis (early - advanced)",
    "Cystic fibrosis (mild - severe)",
    "Advanced arthritis (affecting mobility)",
    "HIV positive (managed - advanced)",
    "Parkinson's disease (early - advanced)",
    "End-stage renal disease (requires dialysis)",
    "Quadriplegia",
    "Paraplegia",
    "Muscular dystrophy (mild - advanced)",
    "Severe asthma (requires frequent medication)",
    "Chronic obstructive pulmonary disease (COPD, mild - severe)",
    "Liver disease (mild - cirrhosis)",
    "Chronic migraines (debilitating)",
    "Severe scoliosis (affects posture and movement)",
    "Legally blind",
    "Deaf",
    "Speech impairment (mild - severe)",
    "Stroke recovery (mild - severe effects)",
    "Severe burn scars",
    "Autoimmune disease (mild - severe, lupus, etc.)",
    "Hemophilia",
    "Cerebral palsy (mild - severe)",
    "Alzheimer's disease (early - advanced)",
    "Schizophrenia (mild - unmanaged)",
    "Bipolar disorder (managed - unmanaged)",
    "Severe obsessive-compulsive disorder",
    "Amputation of one arm",
    "Partial paralysis",
    "Huntington's disease",
    "Severe PTSD",
    "Spinal injury (affecting mobility)",
    "Brain injury with cognitive impairment",
    "Chronic kidney disease (mild - end-stage)",
    "Crohn's disease (mild - severe)",
    "Severe acid reflux (GERD, requires surgery)",
    "Tourette syndrome",
    "Narcolepsy",
    "Advanced Lyme disease",
    "Severe autism spectrum disorder",
    "Thyroid disorder (hypo/hyper, mild - severe)",
    "Hyperhidrosis (excessive sweating)",
    "Blood clotting disorder",
    "Chronic fatigue syndrome (mild - severe)",
    "Ehlers-Danlos syndrome",
    "Polycystic ovary syndrome",
    "Severe vision impairment",
    "Severe allergy to common foods",
    "Arthritis in spine",
    "Partial lung function",
    "Hypersensitivity to sunlight (severe)",
    "Tuberculosis (active or managed)"
]
# Відсотковий шанс бути повністю здоровим
# Percentage chance of being completely healthy
healthy_chance = 15

def generate_health_status():
    # Якщо випадкове число менше або дорівнює шансу на здоров'я, повертаємо здоровий статус
    # If the random number is less than or equal to the health chance, return the healthy status
    if random.randint(1, 100) <= healthy_chance:
        return "Healthy. No health issues"
    
    # Інакше вибираємо випадковий стан здоров'я з наявного списку
    # Otherwise, select a random health condition from the available list
    available_health_statuses = list(set(health_statuses) - used_bunker_cards)
    health_issue = random.choice(available_health_statuses)
    used_bunker_cards.add(health_issue)
    # Генеруємо серйозність проблеми здоров'я у відсотках (від 10 до 100%)
    # We generate the severity of the health problem as a percentage (from 10 to 100%)
    severity = random.randint(5, 100)
    
    # Форматуємо результат з доданою серйозністю
    # Formatting the result with added severity
    return f"{health_issue}, {severity}%"


personality_traits = [
    "Optimistic",
    "Pessimistic",
    "Courageous",
    "Cynical",
    "Empathetic",
    "Introverted",
    "Extroverted",
    "Analytical",
    "Impulsive",
    "Rebellious",
    "Creative",
    "Pragmatic",
    "Generous",
    "Selfish",
    "Meticulous",
    "Adventurous",
    "Reliable",
    "Stubborn",
    "Charismatic",
    "Mischievous",
    "Patient",
    "Nervous",
    "Passionate",
    "Indecisive",
    "Sensitive",
    "Skeptical",
    "Daring",
    "Compulsive",
    "Proud",
    "Diligent",
    "Witty",
    "Ambitious",
    "Resourceful",
    "Compassionate",
    "Nurturing",
    "Sardonic",
    "Serious",
    "Egotistical",
    "Loyal",
    "Disorganized",
    "Melancholic"
]


phobias = [
    "Fear of darkness",
    "Fear of confined spaces",
    "Fear of heights",
    "Fear of spiders",
    "Fear of insects",
    "Fear of large crowds",
    "Fear of public speaking",
    "Fear of being alone",
    "Fear of water",
    "Fear of flying",
    "Fear of blood",
    "Fear of mirrors",
    "Fear of sharp objects",
    "Fear of failure",
    "Fear of loud noises",
    "Fear of open spaces",
    "Fear of aging",
    "Fear of touching plants",
    "Fear of small animals",
    "Fear of dolls",
    "Fear of mirrors",
    "Fear of bright lights",
    "Fear of time passing",
    "Fear of doors",
    "Fear of strange sounds",
    "Fear of bright colors",
    "Fear of falling asleep",
    "Fear of technology",
    "Fear of touching paper",
    "Fear of food textures",
    "Fear of getting dirty",
    "Fear of being touched",
    "Fear of dust",
    "Fear of soap",
    "Fear of metals",
    "Fear of walking on grass",
    "Fear of clouds",
    "Fear of birds",
    "Fear of sleep paralysis",
    "Fear of robots",
    "Fear of shoes",
    "Fear of the moon",
    "Fear of certain numbers",
    "Fear of chewing sounds",
    "Fear of looking at the sun",
    "Fear of being in cars",
    "Fear of escalators",
    "Fear of pets",
    "Fear of kitchen utensils",
    "Fear of random questions",
    "Fear of blinking",
    "Fear of music",
    "Fear of art pieces",
    "Fear of specific words",
    "Fear of silence",
    "Fear of the ocean",
    "Fear of eating in public",
    "Fear of distant stars",
    "Fear of being tickled",
    "Fear of handshakes",
    "Fear of waiting in lines",
    "Fear of seeing patterns",
    "Fear of snow",
    "Fear of thinking too much",
    "Fear of being photographed",
    "Fear of looking at clocks",
    "Fear of the color red",
    "Fear of tunnels",
    "Fear of being watched",
    "Fear of strong wind",
    "Fear of paper cuts",
    "Fear of people with glasses",
    "Fear of perfectly straight lines",
    "Fear of specific patterns",
    "Fear of the color black",
    "Fear of bridges",
    "Fear of trains",
    "Fear of old furniture",
    "Fear of neon lights",
    "Fear of waste and trash",
    "Fear of staring",
    "Fear of children’s laughter",
    "Fear of buttons",
    "Fear of random noises at night",
    "Fear of abandoned places",
    "Fear of being wrong",
    "Fear of wearing hats",
    "Fear of neckties",
    "Fear of ancient artifacts",
    "Fear of electronic sounds"
]



hobbies = [
    "Gardening",
    "Cooking",
    "Reading",
    "Photography",
    "Painting",
    "Hiking",
    "Writing",
    "Playing musical instruments",
    "Gaming",
    "Crafting",
    "Traveling",
    "Birdwatching",
    "Collecting antiques",
    "Fishing",
    "Baking",
    "Cycling",
    "Knitting",
    "Woodworking",
    "Playing sports",
    "Volunteering",
    "Meditation",
    "Dancing",
    "Scrapbooking",
    "Drawing",
    "Fitness training",
    "Homebrewing",
    "Pottery",
    "Sewing",
    "Rock climbing",
    "Playing board games",
    "Attending concerts",
    "Learning languages",
    "Martial arts",
    "Blogging",
    "Stargazing",
    "Model building",
    "Travel blogging",
    "Making jewelry",
    "Listening to music",
    "Origami",
    "Playing video games",
    "Camping"
    "Studying ancient civilizations",
    "Trying out every flavor of potato chips",
    "Competing in extreme ironing contests"
]

addictions = [
    "Addiction to caffeine",
    "Addiction to nicotine",
    "Addiction to sugar",
    "Addiction to alcohol",
    "Addiction to social media",
    "Addiction to video games",
    "Addiction to gambling",
    "Addiction to painkillers",
    "Addiction to adrenaline (thrill-seeking)",
    "Addiction to energy drinks",
    "Addiction to fast food",
    "Addiction to shopping",
    "Addiction to exercise",
    "Addiction to TV series",
    "Addiction to chocolate",
    "Addiction to spicy food",
    "Addiction to tattoos",
    "Addiction to collecting items",
    "Addiction to soda",
    "Addiction to reality TV shows",
    "Addiction to online forums",
    "Addiction to conspiracy theories",
    "Addiction to cleaning",
    "Addiction to chewing gum",
    "Addiction to romance novels",
    "Addiction to working (workaholic)",
    "Addiction to sleeping pills",
    "Addiction to supplements",
    "Addiction to celebrity gossip",
    "Addiction to listening to music",
    "Addiction to taking selfies",
    "Addiction to cryptocurrency trading",
    "Addiction to browsing the internet",
    "Addiction to online shopping",
    "Addiction to driving fast",
    "Addiction to cosmetic products",
    "Addiction to perfume",
    "Addiction to collecting shoes",
    "Addiction to self-improvement books",
    "Addiction to herbal teas",
    "Addiction to soft drinks",
    "Addiction to hand sanitizer",
    "Addiction to bread",
    "Addiction to peanut butter",
    "Addiction to flavored snacks",
    "Addiction to personal care products",
    "Addiction to diet pills",
    "Addiction to weather news",
    "Addiction to coffee shop visits",
    "Addiction to podcasts",
    "Addiction to chewing ice",
    "Addiction to daydreaming",
    "Addiction to reading about history",
    "Addiction to online auctions",
    "Addiction to plant care",
    "Addiction to hiking",
    "Addiction to aromatherapy",
    "Addiction to taking vitamins",
    "Addiction to posting online reviews",
    "Addiction to thrift shopping",
    "Addiction to crafting",
    "Addiction to recording daily events",
    "Addiction to solving puzzles",
    "Addiction to watching documentaries",
    "Addiction to meditation apps",
    "Addiction to political news",
    "Addiction to home decoration",
    "Addiction to checking notifications",
    "Addiction to memory training",
    "Addiction to wearing sunglasses",
    "Addiction to collecting recipes"
]


unique_knowledges = [
    "Expert in local plant identification",
    "Completed a survival course",
    "Fluent in four languages",
    "Knows how to pick locks",
    "Skilled at repairing electronics",
    "Trained in wilderness first aid",
    "Knows Morse code by heart",
    "Experienced in urban farming",
    "Knows extensive facts about astrology",
    "Can read ancient runes",
    "Trained in traditional healing practices",
    "Specialist in constructing improvised shelters",
    "Memorized dozens of knots and their uses",
    "Can navigate using only the stars",
    "Expert in recycling and waste management",
    "Familiar with all edible mushrooms in the region",
    "Can make fire without modern tools",
    "Specialized knowledge of medicinal herbs",
    "Has mastered the art of making traps",
    "Can produce clean water from various sources",
    "Advanced knowledge of survival cooking",
    "Knows how to handle wild animals safely",
    "Expert in jury-rigging machinery",
    "Has a photographic memory for faces",
    "Studied ancient myths and legends",
    "Can calculate calorie needs for groups",
    "Expert in local geography and shortcuts",
    "Can accurately assess others' health conditions",
    "Master in the art of camouflage",
    "Knows secrets of underwater navigation",
    "Skilled in brewing medicinal teas",
    "Historian with extensive knowledge of wars",
    "Expert in hiding and evasion tactics",
    "Knows how to make natural insect repellents",
    "Certified in psychological first aid",
    "Can forge basic tools with minimal materials",
    "Knows safe building structures",
    "Experienced with disaster relief protocols",
    "Skilled in dismantling electrical devices",
    "Understands basic forensic science",
    "Has a unique sense of direction",
    "Can accurately judge the time without a clock",
    "Studies sleep and its patterns",
    "Knows how to hunt and prepare animals",
    "Experienced with ancient weapons and tools",
    "Can quickly adapt to new languages",
    "Specialist in alternative energy sources",
    "Knowledge of eco-friendly waste disposal",
    "Skilled in underwater survival techniques",
    "Deep knowledge of fungi and their uses",
    "Specialist in meteorology and weather patterns",
    "Knows how to create natural dyes",
    "Expert in reading body language",
    "Can recognize the constellations easily",
    "Has an impressive ability to make allies quickly",
    "Professional barista skills",
    "Knows unique local legends and mysteries",
    "Deep knowledge of mechanical systems",
    "Familiar with obscure ancient languages",
    "Can track time by plant movements",
    "Trained in animal psychology",
    "Knows the hidden history of surrounding areas",
    "Memorized dozens of board game strategies",
    "Extensive knowledge of edible bugs",
    "Studied alchemy and early chemistry",
    "Skilled at crafting clothing from raw materials",
    "Expert in micro-gardening techniques",
    "Possesses rare knowledge of foraging",
    "Can interpret unusual dreams",
    "Trained in ancient calligraphy",
    "Knows shortcuts in mathematical calculations",
    "Skilled in creating improvised barriers",
    "Expert in minimalism and efficient resource use",
    "Has in-depth knowledge of astrology charts",
    "Extensive knowledge of entomology",
    "Knows the location of ancient underground tunnels",
    "Can predict people's reactions accurately",
    "Knows archaic survival methods",
    "Deep understanding of human psychology",
    "Able to detect poisonous plants easily",
    "Skilled in stone carving and basic masonry",
    "Expert on historical agriculture techniques",
    "Can determine water sources underground",
    "Experienced in extreme weather survival",
    "Skilled at fermenting various foods",
    "Knowledgeable in natural soap making",
    "Understands mechanisms of old clocks",
    "Can identify bird species by their songs",
    "Knowledge of archaic fishing techniques",
    "Expert in identifying animal tracks",
    "Skilled at staying undetected in urban environments",
    "Trained in archery and handmade bow crafting",
    "Knows how to interpret seismic activity patterns",
    "Expert in food rationing techniques",
    "Able to estimate distances precisely by eye",
    "Knows the full script of a popular TV show by heart",
    "Completed a course on interpretive dance",
    "Expert in identifying different types of pasta",
    "Can whistle entire classical symphonies",
    "Has memorized thousands of internet memes",
    "Skilled at folding origami animals",
    "Knows all trivia about a single obscure movie",
    "Professional at stacking rocks",
    "Won several local bubble-gum blowing contests",
    "Trained in advanced yodeling techniques",
    "Can identify every type of coffee bean by smell",
    "Specialist in making shadow puppets",
    "Has extensive knowledge of medieval jokes",
    "Familiar with ancient board game strategies",
    "Expert at catching paper airplanes mid-flight",
    "Knows how to make toast perfectly every time",
    "Can name all countries by their obscure landmarks",
    "Once spent a week studying seagull behavior",
    "Proficient in flipping pancakes without breaking",
    "Expert in recognizing celebrity impersonators",
    "Knows detailed history of a forgotten soft drink brand",
    "Has read every pamphlet in a single subway station",
    "Can distinguish dozens of types of rocks by touch",
    "Advanced knowledge of speed-walking techniques",
    "Can guess the exact weight of most objects",
    "Specialist in non-verbal communication with pets",
    "Collected a vast number of different pencils",
    "Familiar with rare varieties of potato chips",
    "Knows obscure facts about various types of socks",
    "Can accurately imitate different types of bells",
    "Knows the lyrics to every song from 90s boy bands",
    "Expert in silent disco etiquette",
    "Master of making paperclip sculptures",
    "Identifies every type of cloud formation",
    "Can flawlessly imitate a fax machine sound",
    "Knows the release dates of all cereal box toys",
    "Can count cards—but only in Uno",
    "Skilled in deciphering supermarket discount codes",
    "Recognizes obscure video game Easter eggs",
    "Can differentiate carpet patterns from memory",
    "Collected a vast range of antique bottle caps",
    "Knows trivia on every brand of bottled water",
    "Professional-level bubble wrap popper",
    "Expert on soap opera plotlines from the 80s",
    "Can perfectly recall old commercial jingles",
    "Once memorized an entire furniture catalog",
    "Experienced in identifying fonts on sight",
    "Learned Morse code but only for punctuation",
    "Knows the precise rules of imaginary sports",
    "Certified in ‘advanced sticker placement’",
    "Can draw a perfect circle freehand—sometimes",
    "Pro at balancing books on their head",
    "Knows minor historical events involving cats",
    "Detailed knowledge of hat-wearing etiquette",
    "Experienced in deflating air mattresses quietly",
    "Skilled in ice cube tray filling techniques",
    "Can taste the difference between tap waters",
    "Memorized famous sandwich recipes",
    "Experienced at 'extreme ironing' techniques",
    "Knows the origins of various emoji",
    "Studied the sleeping habits of pet goldfish",
    "Has memorized every airport code worldwide",
    "Expert on where certain tree species grow",
    "Knows the historical changes in sock design",
    "Can distinguish grass types by smell",
    "Spent years documenting types of sand",
    "Expert in chewing gum bubble techniques",
    "Knows the entire library catalog of a small town",
    "Can flawlessly pronounce difficult city names",
    "Collected rare lint samples from dryers",
    "Skilled at the ‘science’ of skipping stones"
]


special_items = [
    "A well-worn map of the area",
    "A multi-tool with numerous functions",
    "A mysterious key with no lock in sight",
    "A jar of pickles that never seems to go bad",
    "A notebook filled with survival tips",
    "A magic 8-ball that always gives accurate answers",
    "A lucky charm made from twigs and string",
    "A compass that points to the nearest snack",
    "A harmonica that plays itself",
    "A pair of binoculars with cracked lenses",
    "A rubber chicken that brings good luck",
    "A vintage pocket watch that tells the wrong time",
    "An inflatable dinosaur costume for emergencies",
    "A collection of random buttons",
    "A mysterious potion that changes colors",
    "A deck of playing cards that reveals secrets",
    "A fishing rod made from a broomstick",
    "A pet rock with a backstory",
    "A pair of roller skates with broken wheels",
    "A sign that says 'The End is Near!'",
    "A trophy for winning the 'Best at Losing' competition",
    "A collection of expired coupons",
    "A bag of marbles that can predict the future",
    "A quirky statue of a mythical creature",
    "A megaphone that only amplifies whispers",
    "A box of chocolate-covered broccoli",
    "A feather from a legendary bird",
    "A jar filled with the last breath of a dragon",
    "A rock that claims to grant wishes",
    "A soap bubble that never pops",
    "A pair of sunglasses that see the past",
    "Portable solar charger",
    "Water filtration straw",
    "Limited-edition survival multi-tool",
    "Large stash of canned spaghetti",
    "High-power flashlight with spare batteries",
    "Book on edible plants",
    "Folding camping stove with fuel canisters",
    "Set of durable blankets",
    "Comprehensive first aid kit",
    "Vintage hand-crank radio",
    "Waterproof notebook and pencil",
    "Collection of classic comic books",
    "Backpack with hidden compartments",
    "Self-defense pepper spray",
    "Pack of freeze-dried astronaut ice cream",
    "Solar-powered flashlight and radio",
    "Pocket microscope",
    "Night vision goggles (low quality)",
    "DIY herbal remedies kit",
    "Detailed map of the surrounding area",
    "Collection of essential oils",
    "Set of small lockpicks",
    "Portable mini projector",
    "Funky, glow-in-the-dark paracord",
    "Deck of waterproof playing cards",
    "Wooden puzzle games for mental exercise",
    "Sewing kit with various types of thread",
    "Personal diary with a lock",
    "Digital thermometer with battery",
    "Solar panel blanket for recharging devices",
    "Limited-edition gaming console with games",
    "One-way mirror glasses",
    "Miniature hammock",
    "Waterproof boots (one size fits all)",
    "Box of unique spices",
    "Inflatable kayak and paddle",
    "Bunker garden seeds pack",
    "A crystal ball",
    "Vintage record player with some vinyl",
    "Book of classic survival myths",
    "Battery-operated blender",
    "Set of rare international stamps",
    "Large magnifying glass",
    "Antique compass that 'always points north'",
    "Personal stash of exotic teas",
    "Pack of colored chalk",
    "Fur-lined sleeping bag",
    "Detailed blueprint of a submarine",
    "Ancient scroll with cryptic writing",
    "High-tech portable coffee maker",
    "Box of vegan protein bars",
    "Glitter glue and crafting supplies",
    "A collection of scented candles",
    "Small drum set",
    "Notebook on conspiracy theories",
    "Personal-sized bubble machine",
    "Jar of pickled eggs",
    "Stainless steel marshmallow roasting forks",
    "World’s tiniest shovel",
    "Custom embroidered chef's apron",
    "Set of cryptographic ciphers",
    "Small mannequin for learning first aid",
    "Super absorbent towel",
    "Rainwater collection tarp",
    "Bag of rare collectible dice"
]

actions = [
    "Require a player to trade health status with another player.",
    "Reveal that there are hidden supplies in the bunker. (one more person can stay)",
    "Make a player discard one of their unique items.",
    "Demand that a player share their addiction with the group.",
    "Require a player to swap a hobby with another player.",
    "Make a player admit to having a mild hidden illness (on your choice).",
    "Force a player to give up a turn in the next round.",
    "Reveal that there is a way to barricade the bunker entrance.",
    "Force a player to reveal their phobia.",
    "Expose a hidden item that can benefit the group.",
    "Require a player to choose an item to discard.",
    "Demand a player to trade their profession with another player.",
    "Expose that someone has a stash of secret supplies.",
    "Make a player give away a resource to another player.",
    "Require a player to change their gender for the next round."
    "Make a player swap their health status with another player.",
    "Force a player to skip their vote this round.",
    "Require a player to vote for one of two specified players.",
    "Demand that a player trade a unique knowledge with another player.",
    "Require a player to reveal their addiction to the group.",
    "Make a player swap one of their hobbies with another player.",
    "Demand that a player disclose their phobia.",
    "Сhoose another player's health status to change.",
    "Force a player to give up a special item",
    "Make a player give away their unique item to the group.",
    "Force a player to change their gender.",
    "Require a player to swap their profession with another player.",
    "Require a player to disclose any hidden medical conditions.",
    "Demand a player to trade their addiction with another player.",
    "Force a player to swap health statuses with you.",
    "Make a player reveal their addiction to the group.",
    "Choose a player who cannot vote this round.",
    "Require a player to give up their special item.",
    "Make two players vote against each other in a decision.",
    "Change a player's profession to a different one.",
    "Compel a player to demonstrate their unique knowledge.",
    "Bunker has less food than planed (one less person can stay)",
    "Reveal a hidden danger outside the bunker. (on your choice)",
    "Reveal an agressive bunker close to the bunker.",
    "Take a look at another player's health status.",
    "Choose a player to take an extra action this round.",
    "Swap hobbies with another player.",
    "Force a player to recount their last meal.",
    "Make a player draw a special item from the pile.",
    "Challenge a player to a game of chance to determine their fate.",
    "Provide one player with immunity for this round.",
    "Require a player to share their phobia.",
    "Make a player reveal their unique hobby.",
    "Choose a player who must vote first."
]


# Списки для катастроф та карт бункера
# Lists for disasters and bunker cards
disasters = [
    "Nuclear war:\nRequired bunker time: 3 years.\nBunker contents: power generator, food and water supplies for 4 years, medical kit, seed storage. \nAfter exit: Radioactive land, destroyed cities, no infrastructure. Survivors must clear land to rebuild and restore ecosystems.",
    "Pandemic of an unknown virus:\nRequired bunker time: 2 years.\nBunker contents: air filtration system, extensive supply of medicine, additional medical equipment, isolation room.\nAfter exit: Disease might still linger in areas. Survival depends on finding uninfected zones, with risks of outbreaks.",
    "Asteroid impact:\nRequired bunker time: 5 years.\nBunker contents: preserved food stores for 6 years, water filtration system, tools for cultivation, basic construction materials.\nAfter exit: World blanketed in dust, blocking sunlight, low temperatures. Limited flora and fauna; survivors must establish agriculture quickly.",
    "Supervolcano eruption:\nRequired bunker time: 4 years.\nBunker contents: geothermal heating, seed vault, durable food supplies, oxygen supplies, hydroponic farming equipment.\nAfter exit: Ash-covered land and toxic air. Survivors face long winters and lack of arable land due to volcanic ash layers.",
    "Climate catastrophe:\nRequired bunker time: 10 years.\nBunker contents: water reserves, solar panels, indoor growing facilities, extensive toolset, and climate-resistant seeds.\nAfter exit: Extreme weather conditions—scorching summers and frozen winters. Limited arable land; survivors must adapt agriculture and resource collection to a harsh environment.",
    "Alien invasion:\nRequired bunker time: 15 years.\nBunker contents: enhanced security doors, radio communication system, weapons cache, minimal food and water (enough for 5 years, requires rationing).\nAfter exit: Alien machinery and settlements dot the landscape. Few humans are left; survivors must avoid detection and reclaim territory.",
    "Global blackout and tech collapse:\nRequired bunker time: 6 months.\nBunker contents: extensive printed books library, seed vault, mechanical tools, emergency food, and water supplies.\nAfter exit: Societal collapse, no electricity, and no functioning technology. Survivors must rely on manual tools and traditional knowledge to rebuild communities.",
    "Rogue AI takeover:\nRequired bunker time: 8 years.\nBunker contents: faraday-shielded control room, basic food and water supplies, rudimentary farming equipment, manual tools, a radio.\nAfter exit: AI presence worldwide, humans considered threats by machines. Survivors face AI patrolled zones and must avoid tech dependency.",
    "Ecosystem collapse:\nRequired bunker time: 2 years.\nBunker contents: large-scale hydroponic gardens, extensive water filtration, variety of seeds, tools for small-scale habitat construction.\nAfter exit: Loss of biodiversity, failing ecosystems, most wildlife extinct. Survivors must develop artificial ecosystems to sustain life."
]



bunker_cards = [
    "There is extra food in the bunker. (one more person can stay)",
    "You find a stash of seeds for planting.",
    "A group of rats has taken up residence in the bunker.",
    "You discover a hidden stash of medical supplies.",
    "There is a malfunctioning generator that needs repair.",
    "You find a map of the surrounding area.",
    "There is an underground water supply.",
    "You come across a crate of batteries.",
    "You discover a secret exit from the bunker.",
    "There are mysterious noises coming from the ventilation system.",
    "You find a collection of books on survival techniques.",
    "There are signs of previous inhabitants.",
    "You find a working radio.",
    "You discover a cache of weapons.",
    "There is a hidden room filled with supplies.",
    "You encounter a colony of insects in the food storage.",
    "You find a stash of tools for repairs.",
    "You discover a secret compartment with old documents.",
    "There is a strange device that you can't identify.",
    "You find an old board game to pass the time.",
    "You discover a hidden garden.",
    "There is a leaking pipe that threatens the water supply.",
    "You find a small supply of antibiotics.",
    "There is a stash of canned food, but some are expired.",
    "You find a pile of spare parts for the generator.",
    "A nest of spiders is discovered in the storage room.",
    "You uncover a manual on emergency first aid procedures.",
    "You find a working flashlight with extra batteries.",
    "There is a set of hand-cranked radios.",
    "You discover a bag of old clothes and blankets.",
    "You find a rationed supply of chocolate bars.",
    "You come across a box of survival kits with random items.",
    "There is a dusty mirror in a corner of the bunker.",
    "You find a stash of coffee and tea.",
    "The ceiling has a small crack that lets in a faint sound of wind."
]

def generate_character():
    # Виключаємо використані картки і статуси із списку до наступного запуску бота
    # Remove used cards and statuses from the list until the next bot launch
    available_professions = list(set(professions) - used_bunker_cards)
    available_personality_traits = list(set(personality_traits) - used_bunker_cards)
    available_phobias = list(set(phobias) - used_bunker_cards)
    available_hobbies = list(set(hobbies) - used_bunker_cards)
    available_addictions = list(set(addictions) - used_bunker_cards)
    available_unique_knowledges = list(set(unique_knowledges) - used_bunker_cards)
    available_special_items = list(set(special_items) - used_bunker_cards)
    available_actions = list(set(actions) - used_bunker_cards)
    Profession = random.choice(available_professions)
    used_bunker_cards.add(Profession)
    Health = generate_health_status()
    Personality = random.choice(available_personality_traits)
    used_bunker_cards.add(Personality)
    Phobia = random.choice(available_phobias)
    used_bunker_cards.add(Phobia)
    Hobby = random.choice(available_hobbies)
    used_bunker_cards.add(Hobby)
    Addiction = random.choice(available_addictions)
    used_bunker_cards.add(Addiction)
    Unique = random.choice(available_unique_knowledges)
    used_bunker_cards.add(Unique)
    Item = random.choice(available_special_items)
    used_bunker_cards.add(Item)
    Action1 = random.choice(available_actions)
    used_bunker_cards.add(Action1)
    available_actions = list(set(actions) - used_bunker_cards)
    Action2 = random.choice(available_actions)
    used_bunker_cards.add(Action2)
    character = {
        "Bio": generate_bio(),
        "Profession": Profession,
        "Health": Health,
        "Personality Trait": Personality,
        "Phobia": Phobia,
        "Hobby": Hobby,
        "Addiction": Addiction,
        "Unique Knowledge": Unique,
        "Special Item": Item,
        "Action 1": Action1,
        "Action 2": Action2,
    }

    return character
# Обробник команди /start
# Command handler /start
@bot.message_handler(commands=['start'])
def send_start(message):
    
    commands_list = (    
        "/char - Generate a character",
        "/bio - Get a random bio",
        "/profession - Get a random profession",
        "/health - Get random health status",
        "/personality - Get a random personality trait",
        "/phobia - Get a random phobia",
        "/hobby - Get a random hobby",
        "/addiction - Get a random addiction",
        "/knowledge - Get unique knowledge",
        "/item - Get a special item",
        "/action - Get a random action ",
        "/disaster - Get a random disaster",
        "/card - Get a random bunker card",
        "/rules - See short rules of the game"
    )
    
    bot.reply_to(message, f"👋Hello!👋\n😺It`s IHT Speaks Bot for playing bunker!😺\n👾Available commands:\n" + "👈\n".join(commands_list) + "👈")
# Обробники характеристик
# Characteristic handlers

@bot.message_handler(commands=['char'])
def send_character(message):
    character = generate_character()
    character_info = "✍️\n".join([f"{key}: {value}" for key, value in character.items()]  )
    bot.reply_to(message, character_info + "✍️")
@bot.message_handler(commands=['bio'])
def send_bio(message):
    bot.reply_to(message, f"Bio: {generate_bio()}")

@bot.message_handler(commands=['rules'])
def send_rules(message):
    bot.reply_to(message, f"""Objective: The goal is to secure your spot in the bunker.

Character Creation: Each player receives a randomly assigned character with specific traits. Use /char to generate yours.

Catastrophe Scenario: The game begins with a specific apocalypse scenario (nuclear war, plague, etc.), determining how long players need to stay in the bunker and what conditions they’ll face when they leave.

Debate and Vote: The game is played in rounds. After each round of discussion, players vote on who should be eliminated. Eliminated players are “left outside the bunker.”

Game End: The game concludes when the bunker reaches its capacity. Those who remain inside are the "survivors.".
                 
{54*"*"}           

Мета: Ціль гри — забезпечити собі місце в бункері.

Створення персонажа: Кожен гравець отримує випадково згенерованого персонажа з унікальними характеристиками. Використовуй команду /char для створення свого персонажа.

Сценарій катастрофи: Гра починається з конкретного апокаліптичного сценарію (ядерна війна, пандемія тощо), який визначає, скільки часу гравці повинні залишатися в бункері і які умови будуть після виходу.

Обговорення і голосування: Гра проходить у раундах. Після кожного раунду обговорення гравці голосують, хто має покинути гру. Ті, кого усунули, залишаються «за межами бункера».

Завершення гри: Гра завершується, коли кількість гравців у бункері досягає його максимальної місткості. Ті, хто залишився в бункері, — «вцілілі».                 
""")
    
@bot.message_handler(commands=['profession'])
def send_profession(message):
    available_professions = list(set(professions) - used_bunker_cards)
    Profession = random.choice(available_professions)
    used_bunker_cards.add(Profession)
    bot.reply_to(message, f"Profession: {Profession}")

@bot.message_handler(commands=['health'])
def send_health(message):
    bot.reply_to(message, f"Health: {generate_health_status()}")

@bot.message_handler(commands=['personality'])
def send_personality(message):
    available_personality_traits = list(set(personality_traits) - used_bunker_cards)
    personality = random.choice(available_personality_traits)
    used_bunker_cards.add(personality)
    bot.reply_to(message, f"Personality Trait: {personality}")

@bot.message_handler(commands=['phobia'])
def send_phobia(message):
    available_phobias = list(set(phobias) - used_bunker_cards)
    
    phobia = random.choice(available_phobias)
    used_bunker_cards.add(phobia)
    bot.reply_to(message, f"Phobia: {phobia}")

@bot.message_handler(commands=['hobby'])
def send_hobby(message):
    available_hobbies = list(set(hobbies) - used_bunker_cards)
    hobbie = random.choice(available_hobbies)
    used_bunker_cards.add(hobbie)
    bot.reply_to(message, f"Hobby: {hobbie}")

@bot.message_handler(commands=['addiction'])
def send_addiction(message):
    available_addictions = list(set(addictions) - used_bunker_cards)
    addiction = random.choice(available_addictions)
    used_bunker_cards.add(addiction)
    bot.reply_to(message, f"Addiction: {addiction}")

@bot.message_handler(commands=['knowledge'])
def send_unique_knowledge(message):
    available_unique_knowledges = list(set(unique_knowledges) - used_bunker_cards)
    unique_knowledge = random.choice(available_unique_knowledges)
    used_bunker_cards.add(unique_knowledge)
    bot.reply_to(message, f"Unique Knowledge: {unique_knowledge}")

@bot.message_handler(commands=['item'])
def send_special_item(message):
    available_special_items = list(set(special_items) - used_bunker_cards)
    special_item = random.choice(available_special_items)
    used_bunker_cards.add(special_item)
    bot.reply_to(message, f"Special Item: {special_item}")

@bot.message_handler(commands=['action'])
def send_action1(message):
    available_actions = list(set(actions) - used_bunker_cards)
    action = random.choice(available_actions)
    used_bunker_cards.add(action)
    bot.reply_to(message, f"Action: {action}")
# Обробники для катастроф та карт бункера
@bot.message_handler(commands=['disaster'])
def send_disaster(message):
    bot.reply_to(message, f"Disaster: {random.choice(disasters)}")

@bot.message_handler(commands=['card'])
def send_map(message):
    bot.reply_to(message, f"Bunker Card: {random.choice(bunker_cards)}")

# Запуск бота
if __name__ == '__main__':
     print("Все працює. @bunkerIHT_bot")
     bot.polling(none_stop=True)
     
    