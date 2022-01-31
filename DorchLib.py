# -*- coding: utf-8 -*-

#DorchLibrary
Version = "0.0.2"

from DorchTypes import *

from Assistant import Engine
from ClassicAssist.Data.Macros.Commands.AbilitiesCommands import *
from ClassicAssist.Data.Macros.Commands.ActionCommands import *
from ClassicAssist.Data.Macros.Commands.AgentCommands import *
from ClassicAssist.Data.Macros.Commands.AliasCommands import *
from ClassicAssist.Data.Macros.Commands.ConsumeCommands import *
from ClassicAssist.Data.Macros.Commands.DummyCommands import *
from ClassicAssist.Data.Macros.Commands.EntityCommands import *
from ClassicAssist.Data.Macros.Commands.GumpCommands import *
from ClassicAssist.Data.Macros.Commands.JournalCommands import *
from ClassicAssist.Data.Macros.Commands.ListCommands import *
from ClassicAssist.Data.Macros.Commands.MacroCommands import *
from ClassicAssist.Data.Macros.Commands.MainCommands import *
from ClassicAssist.Data.Macros.Commands.MenuCommands import *
from ClassicAssist.Data.Macros.Commands.MobileCommands import *
from ClassicAssist.Data.Macros.Commands.MovementCommands import *
from ClassicAssist.Data.Macros.Commands.MsgCommands import *
from ClassicAssist.Data.Macros.Commands.NotorietyCommands import *
from ClassicAssist.Data.Macros.Commands.ObjectCommands import *
from ClassicAssist.Data.Macros.Commands.OrganizerCommands import *
from ClassicAssist.Data.Macros.Commands.PropertiesCommands import *
from ClassicAssist.Data.Macros.Commands.RegionCommands import *
from ClassicAssist.Data.Macros.Commands.SkillCommands import *
from ClassicAssist.Data.Macros.Commands.SpellCommands import *
from ClassicAssist.Data.Macros.Commands.TargetCommands import *
from ClassicAssist.Data.Macros.Commands.TimerCommands import *
from ClassicAssist.Data.Macros.Commands.WandCommands import *
from ClassicAssist.UO.Objects import *
from ClassicAssist.UO.Data import Direction
import os
import json
import codecs
import math
from System.Net import WebClient
from distutils.version import LooseVersion
import re
import webbrowser
from datetime import datetime, timedelta
import time
from collections import namedtuple

CONFIG = "Data\Plugins\ClassicAssist\Modules\DorchLib.config"

def GetType(itemTypeName):
	if itemTypeName in Graphics:
		return Graphics[itemTypeName]
	elif itemTypeName in Types:
		return Types[itemTypeName]

	return 0

def GetGraphicsIdWithType(itemTypeName):
	if itemTypeName in Graphics:
		return Graphics[itemTypeName]
	elif itemTypeName in Types:
		type = Types[itemTypeName]
		if isinstance(type.types, str):
			return type.types
		else:
			return type.types[0]

	return 0

def FindTypeBy(itemType, range=None, container=None, minAmount = None, returnAllItems = False):
	if isinstance(itemType, str):
		itemType = GetType(itemType)
		if itemType == 0:
			print("Type " + itemType + " not exists")
			return None

		return FindTypeBy(itemType, range, container, minAmount)

	isObjectType = False
	if isinstance(itemType, ItemTypeClass):
		isObjectType = True


	items = []
	if container is not None:
		if isinstance(container, str):
			container = GetAlias(container)

		if isObjectType:
			items = Engine.Items.SelectEntities(lambda i: itemType.match(i) and i.IsDescendantOf(container, range))
		else:
			items = Engine.Items.SelectEntities(lambda i: i.ID == itemType and i.IsDescendantOf(container, range))
	else:
		if isObjectType:
			items = Engine.Items.SelectEntities(lambda i: itemType.match(i))
		else:
			items = Engine.Items.SelectEntities(lambda i: i.ID == itemType)

	if items is None:
		if isObjectType:
			items = Engine.Mobiles.SelectEntities(lambda m: itemType.match(m))
		else:
			items = Engine.Mobiles.SelectEntities(lambda m: m.ID == itemType)

	if items is None:
		return None

	returnItems = []
	for item in items:
		if range != -1 and range is not None:
			if item.Distance > range:
				continue

		if minAmount != -1 and minAmount is not None:
			if isinstance(item, Item) and item.Count < minAmount:
				continue

		if not InIgnoreList(item.Serial):
			returnItems.append(item)

	if returnItems == []:
		return None

	sortedByDistance = sorted(returnItems, key=lambda i: i.Distance, reverse=False)

	if returnAllItems:
		return sortedByDistance

	found = sortedByDistance[0]
	SetAlias("found", found.Serial)
	return found

