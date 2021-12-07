from Peep.Standards import Standards
a = Standards()
from Actions.Tree import Tree
from Actions.action import action
import Blackboard
from peepBoard import peepBoard


class actionTree(object):
    """The full tree object definition that peeps use."""

    

    def __init__(self):
        return

    # Tree node functions
    # These are the functions that tree nodes use. 
    
    def selectNeed(s):
        needNo = 0
        for i in range(0, 8): #len(s.peep.needs) - 1
            if s.pBoard.needlist[i].data.value >= s.pBoard.needlist[needNo].data.value:
                needNo = i
        return needNo

    def rando(s, childNo):
        import random
        return random.randint(0, childNo-1)

    def needTick(s, needNos):
        for i in range(0, len(needNos)-1):
            s.pBoard.needlist[needNos[i][0]].data.valueUp(-needNos[i][1])
            #print(s.pBoard.needlist[needNos[i][0]].data.value)

    def newTree(s, pBoard:peepBoard):
        from Actions.Tr_Sequence import Tr_Sequence
        from Actions.Tr_Selector import Tr_Selector
        from Actions.Tr_Leaf import Tr_Leaf
        from Actions.Tr_Repeater_TillFail import Tr_Repeater_TillFail
        from Actions.Tr_Succeeder import Tr_Succeeder
        from Actions.Tr_Inverter import Tr_Inverter

        s.pBoard = pBoard

        s.newNeedsTree = [Tr_Sequence(name="Hunger", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(0, 2000), (1, 200), (6, -150)]), name="Eat something", ticks=30),
                                                               Tr_Leaf(s.pBoard, lambda: s.needTick([(0, 2000), (1, 200), (6, -150)]), name="Eat something else", ticks=30)]),
                          Tr_Selector(lambda: s.rando(1), name="Thirst", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(1, 3000), (5, -100)]), name="Drink something", ticks=5)]),
                          Tr_Selector(lambda: s.rando(1), name="Fatigue", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(2, 400)]), name="Sleep", ticks=480)]),
                          Tr_Selector(lambda: s.rando(1), name="Social", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(3, 2000)]), name="Talk to someone", ticks=10)]),
                          Tr_Selector(lambda: s.rando(1), name="Hygiene", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(4, 10000)]), name="Have a shower", ticks=7)]),
                          Tr_Selector(lambda: s.rando(1), name="Bladder", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(5, 25000), (6, 1000)]), name="Go to toilet", ticks=2)]),
                          Tr_Selector(lambda: s.rando(1), name="Solids", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(5, 25000), (6, 25000)]), name="Go to toilet", ticks=6)]),
                          Tr_Selector(lambda: s.rando(1), name="Fun", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(7, 1000)]), name="Play a game", ticks=25)]),
                          Tr_Selector(lambda: s.rando(1), name="Fulfillment", children=[Tr_Leaf(s.pBoard, lambda: s.needTick([(8, 1200)]), name="Fulfill yo self", ticks=45)])]

        s.newActionTree = Tr_Sequence(name="Action Tree", children=s.newNeedsTree)

        return s.newActionTree

    # Make the full tree
    def makeTree(self, interests, knowledge, skills):
        # Interest Trees
        wellbeingTrees = [Tree(name="Yoga", data=action(name="Doing Yoga", needsFS=[0,0,0,0,-100,0,0,0,1200], secs=57, tickEffects=[(interests[a.interests["Wellbeing"]], 10000)])),
                          Tree(name="Meditation", data=action(name="Meditating", needsFS=[0,0,0,0,0,0,0,0,1200], secs=21, tickEffects=[(interests[a.interests["Wellbeing"]], 10000)])),
                          Tree(name="Aromatherapy", data=action(name="Taking Aromatherapy", needsFS=[0,0,0,0,0,0,0,0,1200], secs=39, tickEffects=[(interests[a.interests["Wellbeing"]], 10000)])),
                          Tree(name="Massage", data=action(name="Having A Massage", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Wellbeing"]], 10000)]))]
        sportsTrees = [Tree(name="Skating", data=action(name="Ice Scating", needsFS=[0,0,0,0,-50,0,0,0,1200], secs=60, tickEffects=[(interests[a.interests["Sports"]], 10000)])),
                       Tree(name="Roller Blading", data=action(name="Rollerblading", needsFS=[0,0,0,0,-50,0,0,0,1200], secs=50, tickEffects=[(interests[a.interests["Sports"]], 10000)])),
                       Tree(name="Gymnastics", data=action(name="Doing Gymnastics", needsFS=[0,0,0,0,-50,0,0,0,1200], secs=63, tickEffects=[(interests[a.interests["Sports"]], 10000)]))]
        craftsTrees = [Tree(name="Papercraft", data=action(name="Doing Papercraft", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Crafts"]], 10000)])),
                       Tree(name="Knitting", data=action(name="Knitting", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Crafts"]], 10000)])),
                       Tree(name="Sewing", data=action(name="Sewing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Crafts"]], 10000)])),
                       Tree(name="Felting", data=action(name="Felting", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Crafts"]], 10000)])),
                       Tree(name="Dressmaking", data=action(name="Making Dresses", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Crafts"]], 10000)])),
                       Tree(name="Weaving", data=action(name="Weaving", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Crafts"]], 10000)]))]
        artTrees = [Tree(name="Drawing", data=action(name="Drawing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Painting", data=action(name="Painting", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Cinematography", data=action(name="Filming", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="2D Animation", data=action(name="Animating (2D)", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="3D Animation", data=action(name="Animating (3D)", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="VFX", data=action(name="Doing VFX Work", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Pottery", data=action(name="Making Pottery", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Claymation", data=action(name="Making Claymation", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Sculpture", data=action(name="Sculpture", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Woodworking", data=action(name="Woodworking", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Metalworking", data=action(name="Metalworking", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Stone Carving", data=action(name="Carving Stone", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Nail Art", data=action(name="Paintin' Nails", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Photography", data=action(name="Taking Photos", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Textiles", data=action(name="Working with Textiles", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Printing", data=action(name="Print Making", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Collage", data=action(name="Makin' Collages", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Digital Painting", data=action(name="Drawin' Digital", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Pixel Art", data=action(name="Drawin' Pixelart", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Carvings", data=action(name="Making Carvings", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)])),
                    Tree(name="Glasswork", data=action(name="Making Glasswork", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Art"]], 10000)]))]
        musicTrees = [Tree(name="Instruments", data=action(name="Playing an Instrument", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Music"]], 10000)])),
                      Tree(name="Composing", data=action(name="Composing Music", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Music"]], 10000)]))]
        foodTrees = [Tree(name="Baking", data=action(name="Baking a cake", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Food"]], 10000)])),
                     Tree(name="Cooking", data=action(name="Cooking food", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Food"]], 10000)]))]
        techTrees = [Tree(name="Tinkering", data=action(name="Tinkering", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Tech"]], 10000)])),
                     Tree(name="Scambaiting", data=action(name="Scambaiting", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Tech"]], 10000)])),
                     Tree(name="Podcasting", data=action(name="Podcasting", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Tech"]], 10000)]))]
        literatureTrees = [Tree(name="Study", data=action(name="Studying", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Literature"]], 10000)])),
                           Tree(name="Poetry", data=action(name="Writing Poetry", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Literature"]], 10000)])),
                           Tree(name="Writing", data=action(name="Practising Writing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Literature"]], 10000)])),
                           Tree(name="Reading", data=action(name="Reading a Book", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Literature"]], 10000)]))]
        gardeningTrees = [Tree(name="Gardening", data=action(name="Gardening", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Gardening"]], 10000)]))]
        agricultureTrees = [Tree(name="Agriculture", data=action(name="Agriculture...ing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Agriculture"]], 10000)])),
                            Tree(name="Farming", data=action(name="Farming", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Agriculture"]], 10000)]))]
        cultureTrees = [Tree(name="Critique", data=action(name="Critiquing works", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Culture"]], 10000)])),
                        Tree(name="Politics", data=action(name="Making a Political Statement", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Culture"]], 10000)])),
                        Tree(name="Debate", data=action(name="Debating", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Culture"]], 10000)])),
                        Tree(name="High Fashion", data=action(name="Studying Fashion", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Culture"]], 10000)]))]
        outdoorsmanshipTrees = [Tree(name="Fishing", data=action(name="Gone Fishing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Hiking", data=action(name="Gone Hiking", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Cycling", data=action(name="Gone Cycling", needsFS=[0,0,0,0,0,0,0,0,12000], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Biking", data=action(name="Gone Biking", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Driving", data=action(name="Gone Diving", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Driving", data=action(name="Gone Diving", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Archery", data=action(name="Doing Archery", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Guns.", data=action(name="At the gun range.", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Diving", data=action(name="Gone Diving", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Snorkelling", data=action(name="Gone Snorkelling", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Bodyboarding", data=action(name="Gone Bodyboarding", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Surfing", data=action(name="Gone Surfing", needsFS=[0,0,0,0,0,0,0,500,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Skiing", data=action(name="Gone Skiing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Piloting", data=action(name="Gone Plane Flying", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Sailing", data=action(name="Gone Sailing", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Ecology", data=action(name="Doing some Ecology", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Paleontology", data=action(name="Finding Fossils", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Archaeology", data=action(name="Finding Relics", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Zoo", data=action(name="Gone to the Zoo", needsFS=[0,0,0,0,0,0,0,500,1200], secs=40, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)])),
                                Tree(name="Camping", data=action(name="Gone Camping", needsFS=[0,0,0,0,0,0,0,0,1200], secs=340, tickEffects=[(interests[a.interests["Outdoorsmanship"]], 10000)]))]
        educationTrees = [Tree(name="Teaching Online", data=action(name="Teaching Online", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Education"]], 10000)]))]
        performanceTrees = [Tree(name="Teaching Online", data=action(name="Teaching Online", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Performance"]], 10000)]))]
        gamingTrees = [Tree(name="Gaming", data=action(name="Playing videogames", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Gaming"]], 10000)])),
                       Tree(name="Streaming", data=action(name="Streaming", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Gaming"]], 10000)]))]
        fashionTrees = [Tree(name="Studying Fashion", data=action(name="Studying Fashion", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Fashion"]], 10000)])),
                        Tree(name="Gone clohtes shopping", data=action(name="Gone clothes shopping", needsFS=[0,0,0,0,0,0,0,0,1200], secs=80, tickEffects=[(interests[a.interests["Fashion"]], 10000)]))]
        wildlifeTrees = [Tree(name="Out in nature", data=action(name="Out in nature", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Wildlife"]], 10000)]))]
        cleanlinessTrees = [Tree(name="Cleaning", data=action(name="Cleaning", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Cleanliness"]], 10000)]))]
        healthTrees = [Tree(name="Studying health", data=action(name="Studying medical science", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Health"]], 10000)]))]
        automobilesTrees = [Tree(name="Tinkering with cars", data=action(name="Tinkering with the car", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Automobiles"]], 10000)]))]
        designTrees = [Tree(name="Typography", data=action(name="Studying Typography", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Design"]], 10000)])),
                       Tree(name="Calligraphy", data=action(name="Practising Calligraphy", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Design"]], 10000)])),
                       Tree(name="Interior Design", data=action(name="Designing Interiors", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Design"]], 10000)])),
                       Tree(name="Architecture", data=action(name="Making Architecture", needsFS=[0,0,0,0,0,0,0,0,1200], secs=40, tickEffects=[(interests[a.interests["Design"]], 10000)])),]
           
        self.interestTree = [Tree(name="Interests",children=[Tree(name="Wellbeing", data=action(name="WellBeing"), children=wellbeingTrees),
                                                             Tree(name="Sports", data=action(name="Sports"), children=sportsTrees),
                                                             Tree(name="Crafts", data=action(name="Crafts"), children=craftsTrees),
                                                             Tree(name="Art", data=action(name="Art"), children=artTrees),
                                                             Tree(name="Music", data=action(name="Music"), children=musicTrees),
                                                             Tree(name="Food", data=action(name="Food"), children=foodTrees),
                                                             Tree(name="Tech", data=action(name="Tech"), children=techTrees),
                                                             Tree(name="Literature", data=action(name="Literature"), children=literatureTrees),
                                                             Tree(name="Gardening", data=action(name="Gardening"), children=gardeningTrees),
                                                             Tree(name="Agriculture", data=action(name="Agriculture"), children=agricultureTrees),
                                                             Tree(name="Culture", data=action(name="Culture"), children=cultureTrees),
                                                             Tree(name="Outdoorsmanship", data=action(name="Outdoorsmanship"), children=outdoorsmanshipTrees),
                                                             Tree(name="Education", data=action(name="Education"), children=educationTrees),
                                                             Tree(name="Performance", data=action(name="Performance"), children=performanceTrees),
                                                             Tree(name="Gaming", data=action(name="Gaming"), children=gamingTrees),
                                                             Tree(name="Fashion", data=action(name="Fashion"), children=fashionTrees),
                                                             Tree(name="Wildlife", data=action(name="Wildlife"), children=wildlifeTrees),
                                                             Tree(name="Cleanliness", data=action(name="Cleanliness"), children=cleanlinessTrees),
                                                             Tree(name="Health", data=action(name="Health"), children=healthTrees),
                                                             Tree(name="Automobiles", data=action(name="Automobiles"), children=automobilesTrees),
                                                             Tree(name="Design", data=action(name="Design"), children=designTrees)
                                                             ], data=action(name="Interests"))]

        # Default Inactive Tree
        self.inactionTree = Tree(name="Inactive", data=action(name="Doing Nothing", value=0, needsFS=[0,0,0,0,0,0,0,0,0], secs=0))

        # Need Trees
        hungerTrees = [Tree(name="Eat", data=action(name="Eat something", value=0, needsFS=[2000,200,0,0,0,0,-50,0,0], secs=30))]
        thirstTrees = [Tree(name="Drink", data=action(name="Drink something", value=0, needsFS=[0,3000,0,0,0,-100,0,0,0], secs=5))]
        fatigueTrees = [Tree(name="Sleep", data=action(name="Go to sleep", value=0, min = 60000, needsFS=[0,0,400,0,0,0,0,0,0], secs=480)),
                        Tree(name="Coffee", data=action(name="Drink Coffe", value=0, needsFS=[0,1000,500,0,0,-500,0,0,0], secs=10))]
        socialTrees = [Tree(name="Talk", data=action(name="Talk to someone", value=0, needsFS=[0,0,0,2000,0,0,0,0,0], secs=10))]
        hygieneTrees = [Tree(name="Shower", data=action(name="Have a shower", value=0, needsFS=[0,0,0,0,10000,0,0,0,0], secs=7))]
        bladderTrees = [Tree(name="Toilet", data=action(name="Go to toilet", value=0, needsFS=[0,0,0,0,0,25000,1000,0,0], secs=2))]
        solidsTrees = [Tree(name="Toilet", data=action(name="Go to toilet", value=0, needsFS=[0,0,0,0,0,25000,25000,0,0], secs=6))]
        funTrees = [Tree(name="Play", data=action(name="Play a game", value=0, needsFS=[0,0,0,0,0,0,0,1000,0], secs=25))]
        fulfillmentTrees = [Tree(name="Hobby", data=action(name="Do a hobby", value=0, needsFS=[0,0,0,0,0,0,0,0,1000], secs=45), children=self.interestTree)]
        cleanTrees = [Tree(name="Take out rubbish", data=action(name="Taking out rubbish", secs=5))]##

        needTrees = [Tree(name="Hunger", data=action(name="Hunger"), min = 10000, children=hungerTrees),
                     Tree(name="Thirst", data=action(name="Thirst"), min = 10000, children=thirstTrees),
                     Tree(name="Fatigue", data=action(name="Fatigue"), min = 60000, children=fatigueTrees),
                     Tree(name="Social", data=action(name="Social"), min = 10000, children=socialTrees),
                     Tree(name="Hygiene", data=action(name="Hygiene"), min = 10000, children=hygieneTrees),
                     Tree(name="Bladder", data=action(name="Bladder", min = 60000), children=bladderTrees),
                     Tree(name="Solids", data=action(name="Solids", min = 60000), children=solidsTrees),
                     Tree(name="Fun", data=action(name="Fun"), children=funTrees),
                     Tree(name="Fulfillment", data=action(name="Fulfillment"), min = 10000, children=fulfillmentTrees),
                     Tree(name="Cleaning", data=action(name="Doing Cleaning"), min = 10000, children=cleanTrees)]

        # Final Base Tree
        self.weightedActionTree = Tree(name="Actions", children=needTrees)
        return self.weightedActionTree
