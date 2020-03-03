class CourseChoices:
    ACCOUNTING = "Accounting"
    ANATOMY = "Anatomy"
    ARCHAEOLOGY = "Archaeology"
    ASTRONOMY = "Astronomy"
    BIOCHEMISTRY = "Biochemistry"
    BUSINESS = "Business"
    CELTIC_STUDIES = "Celtic Studies"
    CHEMISTRY = "Chemistry"
    CIVIL_ENGINEERING = "Civil Engineering"
    COMPUTING_SCIENCE = "Computing Science"
    DENTISTRY = "Dentistry"
    EARTH_SCIENCE = "Earth Science"
    ECONOMICS = "Economics"
    ENGINEERING = "Engineering"
    ENGLISH_LITERATURE = "English Literature"
    FILM = "Film and Television Studies"
    FINANCE = "Finance"
    FRENCH = "French"
    GAELIC = "Gaelic"
    GENETICS = "Genetics"
    GEOGRAPHY = "Geography"
    GEOLOGY = "Geology"
    GERMAN = "German"
    GREEK = "Greek"
    HISTORY = "History"
    HISTORY_OF_ART = "History of Art"
    HUMAN_BIOLOGY = "Human Biology"
    IMMUNOLOGY = "Immunology"
    ITALIAN = "Italian"
    LATIN = "Latin"
    MARINE_BIOLOGY = "Marine Biology"
    MATHS = "Mathematics"
    MEDICINE = "Medicine"
    MICROBIOLOGY = "Microbiology"
    MUSIC = "Music"
    NEUROSCIENCE = "Neuroscience"
    NURSING = "Nursing"
    PHARMACOLOGY = "Pharmacology"
    PHILOSOPHY = "Philosophy"
    PHYSICS = "Physics"
    PHYSIOLOGY = "Physiology"
    POLITICS = "Politics"
    PORTUGUESE = "Portuguese"
    PSYCHOLOGY = "Psychology"
    RUSSIAN = "Russian"
    SOCIOLOGY = "Sociology"
    SOFTWARE_ENGINEERING = "Software Engineering"
    SPANISH = "Spanish"
    STATISTICS = "Statistics"
    THEOLOGY = "Theology"
    VET_MEDICINE = "Veterinary Medicine"
    ZOOLOGY = "Zoology"

    ALL_CHOICES = [ACCOUNTING, ANATOMY, ARCHAEOLOGY, ASTRONOMY, BIOCHEMISTRY, BUSINESS, CELTIC_STUDIES,
        CHEMISTRY, CIVIL_ENGINEERING, COMPUTING_SCIENCE, DENTISTRY, EARTH_SCIENCE, ECONOMICS, ENGINEERING,
        ENGLISH_LITERATURE, FILM, FINANCE, FRENCH, GAELIC, GENETICS, GEOGRAPHY, GEOLOGY, GERMAN, GREEK,
        HISTORY, HISTORY_OF_ART, HUMAN_BIOLOGY, IMMUNOLOGY, ITALIAN, LATIN, MARINE_BIOLOGY, MATHS, MEDICINE,
        MICROBIOLOGY, MUSIC, NEUROSCIENCE, NURSING, PHARMACOLOGY, PHILOSOPHY, PHYSICS, PHYSIOLOGY, POLITICS,
        PORTUGUESE, PSYCHOLOGY, RUSSIAN, SOCIOLOGY, SOFTWARE_ENGINEERING, SPANISH, STATISTICS, THEOLOGY,
        VET_MEDICINE, ZOOLOGY]

    @staticmethod
    def get_choices():
        return [(v,v) for v in CourseChoices.ALL_CHOICES]

