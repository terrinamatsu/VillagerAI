from Actions.Tree import Tree
from Actions.action import action
from WorldObject import WorldObject

class Standards(object):
    """A list of all the static values in the game."""

    def getRND_LName(self):
        import random
        lines = open('Peep/Surnames.txt').read().splitlines()
        return random.choice(lines)

    def getRND_FName(self):
        import random
        lines = open('Peep/FirstNames_F.txt').read().splitlines()
        return random.choice(lines)

    def getRND_Job(self):
        import random
        return random.randint(1, self.jobNo)

    def __init__(self):
        '''
        '''

        from bidict import bidict

        # # WeekDays
        self.weekdays = bidict({'Monday':0,
                                'Tuesday':1,
                                'Wednesday':2,
                                'Thursday':3,
                                'Friday':4,
                                'Saturday':5,
                                'Sunday':6})

        # # Months
        self.months = bidict({'January':0,
                              'February':1,
                              'March':2,
                              'April':3,
                              'May':4,
                              'June':5,
                              'July':6,
                              'August':7,
                              'September':8,
                              'October':9,
                              'November':10,
                              'December':11})


        # # Jobs
        self.jobNo = 20
        self.jobs = bidict({'Unemployed':1,
                           'Plumber':2, #trades
                           'Shop Assistant':3, #retail
                           'Personal Shopper':4,
                           'Salesperson':5,
                           'Manager':6,
                           'Events Planner':7, #events
                           'Wedding Planner':8,
                           'Waiter':9, #food
                           'Chef':10,
                           'Sous-Chef':11,
                           'Baker':12,
                           'Artist':13, #arts
                           'Writer':14,
                           'LorryDriver':15, #transport
                           'Florist':16,
                           'Teacher':17, #healthcare #childcare #education
                           'Vet':18,
                           'Nurse':19,
                           'Doctor':20}) 
        #0 is reserved for default value


        # # Traits
        self.TraitNo = 35
        self.traits = bidict({'Always Hungry':1,
                             'Never Hungry':2,
                             'Critical':3,
                             'Supportive':4,
                             'Dopamine Junkie':5,
                             'Lucky':6,
                             'Unlucky':7,
                             'Clumsy':8,
                             'Illiterate':9,
                             'Outgoing':10,
                             'Agoraphobic':11,
                             'Nudist':12,
                             'Optimist':13,
                             'Pessimist':14,
                             'Buzzkill':15,
                             'Nearsighted':16,
                             'Farsighted':17,
                             'Narcissist':18,
                             'Self-Critical':19,
                             'Flamboyant':20,
                             'Never Nude':21,
                             'Motivated':22,
                             'Procrastinator':23,
                             'Romantic':24,
                             'Vegetarian':25,
                             'Vegan':26,
                             'Clean':27,
                             'Slob':28,
                             'Jealous':29,
                             'Alluring':30,
                             'Perfect Pallet':31,
                             'Serial Romantic':32,
                             'Ace':33,
                             'Steel Bladder':34,
                             'Tiny Bladder':35})
                            #Gratefull, Longing, Restless, 

        # # Skills
        self.SkillNo = 18
        self.skills = bidict({'First Aid':1,
                              'Throwing':2,
                              'Medical':3,
                              'Stealth':4,
                              'Lockpicking':5,
                              'Pickpocketing':6,
                              'Gaming':7,
                              'Gardening':8,
                              'Flower Arranging':9,
                              'Writing':10,
                              'Fishing':11,
                              'Repair':12,
                              'Oration':13,
                              'Bartering':14,
                              'Gambling':15,
                              'Outdoorsmanship':16,
                              'Meditation':17,
                              'Cooking':18})

        # # Areas of Interest <- make hierarchical
        self.InterestNo = 21
        self.interests = bidict({'Wellbeing':1,
                                 'Sports':2,
                                 'Crafts':3,
                                 'Art':4,
                                 'Music':5,
                                 'Food':6,
                                 'Tech':7,
                                 'Literature':8,
                                 'Gardening':9,
                                 'Agriculture':10,
                                 'Culture':11,
                                 'Outdoorsmanship':12,
                                 'Education':13,
                                 'Performance':14,
                                 'Gaming':15,
                                 'Fashion':16,
                                 'Wildlife':17,
                                 'Cleanliness':18,
                                 'Health':19,
                                 'Automobiles':20,
                                 'Design':21,
                                 '...':22,
                                 'Nature':23,
                                 'Partying':24,
                                 'Exercise':25})
        
        # # Knowledge Areas
        self.KnowledgeNo = 36
        self.knowledges = bidict({'Physics':1,
                                  'Chemistry':2,
                                  'Biology':3, 
                                  'Cooking':4,
                                  'Fitness':5,
                                  'Crafts':6,
                                  'Fine Art':7,
                                  'Gaming':8,
                                  'Astrology':9,
                                  'Astonomy':10,
                                  'Finance':11,
                                  'Superheroes':12,
                                  'Westerns':13,
                                  'Steampunk':14,
                                  'Cyberpunk':15,
                                  'Cars':16,
                                  'Aviation':17,
                                  'Space':18,
                                  'Music':19,
                                  'Film':20,
                                  'Prototyping':21,
                                  'Technology':22,
                                  'Politics':23,
                                  'Travel':24,
                                  'Weather':25,
                                  'Sports':26,
                                  'Pets':27,
                                  'Food':28,
                                  'Fashion':29,
                                  'Health':30,
                                  'Wellness':31,
                                  'Environmentalism':32,
                                  'Nature':33,
                                  'Partying':34,
                                  'Exercise':35,
                                  'Science Fiction':36})
        ##/\ Probably actually makes sense for knowledge and interest areas to be the same list

        # # Life Goals
        self.LifeGoalNo = 20
        self.LifeGoals = bidict({'':1,
                                 '':2,
                                 '':3,
                                 '':4,
                                 '':5,
                                 '':6,
                                 '':7,
                                 '':8,
                                 '':9,
                                 '':10,
                                 '':11,
                                 '':12,
                                 '':13,
                                 '':14,
                                 '':15,
                                 '':16,
                                 '':17,
                                 '':18,
                                 '':19,
                                 '':20})


        #self.weightedActionTree.children.sort()

        #self.t_ = 