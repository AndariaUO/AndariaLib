# -*- coding: utf-8 -*-

import unicodedata
REMOVE_STRINGS = {
	"š": "s",
	"é": "e",
	"": "s",
	"í": "i",
	"ý": "y",
}

def NormalizeString(string):
	returnString = string
	for fr, to in REMOVE_STRINGS.items():
		returnString = returnString.replace(fr, to)

	return returnString.lower().strip()

class ItemTypeClass:

	def __init__(self, types, names=None, colors=None, notNames=None):
		self.types = types
		if names is not None:
			if isinstance(names, list):
				namesTo = []
				for name in names:
					namesTo.append(NormalizeString(name))

				self.names = namesTo
			else:
				self.names = NormalizeString(names)
		else:
			self.names = None

		self.colors = colors

		if notNames is not None:
			if isinstance(notNames, list):
				notNamesTo = []
				for notName in notNames:
					notNamesTo.append(NormalizeString(notName))

				self.notNames = notNamesTo
			else:
				self.notNames = NormalizeString(notNames)
		else:
			self.notNames = None

	def match(self, item):
		matched = False
		if isinstance(self.types, list):
			for type in self.types:
				if type == item.ID:
					matched = True
		else:
			matched = self.types == item.ID

		if matched is False:
			return False

		matchedName = True
		if self.names is not None:
			matchedName = self.matchName(item.Name)

		matchedColor = True
		if self.colors is not None:
			matchedColor = self.colors == item.Hue

		matchedNotName = True
		if self.notNames is not None:
			matchedNotName = self.notMatchName(item.Name)

		return matched and matchedName and matchedColor and matchedNotName

	def matchName(self, itemName):
		itemName = NormalizeString(itemName)
		if isinstance(self.names, list):
			for name in self.names:
				if itemName.find(name) != -1:
					return True
		else:
			return itemName.find(self.names) != -1

	def notMatchName(self, itemName):
		itemName = NormalizeString(itemName)
		if isinstance(self.notNames, list):
			for name in self.notNames:
				if itemName.find(name) != -1:
					return False

			return True
		else:
			return itemName.find(self.notNames) == -1


