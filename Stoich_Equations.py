import Periodic_Table as PT

AvoNum = 6.022e23


def compound_calc_one(CompoundOne, CompoundOneCo, CompoundMass, Subscript, Index):  # Given Mass of Compound Calc its Molar Mass and find # of Mols
    MolarMass = []
    i = 0
    for x in range(len(CompoundOne)):
        if (x == len(CompoundOne)-1) & (len(Index) > 1):
            CompoundElementSub = float(Subscript[-1])
        elif len(Index)>0:
            if Index[i] == (x+1):
                CompoundElementSub = float(Subscript[i])
                if len(Index) > 1:
                    i += 1
                else:
                    None
            else:
                CompoundElementSub = 1.0
        else:
            CompoundElementSub = 1.0
        CompoundElement = CompoundOne[x]
        MolarMass.append(CompoundElementSub * PT.Element.MolarMass(PT.Element(CompoundElement)))
        # print(CompoundElement)
        # print(CompoundElementSub)
        # print(MolarMass)

    CompoundOneMolarMass = sum(MolarMass) * CompoundOneCo
    CompoundOneMol = CompoundMass / CompoundOneMolarMass
    return CompoundOneMol


# def compound_calc_two(CompoundOne, CompoundElements, Compound1Co, Compound1Liters):
#     Cycle = 0
#     while Cycle < CompoundElements:
#         if Cycle == 0:
#             CompoundElement1 = input("What is the first Element in " + CompoundOne + "?\n")
#             CompoundElement1Sub = float(input("What is the subscript on " + CompoundElement1 + "?"))
#             CompoundElement1MolarMass = Element.MolarMass(Element(CompoundElement1))
#             Cycle = 1
#         if Cycle == 1:
#             CompoundElement2 = input("What is the second Element in " + CompoundOne + "?\n")
#             CompoundElement2Sub = float(input("What is the subscript on " + CompoundElement2 + "?"))
#             CompoundElement2MolarMass = Element.MolarMass(Element(CompoundElement2))
#             CompoundMolarMass = ((CompoundElement1MolarMass * CompoundElement1Sub) + (
#                         CompoundElement2MolarMass * CompoundElement2Sub))
#             CompoundMol = Compound1Liters / 22.4
#             Cycle = 2
#         '''
#         print("Element One Name: "+CompoundElement1)## print Element 1 Name
#         print("Element One Mol: "+str(CompoundElement1Mol))## print Element 1 Mol
#         print("Element Two Name: "+CompoundElement2)## print Element 2 Name
#         print("Element Two Mol: "+str(CompoundElement2Mol))## print Element 2 Mol
#         print("Compound One Name: "+CompoundOne)## Compound 1 Name
#         print("Compound One Molar Mass: "+str(CompoundMolarMass))## print Compound Molar Mass
#         print("Compound One Mol: "+str(CompoundMol))## print Compound Mols
#         '''
#         return CompoundMolarMass
#
#
# def compound_calc_three(CompoundOne, CompoundElements, Compound1Co, Compound1Liters):
#     Cycle = 0
#     while Cycle < CompoundElements:
#         if Cycle == 0:
#             CompoundElement1 = input("What is the first Element in " + CompoundOne + "?\n")
#             CompoundElement1Sub = float(input("What is the subscript on " + CompoundElement1 + "?"))
#             CompoundElement1MolarMass = Element.MolarMass(Element(CompoundElement1))
#             Cycle = 1
#         if Cycle == 1:
#             CompoundElement2 = input("What is the second Element in " + CompoundOne + "?\n")
#             CompoundElement2Sub = float(input("What is the subscript on " + CompoundElement2 + "?"))
#             CompoundElement2MolarMass = Element.MolarMass(Element(CompoundElement2))
#             CompoundMolarMass = ((CompoundElement1MolarMass * CompoundElement1Sub) + (
#                         CompoundElement2MolarMass * CompoundElement2Sub))
#             CompoundMol = Compound1Liters / 22.4
#             Cycle = 2
#         '''
#         print("Element One Name: "+CompoundElement1)## print Element 1 Name
#         print("Element One Mol: "+str(CompoundElement1Mol))## print Element 1 Mol
#         print("Element Two Name: "+CompoundElement2)## print Element 2 Name
#         print("Element Two Mol: "+str(CompoundElement2Mol))## print Element 2 Mol
#         print("Compound One Name: "+CompoundOne)## Compound 1 Name
#         print("Compound One Molar Mass: "+str(CompoundMolarMass))## print Compound Molar Mass
#         print("Compound One Mol: "+str(CompoundMol))## print Compound Mols
#         '''
#         return CompoundMol
#
#
def compound_calc_four(CompoundOne, CompoundOneCo, Subscript, Index):  # Returns the Molar Mass of Compounds
    MolarMass = []
    i = 0
    for x in range(len(CompoundOne)):
        if (x == len(CompoundOne)-1) & (len(Index) > 1):
            CompoundElementSub = float(Subscript[-1])
        elif len(Index)>0:
            if Index[i] == (x+1):
                CompoundElementSub = float(Subscript[i])
                if len(Index) > 1:
                    i += 1
                else:
                    None
            else:
                CompoundElementSub = 1.0
        else:
            CompoundElementSub = 1.0
        CompoundElement = CompoundOne[x]
        MolarMass.append(CompoundElementSub * PT.Element.MolarMass(PT.Element(CompoundElement)))
        # print(CompoundElement)
        # print(CompoundElementSub)
        # print(MolarMass)

    CompoundOneMolarMass = sum(MolarMass) * float(CompoundOneCo[0])
    # print(CompoundOneMolarMass)
    return CompoundOneMolarMass