class SocietyChoices:
    ACAPELLA = "Acapella"
    ART_LIFE_DRAWING = "Art and Life Drawing"
    ART_APPRECIATION = "Art Appreciation"
    ASTROLOGY = "Astrology"
    ASTRONOMY = "Astronomy"
    BAD_MOVIE = "Bad Movie"
    BAKING = "Baking"
    BALLROOM_LATIN = "Ballroom and Latin Dancing"
    BEEKEEPING = "Beekeeping"
    BHAKTI_YOGA = "Bhakti Yoga"
    BIG_BAND = "Big Band"
    GUBES = "Bridging Education"
    BUDDHIST = "Buddhist"
    BUSINESS = "Business Club"
    FBP = "Food and Body Positivity"
    BHF = "Friends of BHF"
    GUCVS = "Cardiovascular"
    CATHOLIC = "Catholic Association"
    CECILIAN = "Cecilian"
    CHICKEN = "Chicken Wing"
    CHINESE = "Chinese Students Community"
    CHOCOLATE = "Chocolate"
    CHRISTIAN = "Christian Union"
    COMIC = "Comic Creators Club"
    COMMUNIST = "Communist"
    COMP_PROGRAMMING = "Competitive Programming"
    CRAFTS = "Crafts"
    CHOICE = "Glagow Students for Choice"
    OPEN_CAGES = "Open Cages"
    GUSCDC = "Scottish Country Dance Club"
    CLIMATE = "Students Against Climate Change"
    DANCE4WATER = "Dance4Water Glasgow"
    DANCEMANIA = "Dancemania"
    DISNEY = "Disney"
    DOC_WHO = "Doctor Who"
    DOCUMENTARY = "Documentary"
    DRAG = "Drag"
    POLE_DANCING = "Pole Dancing Club"
    GSDC = "Student Dance Company"
    SELF_DEFENCE = "Self Defence"
    EUROPEAN = "European"
    EUROVISION = "Eurovision"
    EXPLORATION = "Exploration"
    X_REBELION = "Extinction Rebellion"
    FILM = "Film"
    WAR_FILM = "War Film"
    GAMING = "Gaming"
    GIN = "Gin"
    GIST = "Glasgow International Student Theatre"
    GUDEV = "Game Design and Development"
    GREENS = "Scottish Greens"
    GIST = "Glasgow Insight into Science and Technology"
    HARM = "Harm Reduction"
    HARRY_POTTER = "Harry Potter"
    HISTORY = "History"
    JAPAN = "Japan"
    JEWISH = "Jewish"
    JUGGLING = "Juggling at GU"
    JANE_AUSTEN = "Students of a Jane Austen Persuasion"
    KPOP = "K-Pop"
    KOREAN = "Korean"
    GULGBTQ = "GULGBTQ+"
    MANGA = "Manga and Anime"
    MARXISTS = "Marxists"
    MATURE = "Mature Students Association"
    MORGUL = "GU Rock and Metal"
    MUSIC = "Music Club"
    MUSLIM = "Muslim Student Association"
    OPERA = "Opera"
    ONEKIND = "Onekind"
    PHILOSOPHY = "Philosophy"
    PHYSICS = "Physics"
    PLASTIC_SURGERY = "Plastic Surgery"
    POLITICS = "Politics"
    QUIZ = "Quiz"
    REAL_ALE = "Real Ale"
    ROBOTICS = "Robotics"
    SCREENWRITING = "Screenwriting"
    SEWING = "Sewing"
    SEXPRESSION = "Sexpression"
    SHAKESPEARE = "Shakespeare"
    SHREK = "Shrek"
    SIGN_LANGUAGE = "Sign Language"
    SOCIALIST = "Socialist"
    WOMEN_TECH = "Society for Women in Tech"
    STAG = "Student Theatre at Glasgow"
    SWAG = "Successful Women at Glasgow"
    SURGICAL = "Surgical"
    GUSTS = "Sustainable Technologies"
    IMPROV = "Improv Teatime"
    TEA = "Tea"
    TECH = "Tech"
    TEDX = "Tedx"
    TENNENTS = "Tennents Lager Appreciation"
    RACING = "UGRacing"
    VEGAN = "Vegan"
    WALKING = "Walking"
    WINE = "Wine"
    WISTEM = "Women in Science, Tech, Engineering and Maths"
    CREATIVE_WRITING = "Createive Writing"
    RUNNING = "Hares and Hounds Running Club"
    KARATE = "Karate"
    HOCKEY = "Hockey"
    RUGBY = "Rugby Football"
    SAILING = "Sailing Club"
    SKI_SNOWBOARD = "Ski & Snowboard Club"
    AIKIDO = "Aikido"
    AMERICAN_FOOTBALL = "American Football"
    ATHLETICS = "Athletics"
    BADMINTON = "Badminton"
    BASKETBALL = "Basketball"
    ROWING = "Boat/Rowing"
    BOXING = "Boxing"
    CANOE = "Canoe"
    CHEERLEADING = "Cheerleading"
    CRICKET = "Cricket"
    CURLING = "Curling"
    CYCLING = "Cycling"
    FENCING = "Fencing"
    FOOTBALL = "Football"
    GAELIC_FOOTBALL = "Gaelic Football"
    GOLF = "Golf"
    GYMNASTICS = "Gymnastics"
    JUDO = "Judo"
    KENDO = "Kendo"
    LACROSSE = "Lacrosse"
    MOUNTENEERING = "Mounteneering"
    MUAY_THAI = "Muay Thai Boxing"
    NETBALL = "Netball"
    POTHOLING = "Potholing (Caving)"
    RIDING = "Riding/Equestrian"
    SHINTY = "Shinty"
    SHORINJI = "Shorinji Kempo"
    SKYDIVE = "Skydive"
    SQUASH = "Squash"
    SURF = "Surf"
    SWIMMING_WATERPOLO = "Swimming and Waterpolo"
    TAEKWONDO = "Taekwondo"
    TRAMPOLINE = "Trampoline"
    TRIATHLON = "Triathlon"
    FRISBEE = "Ultimate Frisbee"
    VOLLEYBALL = "Volleyball"
    WAKEBOARDING = "Wakeboarding"
    WEIGHTLIFTING = "Weightlifting"
    YOGA = "Yoga"
    TABLE_TENNIS = "Table Tennis"
    TENNIS = "Tennis"

    ALL_CHOICES = [ACAPELLA, ART_LIFE_DRAWING, ART_APPRECIATION, ASTROLOGY, ASTRONOMY, BAD_MOVIE, BAKING,
        BALLROOM_LATIN, BEEKEEPING, BHAKTI_YOGA, BIG_BAND, GUBES, BUDDHIST, BUSINESS, FBP, BHF, GUCVS, CATHOLIC,
        CECILIAN, CHICKEN, CHINESE, CHOCOLATE, CHRISTIAN, COMIC, COMMUNIST, COMP_PROGRAMMING, CRAFTS, CHOICE,
        OPEN_CAGES, GUSCDC, CLIMATE, DANCE4WATER, DANCEMANIA, DISNEY, DOC_WHO, DOCUMENTARY, DRAG, POLE_DANCING,
        GSDC, SELF_DEFENCE, EUROPEAN, EUROVISION, EXPLORATION, X_REBELION, FILM, WAR_FILM, GAMING, GIN, GIST,
        GUDEV, GREENS, GIST, HARM, HARRY_POTTER, HISTORY, JAPAN, JEWISH, JUGGLING, JANE_AUSTEN, KPOP, KOREAN,
        GULGBTQ, MANGA, MARXISTS, MATURE, MORGUL, MUSIC, MUSLIM, OPERA, ONEKIND, PHILOSOPHY, PHYSICS, PLASTIC_SURGERY,
        POLITICS, QUIZ, REAL_ALE, ROBOTICS, SCREENWRITING, SEWING, SEXPRESSION, SHAKESPEARE, SHREK, SIGN_LANGUAGE,
        SOCIALIST, WOMEN_TECH, STAG, SWAG, SURGICAL, GUSTS, IMPROV, TEA, TECH, TEDX, TENNENTS, RACING, VEGAN,
        WALKING, WINE, WISTEM, CREATIVE_WRITING, RUNNING, KARATE, HOCKEY, RUGBY, SAILING, SKI_SNOWBOARD, AIKIDO,
        AMERICAN_FOOTBALL, ATHLETICS, BADMINTON, BASKETBALL, ROWING, BOXING, CANOE, CHEERLEADING, CRICKET, CURLING,
        CYCLING, FENCING, FOOTBALL, GAELIC_FOOTBALL, GOLF, GYMNASTICS, JUDO, KENDO, LACROSSE, MOUNTENEERING, MUAY_THAI,
        NETBALL, POTHOLING, RIDING, SHINTY, SHORINJI, SKYDIVE, SQUASH, SURF, SWIMMING_WATERPOLO, TAEKWONDO, TRAMPOLINE,
        TRIATHLON, FRISBEE, VOLLEYBALL, WAKEBOARDING, WEIGHTLIFTING, YOGA, TABLE_TENNIS, TENNIS]

    @staticmethod
    def get_choices():
        return [(v,v) for v in SocietyChoices.ALL_CHOICES]