Graphics = {
	"log": 7133,
	"kos": 3703,
	"kladivkoKovarske": 5091,
	"dyka": 3921,
	"prutyZelezo": 7151,
	"prutyStribro": 7157,
	"prutyMed": 7139,
	"prutyZlato": 7145,
	"dratStribro": 6263,
	"dratMed": 6265,
	"dratZlato": 6264,
	"kolovrat": 4117,
	"kolovrat2": 4124,
	"stav": 4195,
	"sukno": 5983,
	"vlna": 3576,
	"bavlna": 3577,
	"prize": 3613,
	"rudy": 6585,
	"seno": 0xf36,
	"mining1": 0x19b7,
	"mining2": 0x19b8,
	"mining3": 0x19b9,
	"polena": 0x1bdd,
	"driky": 7124,
	"prkna": 7127,
	"vrhacky": 15455,
	"pirka": 7121,
	"sipy": 3903,
	"sipky": 7163,
	"uvaz": 5351,
	"lahvicky": 3854,
	"suroveZelezo": 15141,
	"sirnyPrach": 3980,
	"drevenaDyka": 3921,
	"sukovice": 5113,
	"zelezoDrat": 6262,
	"hrebiky": 4142,
	"naradi": 7868,
	"pila": 4148,
	"peri": 7121,
	"obvaz": 3617,
	"krvavyObvaz": 3616,
	"sucheDrevo": 3984,
	"flousatko": 10154,
	"ostep": 3939,
	"gemsDiamant": 3878,
	"gemsRubin": 3859,
	"gemsHvezdSafir": 3873,
	"gemsSmaragd": 3856,
	"gemsTurmalin": 3864,
	"gemsJantar": 3877,
	"gemsCitrin": 3861,
	"gemsSafir": 3857,
	"gemsAmetyst": 3886,
	"gemsPerla": 0xf1e,
	"gems": 3870,
	"mapaKPokladu": 5355,
	"gems3": 3855,
	"gems4": 3367,
	"rozstrihanaKuze": 4199,
	"hromadaKuze": 4216,
	"siciPotreby": 3997,
	"nuzky": 3998,
	"prazdnySvitek": 3636,
	"tesarskeKladivko": 4138,
	"sekera": 3907,
	"bojovaSekera": 3911,
	"palas": 5184,
	"obsidian": 3977,
	"vikoSudu": 7608,
	"skruze": 7857,
	"obruceSudu": 4321,
	"kohoutek": 4100,
	"nit": 4000,
	"platno": 5982,
	"paklic": 5371,
	"panty": 4181,
	"kolecka": 4179,
	"pruzinky": 4189,
	"sadlo": 7818,
	"strevo": 7407,
	"esence": 15143,
	"chmelSeed": 3818,
	"mandragora": 3974,
	"krvavyMech": 3963,
	"cerneperly": 3962,
	"zensen": 3973,
	"pavuciny": 3981,
	"rulik": 3976,
	"cesneky": 3972,
	"kosti": 3966,
	"lektvarOsvezeni": 3851,
	"lektvarLecivy": 3852,
	"lektvarVybusny": 0xf0d,
	"lektvarSila": 3849,
	"lektvarProtijed": 3847,
	"lektvarMoudrost": 3842,
	"lektvarJed": 3850,
	"lektvarHbitost": 3848,
	"lektvarSvetlo": 3846,
	"lektvarSkrytiPovesti": 3844,
	"lektvarVelky": 0x3bf4,
	"platNohavice": 5137,
	"platRukavice": 5144,
	"platRukavy": 5136,
	"platLimec": 5139,
	"platHrud": 5141,
	"platPrilba": 5138,
	"dratRukavice": 5062,
	"dratKosile": 5055,
	"dratKalhoty": 5054,
	"dratKukla": 5015,
	"bascinet": 5132,
	"ustrizeneVlasy": 3582,
	"stetecPaleta": 4033,
	"kouzelnickyKloboukPlatno": 5912,
	"plastPlatno": 5397,
	"zdobKosilePlatno": 7933,
	"kapePlatno": 9716,
	"kiltPlatno": 5431,
	"zimniBoty": 5897,
	"svitek": 3637,
	"hedvabnaNit": 3614,
	"hedvabnaLatka": 5984,
	"carodejovaRoba": 7939,
	"nadoba": 6870,
	"nadoba2": 6871,
	"hlina": 12793,
	"lopata": 3897,
	"krumpac": 0xe85,
	"zoranaHlina": 12788,
	"rostlinkaZasazenaZensen": 6377,
	"rostlinkaZasazenaMandragora": 6367,
	"rostlinkaVytrzenaMandragora": 6365,
	"rostlinkaVytrzenaZensen": 6379,
	"rostlinkaZasazenaCesnek": 6369,
	"rostlinkaVytrzenaCesnek": 6371,
	"rostlinkaZasazenaBavlna": 3151,
	"rostlinkaZasazenaRulik": 6373,
	"lektvarMana": 6215,
	"krvaveJikry": 3964,
	"urodnePrsti": 3969,
	"katovyKukly": 3971,
	"prachZHrobu": 3983,
	"cernyVres": 3961,
	"krev": 3970,
	"krevDemona": 3965,
	"zmensovak": 3621,
	"pemza": 3979,
	"netopiriKridla": 3960,
	"krystalyNox": 3982,
	"kostiDemona": 3968,
	"stribrnak": 3824,
	"zlatakMedak": 3821,
	"slizkeOko": 3967,
	"plazivec": 3473,
	"draciSrdce": 3985,
	"hospinky": 15195,
	"abrosie": 15165,
	"datle": 5927,
	"kokosoveOrechy": 5926,
	"banany": 5919,
	"citrony": 5928,
	"cajovyListecek": 15163,
	"kukurice": 3199,
	"limetky": 5930,
	"jahody": 15288,
	"hulky": 3572,
	"hulky2": 3571,
	"hulky3": 3570,
	"hulky4": 3573,
	"vypuklyLektvar": 3841,
	"lektvarObnova": 3836,
	"lektvarHrotoveJedy": 6216,
	"knihaChaosu": 9100,
	"knihaMaterie": 8788,
	"valecnak_cerna": 0xCC,
	"valecnak_bila": 0xE2,
	"valecnak_zlata": 0xC8,
	"valecnak_hneda": 0xCC,
	"slechtak_hneda": 0xE4,
	"slechtak_pisek": 0xE4,
	"slechtak_bila": 0xE2,
	"slechtak_cerna": 0xE2,
	"pripousteci_hul": 0x13f5,
	"zlab_n": 0xB41,
	"zlab_s": 0xB42,
	"zlab_w": 0xB43,
	"zlab_e": 0xB44,
	"sud": 0x154D,
	"chleba": 0x103b,
	"pizza": 0x1040,
	"soskaVeverky": 0x2d97,
	"soskaKone": 0x2d9c,
	"soskaFretky": 0x2d98,
	"origamiMotyl": 0x283b,
	"origamiMotyl2": 0x2839,
	"pivo": 0x99f,
	"lahevVino": 0x9c7,
	"kusMasa": 0x9f1,
	"peceneMaso": 0x9f2,

	"rybarskyPrut": 0xdc0,
	"rybiStejk": 0x97a,
	"ryba1": 0x9cc,
	"ryba2": 0x9cd,
	"ryba3": 0x9ce,
	"ryba4": 0x9cf,
	"uhor": 0x379f,
	"perletoveryby": 0xdd5,
	"lviryby": 0xdd6,
	"letajiciryby": 0xdd7,
	"chobotnicka": 0x1b9b,
	"vodnisnek": 0xfc7,
	"vodnirasy": 0x9cc,
	"spinavaLahev": 0xe2b,
	
	#NPCS
	"mrtvola": 0x2006,
	"sliz": 0x33,
}

