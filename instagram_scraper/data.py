from datetime import date

INPUTS = [
    {
        "festival": "Amsterdam Dance Event",
        "hashtags": [
            "amsterdamdanceevent",
            "ade",
            "amsterdamdanceevent2022",
            "ade2022",
        ],
        "start_date": date(2022, 9, 1),
        "end_date": None,
    },
    {
        "festival": "Pinkpop",
        "hashtags": ["pinkpop", "pinkpop2023", "pinkpopfestival"],
        "start_date": date(2023, 5, 1),
        "end_date": None,
    },
]

SUBSTANCES = {
    "Stimulants": {
        "Amfetamine": [
            "Speed",
            "Pep",
            "Snelle",
            "Snufjes",
            "Wittebommen",
            "Uppers",
            "Amphetamine",
        ],
        "Methamfetamine": ["Yaba", "Kristal", "Crystalmeth", "Ice", "Methamphetamine"],
        "Cocaïne": ["Coke", "Snuif", "Wittepoeder", "Snek", "Sneeuw", "Wittedame"],
        "Mephedrone": ["Meow", "Meph", "Miauw", "4MMC"],
        "Poppers": ["Lockerroom", "Aromas", "Pufjes", "Rush", "Aroma"],
        "4CEC": ["Clephedrone"],
        "3MMC": ["Metaphedrone"],
        "4FMA": [],
    },
    "Hallucinogens": {
        "LSD": ["Trip", "Lucy", "Zuur"],
        "Paddos": ["Shrooms", "Truffels", "MagicMushrooms", "Paddo", "MagicMushroom"],
        "Ayahuasca": ["Heilige drank", "Yage"],
        "2CI": ["TripI", "2CIodine", "Smiles"],
        "DMT": ["BusinessmansTrip", "Spiritueelpoeder"],
        "25INBOMe": ["Smiles", "25I", "N-Bomb"],
        "2CB": ["Erox", "Trip2", "2CBro", "Nexus"],
    },
    "Depressants": {
        "Ketamine": ["SpecialK", "Keta", "K", "Kvee"],
        "Benzodiazepines": ["Pammetjes", "Valis", "Downers", "Benzos", "Vali", "Benzo"],
        "Kratom": ["Ketum", "Thang", "Kratombladeren", "Biak"],
        "GHB": [
            "Liquid X",
            "G",
            "GrievousBodilyHarm",
            "VloeibareXTC",
            "Buisje",
            "TanteG",
        ],
        "Temazepam": ["Temas", "Pammetjes", "Goedslapenpil", "Pam", "Tema"],
        "Cannabis": [
            "Wiet",
            "Hasj",
            "Joint",
            "Weed",
            "Blunt",
            "Pot",
            "MaryJane",
            "Ganja",
        ],
        "Alcohol": ["Pils", "Zuipen", "Drank", "Bier", "Gerstenat", "Hopwater"],
        "Lachgas": ["N2O", "Ballonnetje", "Nossies", "Lachies"],
    },
    "Other": {
        "XTC": ["E", "X", "XTCpil", "Snoepje", "Molly", "Energiebooster", "Ectasy"],
        "Tramadol": ["Trammelol", "Trammies", "Trawant", "Trammelant"],
        "4FA": ["4FMP", "4F", "XTClight"],
        "Kanna": ["Kougoed", "Channa"],
        "MDA": ["LoveDrug", "XTCPlus", "Adam", "Sass"],
        "3MMC": ["3M", "3Mtje", "Poes"],
        "Spice": ["Fakewiet"],
    },
    "Drugs": {
        "Pillen": ["Pilletjes"],
        "Smoken": ["Spacen", "High", "Stoned", "Blowen", "Trippen"],
    },
}
