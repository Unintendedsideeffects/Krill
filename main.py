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

def getRoomNames():
    rooms = scanForRooms()
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
        bridge.get_group(target, 'lights')

def getGroups():
    return bridge.get_group()

def getGroupsNames():
    groups = bridge.get_group()
    groupNames = []
    for key, val in groups.items():
        groupNames.append(val['name'])
    return groupNames

def getRoombyName(name, rooms = None):
    
    if rooms != None:
        NotImplemented
    else:
        rooms=scanForRooms()
        for room in rooms:
            if (room['name'] == name):
                return room
        
    

# Main
bridge = discovery()

# pprint.pprint(scanForRooms())