colorTmavo = 1109
colorMitril = 2057
colorOcel = 2824

Types = {
	"orliPeri": ItemTypeClass(Graphics["peri"], "orl"),
	"obycPeri": ItemTypeClass(Graphics["peri"], None, 0),
	"elfiSipy": ItemTypeClass(Graphics["sipy"], "elf"),
	"zlateSipy": ItemTypeClass(Graphics["sipy"], "zlat"),
	"obycSipy": ItemTypeClass(Graphics["sipy"], None, 0),
	"obycSipky": ItemTypeClass(Graphics["sipky"], None, 0),
	"tmavaLatka": ItemTypeClass(Graphics["platno"], None, colorTmavo),
	"zlateSipky": ItemTypeClass(Graphics["sipky"], "zlat"),
	"tmavyDrat": ItemTypeClass(Graphics["zelezoDrat"], None, colorTmavo),
	"mitrilDrat": ItemTypeClass(Graphics["zelezoDrat"], None, colorMitril),
	"prutyTmavy": ItemTypeClass(Graphics["prutyZelezo"], None, colorTmavo),
	"prutyMitril": ItemTypeClass(Graphics["prutyZelezo"], None, colorMitril),
	"prutyOcel": ItemTypeClass(Graphics["prutyZelezo"], None, colorOcel),
	"navodRobyOchrany": ItemTypeClass(Graphics["svitek"], "Roby Ochrany"),
	"obycNit": ItemTypeClass(Graphics["nit"], None, 0),
	"reznaNit": ItemTypeClass(Graphics["nit"], "rezn"),
	"tmavaNit": ItemTypeClass(Graphics["nit"], "tmava"),
	"obycRozstrihanaKuze": ItemTypeClass(Graphics["rozstrihanaKuze"], None, 0),
	"vlciRozstrihanaKuze": ItemTypeClass(Graphics["rozstrihanaKuze"], None, 978),
	"draciRozstrihanaKuze": ItemTypeClass(Graphics["rozstrihanaKuze"], None, 39),
	"medvediRozstrihanaKuze": ItemTypeClass(Graphics["rozstrihanaKuze"], None, 47),
	"obycHromadaKuze": ItemTypeClass(Graphics["hromadaKuze"], None, 0),
	"draciHromadaKuze": ItemTypeClass(Graphics["hromadaKuze"], None, 39),
	"medvediHromadaKuze": ItemTypeClass(Graphics["hromadaKuze"], None, 47),
	"vlciHromadaKuze": ItemTypeClass(Graphics["hromadaKuze"], None, 978),
	"hlina": ItemTypeClass(Graphics["mining1"], "hlína"),
	"piskovec": ItemTypeClass(Graphics["mining2"], "pískovce"),
	"mramor": ItemTypeClass(Graphics["mining2"], "mramor"),
	"stavebniKamen": ItemTypeClass(Graphics["mining2"], "stavební"),
	"uhli": ItemTypeClass(Graphics["mining1"], "uhl"),
	"suroveHedvabi": ItemTypeClass(Graphics["pavuciny"], "Surove Hedva"),
	"lektvarSlabsiOsvezeni": ItemTypeClass(Graphics["lektvarOsvezeni"], "Slabsi Lektva"),
	"lektvarSlabsiLecivy": ItemTypeClass(Graphics["lektvarLecivy"], "Slabsi Leciv"),
	"lektvarSlabsiProtijed": ItemTypeClass(Graphics["lektvarProtijed"], "Slabsi Protijed"),
	"lektvarSlabsiHbitost": ItemTypeClass(Graphics["lektvarHbitost"], ["Slabsi lektvary hbito", "Slabsi lektvar hbi"]),
	"lektvarHbitost": ItemTypeClass(Graphics["lektvarHbitost"], "Hbito", None, "Slabsi"),
	"lektvarHbitostVelky": ItemTypeClass(Graphics["lektvarVelky"], "Hbito", 1361),
	"lektvarProtijed": ItemTypeClass(Graphics["lektvarProtijed"], "Protijed", None, "Slabsi Protije"),
	"lektvarProtijedVelky": ItemTypeClass(Graphics["lektvarVelky"], "Protijed", 1259),
	"lektvarSlabsiSila": ItemTypeClass(Graphics["lektvarSila"], ["Slabsi Lektvar Sily", "Slabsi Lektvary Sily"]),
	"lektvarSila": ItemTypeClass(Graphics["lektvarSila"], "Sily", None, "Slabsi"),
	"lektvarSilaVelky": ItemTypeClass(Graphics["lektvarVelky"], "Sily", 0),
	"lektvarSlabsiDoplneniMany": ItemTypeClass(Graphics["lektvarMana"],
											   ["Slabsi Lektvar Doplneni Many", "Slabsi Lektvary Doplneni Many"]),
	"lektvarDoplneniMany": ItemTypeClass(Graphics["lektvarMana"], "Doplneni Many", None, "Slabsi"),
	"lektvarDoplneniManyVelky": ItemTypeClass(Graphics["lektvarVelky"], "Doplneni Many", 499),
	"lektvarSlabsiMoudrost": ItemTypeClass(Graphics["lektvarMoudrost"],
										   ["Slabsi Lektvar Moudro", "Slabsi Lektvary Moudrost"]),
	"lektvarMoudrost": ItemTypeClass(Graphics["lektvarMoudrost"], "Moudrost", None, "Slabsi"),
	"lektvarMoudrostVelky": ItemTypeClass(Graphics["lektvarVelky"], "Moudrost", 1276),
	"lektvarSlabsiVybusny": ItemTypeClass(Graphics["lektvarVybusny"], ["Slabsi Vybusn"]),
	"lektvarVybusny": ItemTypeClass(Graphics["lektvarVybusny"], "Vybušn", None, ["Slabsi Vybus"]),
	"lektvarVybusnyVelky": ItemTypeClass(Graphics["lektvarVelky"], "Výbušn", 1377),
	"lektvarSlabsiTranz": ItemTypeClass(Graphics["vypuklyLektvar"],
										["Slabsi Lektvar Tranzu", "Slabsi Lektvary Tranzu"]),
	"lektvarTranz": ItemTypeClass(Graphics["vypuklyLektvar"], "Tranz", None,
								  ["Slabsi Lektvar Tranzu", "Slabsi Lektvary Tranzu"]),
	"lektvarTranzVelky": ItemTypeClass(Graphics["lektvarVelky"], "Tranz", 1423),
	"lektvarSlabsiObnova": ItemTypeClass(Graphics["lektvarObnova"],
										 ["Slabsi Lektvar Obnovy", "Slabsi Lektvary Obnovy"]),
	"lektvarObnova": ItemTypeClass(Graphics["lektvarObnova"], "Obnovy", None,
								   ["Slabsi Lektvar Obnovy", "Slabsi Lektvary Obnovy"]),
	"lektvarObnovaVelky": ItemTypeClass(Graphics["lektvarVelky"], "Obnovy", 33),
	"lektvarHrotoveJedy": ItemTypeClass(Graphics["lektvarHrotoveJedy"], ["Hrotove Jedy", "Hrotovy Jed"]),
	"lektvarRozptyleniMagie": ItemTypeClass(Graphics["lektvarSila"], "Rozptyleni", 1151),
	"lektvarRozptyleniMagieVelky": ItemTypeClass(Graphics["lektvarVelky"], "Rozptyleni", 1151),
	"lektvarOsvezeni": ItemTypeClass(Graphics["lektvarOsvezeni"], "Osvezeni", None, "Slabsi Lektvar"),
	"lektvarLecivy": ItemTypeClass(Graphics["lektvarLecivy"], "Leciv", None, "Slabsi Leciv"),
	"lektvarLecivyVelky": ItemTypeClass(Graphics["lektvarVelky"], "Leciv", 2642),
	"lektvarSlabsiJed": ItemTypeClass(Graphics["lektvarJed"], "Slabsi Jed"),
	"lektvarJed": ItemTypeClass(Graphics["lektvarJed"], "Jed", None, ["Slabsi jed", "Silny jed", "Silne jedy"]),
	"lektvarJedVelky": ItemTypeClass(Graphics["lektvarJed"], ["Silny Jed", "Silne Jedy"]),
	"lektvarJedSmrtelny": ItemTypeClass(Graphics["lektvarVelky"], ["Smrtelny Jed", "Smrtelne Jedy"]),
	"lektvarSkrytiPovesti": ItemTypeClass(Graphics["lektvarSkrytiPovesti"], "Skryti Povesti"),
	"misicka": ItemTypeClass(Graphics["nadoba"], "Misicka Le"),
	"svitekOhnivaKoule": ItemTypeClass(Graphics["svitek"], "Ohnivá koule", 2878),
	"kosti": ItemTypeClass(Graphics["kosti"], None, 0),
	"cerneKosti": ItemTypeClass(Graphics["kosti"], None, 1109),
	"krvaveKosti": ItemTypeClass(Graphics["kosti"], None, 1171),
	"rostlinkaZasazenaMandragora": ItemTypeClass(Graphics["rostlinkaZasazenaMandragora"], None, 0),
	"rostlinkaZasazenaRulik": ItemTypeClass(Graphics["rostlinkaZasazenaRulik"], None, 0),
	"svitekChaos": ItemTypeClass(Graphics["svitek"], None, 2878),
	"svitekChaosExploze": ItemTypeClass(Graphics["svitek"], "Exploze", 2878),
	"svitekChaosUder": ItemTypeClass(Graphics["svitek"], "úder", 2878),
	"svitekPriroda": ItemTypeClass(Graphics["svitek"], None, 1368),
	"svitekMaterie": ItemTypeClass(Graphics["svitek"], None, 2805),
	"svitekMaterieNeviditelnost": ItemTypeClass(Graphics["svitek"], "Nevidi", 2805),
	"svitekMaterieSmrst": ItemTypeClass(Graphics["svitek"], "Smršť", 2805),
	"svitekRad": ItemTypeClass(Graphics["svitek"], None, 2934),
	"svitekZivot": ItemTypeClass(Graphics["svitek"], None, 2705),
	"svitekSmrt": ItemTypeClass(Graphics["svitek"], None, 977),
	"svitekPrvniStupen": ItemTypeClass(Graphics["svitek"], None, 0),
	"nadobaLektvar": ItemTypeClass([Graphics["nadoba"], Graphics["nadoba2"]], None, 1045),
	"draciKrev": ItemTypeClass(Graphics["krev"], "Drač", 0),
	"esenceSlizu": ItemTypeClass(Graphics["esence"], "Slizu", 63),
	"esenceZeme": ItemTypeClass(Graphics["esence"], "Zem", 2263),
	"esenceVody": ItemTypeClass(Graphics["esence"], "Vod", 6),
	"esenceOhne": ItemTypeClass(Graphics["esence"], "Ohn", 2994),
	"esenceVzduchu": ItemTypeClass(Graphics["esence"], "Vzduch", 21),
	"lektvarZmenseni": ItemTypeClass(Graphics["zmensovak"], None, 904),
	"navody": ItemTypeClass(Graphics["svitek"], "Navod"),
	"kokosovyOrech": ItemTypeClass(Graphics["kokosoveOrechy"], "Kokosov"),
	"magickaKnihaChaosu": ItemTypeClass(Graphics["knihaChaosu"], "Chaosu"),
	"magickaKnihaMaterie": ItemTypeClass(Graphics["knihaMaterie"], "Materie"),
	"hnedePivo": ItemTypeClass(Graphics["pivo"], "Hnede"),
	"jantarovePivo": ItemTypeClass(Graphics["pivo"], "Jantarov"),
	"vino": ItemTypeClass(Graphics["lahevVino"], "vin"),
	"jeseter": ItemTypeClass(Graphics["ryba1"], "jeseter"),
	"sumec": ItemTypeClass(Graphics["ryba1"], "sumec"),
	"kapr": ItemTypeClass(Graphics["ryba1"], "kapr"),
	"zlataryba": ItemTypeClass(Graphics["ryba1"], "zlatá ryba"),
	"stika": ItemTypeClass(Graphics["ryba1"], "tika"),
	"okoun": ItemTypeClass(Graphics["ryba2"], "okoun"),
	"lin": ItemTypeClass(Graphics["ryba3"], "lín"),
	"candat": ItemTypeClass(Graphics["ryba2"], "candát"),
}

