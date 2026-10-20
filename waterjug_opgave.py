# Opdracht ( zodat ik niet steeds over en weer moet gaan als ik iets opnieuw wil lezen.)
# Je gaat een algoritme implementeren om de 8-5-3 waterpuzzel op te lossen. De puzzel gaat als volgt

# - Je krijgt een beker van exact 8 liter, een andere van 5 liter, en een laatste van 3 liter.
# - Je mag zoveel water bijnemen (van een kraan) en weggooien zoals je wilt
# - Doel van de puzzel is om zowel in de beker van 8 en 5 liter exact 4 liter te krijgen (en 0 in de laatste beker)
# - Voor de rest heb je geen meetinstrumenten. Enkel overgieten, vullen en leegmaken van bekers zijn toegestaan in de puzzel.

# Je mag ervan uit gaan dat je 'perfect' kan overgieten zonder te morsen. Dus als je met de emmer van 8 liter de 5 liter emmer vult, blijft er 3 liter achter.

# Je krijgt startcode die een eerste aanzet geeft. Je taak is om de code te laten werken, eventueel door extra methodes bij te creëren indien nodig. De eindgebruiker wil in de console de tussenstappen zien om tot de oplossing te raken. Hoe je dit precies laat printen kan je zelf kiezen.

# Je bent vrij om te kiezen of je je zoekalgoritme implementeert als aparte klasse, dan wel als methode in de klasse van je probleem/puzzel.

# Indicatieve puntenverdeling

# - Implementatie staat van de puzzel - 10p
# - implementatie zoekstrategie - 10p

class WaterJugState:
    def __init__(self, jug8, jug5, jug3):
        self.jug8 = jug8
        self.jug5 = jug5
        self.jug3 = jug3
        self.parent = None
        self.start = (jug8,jug5,jug3)
        self.cap_jug8 = 8
        self.cap_jug5 = 5
        self.cap_jug3 = 3
        self.goal = (0,4,4)

    def __eq__(self, other):
        #deze krijg je cadeau, zodat python kan checken of twee states hetzelfde zijn
        return self.jug8 == other.jug8 and self.jug5 == other.jug5 and self.jug3 == other.jug3

    def __hash__(self):
        return hash((self.jug8, self.jug5, self.jug3))
    
    def is_valid_state(self):
        pass
    
    def get_next_states(self):
        next_states = []
        
        vul_jug8 = min(self.jug8, 8)
        next_states.append((vul_jug8,self.jug5,self.jug3))

        vul_jug5 = min(self.jug5, 5)
        next_states.append((self.jug8,vul_jug5,self.jug3))

        vul_jug3 = min(self.jug3, 3)
        next_states.append((self.jug8,self.jug5,vul_jug3))

        leeg_jug8 = min(self.jug8, 0)
        next_states.append((leeg_jug8,self.jug5,self.jug3))

        leeg_jug5 = min(self.jug5, 0)
        next_states.append((self.jug8,leeg_jug5,self.jug3))

        leeg_jug3 = min(self.jug3, 0)
        next_states.append((self.jug8,leeg_jug3,self.jug3))

        if (self.jug8 + self.jug5) > self.cap_jug8 :
            self.jug8 = 8
            verschil = min((8 - self.jug8),(self.jug5))
            self.jug5 = verschil
            next_states.append((self.jug8,self.jug5,self.jug3))

        if (self.jug8 + self.jug3) > self.cap_jug8 :
            self.jug8 = 8
            verschil = min((8 - self.jug8),(self.jug3))
            self.jug3 = verschil
            next_states.append((self.jug8,self.jug5,self.jug3))

        if (self.jug5 + self.jug8) > self.cap_jug5 :
            self.jug5 = 5
            verschil = min((5-self.jug5),(self.jug8))
            self.jug8 = verschil
            next_states.append((self.jug8,self.jug5,self.jug3))

        if (self.jug5 + self.jug3) > self.cap_jug5 :
            self.jug5 = 5
            verschil = min((5-self.jug5),(self.jug3))
            self.jug3 = verschil
            next_states.append((self.jug8,self.jug5,self.jug3))

        if (self.jug3 + self.jug8) > self.cap_jug3 :
            self.jug3 = 3
            verschil = min((3-self.jug3),(self.jug8))
            self.jug8 = verschil
            next_states.append((self.jug8,self.jug5,self.jug3))

        if (self.jug3 + self.jug5) > self.cap_jug3 :
            self.jug3 = 3
            verschil = min((3-self.jug3),(self.jug5))
            self.jug5 = verschil
            next_states.append((self.jug8,self.jug5,self.jug3))
        
        return next_states
        
        


        # Mogelijke acties: vul jug8, vul jug5, vul jug3,  leeg jug8, leeg jug5, leeg jug3, elke mogelijk combinatie van giet van pot x naar pot y
        
        # HINT: als je overgiet van de bijvoorbeeld jug5 naar jug8, dan heb je in jug8 (8 - self.jug8) liter plaats, 
        # en in jug5 heb je (self.jug5) liter water zitten. Het kleinste getal van die 2, kan je effectief overgieten zonder morsen.

    def find_solution(waterjug):
        # ik heb gekozen voor een dfs, omdat je niet per se de beste en snelste oplossing wilt, je wilt er gewoon 1
        stack = [waterjug.start]
        parent = {waterjug.start: None}
        visited = {waterjug.start}
        
        while stack:
                current = stack.pop()
                if current == waterjug.goal:
                    pad = []
                    stap = current
                    while stap is not None:
                        pad.append(stap)
                        stap = parent[stap]
                    pad.reverse()
                    return (pad, len(pad) - 1)
                for buur in waterjug.get_next_states():
                    if buur not in visited:
                        visited.add(buur)
                        parent[buur] = current
                        stack.append(buur)
        return (None, 0)


if __name__ == '__main__':
    initial_state = WaterJugState(8, 5, 0)
    solution = initial_state.find_solution()

    if solution:
        print("Oplossing gevonden:")
        # print opeenvolgende stappen van de oplossing
        # had het gewerkt had normaal gezien ook het pad moeten geprint worden.
        print(solution)
    else:
        print("Geen oplossing gevonden.")
#het werkt niet maar mijn idee was: min() pakt het kleinste aantal tussen de 2 argumenten voorbeeld: als je hem wilt vullen dan
# doe je min(jug en max) en dan zelf als de max hoger is dan de cap wordt die vanzelf de max.
# heb ook een cap toegevoegd zodat het iets flexibeler is en ben je niet harcoded met 8-5-3
# mijn idee was om dan alle mogelijke overgieten,legen en vullen af te gaan tot je uitkomt op 0,4,4
# dit is niet helemaal gelukt omdat de logica van de waterpuzzel niet erg lukt voor mij, ik kan me geen manier bedenken om alle 
# mogelijke opties te doen zonder het te hardcoden en dan duurt het langer dan 60-75 minuten.
# ik moet ook eerlijk toegeven dat ik niet honderd percent snap hoe de waterflessen werken. Kan je er van 2 tegelijk in 1 andere ingieten? of moet dit
# telkens 1 per 1.
