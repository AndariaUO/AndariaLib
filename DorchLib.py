# coding=utf-8

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
import os
import json
import codecs

CONFIG = "Data\Plugins\ClassicAssist\Modules\DorchLib.config"

Graphics = {
	"kolovrat": 0x1015,
	"vlna": 0xdf8,
	"prize": 0xe1d
}

def VratTyp(graphics):
	if graphics in Graphics:
		return Graphics[graphics]
	else:
		return 0

#Funkce pro přesun itemu
#args - %1 TYPE Itemu
#       %2 UID kontejneru odkud
#       %3 UID kontejneru kam
#       %4 CISLO kolik, bere i klíčová slova All/Weight, tedy Vše nebo Podle Váhy
#       %5 CISLO barva
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

def SaveRails(rails):
	config = LoadConfig()
	config["Rails"] = rails
	SaveConfig(config)

def LoadRails(macro = None, rail = None, index = None):
	config = LoadConfig()
	if "Rails" in config:
		rails = config["Rails"]
		if macro is not None and macro in rails:
			if rail is not None and rail in rails[rail]:
				if index is not None and index < len(rails[macro][rail]):
					return rails[macro][rail][index]
				return rails[macro][rail]
			return rails[macro]
		return rails
	return {}

def RunAFK():
	PlayMacro("AFK Gump")

def StopAFK():
	CloseGump(0x2fb1ee43)