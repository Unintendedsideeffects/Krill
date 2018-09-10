import phue
import discoverhue
from phue import Group
import pprint


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
    #bridge.connect()
    return bridge

def scanForRooms(bridge):
    groups = bridge.get_group()
    rooms = []
    for key, val in groups.items():
        if val['type'] == 'Room':
            rooms.append(val)
    return rooms


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



    
#addLightToGroup()
# set up room control
# def createNewRoom()
# def createNewGroup()
# def listLights(Target room or group)
# def getGroups()


# Main
bridge = discovery()