MultiTypes = {
	"horses": [
		Graphics["valecnak_cerna"],
		Graphics["valecnak_bila"],
		Graphics["valecnak_zlata"],
		Graphics["valecnak_hneda"],
		Graphics["slechtak_hneda"],
		Graphics["slechtak_pisek"],
		Graphics["slechtak_bila"],
		Graphics["slechtak_cerna"],
	],
	"watersources": [
		Graphics["zlab_s"],
		Graphics["zlab_e"],
		Graphics["zlab_n"],
		Graphics["zlab_w"],
		Graphics["sud"],
	],
	"doors": [
		1661, 1653, 1663, 1664, 1662, 1663, 2567, 2134, 4239, 1757, 1758, 1653, 1654, 1655, 1656, 1711, 1712,
		1767, 1768,
		1671, 8174, 1672, 1677, 1669, 8183, 8184, 2160, 2158, 1709, 1710, 1705, 1706, 1765, 1766, 1775, 1773,
		1776, 1774, 9141, 9144, 9138, 9137,
		9135, 9139, 1779, 1780, 1657, 1658, 1737, 1739, 2151, 2150, 2156, 2154, 2155, 2157, 2133, 2132, 1703,
		1701, 1704, 1702,
		4242  # packa,
	],
	"ovoce": [
		Graphics["hospinky"], Graphics["abrosie"], Graphics["datle"], Types["kokosovyOrech"],
		Graphics["banany"], Graphics["citrony"], Graphics["cajovyListecek"], Graphics["kukurice"], Graphics["limetky"],
	],
	"hulky": [
		Graphics["hulky"], Graphics["hulky2"], Graphics["hulky3"], Graphics["hulky4"],
	],
	"stromy": [15189, 3242, 870, 3222, 3221, 15190, 15186, Graphics["jahody"], 15182, 3478, 3486, 3482,
			   871  # krvavy mech
			   ],
	"gems": [
		Graphics["gemsCitrin"], Graphics["gemsDiamant"], Graphics["gemsRubin"], Graphics["gemsHvezdSafir"],
		Graphics["gemsSmaragd"], Graphics["gemsTurmalin"], Graphics["gemsJantar"], Graphics["gemsSafir"],
		Graphics["gemsAmetyst"],
		Graphics["gems"], Graphics["gems3"], Graphics["gems4"],
	],
	"throphy": [15170, Graphics["kokosoveOrechy"], 5640, 7408, 15174, 5357, ],
	"rudy": [
		ItemTypeClass([6585, 6584, 6586, 3978, 6583], ["ruda", "rudy"])
	],
	"dolovane": [ Graphics["mining1"], Graphics["mining2"], Graphics["mining3"], Graphics["sirnyPrach"], Graphics["suroveZelezo"], Graphics["obsidian"] ],
	"zakladRegy": [
		Graphics["mandragora"], Graphics["krvavyMech"], Graphics["sirnyPrach"], Graphics["cerneperly"], Graphics["pavuciny"],
		Graphics["rulik"], Graphics["cesneky"], Graphics["krvaveJikry"], Graphics["urodnePrsti"], Graphics["zensen"],
	],
	"esence": [
		Types["esenceVody"], Types["esenceZeme"], Types["esenceSlizu"],
	],
	"rostlinkyZasazene": [
		Types["rostlinkaZasazenaMandragora"], Types["rostlinkaZasazenaRulik"], Graphics["rostlinkaZasazenaZensen"],
		Graphics["rostlinkaZasazenaCesnek"], Graphics["rostlinkaZasazenaBavlna"],
	],
	"rostlinkyVytrzena": [
		Graphics["rostlinkaVytrzenaZensen"], Graphics["rostlinkaVytrzenaMandragora"],
		Graphics["rostlinkaVytrzenaCesnek"],
	],
	"lektvary": [
		Types["lektvarSlabsiSila"], Types["lektvarSlabsiLecivy"], Types["lektvarSlabsiJed"],
		Types["lektvarSlabsiOsvezeni"], Types["lektvarSlabsiLecivy"], Types["lektvarSlabsiJed"],
		Types["lektvarSlabsiProtijed"], Types["lektvarSlabsiHbitost"], Types["lektvarHbitost"],
		# --Types["lektvarHbitostVelky"], Types["lektvarProtijed"], Types["lektvarProtijedVelky"],
		# --Types["lektvarSlabsiSila"], Types["lektvarSila"], Types["lektvarSilaVelky"],
		# --Types["lektvarSlabsiMoudrost"], Types["lektvarMoudrost"], Types["lektvarSlabsiVybusny"],
		# --Types["lektvarVybusny"], Types["lektvarVybusnyVelky"], Types["lektvarOsvezeni"],
		Types["lektvarLecivy"], Types["lektvarLecivyVelky"], Types["lektvarJed"],
		# --Types["lektvarJedVelky"], Types["lektvarSkrytiPovesti"],
	],
	"kostiSber": [
		0x1b0e,0x1b0a,0x1b1a,0x1b19
	],
	"AndorStokyNPCs": [
		0x33, 0xd7, 0x2a
	],
	"stahovaciNuz": [
		0xec4, 0xec5
	],
	"rybolovCennosti": [
		Types["jeseter"], Graphics["cerneperly"], Types["zlataryba"], Graphics["spinavaLahev"], Graphics["gemsPerla"]
	],
	"rybolovKuch": [
		Graphics["krvaveJikry"], Graphics["rybiStejk"]
	],
	"ryby": [
		Types["jeseter"], Types["sumec"], Types["kapr"], Types["zlataryba"], Types["stika"], Types["okoun"], Types["lin"], Types["candat"], Graphics["lviryby"], Graphics["letajiciryby"], Graphics["perletoveryby"]
	]
}
