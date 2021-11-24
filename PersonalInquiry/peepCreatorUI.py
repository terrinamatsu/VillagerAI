from Peep.peep import Peep
from tkinter import *
import Peep.Standards
from Peep.Levels import Levels
from Peep.Skill import Skill
import Blackboard

St = Peep.Standards.Standards()

class peepCreatorUI(object):
    """description of class"""
    
    def clearPeep(s):
        s.f_name_entry.delete(0, END)
        s.l_name_entry.delete(0, END)
        s.clicked.set("Unemployed")
        s.age_slider.set(20)
        # Clear traits
        for i in range(1, St.TraitNo + 1):
            s.trait_chqs[i].deselect()
        # Clear Skills
        for i in range(1, St.SkillNo + 1):
            s.skill_sliders[i].set(0)
        # Clear Knowledge
        for i in range(1, St.KnowledgeNo + 1):
            s.knowledge_sliders[i].set(0)
        # Clear Interest
        for i in range(1, St.InterestNo + 1):
            s.interest_sliders[i].set(0)

    def getPeep(s, peeper : Peep):
        s.clearPeep()
        s.f_name_entry.insert(0, peeper.name)
        s.l_name_entry.insert(0, peeper.surname)
        s.clicked.set(St.jobs.inv[peeper.job])
        s.age_slider.set(peeper.age)

        # Set Traits
        for i in range(1, St.TraitNo + 1):
            if peeper.traits[i] == 1:
                s.trait_chqs_vars[i].set(1)
                #s.trait_chqs[i].select()
            else:
                s.trait_chqs_vars[i].set(0)
                #s.trait_chqs[i].deselect()
            #s.trait_chqs[i].
        # Set Skills
        for i in range(1, St.SkillNo + 1):
            s.skill_sliders[i].set(peeper.skills[i].lvl)
        # Set Knowledge
        for i in range(1, St.KnowledgeNo + 1):
            s.knowledge_sliders[i].set(peeper.knowledge[i].lvl)
        # Set Interest
        for i in range(1, St.InterestNo + 1):
            s.interest_sliders[i].set(peeper.interest[i].lvl)

    def setPeep(s):
        pName = s.f_name_entry.get()
        pSurname = s.l_name_entry.get()
        pJob = St.jobs[s.clicked.get()]
        pAge = s.age_slider.get()
        # Set Traits
        pTraits = [0]
        for i in range(1, St.TraitNo + 1):
            pTraits.append(s.trait_chqs_vars[i].get())
            print(s.trait_chqs_vars[i].get())
        # Set Skills
        pSkills = [Skill("",0)]
        for skill in range(1, St.SkillNo+1):
            b = Skill(St.skills.inverse[skill], skill, lvl=s.skill_sliders[skill].get())
            pSkills.append(b)
        # Set Knowledge
        pKnowledge = [Levels("",0)]
        for kn in range(1, St.KnowledgeNo+1):
            b = Levels(St.knowledges.inverse[kn], kn, lvl=s.knowledge_sliders[kn].get())
            pKnowledge.append(b)
        # Set Interest
        pInterest = [Levels("",0)]
        for intr in range(1, St.InterestNo+1):
            b = Levels(St.interests.inverse[intr], intr, lvl=s.interest_sliders[intr].get())
            pInterest.append(b)

        print(pTraits)
        peeper = Peep(s.BB, name=pName, surname=pSurname, age=pAge, traits=pTraits, skills=pSkills, knowledges=pKnowledge, interests=pInterest, job=pJob)
        s.clearPeep()

        return peeper

    def overridePeep(s, peepers, peepNo):
        peepers[peepNo] = s.setPeep()

    def saveNewPeep(s):
        return

    def RndFName(s):
        s.f_name_entry.delete(0, END)
        s.f_name_entry.insert(0, St.getRND_FName())

    def RndLName(s):
        s.l_name_entry.delete(0, END)
        s.l_name_entry.insert(0, St.getRND_LName())

    def SelectTrait(s, TraitNo):
        return 