class InterestChoices:
    YOGA = "Yoga"
    FOOTBALL = "Football"
    TENNIS = "Tennis"
    ART = "Art"
    PHOTOGRAPHY = "Photography"
    SWIMMING = "Swimming"
    # TODO: Add more interests

    ALL_CHOICES = [YOGA, FOOTBALL, TENNIS, ART, PHOTOGRAPHY, SWIMMING]

    @staticmethod
    def get_choices():
        return [(v,v) for v in InterestChoices.ALL_CHOICES]

class GenderChoices:
    FEMALE = "F"
    MALE = "M"
    NON_BINARY = "N"

    ALL_CHOICES = [FEMALE, MALE, NON_BINARY]

    @staticmethod
    def get_choices():
        labels = ["Female", "Male", "Non-Binary"]
        return [(gender, label) for gender, label in zip(GenderChoices.ALL_CHOICES, labels)]

class LibraryFloorChoices:
    LEVEL_1 = "Level 1"
    LEVEL_2 = "Level 2"
    LEVEL_3 = "Level 3"
    LEVEL_4 = "Level 4"
    LEVEL_5 = "Level 5"
    LEVEL_6 = "Level 6"
    LEVEL_7 = "Level 7"
    LEVEL_8 = "Level 8"
    LEVEL_9 = "Level 9"
    LEVEL_10 = "Level 10"
    LEVEL_11 = "Level 11"
    LEVEL_12 = "Level 12"
    READINGROOM = "Round Reading Room"
    OTHER = "Other"

    ALL_CHOICES = [LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5, LEVEL_6, LEVEL_7, LEVEL_8,
                    LEVEL_9, LEVEL_10, LEVEL_11, LEVEL_12, READINGROOM, OTHER]

    @staticmethod
    def get_choices():
        return [(v,v) for v in LibraryFloorChoices.ALL_CHOICES]