def Stoich(Con, TypeCon, Substance, SubstanceGrams, Coefficient, Subscript, Index, Substance2, Coefficient2, Subscript2, Index2):
    if Con == "Starting Mass":
        if TypeCon == 1:  # Convert Single Element Mass to its Volume
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = (SubstanceGrams * Coefficient[0]) / (ElementOneMolarMass * float(Subscript[0]))
            Answer = ElementOneMol * 22.4
            return[Answer, 2]

        if TypeCon == 2:  # Convert Single Compounds Mass to its Volume
            CompoundOneCo = Coefficient[0]
            CompoundMol = float(compound_calc_one(Substance, CompoundOneCo, SubstanceGrams, Subscript, Index))
            Answer = CompoundMol * 22.4
            return[Answer, 2]

        if TypeCon == 3:  # Converts Element 1s Mass to Element 2s Volume
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = SubstanceGrams / (ElementOneMolarMass * Subscript[0])
            ElementTwoMol = (ElementOneMol * Coefficient2[0]) / (Coefficient[0] * Coefficient2[0])
            Answer = ElementTwoMol * 22.4
            return[Answer, 2]

        if TypeCon == 4:  # Converts Element 1s Mass to Compound 1s Volume
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = SubstanceGrams / (ElementOneMolarMass * float(Subscript[0]))
            CompoundOneMol = (ElementOneMol) / (Coefficient[0])
            Answer = CompoundOneMol * 22.4
            return[Answer, 2]

        if TypeCon == 5:  # Converts Compound 1s Mass to Compound 2s Volume
            CompoundOneCo = Coefficient[0]
            CompoundOneMol = float(compound_calc_one(Substance, CompoundOneCo, SubstanceGrams, Subscript, Index))
            CompoundTwoCo = Coefficient2[0]
            Answer = (CompoundTwoCo * CompoundOneMol * 22.4)
            return[Answer, 2]

        if TypeCon == 6:  # Converts Compound 1s Mass to Element 1s Volume
            CompoundOneCo = Coefficient[0]
            CompoundOneMol = float(compound_calc_one(Substance, CompoundOneCo, SubstanceGrams, Subscript, Index))
            Answer = (Coefficient2 * CompoundOneMol * 22.4)
            return[Answer, 2]

        if TypeCon == 7:  # Converts Element 1 Mass to Element 2 Mass
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = SubstanceGrams / (ElementOneMolarMass * Subscript[0])
            ElementTwoMolarMass = PT.Element.MolarMass(PT.Element(Substance2[0]))
            Answer = (ElementOneMol * ElementTwoMolarMass) / (float(Coefficient2[0]) * float(Subscript2[0]))
            return[Answer, 1]

        if TypeCon == 8:  # Converts Element 1 Mass to Compound 2 Mass
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = SubstanceGrams / (ElementOneMolarMass * float(Subscript[0]))
            CompoundOneMolarMass = float(compound_calc_four(Substance2, Coefficient2, Subscript2, Index2))
            Answer = (ElementOneMol * CompoundOneMolarMass) / (float(Coefficient2[0]))
            return[Answer, 1]

        if TypeCon == 9:  # Converts Compound 1 Mass to Element 2 Mass
            CompoundOneCo = Coefficient[0]
            CompoundOneMol = float(compound_calc_one(Substance, CompoundOneCo, SubstanceGrams, Subscript, Index))
            ElementTwoMolarMass = PT.Element.MolarMass(PT.Element(Substance2[0]))
            Answer = (CompoundOneMol * ElementTwoMolarMass * float(Subscript2[0])) / (float(Coefficient2[0]))
            return[Answer, 1]

        if TypeCon == 10:  # Converts Compound 1 Mass to Compound 2 Mass
            CompoundOneCo = Coefficient[0]
            CompoundOneMol = float(compound_calc_one(Substance, CompoundOneCo, SubstanceGrams, Subscript, Index))
            CompoundTwoMolarMass = float(compound_calc_four(Substance2, Coefficient2, Subscript2, Index2))
            Answer = (CompoundOneMol * CompoundTwoMolarMass) / (Coefficient2[0])
            return[Answer, 1]

        if TypeCon == 11:  # Converts Element 1 Mass to its Particle Count
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = SubstanceGrams / (ElementOneMolarMass * float(Subscript[0]))
            Answer = ElementOneMol * AvoNum
            return[Answer, 3]

        if TypeCon == 12:  # Converts Compound 1 to its Particle Count
            CompoundOneCo = Coefficient[0]
            CompoundMol = float(compound_calc_one(Substance, CompoundOneCo, SubstanceGrams, Subscript, Index))
            Answer = CompoundMol * AvoNum
            return[Answer, 3]

        if TypeCon == 13:  # Converts Element 1s Mass to Element 2s Particle Count
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(Substance[0]))
            ElementOneMol = SubstanceGrams / (ElementOneMolarMass * float(Subscript[0]))
            Answer = (ElementOneMol * AvoNum) / (float(Subscript2[0]) * float(Coefficient2[0]))
            return[Answer, 3]

        if TypeCon == 14:  # Converts Element 1s Mass to Compound 1s Particle Count
            ElementOne = input("Element Name? ")
            ElementOneMolarMass = PT.Element.MolarMass(PT.Element(ElementOne))
            ElementOneGrams = float(input("How many grams of " + ElementOne + " do you have? "))
            SubscriptOne = int(input("Subscript On " + ElementOne + "? "))
            ElementOneMol = ElementOneGrams / (ElementOneMolarMass * SubscriptOne)
            CompoundTwo = input("Compound Two name? ")
            CompoundTwoCo = float(input("What is the coefficient on " + CompoundTwo + "? "))
            Answer = (ElementOneMol * AvoNum) / (CompoundTwoCo)
            output(Answer, 3, CompountTwo)

        if TypeCon == 15:  # Converts Compound 1s Mass to Element 2s Particle Count
            CompoundOne = input("Compound One Name? ")
            CompoundElements = int(input("How many elements in " + CompoundOne + "? "))
            CompoundOneCo = float(input("What is the coefficient on " + CompoundOne + "? "))
            CompoundOneMol = float(compound_calc_one(CompoundOne, CompoundElements, CompoundOneCo))
            ElementTwo = input("Element two name? ")
            SubscriptTwo = int(input("Subscript on " + ElementTwo + "? "))
            ElementTwoCo = int(input("Coefficient on " + ElementTwo + "? "))
            Answer = (CompoundOneMol) / (SubscriptTwo * ElementTwoCo)
            output(Answer, 3, ElementTwo)

        if TypeCon == 16:  # Converts Compound 1s Mass to Compound 2s Particle Count
            CompoundOne = input("Compound One Name? ")
            CompoundElements = int(input("How many elements in " + CompoundOne + "? "))
            CompoundOneCo = float(input("What is the coefficient on " + CompoundOne + "? "))
            CompoundOneMol = float(compound_calc_one(CompoundOne, CompoundElements, CompoundOneCo))
            CompoundTwo = input("Compound Two name? ")
            CompoundTwoCo = float(input("What is the coefficient on " + CompoundTwo + "? "))
            Answer = (CompoundOneMol) / (CompoundTwoCo)
            output(Answer, 3, ElementTwo)