########################################################Constructor
    def __init__(s, peepList, BB : Blackboard.Blackboard):
        s.BB = BB
        no_width=8

        s.root = Tk()
        s.root.title('Create A Peep')
        s.root.geometry("1400x900")

        # DETAILS TAB
        s.f_detail = LabelFrame(s.root, text="Personal Details")
        s.f_detail.grid(row=0, column=0, sticky="W")
        s.f_detail.rowconfigure(0, weight=1)
        s.f_detail.columnconfigure(0, weight=1)

            #First Name Entry
        s.f_name_Label = Label(s.f_detail, text="Name")
        s.f_name_Label.grid(row=0, column=0, sticky="W")
        s.f_name_entry = Entry(s.f_detail, width=30)
        s.f_name_entry.grid(row=1, column=0, padx=5)
        s.f_name_rndbtn = Button(s.f_detail, text="RND", command=s.RndFName)
        s.f_name_rndbtn.grid(row=1, column=1)

            #Surname Entry
        s.l_name_label = Label(s.f_detail, text="Surname")
        s.l_name_label.grid(row=0, column=2, sticky="W")
        s.l_name_entry = Entry(s.f_detail, width=30)
        s.l_name_entry.grid(row=1, column=2, padx=5)
        s.l_name_rndbtn = Button(s.f_detail, text="RND", command=s.RndLName)
        s.l_name_rndbtn.grid(row=1, column=3)

            #Age Entry
        s.age_Label = Label(s.f_detail, text="Age")
        s.age_Label.grid(row=0, column=4, sticky="W")
        s.age_slider = Scale(s.f_detail, from_=0, to=120, orient=HORIZONTAL)
        s.age_slider.grid(row=0, column=5, columnspan=2, padx=5, ipadx=50)
        s.age_slider.set(20)
            
        month_clicked = StringVar(s.root)
        month_clicked.set("January")
        month_options = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
        s.birth_month_entry = OptionMenu(s.f_detail, month_clicked, *month_options)
        s.birth_month_entry.config(width=12)
        s.birth_month_entry.grid(row=1, column=6, sticky="E", ipadx=5)

        day_clicked = StringVar(s.root)
        day_clicked.set("Monday")
        day_options = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
            ]
        s.birth_day_entry = OptionMenu(s.f_detail, day_clicked, *day_options)
        s.birth_day_entry.config(width=12)
        s.birth_day_entry.grid(row=1, column=4, columnspan=2, sticky="E")

            #Job Entry
        s.job_Label = Label(s.f_detail, text="Job")
        s.job_Label.grid(row=0, column=7, sticky="W")


        s.clicked = StringVar(s.root)
        s.clicked.set("Unemployed")
        s.job_entry = OptionMenu(s.f_detail, s.clicked, *St.jobs)
        s.job_entry.grid(row=1, column=7)

        # TRAITS TAB
        s.trait_detail = LabelFrame(s.root, text="Traits")
        s.trait_detail.grid(row=1, column=0, sticky="WE")
        s.trait_detail.rowconfigure(0, weight=1)
        s.trait_detail.columnconfigure(0, weight=1)

        s.trait_chqs = [Checkbutton(s.root)]
        s.trait_chqs_vars = [IntVar(s.root)]
        for i in range(1, St.TraitNo + 1):
            #l = Label(s.trait_detail, text=St.traits.inverse[i])
            #l.grid(row=int((i-1)/5) , column=((i-1)%5))
            s.trait_chqs_vars.append(IntVar(s.root))
            s.trait_chqs.append(Checkbutton(s.trait_detail, text=St.traits.inverse[i], command=lambda: s.SelectTrait(i), variable=s.trait_chqs_vars[i]))
            s.trait_chqs[i].var = s.trait_chqs_vars[i]
            s.trait_chqs[i].grid(row=int((i-1)/no_width) , column=((i-1)%no_width))
            
        # SKILLS TAB
        s.skill_detail = LabelFrame(s.root, text="Skills")
        s.skill_detail.grid(row=4, column=0, sticky="WE")
        s.skill_detail.rowconfigure(0, weight=1)
        s.skill_detail.columnconfigure(0, weight=1)

        s.skill_labels = [Label(s.root)]
        s.skill_sliders = [Scale(s.root)]

        for i in range(1, St.SkillNo + 1):
            s.skill_labels.append(Label(s.skill_detail, text=St.skills.inverse[i]))
            s.skill_labels[i].grid(row=int((i-1)/no_width)*2 , column=((i-1)%no_width))

            s.skill_sliders.append(Scale(s.skill_detail, from_=0, to=10, orient=HORIZONTAL))
            s.skill_sliders[i].grid(row=int((i-1)/no_width)*2+1 , column=((i-1)%no_width), ipadx=20)

        # KNOWLEDGE TAB
        s.knowledge_detail = LabelFrame(s.root, text="Knowledge")
        s.knowledge_detail.grid(row=5, column=0, sticky="WE")
        s.knowledge_detail.rowconfigure(0, weight=1)
        s.knowledge_detail.columnconfigure(0, weight=1)

        s.knowledge_labels = [Label(s.root)]
        s.knowledge_sliders = [Scale(s.root)]

        for i in range(1, St.KnowledgeNo + 1):
            s.knowledge_labels.append(Label(s.knowledge_detail, text=St.knowledges.inverse[i]))
            s.knowledge_labels[i].grid(row=int((i-1)/no_width)*2 , column=((i-1)%no_width))

            s.knowledge_sliders.append(Scale(s.knowledge_detail, from_=0, to=100, orient=HORIZONTAL))
            s.knowledge_sliders[i].grid(row=int((i-1)/no_width)*2+1 , column=((i-1)%no_width), ipadx=20)


        # INTERESTS TAB
        s.interest_detail = LabelFrame(s.root, text="Interest")
        s.interest_detail.grid(row=6, column=0, sticky="WE")
        s.interest_detail.rowconfigure(0, weight=1)
        s.interest_detail.columnconfigure(0, weight=1)

        s.interest_labels = [Label(s.root)]
        s.interest_sliders = [Scale(s.root)]

        for i in range(1, St.InterestNo + 1):
            s.interest_labels.append(Label(s.interest_detail, text=St.interests.inverse[i]))
            s.interest_labels[i].grid(row=int((i-1)/no_width)*2 , column=((i-1)%no_width))

            s.interest_sliders.append(Scale(s.interest_detail, from_=0, to=100, orient=HORIZONTAL))
            s.interest_sliders[i].grid(row=int((i-1)/no_width)*2+1 , column=((i-1)%no_width), ipadx=20)


        # SAVE TAB
        s.save_detail = LabelFrame(s.root, text="Options")
        s.save_detail.grid(row=0, column=1, sticky="NESW", rowspan=6)
        s.save_detail.rowconfigure(0, weight=1)
        s.save_detail.columnconfigure(0, weight=1)
        
            #Select Peep Dropdown
        peep_clicked = IntVar()
        peepNames = []

        #for peep in peepList:
            #peepNames.append(peep.name + " " + peep.surname)
        for i in range(0, len(peepList)):    
            peepNames.append(i)

        peep_clicked.set(peepNames[0])
        s.peeplist_entry = OptionMenu(s.save_detail, peep_clicked, *peepNames)
        s.peeplist_entry.grid(row=0, column=0, columnspan=2, sticky="WE")

            #Save Peep
        s.savebuttonn_btn = Button(s.save_detail, text="Save Peep", command=lambda : s.overridePeep(peepList, peep_clicked.get()))
        s.savebuttonn_btn.grid(row=1, column=0, sticky="WE")

            #Load Peep
        s.loadbutton_btn = Button(s.save_detail, text="Load Peep", command=lambda: s.getPeep(peepList[peep_clicked.get()]))
        s.loadbutton_btn.grid(row=1, column=1, sticky="WE")

        s.root.mainloop()