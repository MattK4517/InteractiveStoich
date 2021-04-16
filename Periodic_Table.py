class Element():
    def __init__(self, ElementName):
        self.Element = ElementName

    def MolarMass(self):
        ## Given an element name, returns its Molar Mass
        if self.Element == "0":
            ElementMolarMass = 0
        if self.Element == "Hydrogen" or self.Element == "H":
            ElementMolarMass = 1.008
        if self.Element == "Helium" or self.Element == "He":
            ElementMolarMass = 4.003
        if self.Element == "Lithium" or self.Element == "Li":
            ElementMolarMass = 6.94
        if self.Element == "Beryllium" or self.Element == "Be":
            ElementMolarMass = 9.012
        if self.Element == "Boron" or self.Element == "B":
            ElementMolarMass = 10.81
        if self.Element == "Carbon" or self.Element == "C":
            ElementMolarMass = 12.011
        if self.Element == "Nitrogen" or self.Element == "N":
            ElementMolarMass = 14.007
        if self.Element == "Oxygen" or self.Element == "O":
            ElementMolarMass = 15.999
        if self.Element == "Fluorine" or self.Element == "F":
            ElementMolarMass = 18.998
        if self.Element == "Neon" or self.Element == "Ne":
            ElementMolarMass = 20.180
        if self.Element == "Sodium" or self.Element == "Na":
            ElementMolarMass = 22.99
        if self.Element == "Magnesium" or self.Element == "Mg":
            ElementMolarMass = 24.305
        if self.Element == "Aluminum" or self.Element == "Al":
            ElementMolarMass = 26.982
        if self.Element == "Silicon" or self.Element == "Si":
            ElementMolarMass = 28.085
        if self.Element == "Phosphorus" or self.Element == "P":
            ElementMolarMass = 30.974
        if self.Element == "Sulfur" or self.Element == "S":
            ElementMolarMass = 32.06
        if self.Element == "Chlorine" or self.Element == "Cl":
            ElementMolarMass = 35.45
        if self.Element == "Argon" or self.Element == "Ar":
            ElementMolarMass = 39.948
        if self.Element == "Potassium" or self.Element == "K":
            ElementMolarMass = 39.098
        if self.Element == "Calcium" or self.Element == "Ca":
            ElementMolarMass = 40.078
        if self.Element == "Scandium" or self.Element == "Sc":
            ElementMolarMass = 44.956
        if self.Element == "Titanium" or self.Element == "Ti":
            ElementMolarMass = 47.867
        if self.Element == "Vanadium" or self.Element == "V":
            ElementMolarMass = 50.942
        if self.Element == "Chromium" or self.Element == "Cr":
            ElementMolarMass = 51.996
        if self.Element == "Manganese" or self.Element == "Mn":
            ElementMolarMass = 54.938
        if self.Element == "Iron" or self.Element == "Fe":
            ElementMolarMass = 55.845
        if self.Element == "Cobalt" or self.Element == "Co":
            ElementMolarMass = 58.993
        if self.Element == "Nickel" or self.Element == "Ni":
            ElementMolarMass = 58.693
        if self.Element == "Copper" or self.Element == "Cu":
            ElementMolarMass = 63.546
        if self.Element == "Zinc" or self.Element == "Zn":
            ElementMolarMass = 65.38
        if self.Element == "Gallium" or self.Element == "Ga":
            ElementMolarMass = 69.723
        if self.Element == "Germanium" or self.Element == "Ge":
            ElementMolarMass = 72.63
        if self.Element == "Arsenic" or self.Element == "As":
            ElementMolarMass = 74.922
        if self.Element == "Selenium" or self.Element == "Se":
            ElementMolarMass = 78.971
        if self.Element == "Bromine" or self.Element == "Br":
            ElementMolarMass = 79.904
        if self.Element == "Krypton" or self.Element == "Kr":
            ElementMolarMass = 83.79
        if self.Element == "Rubidium" or self.Element == "Rb":
            ElementMolarMass = 85.468
        if self.Element == "Strontium" or self.Element == "Sr":
            ElementMolarMass = 87.62
        if self.Element == "Yttrium" or self.Element == "Y":
            ElementMolarMass = 88.906
        if self.Element == "Zirconium" or self.Element == "Zr":
            ElementMolarMass = 91.224
        if self.Element == "Niobium" or self.Element == "Nb":
            ElementMolarMass = 92.906
        if self.Element == "Molybdenum" or self.Element == "Mo":
            ElementMolarMass = 95.95
        if self.Element == "Technetium" or self.Element == "Tc":
            ElementMolarMass = 98.000
        if self.Element == "Ruthenium" or self.Element == "Ru":
            ElementMolarMass = 101.07
        if self.Element == "Rhodium" or self.Element == "Rh":
            ElementMolarMass = 102.91
        if self.Element == "Palladium" or self.Element == "Pd":
            ElementMolarMass = 106.42
        if self.Element == "Silver" or self.Element == "Ag":
            ElementMolarMass = 107.87
        if self.Element == "Cadmium" or self.Element == "Cd":
            ElementMolarMass = 112.41
        if self.Element == "Indium" or self.Element == "In":
            ElementMolarMass = 114.82
        if self.Element == "Tin" or self.Element == "Sn":
            ElementMolarMass = 118.71
        if self.Element == "Antimony" or self.Element == "Sb":
            ElementMolarMass = 121.76
        if self.Element == "Tellurium" or self.Element == "Te":
            ElementMolarMass = 127.60
        if self.Element == "Iodine" or self.Element == "I":
            ElementMolarMass = 126.90
        if self.Element == "Xenon" or self.Element == "Xe":
            ElementMolarMass = 131.29
        if self.Element == "Caesium" or self.Element == "Cs":
            ElementMolarMass = 132.91
        if self.Element == "Barium" or self.Element == "Ba":
            ElementMolarMass = 137.33
        if self.Element == "Lanthanum" or self.Element == "La":
            ElementMolarMass = 138.91
        if self.Element == "Cerium" or self.Element == "Ce":
            ElementMolarMass = 140.12
        if self.Element == "Praseodymium" or self.Element == "Pr":
            ElementMolarMass = 140.91
        if self.Element == "Neodymium" or self.Element == "Nd":
            ElementMolarMass = 144.24
        if self.Element == "Promethium" or self.Element == "Pm":
            ElementMolarMass = 145.00
        if self.Element == "Samarium" or self.Element == "Sm":
            ElementMolarMass = 150.36
        if self.Element == "Europium" or self.Element == "Eu":
            ElementMolarMass = 151.96
        if self.Element == "Gadolinium" or self.Element == "Gd":
            ElementMolarMass = 157.25
        if self.Element == "Terbium" or self.Element == "Tb":
            ElementMolarMass = 158.93
        if self.Element == "Dysprosium" or self.Element == "Dy":
            ElementMolarMass = 162.50
        if self.Element == "Holmium" or self.Element == "Ho":
            ElementMolarMass = 164.93
        if self.Element == "Erbium" or self.Element == "Er":
            ElementMolarMass = 167.26
        if self.Element == "Thulium" or self.Element == "Tm":
            ElementMolarMass = 168.93
        if self.Element == "Ytterbium" or self.Element == "Yb":
            ElementMolarMass = 173.05
        if self.Element == "Lutetium" or self.Element == "Lu":
            ElementMolarMass = 174.97
        if self.Element == "Hafnium" or self.Element == "Hf":
            ElementMolarMass = 178.49
        if self.Element == "Tantalum" or self.Element == "Ta":
            ElementMolarMass = 180.95
        if self.Element == "Tungsten" or self.Element == "W":
            ElementMolarMass = 183.84
        if self.Element == "Rhenium" or self.Element == "Re":
            ElementMolarMass = 186.21
        if self.Element == "Osmium" or self.Element == "Os":
            ElementMolarMass = 190.23
        if self.Element == "Iridium" or self.Element == "Ir":
            ElementMolarMass = 192.22
        if self.Element == "Platinum" or self.Element == "Pt":
            ElementMolarMass = 195.08
        if self.Element == "Gold" or self.Element == "Au":
            ElementMolarMass = 196.97
        if self.Element == "Mercury" or self.Element == "Hg":
            ElementMolarMass = 200.59
        if self.Element == "Thallium" or self.Element == "Tl":
            ElementMolarMass = 204.38
        if self.Element == "Lead" or self.Element == "Pb":
            ElementMolarMass = 207.2
        if self.Element == "Bismuth" or self.Element == "Bi":
            ElementMolarMass = 208.98
        if self.Element == "Polonium" or self.Element == "Po":
            ElementMolarMass = 209.00
        if self.Element == "Astatine" or self.Element == "At":
            ElementMolarMass = 210.00
        if self.Element == "Radon" or self.Element == "Rn":
            ElementMolarMass = 222.00
        if self.Element == "Francium" or self.Element == "Fr":
            ElementMolarMass = 223.00
        if self.Element == "Radium" or self.Element == "Ra":
            ElementMolarMass = 226.00
        if self.Element == "Actinium" or self.Element == "Ac":
            ElementMolarMass = 227.00
        if self.Element == "Thorium" or self.Element == "Th":
            ElementMolarMass = 232.04
        if self.Element == "Protactinium" or self.Element == "Pa":
            ElementMolarMass = 231.04
        if self.Element == "Uranium" or self.Element == "U":
            ElementMolarMass = 238.03
        if self.Element == "Neptunium" or self.Element == "Np":
            ElementMolarMass = 237.00
        if self.Element == "Plutonium" or self.Element == "Pu":
            ElementMolarMass = 244.00
        if self.Element == "Americium" or self.Element == "Am":
            ElementMolarMass = 243.00
        if self.Element == "Curium" or self.Element == "Cm":
            ElementMolarMass = 247.00
        if self.Element == "Berkelium" or self.Element == "Bk":
            ElementMolarMass = 247.00
        if self.Element == "Californium" or self.Element == "Cf":
            ElementMolarMass = 251.00
        if self.Element == "Einsteinium" or self.Element == "Es":
            ElementMolarMass = 252.00
        if self.Element == "Fermium" or self.Element == "Fm":
            ElementMolarMass = 257.00
        if self.Element == "Mendelevium" or self.Element == "Md":
            ElementMolarMass = 258.00
        if self.Element == "Nobelium" or self.Element == "No":
            ElementMolarMass = 259.00
        if self.Element == "Lawrencium" or self.Element == "Lr":
            ElementMolarMass = 266.00
        if self.Element == "Rutherfordium" or self.Element == "Rf":
            ElementMolarMass = 267.00
        if self.Element == "Dubnium" or self.Element == "Db":
            ElementMolarMass = 268.00
        if self.Element == "Seaborgium" or self.Element == "Sg":
            ElementMolarMass = 269.00
        if self.Element == "Bohrium" or self.Element == "Bh":
            ElementMolarMass = 270.00
        if self.Element == "Hassium" or self.Element == "Hs":
            ElementMolarMass = 270.00
        if self.Element == "Meitnerium" or self.Element == "Mt":
            ElementMolarMass = 278.00
        if self.Element == "Damstadium" or self.Element == "Ds":
            ElementMolarMass = 281.00
        if self.Element == "Roentgenium" or self.Element == "Rg":
            ElementMolarMass = 282.00
        if self.Element == "Copernicium" or self.Element == "Cn":
            ElementMolarMass = 285.00
        if self.Element == "Nihonium" or self.Element == "Nh":
            ElementMolarMass = 286.00
        if self.Element == "Flerovium" or self.Element == "Fl":
            ElementMolarMass = 289.00
        if self.Element == "Moscovium" or self.Element == "Mc":
            ElementMolarMass = 290.00
        if self.Element == "Livermorium" or self.Element == "Lv":
            ElementMolarMass = 293.00
        if self.Element == "Tennessine" or self.Element == "Ts":
            ElementMolarMass = 294.00
        if self.Element == "Oganesson" or self.Element == "Og":
            ElementMolarMass = 294.00
        return ElementMolarMass
