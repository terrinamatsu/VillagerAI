from Peep.peep import Peep
from tkinter import *
from tkinter import ttk

import Peep.Standards
from Peep.Levels import Levels
from Peep.Skill import Skill
from functools import partial
import peepCreatorUI
import Blackboard
from PIL import ImageTk, Image

St = Peep.Standards.Standards()

class MainWindow(object):
    """This is the main game window, which displays the currently selected peep,
       as well as the option to select other peeps to display from the peeplist."""
    

    def __init__(s, peepList : [Peep], blackboard : Blackboard.Blackboard):
        s.BB = blackboard
        s.peepListRef = s.BB.peeps

        # Window Setup
        s.root = Tk()
        s.root.title('The Village AI')
        s.root.geometry("1400x1000")
        # Main Character Frame
        s.MainPeep_Frame = LabelFrame(s.root, text="Current Active Peep")
        s.MainPeep_Frame.grid(row=0, column=0, sticky="W")
        s.MainPeep_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Frame.columnconfigure(0, weight=1)
            # Details Frame
        s.MainPeep_Detail_Frame = LabelFrame(s.MainPeep_Frame, text="Details")
        s.MainPeep_Detail_Frame.grid(row=0, column=0, sticky="W")
        s.MainPeep_Detail_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Detail_Frame.columnconfigure(0, weight=1)
                # Name
        s.MP_name_Label = Label(s.MainPeep_Detail_Frame, text=(peepList[0].name + " " + peepList[0].surname))
        s.MP_name_Label.grid(row=0, column=0, sticky="W", padx=5)
                # Age
        s.MP_age_Label = Label(s.MainPeep_Detail_Frame, text=str(peepList[0].age))
        s.MP_age_Label.grid(row=0, column=1, sticky="W", padx=5)
                # Personality Type
        s.MP_personality_Label = Label(s.MainPeep_Detail_Frame, text=peepList[0].personalityString())
        s.MP_personality_Label.grid(row=0, column=2, sticky="W", padx=5)
                # Job
        s.MP_job_Label = Label(s.MainPeep_Detail_Frame, text=St.jobs.inverse[peepList[0].job])
        s.MP_job_Label.grid(row=0, column=3, sticky="W", padx=5)
                # Current Action
        s.MP_action_Label = Label(s.MainPeep_Detail_Frame, text=peepList[0].currentAction.data.name, width=20)
        s.MP_action_Label.grid(row=0, column=4, sticky="W", padx=10)
                # Current Time
        s.MP_Time_Label = Label(s.MainPeep_Detail_Frame, text=str(int(s.BB.time/60)) + ":" + str(s.BB.time%60), width=20)
        s.MP_Time_Label.grid(row=0, column=5, padx=10)
                # Current Date
        s.MP_Date_Label = Label(s.MainPeep_Detail_Frame, text=(St.weekdays.inv[s.BB.day%7]) + " " + (St.months.inv[int(s.BB.day/7)] + " " + str(s.BB.year)), width=20)
        s.MP_Date_Label.grid(row=0, column=6, padx=10)
            # Needs Frame
        s.MainPeep_Needs_Frame = LabelFrame(s.MainPeep_Frame, text="Needs")
        s.MainPeep_Needs_Frame.grid(row=1, column=0, sticky="W")
        s.MainPeep_Needs_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Needs_Frame.columnconfigure(0, weight=1)
                # Need Values, Icon, Progress Bars
                    # Hunger
        s.MainPeep_nHunger_Label = Label(s.MainPeep_Needs_Frame, text="Hunger: " + str(peepList[0].currentHunger.data.value),width=15)
        s.MainPeep_nHunger_Label.grid(row=0, column=0, columnspan=2, sticky="W", padx=5)

        hungerIcon0 = ImageTk.PhotoImage(Image.open("food_need.png"))
        s.MP_nHunger_Icon = Label(s.MainPeep_Needs_Frame, image = hungerIcon0)
        s.MP_nHunger_Icon.grid(row=1, column=0, sticky="W", padx=5)

        s.MP_nHunger_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nHunger_PBar.grid(row=1, column=1, sticky="WE", padx=5)
                    # Thirst
        s.MainPeep_nThirst_Label = Label(s.MainPeep_Needs_Frame, text="Thirst: " + str(peepList[0].currentThirst.data.value),width=15)
        s.MainPeep_nThirst_Label.grid(row=0, column=2, columnspan=2, sticky="W", padx=5)

        thirstIcon0 = ImageTk.PhotoImage(Image.open("thirst_need.png"))
        s.MP_nThist_Icon = Label(s.MainPeep_Needs_Frame, image = thirstIcon0)
        s.MP_nThist_Icon.grid(row=1, column=2, sticky="W", padx=5)

        s.MP_nThirst_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nThirst_PBar.grid(row=1, column=3, sticky="WE", padx=5)
                    # Fatigue
        s.MainPeep_nFatigue_Label = Label(s.MainPeep_Needs_Frame, text="Fatigue: " + str(peepList[0].currentFatigue.data.value),width=15)
        s.MainPeep_nFatigue_Label.grid(row=0, column=4, columnspan=2, sticky="W", padx=5)

        fatigueIcon0 = ImageTk.PhotoImage(Image.open("sleep_need.png"))
        s.MP_nFatigue_Icon = Label(s.MainPeep_Needs_Frame, image = fatigueIcon0)
        s.MP_nFatigue_Icon.grid(row=1, column=4, sticky="W", padx=5)

        s.MP_nFatigue_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nFatigue_PBar.grid(row=1, column=5, sticky="WE", padx=5)
                    # Social
        s.MainPeep_nSocial_Label = Label(s.MainPeep_Needs_Frame, text="Social: " + str(peepList[0].currentSocial.data.value),width=15)
        s.MainPeep_nSocial_Label.grid(row=0, column=6, columnspan=2, sticky="W", padx=5)

        socialIcon0 = ImageTk.PhotoImage(Image.open("social_need.png"))
        s.MP_nSocial_Icon = Label(s.MainPeep_Needs_Frame, image = socialIcon0)
        s.MP_nSocial_Icon.grid(row=1, column=6, sticky="W", padx=5)

        s.MP_nSocial_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nSocial_PBar.grid(row=1, column=7, sticky="WE", padx=5)
                    # Hygiene
        s.MainPeep_nHygiene_Label = Label(s.MainPeep_Needs_Frame, text="Hygiene: " + str(peepList[0].currentHygiene.data.value),width=15)
        s.MainPeep_nHygiene_Label.grid(row=0, column=8, columnspan=2, sticky="W", padx=5)

        hygieneIcon0 = ImageTk.PhotoImage(Image.open("hygienebSolid_need.png"))
        s.MP_nHygiene_Icon = Label(s.MainPeep_Needs_Frame, image = hygieneIcon0)
        s.MP_nHygiene_Icon.grid(row=1, column=8, sticky="W", padx=5)

        s.MP_nHygiene_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nHygiene_PBar.grid(row=1, column=9, sticky="WE", padx=5)
                    # Bladder
        s.MainPeep_nBladder_Label = Label(s.MainPeep_Needs_Frame, text="Bladder: " + str(peepList[0].currentBladderLiquid.data.value),width=15)
        s.MainPeep_nBladder_Label.grid(row=0, column=10, columnspan=2, sticky="W", padx=5)

        bladderIcon0 = ImageTk.PhotoImage(Image.open("bLiquid_need.png"))
        s.MP_nBladder_Icon = Label(s.MainPeep_Needs_Frame, image = bladderIcon0)
        s.MP_nBladder_Icon.grid(row=1, column=10, sticky="W", padx=5)

        s.MP_nBladder_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nBladder_PBar.grid(row=1, column=11, sticky="WE", padx=5)
                    # Solids
        s.MainPeep_nSolids_Label = Label(s.MainPeep_Needs_Frame, text="Solids: " + str(peepList[0].currentBladderSolid.data.value),width=15)
        s.MainPeep_nSolids_Label.grid(row=0, column=12, columnspan=2, sticky="W", padx=5)

        solidsIcon0 = ImageTk.PhotoImage(Image.open("bSolid_need.png"))
        s.MP_nSolids_Icon = Label(s.MainPeep_Needs_Frame, image = solidsIcon0)
        s.MP_nSolids_Icon.grid(row=1, column=12, sticky="W", padx=5)

        s.MP_nSolids_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nSolids_PBar.grid(row=1, column=13, sticky="WE", padx=5)
                    # Fun
        s.MainPeep_nFun_Label = Label(s.MainPeep_Needs_Frame, text="Fun: " + str(peepList[0].currentFun.data.value),width=15)
        s.MainPeep_nFun_Label.grid(row=0, column=14, columnspan=2, sticky="W", padx=5)

        funIcon0 = ImageTk.PhotoImage(Image.open("fun_need.png"))
        s.MP_nFun_Icon = Label(s.MainPeep_Needs_Frame, image = funIcon0)
        s.MP_nFun_Icon.grid(row=1, column=14, sticky="W", padx=5)

        s.MP_nFun_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nFun_PBar.grid(row=1, column=15, sticky="WE", padx=5)
                    # Fulfillment
        s.MainPeep_nFulfillment_Label = Label(s.MainPeep_Needs_Frame, text="Fulfillment: " + str(peepList[0].currentFulfillment.data.value),width=15)
        s.MainPeep_nFulfillment_Label.grid(row=0, column=16, columnspan=2, sticky="W", padx=5)

        fulfillmentIcon0 = ImageTk.PhotoImage(Image.open("fulfillment_need.png"))
        s.MP_nFulfillment_Icon = Label(s.MainPeep_Needs_Frame, image = fulfillmentIcon0)
        s.MP_nFulfillment_Icon.grid(row=1, column=16, sticky="W", padx=5)

        s.MP_nFulfillment_PBar = ttk.Progressbar(s.MainPeep_Needs_Frame, orient=HORIZONTAL, mode='determinate')
        s.MP_nFulfillment_PBar.grid(row=1, column=17, sticky="WE", padx=5)


            # Traits Frame
        s.MainPeep_Traits_Frame = LabelFrame(s.MainPeep_Frame, text="Traits")
        s.MainPeep_Traits_Frame.grid(row=2, column=0, sticky="W")
        s.MainPeep_Traits_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Traits_Frame.columnconfigure(0, weight=1)

        s.MainPeep_Traits_Labels = [Label()]
        for i in range(1, St.TraitNo + 1):
            if peepList[0].traits[i] == 1:
                s.MainPeep_Traits_Labels.append(Label(s.MainPeep_Traits_Frame, text=St.traits.inverse[i], width=15))
                s.MainPeep_Traits_Labels[i].grid(row=int((i-1)/10) , column=((i-1)%10))
            else:
                s.MainPeep_Traits_Labels.append(Label(s.MainPeep_Traits_Frame, text="", width=15))
                s.MainPeep_Traits_Labels[i].grid(row=int((i-1)/10) , column=((i-1)%10))
            # Skills Frame
        s.MainPeep_Skills_Frame = LabelFrame(s.MainPeep_Frame, text="Skills")
        s.MainPeep_Skills_Frame.grid(row=3, column=0, sticky="W")
        s.MainPeep_Skills_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Skills_Frame.columnconfigure(0, weight=1)

        s.MainPeep_Skills_Labels = [Label()]
        for i in range(1, St.SkillNo + 1):
            text = St.skills.inverse[i] + "  " + str(peepList[0].skills[i].lvl)
            s.MainPeep_Skills_Labels.append(Label(s.MainPeep_Skills_Frame, text=text, width=15))
            s.MainPeep_Skills_Labels[i].grid(row=int((i-1)/10) , column=((i-1)%10))
            # Knowledge Frame
        s.MainPeep_Knowledge_Frame = LabelFrame(s.MainPeep_Frame, text="Knowledge")
        s.MainPeep_Knowledge_Frame.grid(row=4, column=0, sticky="W")
        s.MainPeep_Knowledge_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Knowledge_Frame.columnconfigure(0, weight=1)

        s.MainPeep_Knowledge_Labels = [Label()]
        for i in range(1, St.KnowledgeNo + 1):
            text = St.knowledges.inverse[i] + "  " + str(peepList[0].knowledge[i].lvl)
            s.MainPeep_Knowledge_Labels.append(Label(s.MainPeep_Knowledge_Frame, text=text, width=15))
            s.MainPeep_Knowledge_Labels[i].grid(row=int((i-1)/10) , column=((i-1)%10))
            # Interests Frame
        s.MainPeep_Interests_Frame = LabelFrame(s.MainPeep_Frame, text="Interests")
        s.MainPeep_Interests_Frame.grid(row=5, column=0, sticky="W")
        s.MainPeep_Interests_Frame.rowconfigure(0, weight=1)
        s.MainPeep_Interests_Frame.columnconfigure(0, weight=1)

        s.MainPeep_Interests_Labels = [Label()]
        for i in range(1, St.InterestNo + 1):
            text = St.interests.inverse[i] + "  " + str(peepList[0].interest[i].lvl)
            s.MainPeep_Interests_Labels.append(Label(s.MainPeep_Interests_Frame, text=text, width=15))
            s.MainPeep_Interests_Labels[i].grid(row=int((i-1)/10) , column=((i-1)%10))

        # Other Peep Frames
        s.OtherPeep_Frame = LabelFrame(s.root, text="Other Peeps")
        s.OtherPeep_Frame.grid(row=1, column=0, sticky="WE")
        s.OtherPeep_Frame.rowconfigure(0, weight=1)
        s.OtherPeep_Frame.columnconfigure(0, weight=1)

        s.PeepWindows = [LabelFrame()]
        s.PeepWindowsLabels = [[Label()]]
        s.PeepWindowsIcons = [[Label()]]
        s.PeepWindowsProgressBars = [[ttk.Progressbar()]]
        s.PeepWindowsButtons = [Button()]

        hungerIcon = [[ImageTk.PhotoImage]]
        thirstIcon = [[ImageTk.PhotoImage]]
        fatigueIcon = [[ImageTk.PhotoImage]]
        socialIcon = [[ImageTk.PhotoImage]]
        hygieneIcon = [[ImageTk.PhotoImage]]
        bladderIcon = [[ImageTk.PhotoImage]]
        solidsIcon = [[ImageTk.PhotoImage]]
        funIcon = [[ImageTk.PhotoImage]]
        fulfillmentIcon = [[ImageTk.PhotoImage]]

        for i in range(1,  len(peepList)):
            s.PeepWindows.append(LabelFrame(s.OtherPeep_Frame, text=peepList[i].name))
            s.PeepWindows[i].grid(row=int((i-1)/10), column=((i-1)%10))

            ''' Text Labels
            Labels = [Label(s.PeepWindows[i], text=peepList[i].currentHunger, width=10)]
            Labels[0].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentThirst.data.value, width=10))
            Labels[1].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentFatigue.data.value, width=10))
            Labels[2].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentSocial.data.value, width=10))
            Labels[3].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentHygiene.data.value, width=10))
            Labels[4].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentBladderLiquid.data.value, width=10))
            Labels[5].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentBladderSolid.data.value, width=10))
            Labels[6].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentFun.data.value, width=10))
            Labels[7].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentFulfillment.data.value, width=10))
            Labels[8].pack()
            Labels.append(Label(s.PeepWindows[i], text=peepList[i].currentAction.data.name))
            Labels[9].pack()

            s.PeepWindowsLabels.append(Labels)
            '''

            # Icon & Progress Bars

            # Need Icons
            hungerIcon.append(ImageTk.PhotoImage(Image.open("food_need.png")))
            Icons = [Label(s.PeepWindows[i], image = hungerIcon[i])]
            Icons[0].grid(row=0, column=0, sticky="W")
            thirstIcon.append(ImageTk.PhotoImage(Image.open("thirst_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = thirstIcon[i]))
            Icons[1].grid(row=1, column=0, sticky="W")
            fatigueIcon.append(ImageTk.PhotoImage(Image.open("sleep_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = fatigueIcon[i]))
            Icons[2].grid(row=2, column=0, sticky="W")
            socialIcon.append(ImageTk.PhotoImage(Image.open("social_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = socialIcon[i]))
            Icons[3].grid(row=3, column=0, sticky="W")
            hygieneIcon.append(ImageTk.PhotoImage(Image.open("hygienebSolid_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = hygieneIcon[i]))
            Icons[4].grid(row=4, column=0, sticky="W")
            bladderIcon.append(ImageTk.PhotoImage(Image.open("bLiquid_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = bladderIcon[i]))
            Icons[5].grid(row=5, column=0, sticky="W")
            solidsIcon.append(ImageTk.PhotoImage(Image.open("bSolid_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = solidsIcon[i]))
            Icons[6].grid(row=6, column=0, sticky="W")
            funIcon.append(ImageTk.PhotoImage(Image.open("fun_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = funIcon[i]))
            Icons[7].grid(row=7, column=0, sticky="W")
            fulfillmentIcon.append(ImageTk.PhotoImage(Image.open("fulfillment_need.png")))
            Icons.append(Label(s.PeepWindows[i], image = fulfillmentIcon[i]))
            Icons[8].grid(row=8, column=0, sticky="W")
            
            s.PeepWindowsIcons.append(Icons)
            
            
            # Progress Bars
            PBars = [ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate')]
            PBars[0].grid(row=0, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[1].grid(row=1, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[2].grid(row=2, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[3].grid(row=3, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[4].grid(row=4, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[5].grid(row=5, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[6].grid(row=6, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[7].grid(row=7, column=1, sticky="WE")
            PBars.append(ttk.Progressbar(s.PeepWindows[i], orient=HORIZONTAL, mode='determinate'))
            PBars[8].grid(row=8, column=1, sticky="WE")
            
            s.PeepWindowsProgressBars.append(PBars)


            # Action Label
            Labels = [(Label(s.PeepWindows[i], text=peepList[i].currentAction.data.name))]
            Labels[0].grid(row=9, column=0, columnspan = 2)

            s.PeepWindowsLabels.append(Labels)


            # Swap Button
            s.PeepWindowsButtons.append(Button(s.PeepWindows[i], text="Swap", command=partial(s.swapPeeps, i), width=15))
            s.PeepWindowsButtons[i].grid(row=10, column=0, columnspan=2)


        # Options Pannel Frame
        s.Options_Frame = LabelFrame(s.root, text="Options")
        s.Options_Frame.grid(row=0, column=1, columnspan=2, sticky="NS")
        s.Options_Frame.rowconfigure(0, weight=1)
        s.Options_Frame.columnconfigure(0, weight=1)
            # Game Speed/Pause
        s.Options_Step_Button = Button(s.Options_Frame, text="Step", width=10, command=s.tick)
        s.Options_Step_Button.grid(row=1, column=0, columnspan=2)
        s.Options_Play1_Button = Button(s.Options_Frame, text="Play (x1)", width=10, command=lambda: s.play(1))
        s.Options_Play1_Button.grid(row=2, column=0, columnspan=2)
        s.Options_Pause_Button = Button(s.Options_Frame, text="Pause", width=10, command=s.pause)
        s.Options_Pause_Button.grid(row=3, column=0, columnspan=2)
        s.Options_Speed2_Button = Button(s.Options_Frame, text="x2", width=5, command=lambda: s.setSpeed(2))
        s.Options_Speed2_Button.grid(row=4, column=0)
        s.Options_Speed3_Button = Button(s.Options_Frame, text="x3", width=5, command=lambda: s.setSpeed(3))
        s.Options_Speed3_Button.grid(row=4, column=1)
            # Edit Peep List
        s.Options_Edit_Button = Button(s.Options_Frame, text="Edit Peeps", width=10, command=s.editPeeps)
        s.Options_Edit_Button.grid(row=5, column=0, columnspan=2)
            # Refresh
        s.Options_Refresh_Button = Button(s.Options_Frame, text="Refresh", width=10, command=s.redraw)
        s.Options_Refresh_Button.grid(row=6, column=0, columnspan=2)
            # Exit

        s.root.mainloop()


    def redraw(s):
        '''
            Redraws the window; updates all the information for the whole window. 
        '''

        # Details
        s.MP_name_Label.configure(text=(s.peepListRef[0].name + " " + s.peepListRef[0].surname))
        s.MP_age_Label.configure(text=str(s.peepListRef[0].age))
        s.MP_personality_Label.configure(text=s.peepListRef[0].personalityString())
        s.MP_job_Label.configure(text=St.jobs.inverse[s.peepListRef[0].job])
        s.MP_action_Label.configure(text=s.peepListRef[0].currentAction.data.name)
        s.MP_Time_Label.configure(text=str(int(s.BB.time/60)) + ":" + str(s.BB.time%60))
        s.MP_Date_Label.config(text=(St.weekdays.inv[s.BB.day%7]) + " " + (St.months.inv[int(s.BB.day/7)]) + " " + str(s.BB.year))
        # Needs
        s.MainPeep_nHunger_Label.configure(text="Hunger: " + str(s.peepListRef[0].currentHunger.data.value))
        s.MainPeep_nThirst_Label.configure(text="Thirst: " + str(s.peepListRef[0].currentThirst.data.value))
        s.MainPeep_nFatigue_Label.configure(text="Fatigue: " + str(s.peepListRef[0].currentFatigue.data.value))
        s.MainPeep_nSocial_Label.configure(text="Social: " + str(s.peepListRef[0].currentSocial.data.value))
        s.MainPeep_nHygiene_Label.configure(text="Hygiene: " + str(s.peepListRef[0].currentHygiene.data.value))
        s.MainPeep_nBladder_Label.configure(text="Bladder: " + str(s.peepListRef[0].currentBladderLiquid.data.value))
        s.MainPeep_nSolids_Label.configure(text="Solids: " + str(s.peepListRef[0].currentBladderSolid.data.value))
        s.MainPeep_nFun_Label.configure(text="Fun: " + str(s.peepListRef[0].currentFun.data.value))
        s.MainPeep_nFulfillment_Label.configure(text="Fulfillment: " + str(s.peepListRef[0].currentFulfillment.data.value))
        
        # Need Progress Bars
        s.MP_nHunger_PBar['value'] = (70000 - s.peepListRef[0].currentHunger.data.value) / 700.0
        s.MP_nThirst_PBar['value'] = (70000 - s.peepListRef[0].currentThirst.data.value) / 700.0
        s.MP_nFatigue_PBar['value'] = (70000 - s.peepListRef[0].currentFatigue.data.value) / 700.0
        s.MP_nSocial_PBar['value'] = (70000 - s.peepListRef[0].currentSocial.data.value) / 700.0
        s.MP_nHygiene_PBar['value'] = (70000 - s.peepListRef[0].currentHygiene.data.value) / 700.0
        s.MP_nBladder_PBar['value'] = (70000 - s.peepListRef[0].currentBladderLiquid.data.value) / 700.0
        s.MP_nSolids_PBar['value'] = (70000 - s.peepListRef[0].currentBladderSolid.data.value) / 700.0
        s.MP_nFun_PBar['value'] = (70000 - s.peepListRef[0].currentFun.data.value) / 700.0
        s.MP_nFulfillment_PBar['value'] = (70000 - s.peepListRef[0].currentFulfillment.data.value) / 700.0

        # Traits
        for i in range(1, St.TraitNo + 1):
            if s.peepListRef[0].traits[i] == 1:
                s.MainPeep_Traits_Labels[i].configure(text=St.traits.inverse[i])
            else:
                s.MainPeep_Traits_Labels[i].configure(text="")
        # Skills
        for i in range(1, St.SkillNo + 1):
            text = St.skills.inverse[i] + "  " + str(s.peepListRef[0].skills[i].lvl)
            s.MainPeep_Skills_Labels[i].configure(text=text)
        # Knowledge
        for i in range(1, St.KnowledgeNo + 1):
            text = St.knowledges.inverse[i] + "  " + str(s.peepListRef[0].knowledge[i].lvl)
            s.MainPeep_Knowledge_Labels[i].configure(text=text)
        # Interest
        for i in range(1, St.InterestNo + 1):
            text = St.interests.inverse[i] + "  " + str(s.peepListRef[0].interest[i].lvl)
            s.MainPeep_Interests_Labels[i].configure(text=text)

        # Other Char Frames
        
        for i in range(1,  len(s.peepListRef)):
            
            s.PeepWindows[i].configure(text=s.peepListRef[i].name)

            '''
            s.PeepWindowsLabels[i][0].configure(text=s.peepListRef[i].currentHunger.data.value)
            s.PeepWindowsLabels[i][1].configure(text=s.peepListRef[i].currentThirst.data.value)
            s.PeepWindowsLabels[i][2].configure(text=s.peepListRef[i].currentFatigue.data.value)
            s.PeepWindowsLabels[i][3].configure(text=s.peepListRef[i].currentSocial.data.value)
            s.PeepWindowsLabels[i][4].configure(text=s.peepListRef[i].currentHygiene.data.value)
            s.PeepWindowsLabels[i][5].configure(text=s.peepListRef[i].currentBladderLiquid.data.value)
            s.PeepWindowsLabels[i][6].configure(text=s.peepListRef[i].currentBladderSolid.data.value)
            s.PeepWindowsLabels[i][7].configure(text=s.peepListRef[i].currentFun.data.value)
            s.PeepWindowsLabels[i][8].configure(text=s.peepListRef[i].currentFulfillment.data.value)
            s.PeepWindowsLabels[i][9].configure(text=s.peepListRef[i].currentAction.data.name)
            '''
            
            s.PeepWindowsProgressBars[i][0]['value'] = (70000 - s.peepListRef[i].currentHunger.data.value) / 700.0
            s.PeepWindowsProgressBars[i][1]['value'] = (70000 - s.peepListRef[i].currentThirst.data.value) / 700.0
            s.PeepWindowsProgressBars[i][2]['value'] = (70000 - s.peepListRef[i].currentFatigue.data.value) / 700.0
            s.PeepWindowsProgressBars[i][3]['value'] = (70000 - s.peepListRef[i].currentSocial.data.value) / 700.0
            s.PeepWindowsProgressBars[i][4]['value'] = (70000 - s.peepListRef[i].currentHygiene.data.value) / 700.0
            s.PeepWindowsProgressBars[i][5]['value'] = (70000 - s.peepListRef[i].currentBladderLiquid.data.value) / 700.0
            s.PeepWindowsProgressBars[i][6]['value'] = (70000 - s.peepListRef[i].currentBladderSolid.data.value) / 700.0
            s.PeepWindowsProgressBars[i][7]['value'] = (70000 - s.peepListRef[i].currentFun.data.value) / 700.0
            s.PeepWindowsProgressBars[i][8]['value'] = (70000 - s.peepListRef[i].currentFulfillment.data.value) / 700.0

            s.PeepWindowsLabels[i][0].configure(text=s.peepListRef[i].currentAction.data.name)


    # Peep Editing
    
    def editPeeps(s):
        '''
            Opens up the peep editor window.
        '''
        s.BB.isPlaying = False
        peepCreatorUI.peepCreatorUI(s.peepListRef, s.BB)

    def swapPeeps(s, peepNo):
        '''
            Swaps which peep is shown in full. 
        '''

        peep = s.peepListRef[peepNo]
        s.peepListRef[peepNo] = s.peepListRef[0]
        s.peepListRef[0] = peep
        s.redraw()

    # Play & Speed

    def tick(s):
        s.BB.tick()
        s.redraw()
        
    def playLoop(s):
        if s.BB.isPlaying:
            s.tick()
            s.root.after(int(1000 / s.speed), s.playLoop)

    def play(s, speed:int):
        s.speed=speed
        if not s.BB.isPlaying:
            s.BB.isPlaying = True
            s.playLoop()
        
    def setSpeed(s, speed:int):
        s.speed = speed

    def pause(s):
        s.BB.isPlaying = False