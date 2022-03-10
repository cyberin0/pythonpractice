import time
import sys

CalcTemps=[]
class ComplicateThings():
    def __init__(self, decay_rate, exposure_rate):
        self.dr=decay_rate
        self.er=exposure_rate
        LessCalculation = self.er-self.dr
        self.LessCalculation=self.er-self.dr
        self.LessCalcTwo=self.dr + LessCalculation
        GreatCalculation=self.dr-self.er
        self.GreatCalculation=self.dr-self.er
        self.GreatCalcTwo=self.er+GreatCalculation
    def Half_Life(self):
        if self.dr == self.er:
            time.sleep(1.3)
            print('Current decay rate:', self.dr, end='')
            print('\nand current exposure rate:', self.er)
            print('Please prepare the terminal for calculations.')
            time.sleep(1.7)
            print('\n')
            print('Holy fuck, they\'re even!')
            time.sleep(.7)
            print('Nothing to do here!')
        if self.dr > self.er:
            time.sleep(1.3)
            print('Current decay rate:', self.dr, end='')
            print('\nand current exposure rate:', self.er)
            print('(self.dr > self.er)')
            print('\n')
            time.sleep(2)
            print('Please prepare the terminal for calculations.')
            time.sleep(1.2)
            print('\n')
            print('I think I\'m onto something.', end='')
            sys.stdout.flush()
            time.sleep(1.9)
            print('\nLemme try something. Starting the task now.')
            time.sleep(.7)
            print('\nLoading... Please stand by...')
            print('-----')
            time.sleep(1.8)
            for i in range(0,11):
                time.sleep(0.17)
                sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(26-i)))
                sys.stdout.flush()
            sys.stdout.write('\n')
            time.sleep(2.7)
            print('Calculations complete.', end='')
            print('\n((self.dr - self.er) + self.er)')
            time.sleep(.3)
            print(self.GreatCalcTwo)
            time.sleep(.9)
            print('Oh shit! I think I got it fixed...', end='')
            sys.stdout.flush()
            time.sleep(.8)
            print('\nCome look!')
        if self.dr < self.er:
            time.sleep(1.3)
            print('Current decay rate:', self.dr, end='')
            print('\nand current exposure rate:', self.er)
            print('(self.dr < self.er)')
            print('\n')
            time.sleep(2)
            print('Please prepare the terminal for calculations.')
            time.sleep(1.7)
            print('\nAh shit, the exposure rate is higher than the decay, I\'ll have to try something different.', end='')
            sys.stdout.flush()
            time.sleep(2.7)
            print('\nOkay, I\'ve got an idea.')
            time.sleep(3)
            print('\nStarting the task now, should only take a few seconds.')
            time.sleep(.8)
            print('\nLoading... Please stand by...')
            print('-----')
            for i in range(0,11):
                time.sleep(0.17)
                sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(26-i)))
                sys.stdout.flush()
            sys.stdout.write('\n')
            time.sleep(2.7)
            print('Calculations complete.', end='')
            print('\n((self.er - self.dr) + self.dr)')
            time.sleep(.7)
            print(self.LessCalcTwo)
            time.sleep(2)
            print('Huh, did I fix it?')


HyperCore = ComplicateThings(1500, 160)
TritiumGreat = ComplicateThings(5000, 30)
TritiumEven = ComplicateThings(30,30)
TritiumLess = ComplicateThings(29,7000)

#HyperCore.Half_Life()

#ComplicateThings.Half_Life(TritiumGreat)
#TritiumGreat.Half_Life()

#ComplicateThings.Half_Life(TritiumEven)
#TritiumEven.Half_Life()

#ComplicateThings.Half_Life(TritiumLess)
#TritiumLess.Half_Life()


BruhMomentFossil = ComplicateThings(20, 10)
BruhMomentFossil.Half_Life()
