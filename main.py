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

def stripIP(ipToStrip):
    ipToStrip = ipToStrip.replace(':80', '')
    ipToStrip = ipToStrip.replace('http://', '')
    ipToStrip = ipToStrip.replace('/', '')
    return ipToStrip

def connectToBridge(bridgeIP):
    bridge = phue.Bridge(bridgeIP)
    # TODO ask the user to press the button on the bridge, show a timer
    # this next line has to be run only once.
    # bridge.connect()
    return bridge

def scanForRooms():
    #Rooms are very limited, groups are more flexible, rooms are a subset of groups.
    groups = bridge.get_group()
    rooms = []
    for key, val in groups.items():
        if val['type'] == 'Room':
            rooms.append(val)
    return rooms

def getRoomNames(target = None):
    if target == None:
        rooms = scanForRooms()
    else:
        rooms = target
    roomNames = []
    for room in rooms:
        roomNames.append(room['name'])
    return roomNames

def scanForEnterntainmentRooms(bridge):
    groups = bridge.get_group()
    eRooms = []
    for key, val in groups.items():
        if val['type'] == 'Entertainment':
            eRooms.append(val)
    return eRooms

def createNewGroup(name, lights):
    return bridge.create_group(name, lights)

def getLights(target = None):
    if target == None:
        return bridge.lights
    else:
        target = target['name']
        id = int(bridge.get_group_id_by_name(target))
        return bridge.get_group(id, 'lights')

def getGroupLights(groups):

    groupLights = []
    for group in groups:
        groupLights.append(bridge.get_group(int(bridge.get_group_id_by_name(group)), 'lights'))
    return groupLights

def getGroups():
    return bridge.get_group()

def getGroupsNames():
    groups = bridge.get_group()
    groupNames = []
    for key, val in groups.items():
        groupNames.append(val['name'])
    return groupNames

def getRoombyName(name, target = None):
    
    if target == None:
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

def areAllColor(lights):
    #all of them should have the 'hue' parameter
    # lightObjects = []
    for light in lights:
        check = bridge.get_light(light)
        if ('hue' not in check['state'].keys()):
            return False
    
    return True

def lightTurnOn(lights):
    for light in lights:
        bridge.set_light(light, 'on', True)
        
def lightTurnOff(lights):
    for light in lights:
        bridge.set_light(light, 'on', False)

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

def getAllLightsNames():
    lightNames = []
    lights = bridge.lights
    for light in lights:
        lightNames.append(light.name)
    return lightNames

# Main
bridge = discovery()
# pprint.pprint(bridge.get_light('Storage light 1'))
# pprint.pprint(bridge.get_light('Office desk'))


# print(getGroupsNames())
# getLights('Office')
# pprint.pprint(scanForRooms())
