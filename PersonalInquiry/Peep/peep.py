from WorldObject import WorldObject

import Peep.Standards
import random
from Peep.Levels import Levels
from Peep.Skill import Skill
import Actions.actionTree

from Actions.Tr_Leaf import Tr_Leaf

a = Peep.Standards.Standards()

from Blackboard import Blackboard
from peepBoard import peepBoard

class Peep(WorldObject):
    """description of class"""

    def __init__(self, blackboard,  name="", surname="", age=None, job=0, traits=None, skills=None, knowledges=None, interests=None, rand=True):
        '''
            -Name
            Gender
            -Age
            -Personality Type
            -Traits
            Likes/Dislikes
            Aspirations
            Fears
            gender preference

            Chronotype
            Star Sign
            Enneagram
            Big 5
            -Needs
            Inventory, Money
        '''

        # Initialise from parent WorldObject init 
        super().__init__()

        #self.t = actionTree()
        self.Blackboard = blackboard

        self.isAsleep = False

        #Details
        if name == "":
            self.name = a.getRND_FName()
        else:
            self.name = name

        if surname == "":
            self.surname = a.getRND_LName()
        else:
            self.surname = surname
    
        if age is not None:
            self.age = age     #7 * 12 * 20 - 1
        else:
            self.age = random.randint(15, 50)


        #Personality
        #Introverted/Extroverted, iNtuition/Sensing, Feeling/Thinking(?), Judging/Perceiving
        self.personality = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]

        #Job
        if job == 0:
            self.job = a.getRND_Job()
        else:
            self.job = job
        #Traits
        if traits is not None:
            self.traits = traits
        else:
            self.traitRND()
        #Skills
        if skills is not None:
            self.skills = skills
        else:
            self.skillRND()
        #Knowledge
        if knowledges is not None:
            self.knowledge = knowledges
        else:
            self.knowledgeRND()
        #Interest
        if interests is not None:
            self.interest = interests
        else:
            self.interestRND()
        

        #Action Tree
        self.acTree = Actions.actionTree.actionTree()
        accc = self.acTree.makeTree(self.interest, self.knowledge, self.skills)
        self.actionTree = self.acTree.weightedActionTree

        self.currentHunger = self.actionTree.children[0]
        self.currentThirst = self.actionTree.children[1]
        self.currentFatigue = self.actionTree.children[2]
        self.currentSocial = self.actionTree.children[3]
        self.currentHygiene = self.actionTree.children[4]
        self.currentBladderLiquid = self.actionTree.children[5]
        self.currentBladderSolid = self.actionTree.children[6]
        self.currentFun = self.actionTree.children[7]
        self.currentFulfillment = self.actionTree.children[8]

        self.needs = [self.currentHunger,
                      self.currentThirst,
                      self.currentFatigue,
                      self.currentSocial,
                      self.currentHygiene,
                      self.currentBladderLiquid,
                      self.currentBladderSolid,
                      self.currentFun,
                      self.currentFulfillment]

        self.currentAction = self.acTree.inactionTree
        self.currentActionTicks = 0


        self.peepBoard = peepBoard(Tr_Leaf(self, 1), needlist=self.needs)
        neee = self.acTree.newTree(self.peepBoard)
        self.newTree = self.acTree.newActionTree
       
       #self.randomise()

    ##RANDOMISER
    def randomise(self):
        self.traitRND()
        if(self.name == "" and self.surname == ""):
            self.nameRand()
        self.Personality = [True] * 4
        for i in range(0,3):
            self.Personality[i] = random.randint(0,1)

    def traitRND(self):
        self.traits = [0]
        for i in range(0, a.TraitNo):
            self.traits.append(random.randint(0,1))

    def skillRND(self):
        self.skills = [Skill("",0)]
        for skill in range(1, a.SkillNo+1):
            b = Skill(a.skills.inverse[skill], skill, lvl=random.randint(0,10))
            self.skills.append(b)
            
    def knowledgeRND(self):
        self.knowledge = [Levels("",0)]
        for kn in range(1, a.KnowledgeNo+1):
            b = Levels(a.knowledges.inverse[kn], kn, lvl=random.randint(0,100))
            self.knowledge.append(b)

    def interestRND(self):
        self.interest = [Levels("",0)]
        for intr in range(1, a.InterestNo+1):
            b = Levels(a.interests.inverse[intr], intr, lvl=random.randint(0,100))
            self.interest.append(b)

    def jobRand(self):
        self.job = 1

    def nameRand(self):
        self.name = a.getRND_FName()
        self.surname = a.getRND_LName()
    ##/RANDOMISER

    def personalityString(self):
        persText = ""
        if self.personality[0] > 50:
            persText += "I"
        else:
            persText += "E"
        if self.personality[1] > 50:
            persText += "N"
        else:
            persText += "S"
        if self.personality[2] > 50:
            persText += "F"
        else:
            persText += "T"
        if self.personality[3] > 50:
            persText += "J"
        else:
            persText += "P"
        
        return persText

    def toString(self):
        for i in range(1, (a.TraitNo + 1)):
            if(self.traits[i] == 1):
                print(a.traits.inverse[i])

        print(a.jobs.inverse[self.job])

    def hungerCalc(self, currentTime):
        """ Calculate hunger, with base hunger level (10),
            plus three peaks around each meal time. """
        # Base level + traits
        hunger= 10 + (20 * (self.traits[a.traits['Always Hungry']] - self.traits[a.traits['Never Hungry']]))
        # CurrentAction + Random Offset
        hunger -= self.currentAction.data.needsFulfill_Sec[0] - random.randint(0,20)
        # Peaks before each meal time 
        if ((currentTime < 420) and (currentTime > 120)):
            hunger -= (1/80) * (currentTime - 270) * (currentTime - 270) - 290
        elif ((currentTime < 720) and (currentTime > 420)):
            hunger -= (1/80) * (currentTime - 570) * (currentTime - 570) - 290
        elif ((currentTime < 1020) and (currentTime > 720)):
            hunger -= (1/80) * (currentTime - 870) * (currentTime - 870) - 290

        return int(hunger)

    def thirstCalc(self):
        return 240 - self.currentAction.data.needsFulfill_Sec[1] + random.randint(0,50)

    def fatigueCalc(self, currentTime):
        # Base Level & Traits
        fatigue = 2  - self.currentAction.data.needsFulfill_Sec[2] + random.randint(0,5)
        # Peak before bed @ 10pm
        if (currentTime <= 1320) and (currentTime > 900):
            timeTemp = currentTime - 900
            fatigue += (6 * timeTemp)/5 + (0.00170659 * timeTemp * timeTemp) - (0.00001107 * timeTemp * timeTemp * timeTemp)
        return int(fatigue)
        #-250*(2*(1/1200 * currentTime)*(1/1200 * currentTime)*(1/1200 * currentTime)-3*(1/1200 * currentTime)*(1/1200 * currentTime)) - ((1/5) * currentTime)

    def socialCalc(self):
        
        return 360 + int((self.personality[0] / 4)-25) - self.currentAction.data.needsFulfill_Sec[3] + random.randint(0,50)

    def hygieneCalc(self):
        return 60 - self.currentAction.data.needsFulfill_Sec[4] + random.randint(0,50)

    def bladderCalc(self):
        return 360 + (20 * self.traits[a.traits['Tiny Bladder']]) - (20 * self.traits[a.traits['Steel Bladder']]) - self.currentAction.data.needsFulfill_Sec[5] + random.randint(0,50)

    def solidsCalc(self):
        return 300 + (20 * self.traits[a.traits['Tiny Bladder']]) - (20 * self.traits[a.traits['Steel Bladder']]) - self.currentAction.data.needsFulfill_Sec[6] + random.randint(0,50)

    def funCalc(self):
        return 200 + (20 * self.traits[a.traits['Dopamine Junkie']]) - self.currentAction.data.needsFulfill_Sec[7] + random.randint(0,50)

    def fulfillmentCalc(self):
        return 100 + (20 * self.traits[a.traits['Motivated']]) - (20 * self.traits[a.traits['Procrastinator']]) - self.currentAction.data.needsFulfill_Sec[8] + random.randint(0,50)

    def tick(self, currentTime):
        # Needs Tick
        # Calls to each need calc, corresponding action values updated and action stopped if need emptied by current action. 

        #+ (8 * self.traits[a.traits['']])

        # Hunger
        if self.peepBoard.needlist[0].data.valueUp(self.hungerCalc(currentTime)) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[0].data.value >= 80000:
            self.peepBoard.needlist[0].data.value = 80000
        # Thirst
        if self.peepBoard.needlist[1].data.valueUp(self.thirstCalc()) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[1].data.value >= 80000:
            self.peepBoard.needlist[1].data.value = 80000
        # Fatigue
        if self.peepBoard.needlist[2].data.valueUp(self.fatigueCalc(currentTime)) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[2].data.value >= 80000:
            self.peepBoard.needlist[2].data.value = 80000
        # Social
        if self.peepBoard.needlist[3].data.valueUp(self.socialCalc()) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[3].data.value >= 80000:
            self.peepBoard.needlist[3].data.value = 80000
        # Hygiene
        if self.peepBoard.needlist[4].data.valueUp(self.hygieneCalc()) == 0 and self.currentAction.data.interrupt: # +sweaty/nonsweaty +weight * activity
            self.currentActionTicks = 0 
        elif self.peepBoard.needlist[4].data.value >= 80000:
            self.peepBoard.needlist[4].data.value = 80000
        # Bladder
        if self.peepBoard.needlist[5].data.valueUp(self.bladderCalc()) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[5].data.value >= 80000:
            self.peepBoard.needlist[5].data.value = 80000
        # Solids
        if self.peepBoard.needlist[6].data.valueUp(self.solidsCalc()) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[6].data.value >= 80000:
            self.peepBoard.needlist[6].data.value = 80000
        # Fun
        if self.peepBoard.needlist[7].data.valueUp(self.funCalc()) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[7].data.value >= 80000:
            self.peepBoard.needlist[7].data.value = 80000
        # Fulfillment
        if self.peepBoard.needlist[8].data.valueUp(self.fulfillmentCalc()) == 0 and self.currentAction.data.interrupt:
            self.currentActionTicks = 0
        elif self.peepBoard.needlist[8].data.value >= 80000:
            self.peepBoard.needlist[8].data.value = 80000

        self.newTree.Call()
        print(self.peepBoard.currentLeaf.name)

        for i in range(0, a.InterestNo - 1):
            #print(self.currentFulfillment.children[0].children[0].children[0].name)
            self.currentFulfillment.children[0].children[0].children[i].data.value = self.interest[i + 1].lvl

        if self.currentAction.data.tickEffects is not None:
            for effect in self.currentAction.data.tickEffects:
                effect[0].xpUp(effect[1])
                
        # Actions!!!
        self.actionTree.SortChildren()

        #print(self.actionTree.ToString())
        self.currentActionTicks -= 1
        if self.currentActionTicks <=0:
            if self.actionTree.children[0].data.aboveMin():
                self.currentAction = self.actionTree.getFirstLeaf()
                self.currentActionTicks = self.currentAction.data.secs
                #self.actionTree.children[0].data.value -= 6000
            else:
                for action in self.actionTree.children:
                    if action.data.aboveMin():
                        self.currentAction = action.getFirstLeaf()
                        self.currentActionTicks = self.currentAction.data.secs
                        break
                    else:
                        self.currentAction = self.acTree.inactionTree

        if self.currentAction.data.name == "Go to sleep":
            self.isAsleep = True
            print("EEE")
        else:
            self.isAsleep = False
            print("AAA")

        # Ageing
        if(False):
            self.age += 1
        
        if(self.age % (28 * 4)) == 0:
            print("Birthday time!")

