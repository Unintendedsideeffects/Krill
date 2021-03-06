import phue
import discoverhue
# import pyconfigstore
from phue import Group
import pprint #will be removed


def discovery():
    found = discoverhue.find_bridges()
    #numberOfBridges = len(found)
    # if numberOfBridges > 1:
        # TODO if the number of bridges is more than one make them pick one
    bridgeID=next(iter(found.keys()))
    bridgeIP=found[bridgeID]
    bridgeIP=stripIP(bridgeIP)
    # print('your bridge ID is {} and the IP adress on your network is {}'.format(bridgeID, bridgeIP))
    return connectToBridge(bridgeIP)

def stripIP(ipToStrip): #final
    ipToStrip = ipToStrip.replace(':80', '')
    ipToStrip = ipToStrip.replace('http://', '')
    ipToStrip = ipToStrip.replace('/', '')
    return ipToStrip

def connectToBridge(bridgeIP):
    bridge = phue.Bridge(bridgeIP)
    # TODO ask the user to press the button on the bridge, show a timer in the UI
    # this next line has to be run only once.
    bridge.connect()
    return bridge

def scanForRooms():
    #Scans for groups, filters to just rooms, returns a list of rooms(objects)
    #Rooms are very limited, groups are more flexible, rooms are a subset of groups.
    groups = bridge.get_group()
    rooms = []
    for key, val in groups.items():
        if val['type'] == 'Room':
            rooms.append(val)
    return rooms

def getRoomNames(target = None):
    #With no target takes all the rooms, with target(a custom group or a subset of rooms) returns a list with the names
    #@Requires type(target) == dict
    if target == None:
        rooms = scanForRooms()
    else:
        rooms = target

    roomNames = []
    for room in rooms:
        roomNames.append(room['name'])
    return roomNames

def scanForEntertainmentRooms():
    #Scans for groups, filters to just Entertainment Rooms, returns a list of Entertainment rooms(objects)
    groups = bridge.get_group()
    eRooms = []
    for key, val in groups.items():
        if val['type'] == 'Entertainment':
            eRooms.append(val)
    return eRooms

def createNewGroup(name, lights):
    return bridge.create_group(name, lights)

def getLights(target = None):
    #returns all lights as objects if no target is specified, other behavior to test and document #TODO target given
    if target == None:
        return bridge.lights
    else:
        if type(target) == dict:
            target = target['name']
            id = int(bridge.get_group_id_by_name(target))
            return bridge.get_group(id, 'lights')

def getGroupLights(groups):
    #Get all the lights in a group
    groupLights = []
    for group in groups:
        groupLights.append(bridge.get_group(int(bridge.get_group_id_by_name(group)), 'lights'))
    return groupLights

def getGroups():
    #Get all the groups on the bridge as objects
    return bridge.get_group()

def getGroupsNames():
    #Get all the groups on the bridge as a list of names
    groups = bridge.get_group()
    groupNames = []
    for key, val in groups.items():
        groupNames.append(val['name'])
    return groupNames

def getRoombyName(name, target = None):
    #Get room object by name 
    if(target == None):
        rooms=scanForRooms()
    else:
        rooms = target
    for room in rooms:
        if (room['name'] == name):
            return room

def getGroupsByName(groupNames):
    groups = []
    for groupName in groupNames:
        groups.append(bridge.get_group_id_by_name(groupName))
    return groups


def filterRooms(state):
    filteredRooms = []
    rooms = scanForRooms()
    for room in rooms:
        roomState = room['state']
        if roomState[state] == True:
            filteredRooms.append(room)
    
    return filteredRooms

def groupLights(target):
    allLightsNames = []
    lights = getLights(target)
    for light in lights:
        allLightsNames.append((bridge.get_light(int(light), 'name')))
    return allLightsNames

def areAllColor(lightNames):
    #all of them should have the 'hue' parameter
    # lightObjects = []
    for light in lightNames:
        check = bridge.get_light(light)
        if ('hue' not in check['state'].keys()):
            return False
    
    return True

def lightTurnOn(lights):
        for light in lights:
            if type(light) == dict:
                bridge.set_light(light['name'], 'on', True)
            elif type(light) == list:
                bridge.set_light(light.name, 'on', True)     

def lightTurnOff(lights):
    for light in lights:
            if type(light) == dict:
                bridge.set_light(light['name'], 'on', False)
            elif type(light) == list:
                bridge.set_light(light.name, 'on', False)

def setLightBrightness(lights, brightness):
    for light in lights:
        bridge.set_light(light, 'bri', brightness)

def getLightBrightness(lights):
    for light in lights:
        tmp = bridge.get_light(light)
        if(tmp['state']['on'] != False):
            return(tmp['state']['bri'])
        else:
            return('Off')

def brightnessToPercentage(brightness):
    return format((float(brightness)/254.0)*100, '.2f')

def getLightsNames(lights = None):
    lightNames = []
    if lights == None:
        lights = bridge.lights

    for light in lights:
        lightNames.append(light.name)
    return lightNames

def getLightByName(chosenLightsNames):
    lights = []

    for lightName in chosenLightsNames:
        lights.append(bridge.get_light(lightName))
    return lights


def setColorToLight(lights, color):
    lightNames = getLightsNames(lights)
    command = {'hue': huevalue, 'sat':satvalue}
    if areAllColor(lightNames): #We should just deal with the light objects not the names
        bridge.set_light(lightNames, 'on', True)

            
            
     

# Main
bridge = discovery()

# print(getLights())