#Funkce pro přesun itemu
#args - %1 TYPE Itemu
#	   %2 UID kontejneru odkud
#	   %3 UID kontejneru kam
#	   %4 CISLO kolik, bere i klíčová slova All/Weight, tedy Vše nebo Podle Váhy
#	   %5 CISLO barva
def PresunItem(type, src, tar, amount = 1, color = -1):
	if CountType(type, src) <= 0:
		return False
	
	FindType(type, -1, src, color)
	MoveItem("found", tar, amount)
	return True
	
def LoadAlias(alias, n, max):
	if GetAlias(alias) == 0:
		PromptAlias(alias)
	else:
		HeadMsg(alias, alias)
		if not ConfirmPrompt("Nastavení proměnných " + str(n) + "/" + str(max) + ":\nPoužít tento cíl jako '" + alias + "'?"):
			PromptAlias(alias)

def CheckDistance(alias, d):
	if Distance(alias) > d:
		ConfirmPrompt("Jsi moc daleko od " + alias + ".\nKlikni Okay až budeš maximálně " + str(d) + " polí daleko")
		CheckDistance(alias, d)
	
def SaveConfig(config):
	with codecs.open(CONFIG, "w", encoding='utf-8') as config_file:
		json.dump(config, config_file, indent=4, sort_keys=True, ensure_ascii=False)
		
def LoadConfig():
	if not os.path.isfile(CONFIG):
		DefaultConfig()
		
	with codecs.open(CONFIG, encoding='utf-8') as config_file:
		return json.load(config_file)

def DefaultConfig():
	SaveConfig({ "macros": {}})

def SaveMacroVariable(macro, variable, value):
	config = LoadConfig()
	if macro not in config["macros"]:
		config["macros"][macro] = {}
	config["macros"][macro][variable] = value
		
	SaveConfig(config)
	
def LoadMacroVariable(macro, variable, defaultValue = None):
	config = LoadConfig()
	if macro in config["macros"] and variable in config["macros"][macro]:
		return config["macros"][macro][variable]
	return defaultValue

def LoadMacroVariables(macro, defaultValue = {}):
	config = LoadConfig()
	if macro in config["macros"]:
		return config["macros"][macro]
	return defaultValue

Pos = namedtuple('Pos', 'x y z note')
OpenClosestDoor = namedtuple('OpenClosestDoor', 'door note')

def DictifyRails(rails):
	res = []
	for macro in rails:
		res.append(DictifyMacro(macro))
	return res

def DictifyMacro(macro):
	vals = []
	for rail in macro[1]:
		vals.append(DictifyRail(rail))
	return (macro[0], vals)

def DictifyRail(rail):
	vals = []
	for pos in rail[1]:
		vals.append(pos._asdict())
	return (rail[0], vals)

def UndictifyRails(rails):
	res = []
	for macro in rails:
		res.append(UndictifyMacro(macro))
	return res

def UndictifyMacro(macro):
	vals = []
	for rail in macro[1]:
		vals.append(UndictifyRail(rail))
	return (macro[0], vals)

def UndictifyRail(rail):
	vals = []
	for pos in rail[1]:
		if "door" in pos.keys():
			vals.append(OpenClosestDoor(**pos))
		else:
			vals.append(Pos(**pos))
	return (rail[0], vals)

def SaveRails(rails):
	config = LoadConfig()
	config["Rails"] = DictifyRails(rails)
	SaveConfig(config)

def LoadRails(macro = None, rail = None, index = None):
	config = LoadConfig()
	if "Rails" in config:
		rails = UndictifyRails(config["Rails"])
		if macro is not None:
			mac = next((m for m in rails if m[0] == macro), None)
			if mac is not None:
				if rail is not None:
					rai = next((r for r in mac[1] if r[0] == rail), None)
					if rai is not None:
						if index is not None:
							if index < len(rai[1]):
								return rai[1][index]
							return None
						return rai[1]
				return mac[1]
		return rails
	return []

def PathfindToRail(macro, rail, index, tolerance = -1, maxTries = 30, pause = 1000):
	return PathfindToPos(LoadRails(macro, rail, index), tolerance, maxTries, pause)

def __current_milli_time():
	return round(time.time() * 1000)

def WalkTo(posX, posY, posZ, timeout=8000):
	cMStart = __current_milli_time()
	Pathfind(posX, posY, posZ)

	attempts = 1
	while Engine.Player.X != posX or Engine.Player.Y != posY or Engine.Player.Z != posZ:
		Pause(500)
		if attempts >= 10:
			attempts = 1
			Pathfind(posX, posY, posZ)

		cMCurrent = __current_milli_time()
		if cMCurrent - cMStart > timeout:
			print("Timeout with WalkTo function")
			return False

	return True

