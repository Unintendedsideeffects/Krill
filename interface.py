import inquirer
import main
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    clear()
    mainMenuChoices = ['All lights', 'Rooms', 'Groups', 'Sensors', 'Bridge', 'Quit']
    questions = [
        inquirer.List('Main menu',
                    choices=mainMenuChoices),
    ]
    answer = inquirer.prompt(questions)

    if(answer['Main menu'] == 'All lights'):
        allLightsMenu()
    elif(answer['Main menu'] == 'Rooms'):
        NotImplemented
    elif(answer['Main menu'] == 'Groups'):
        NotImplemented
    elif(answer['Main menu'] == 'Sensors'):
        NotImplemented
    elif(answer['Main menu'] == 'Bridge'):
        NotImplemented
    elif(answer['Main menu'] == 'Quit'):
        exit()

def allLightsMenu():
    clear()
    questions = [
        inquirer.List('AllLightsMenu', choices=['All At Once', 'Pick Lights', 'Go back to Main menu']),
    ]
    answer = inquirer.prompt(questions)

    if(answer['AllLightsMenu'] == 'All At Once'):
        allLightsAtOnceMenu()
    elif(answer['AllLightsMenu'] == 'Pick Lights'):
        pickLightsMenu()
    elif(answer['AllLightsMenu'] == 'Go back to Main'):
        mainMenu()
    elif(answer['AllLightsMenu'] == 'Exit'):
        exit()

def allLightsAtOnceMenu():
    clear()
    questions = [
        inquirer.List('allAtOnce', 
                    choices=['Turn on', 'Turn off', 'Brightness Control', 'Go back']),
    ]
    answer = inquirer.prompt(questions)
    
    if(answer['allAtOnce'] == 'Turn on'):
        main.lightTurnOn(main.getLights())
    elif(answer['allAtOnce'] == 'Turn off'):
        main.lightTurnOff(main.getLights())
    elif(answer['allAtOnce'] == 'Brightness Control'):
       # brightnessControlMenu()
       NotImplemented
    elif(answer['allAtOnce'] == 'Go back'):
        mainMenu()
    elif(answer['allAtOnce'] == 'Exit'):
        exit()
    
def pickLightsMenu():
    clear()
    questions = [
        inquirer.Checkbox('PickLightsMenu',
                        'Select the lights you want to control', choices=main.getAllLightsNames()),
    ]

    answers = inquirer.prompt(questions)

    lightsControl(answers['PickLightsMenu'])    

def lightsControl(chosenLightNames):
    clear()
    possibleChoices = ['Turn on', 'Turn off', 'Brightness Control']
    if(main.areAllColor(chosenLightNames)):
        possibleChoices.append('Color Control')
    possibleChoices.append('Main menu')
    possibleChoices.append('Exit')

    questions = [
        inquirer.List('lightsControl', choices=possibleChoices), 
    ]
    answer = inquirer.prompt(questions)

    if(answer['lightsControl'] == 'Turn on'):
        main.lightTurnOn(main.getLightByName(chosenLightNames))
    elif(answer['lightsControl'] == 'Turn off'):
        main.lightTurnOff(main.getLightByName(chosenLightNames))
    elif(answer['lightsControl'] == 'Brightness Control'):
       # brightnessControlMenu()
        NotImplemented
    elif(answer['lightsControl'] == 'Color Control'):
        #colorControlMenu()
        NotImplemented
    elif(answer['lightsControl'] == 'Main menu'):
        mainMenu()
    elif(answer['lightsControl'] == 'Exit'):
        exit()

def colorControlMenu():
    NotImplemented


mainMenu()