def PathfindToPos(pos, tolerance, maxTries, pause):
	if isinstance(pos, list):
		for onePos in pos:
			PathfindToPos(onePos, tolerance, maxTries, pause)
		return True

	if isinstance(pos, OpenClosestDoor):
		ToggleNearestDoor()
		Pause(200)
		return True

	if tolerance > 0:
		tries = 0
		while Distance(pos.x, pos.y, Engine.Player.X, Engine.Player.Y) > tolerance:
			if not Pathfinding():
				print("{} - {}".format(tries, Pathfinding()))
				if tries > maxTries:
					return False
				tries += 1
				Pathfind(pos.x, pos.y, pos.z)
			Pause(pause)
		return True
	else:			
		return WalkTo(pos.x, pos.y, pos.z)

def Distance(x1, y1, x2, y2):
	return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

def RunAFK():
	PlayMacro("AFK Gump")

def StopAFK():
	CloseGump(0x2fb1ee43)

def CheckVersion():
	url = "https://raw.githubusercontent.com/PoodyCZ/DorchLib/master/DorchLib.py"
	cl = WebClient()
	dwnStr = cl.DownloadString(url)
	todayString = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	remindTomorrow = LoadMacroVariable("DorchLib", "RemindTomorrow", False)
	if remindTomorrow:
		lastVersionCheck = datetime.strptime(LoadMacroVariable("DorchLib", "LastVersionCheck", todayString), '%m/%d/%Y, %H:%M:%S')
		if lastVersionCheck > datetime.now() - timedelta(days=1):
			return
	for line in dwnStr.splitlines():
		if line.startswith("#Version"):
			gitVersion = ''
			for match in re.finditer("\d+(\.\d+)+", line):
				if len(match.group(0)) > len(gitVersion):
					gitVersion = match.group(0)
			ignoreVersion = LoadMacroVariable("DorchLib", "IgnoreVersion", "0.0.0")
			if LooseVersion(ignoreVersion) == LooseVersion(gitVersion):
				return
			if LooseVersion(Version) < LooseVersion(gitVersion):
				res, index = SelectionPrompt(['Otevřít stránku se stažením nové verze', 'Připomenout zítra', 'Tuto verzi nepřipomínat'], "Je dostupná nová verze DorchLib v{}!".format(gitVersion))
				if res:
					if index == 0:
						webbrowser.open("https://github.com/PoodyCZ/DorchLib", new=1)
					elif index == 1:
						SaveMacroVariable("DorchLib", "RemindTomorrow", True)
						SaveMacroVariable("DorchLib", "LastVersionCheck", todayString)
					else:
						SaveMacroVariable("DorchLib", "IgnoreVersion", gitVersion)
			break

__lastOpenedDoors = None

def ToggleNearestDoor():
	global __lastOpenedDoors

	if __lastOpenedDoors is not None:
		FindObject(__lastOpenedDoors, range=2)
		if GetAlias("found") != 0:
			HeadMsg("Tyhle beru", GetAlias("found"))
			UseObject(GetAlias("found"))
			__lastOpenedDoors = None
			return True

	closeDoors = FindTypeList("doors", 2, returnAllItems=True)
	minDistance = 5
	for door in closeDoors:
		if door.Distance < minDistance:
			minDistance = door.Distance

	doorsToCheck = []
	for door in closeDoors:
		if door.Distance == minDistance:
			doorsToCheck.append(door)

	nearestDoor = None
	if len(doorsToCheck) == 0:
		nearestDoor = False
	elif len(doorsToCheck) == 1:
		nearestDoor = doorsToCheck[0]
	else:
		dir = Engine.Player.Direction

		for door in doorsToCheck:
			frontOf = Engine.Player.X + 1
			if (dir == Direction.West or dir == Direction.Southeast or dir == Direction.Northeast) and frontOf == door.X and Engine.Player.Y == door.Y:
				nearestDoor = door
				break

			frontOf = Engine.Player.X - 1
			if (dir == Direction.East or dir == Direction.Southwest or dir == Direction.Northwest) and frontOf == door.X and Engine.Player.Y == door.Y:
				nearestDoor = door
				break

			frontOf = Engine.Player.Y + 1
			if dir == Direction.South and Engine.Player.X == door.X and frontOf == door.Y:
				nearestDoor = door
				break

			frontOf = Engine.Player.Y - 1
			if dir == Direction.North and Engine.Player.X == door.X and frontOf == door.Y:
				nearestDoor = door
				break

		if nearestDoor is None:
			nearestDoor = doorsToCheck[0]

	if nearestDoor is False:
		print("Žádné dveře blízko")
		return False

	HeadMsg("Tyhle beru", nearestDoor.Serial)
	UseObject(nearestDoor.Serial)
	__lastOpenedDoors = nearestDoor.Serial

	return True

def FindTypeList(list, range=None, loc=None, minamount=None, returnAllItems = False):
	if returnAllItems:
		multiItems = []
	if list in MultiTypes:
		for type in MultiTypes[list]:
			objects = FindTypeBy(type, range, loc, minamount, returnAllItems)
			if objects is not None:
				if returnAllItems:
					for object in objects:
						multiItems.append(object)
				else:
					return objects
		if returnAllItems:
			return multiItems
	else:
		raise NameError("MultiType " + list + " not found")

	return False
