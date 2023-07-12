# -*- coding: utf-8 -*-

def Deaccent2(text):
	return ''.join(CharTrans2(ch) for ch in text)

def CharTrans2(ch):
	och = ord(ch)
	if och == 193: return 'a'
	elif och == 196: return 'a'
	elif och == 200: return 'c'
	elif och == 207: return 'd'
	elif och == 201: return 'e'
	elif och == 204: return 'e'
	elif och == 205: return 'i'
	elif och == 197: return 'l'
	elif och == 188: return 'l'
	elif och == 210: return 'n'
	elif och == 211: return 'o'
	elif och == 212: return 'o'
	elif och == 214: return 'o'
	elif och == 192: return 'r'
	elif och == 216: return 'r'
	elif och == 138: return 's'
	elif och == 141: return 't'
	elif och == 218: return 'u'
	elif och == 217: return 'u'
	elif och == 220: return 'u'
	elif och == 221: return 'y'
	elif och == 142: return 'z'
	elif och == 225: return 'a'
	elif och == 228: return 'a'
	elif och == 232: return 'c'
	elif och == 239: return 'd'
	elif och == 233: return 'e'
	elif och == 236: return 'e'
	elif och == 237: return 'i'
	elif och == 229: return 'i'
	elif och == 190: return 'i'
	elif och == 242: return 'n'
	elif och == 243: return 'o'
	elif och == 244: return 'o'
	elif och == 246: return 'o'
	elif och == 224: return 'r'
	elif och == 248: return 'r'
	elif och == 154: return 's'
	elif och == 157: return 't'
	elif och == 250: return 'u'
	elif och == 249: return 'u'
	elif och == 252: return 'u'
	elif och == 253: return 'y'
	elif och == 158: return 'z'
	else:
		return ch

def NormalizeString(string):
	return Deaccent2(string).lower().strip()

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
				if name in itemName:
					return True
		else:
			return self.names in itemName

	def notMatchName(self, itemName):
		itemName = NormalizeString(itemName)
		if isinstance(self.notNames, list):
			for name in self.notNames:
				if name in itemName:
					return False

			return True
		else:
			return self.names not in itemName


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
	"svitekZmenseni": 0xe36,
	"zmensenyMedved": 0x211e,
	"umyvadlo": 0x1008,
	"paprika": 0x3b42,
	"vceliUl": 0x91a,
	"kureciStehynko": 0x1608,
	"mozek": 0x1cf0,
	"lebka": 0x1ae0,
	"misaHrachu": 0x1601,
	"prilbaZKosti": 0x1456,
	
	#NPCS
	"mrtvola": 0x2006,
	"sliz": 0x33,
	"grizzly": 0xd4,
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
	"kosti": ItemTypeClass(Graphics["kosti"], None, 0),
	"cerneKosti": ItemTypeClass(Graphics["kosti"], None, 1109),
	"krvaveKosti": ItemTypeClass(Graphics["kosti"], None, 1171),
	"rostlinkaZasazenaMandragora": ItemTypeClass(Graphics["rostlinkaZasazenaMandragora"], None, 0),
	"rostlinkaZasazenaRulik": ItemTypeClass(Graphics["rostlinkaZasazenaRulik"], None, 0),
	"nadobaLektvar": ItemTypeClass([Graphics["nadoba"], Graphics["nadoba2"]], None, 1045),
	"draciKrev": ItemTypeClass(Graphics["krev"], "Drač", 0),
	"esenceSlizu": ItemTypeClass(Graphics["esence"], "Slizu", 63),
	"esenceZeme": ItemTypeClass(Graphics["esence"], "Zem", 2263),
	"esenceVody": ItemTypeClass(Graphics["esence"], "Vod", 6),
	"esenceOhne": ItemTypeClass(Graphics["esence"], "Ohn", 2994),
	"esenceVzduchu": ItemTypeClass(Graphics["esence"], "Vzduch", 21),
	"lektvarZmenseni": ItemTypeClass(Graphics["zmensovak"], None, 904),
	"navodZlaty": ItemTypeClass(Graphics["svitek"], "Návod", 1944),
	"navodBily": ItemTypeClass(Graphics["svitek"], "Návod", 2064),
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
	"candat": ItemTypeClass(Graphics["ryba4"], "candát"),
	"mapalvl1": ItemTypeClass(Graphics["mapaKPokladu"], "Rozl", 52),
	"mapalvl2": ItemTypeClass(Graphics["mapaKPokladu"], "Rozl", 1975),
	"mapalvl3": ItemTypeClass(Graphics["mapaKPokladu"], "Rozl", 1710),
	"mapalvl4": ItemTypeClass(Graphics["mapaKPokladu"], "Rozl", 41),
	"mapalvl5": ItemTypeClass(Graphics["mapaKPokladu"], "Rozl", 1915),

	#trofeje
	"trophy_zmije": ItemTypeClass(Graphics["paprika"], "Zmiji zub", 871),
	"trophy_kobra": ItemTypeClass(Graphics["paprika"], "Kobri zub", 770),
	"trophy_mamba": ItemTypeClass(Graphics["paprika"], "Zub mamby", 2765),
	"trophy_anakonda": ItemTypeClass(Graphics["paprika"], "Zub anakondy", 2715),
	"trophy_obri_pavouk": ItemTypeClass(Graphics["kokosoveOrechy"], "Zamotek obriho pavouka", 1153),
	"trophy_desivy_pavouk": ItemTypeClass(Graphics["kokosoveOrechy"], "Zamotek desiveho pavouka", 2830),
	"trophy_sklipkan": ItemTypeClass(Graphics["kokosoveOrechy"], "Sklipkani zamotek", 1664),
	"trophy_upiriho_pavouka": ItemTypeClass(Graphics["kokosoveOrechy"], "Zamotek upiriho pavouka", 2246),
	"trophy_vtackar": ItemTypeClass(Graphics["kokosoveOrechy"], "Zamotek vtackare", 2056),
	"trophy_snovac": ItemTypeClass(Graphics["kokosoveOrechy"], "Zamotek snovace", 2921),
	"trophy_cerna_vdova": ItemTypeClass(Graphics["kokosoveOrechy"], "Zamotek cerne vdovy", 2831),
	"trophy_tarantule": ItemTypeClass(Graphics["kokosoveOrechy"], "Tarantuli zamotek", 2240),
	"trophy_vrrk": ItemTypeClass(Graphics["kureciStehynko"], "Vrrci tlapka", 2241),
	"trophy_skret": ItemTypeClass(Graphics["paprika"], "Skreti tesaky", 1446),
	"trophy_aligator": ItemTypeClass(Graphics["paprika"], "Krokodyli zub", 2241),
	"trophy_jesterak": ItemTypeClass(Graphics["paprika"], "Bodec z jesteriho muze", 2832),
	"trophy_gorila": ItemTypeClass(Graphics["mozek"], "Gorili mozek", 2718),
	"trophy_mephitis": ItemTypeClass(Graphics["vceliUl"], "Zamotek Mephitise", 2240),
	"trophy_katakan": ItemTypeClass(Graphics["lebka"], "Upiri lebka", 0),
	"trophy_parasekt": ItemTypeClass(0xe25, "Krev hadiho maga", 0),
	"trophy_zabi_matka": ItemTypeClass(Graphics["misaHrachu"], "Zabi jed", 0),
	"trophy_druid": ItemTypeClass(0x2559, "Medvedi kost", 0),
	"trophy_dabel": ItemTypeClass(Graphics["prilbaZKosti"], "Dablova lebka", 2058),
	"trophy_strazny_golem": ItemTypeClass(0x1023, "Soucastky strazneho golema", 980),
	"trophy_golem_strazce": ItemTypeClass(0x1023, "Soucastky golema strazce", 980),
	"trophy_kuresekt": ItemTypeClass(0xf54, "Ohnive vejce", 0),
	"trophy_kurekral": ItemTypeClass(0xf54, "Zlata pirka a vejice", 0),
	"trophy_minotaur": ItemTypeClass(0x2c7f, "Roh minotaura", 0),
	"trophy_vudce_lidozroutu": ItemTypeClass(0x1b1b, "Pater lidozrouta", 0),
	"trophy_pavouci_kral": ItemTypeClass(0x1504, "Nohy pavouka", 0),
	"trophy_pavouci_kralovna": ItemTypeClass(Graphics["esence"], "Krev kralovny", 0),

	#svitky magie pouze podle typu
	#"svitekChaos": ItemTypeClass(Graphics["svitek"], None, 2878),
	#"svitekPriroda": ItemTypeClass(Graphics["svitek"], None, 1368),
	#"svitekMaterie": ItemTypeClass(Graphics["svitek"], None, 2805),
	#"svitekRad": ItemTypeClass(Graphics["svitek"], None, 2934),
	#"svitekZivot": ItemTypeClass(Graphics["svitek"], None, 2705),
	#"svitekSmrt": ItemTypeClass(Graphics["svitek"], None, 977),
	#"svitekPrvniStupen": ItemTypeClass(Graphics["svitek"], None, 0),

	#svitky magie
    "svitekMateriePast": ItemTypeClass(Graphics["svitek"], "Past", 2805),
    "svitekMaterieOdstranpast": ItemTypeClass(Graphics["svitek"], "Odstran past", 2805),
    "svitekMaterieOdolnostnamagii": ItemTypeClass(Graphics["svitek"], "Odolnost na magii", 2805),
    "svitekMaterieMagickyzamek": ItemTypeClass(Graphics["svitek"], "Magicky zamek", 2805),
    "svitekMaterieOdemceni": ItemTypeClass(Graphics["svitek"], "Odemceni", 2805),
    "svitekMaterieMagickysip": ItemTypeClass(Graphics["svitek"], "Magicky sip", 2805),
    "svitekMaterieLedovasmrst": ItemTypeClass(Graphics["svitek"], "Ledova smrst", 2805),
    "svitekMaterieKamennazed": ItemTypeClass(Graphics["svitek"], "Kamenna zed", 2805),
    "svitekMaterieVymena": ItemTypeClass(Graphics["svitek"], "Vymena", 2805),
    "svitekMaterieRunovateleportace": ItemTypeClass(Graphics["svitek"], "Runova teleportace", 2805),
    "svitekMaterieOznaceniruny": ItemTypeClass(Graphics["svitek"], "Oznaceni runy", 2805),
    "svitekMaterieMagickyportal": ItemTypeClass(Graphics["svitek"], "Magicky portal", 2805),
    "svitekMaterieHromadnateleportace": ItemTypeClass(Graphics["svitek"], "Hromadna teleportace", 2805),
    "svitekMaterieNeviditelnost": ItemTypeClass(Graphics["svitek"], "Neviditelnost", 2805),
    "svitekMaterieHromadnaneviditelnost": ItemTypeClass(Graphics["svitek"], "Hromadna neviditelnost", 2805),
    "svitekMaterieOdhalenineviditelneho": ItemTypeClass(Graphics["svitek"], "Odhaleni neviditelneho", 2805),
    "svitekMaterieKamennygolem": ItemTypeClass(Graphics["svitek"], "Kamenny golem", 2805),
    "svitekMaterieVodnigolem": ItemTypeClass(Graphics["svitek"], "Vodni golem", 2805),
    "svitekMaterieLavovygolem": ItemTypeClass(Graphics["svitek"], "Lavovy golem", 2805),
    "svitekMaterieLedovygolem": ItemTypeClass(Graphics["svitek"], "Ledovy golem", 2805),
    "svitekMaterieKovovygolem": ItemTypeClass(Graphics["svitek"], "Kovovy golem", 2805),
    "svitekMaterieMagickacepel": ItemTypeClass(Graphics["svitek"], "Magicka cepel", 2805),
    "svitekMaterieBludiste": ItemTypeClass(Graphics["svitek"], "Bludiste", 2805),
    "svitekMaterieVytvorzbran": ItemTypeClass(Graphics["svitek"], "Vytvor zbran", 2805),
    "svitekMaterieVytvorzbroj": ItemTypeClass(Graphics["svitek"], "Vytvor zbroj", 2805),
    "svitekMaterieZrusmagii": ItemTypeClass(Graphics["svitek"], "Zrus magii", 2805),
    "svitekMateriePlosnezrusenimagie": ItemTypeClass(Graphics["svitek"], "Plosne zruseni magie", 2805),
    "svitekMaterieMagickykamen": ItemTypeClass(Graphics["svitek"], "Magicky kamen", 2805),
    "svitekMaterieHromovygolem": ItemTypeClass(Graphics["svitek"], "Hromovy golem", 2805),
    "svitekMaterieKresadlo": ItemTypeClass(Graphics["svitek"], "Kresadlo", 2805),
    "svitekMaterieKoroze": ItemTypeClass(Graphics["svitek"], "Koroze", 2805),
    "svitekMateriePromenavevirmagie": ItemTypeClass(Graphics["svitek"], "Promena ve vir magie", 2805),
    "svitekZivotLehkeleceni": ItemTypeClass(Graphics["svitek"], "Lehke leceni", 2705),
    "svitekZivotSilneleceni": ItemTypeClass(Graphics["svitek"], "Silne leceni", 2705),
    "svitekZivotPlosneleceni": ItemTypeClass(Graphics["svitek"], "Plosne leceni", 2705),
    "svitekZivotZmrtvychvstani": ItemTypeClass(Graphics["svitek"], "Zmrtvychvstani", 2705),
    "svitekZivotOchranavuciohni": ItemTypeClass(Graphics["svitek"], "Ochrana vuci ohni", 2705),
    "svitekZivotOchranavucienergii": ItemTypeClass(Graphics["svitek"], "Ochrana vuci energii", 2705),
    "svitekZivotOchranavucikyseline": ItemTypeClass(Graphics["svitek"], "Ochrana vuci kyseline", 2705),
    "svitekZivotOchranavucimrazu": ItemTypeClass(Graphics["svitek"], "Ochrana vuci mrazu", 2705),
    "svitekZivotOchranavucizlu": ItemTypeClass(Graphics["svitek"], "Ochrana vuci zlu", 2705),
    "svitekZivotOchranavucielementum": ItemTypeClass(Graphics["svitek"], "Ochrana vuci elementum", 2705),
    "svitekZivotRegenerace": ItemTypeClass(Graphics["svitek"], "Regenerace", 2705),
    "svitekZivotNesmrtelnost": ItemTypeClass(Graphics["svitek"], "Nesmrtelnost", 2705),
    "svitekZivotModlitba": ItemTypeClass(Graphics["svitek"], "Modlitba", 2705, "Plosna"),
    "svitekZivotSvatesvetlo": ItemTypeClass(Graphics["svitek"], "Svate svetlo", 2705),
    "svitekZivotObnova": ItemTypeClass(Graphics["svitek"], "Obnova", 2705),
    "svitekZivotPozehnejbytosti": ItemTypeClass(Graphics["svitek"], "Pozehnej bytosti", 2705),
    "svitekZivotPozehnejzbroj": ItemTypeClass(Graphics["svitek"], "Pozehnej zbroj", 2705),
    "svitekZivotNeutralizacejedu": ItemTypeClass(Graphics["svitek"], "Neutralizace jedu", 2705),
    "svitekZivotSejmutikletby": ItemTypeClass(Graphics["svitek"], "Sejmuti kletby", 2705),
    "svitekZivotBozipomoc": ItemTypeClass(Graphics["svitek"], "Bozi pomoc", 2705),
    "svitekZivotAchillovapata": ItemTypeClass(Graphics["svitek"], "Achillova pata", 2705),
    "svitekZivotUdernemrtveho": ItemTypeClass(Graphics["svitek"], "Uder nemrtveho", 2705),
    "svitekZivotZrannemrtveho": ItemTypeClass(Graphics["svitek"], "Zran nemrtveho", 2705),
    "svitekZivotZabijnemrtveho": ItemTypeClass(Graphics["svitek"], "Zabij nemrtveho", 2705),
    "svitekZivotOchranaprednemrtvymi": ItemTypeClass(Graphics["svitek"], "Ochrana pred nemrtvymi", 2705),
    "svitekZivotOchranapredumrtim": ItemTypeClass(Graphics["svitek"], "Ochrana pred umrtim", 2705),
    "svitekZivotSebeobetovani": ItemTypeClass(Graphics["svitek"], "Sebeobetovani", 2705),
    "svitekZivotPlosnaModlitba": ItemTypeClass(Graphics["svitek"], "Plosna Modlitba", 2705),
    "svitekSmrtVysatienergie": ItemTypeClass(Graphics["svitek"], "Vysati energie", 977),
    "svitekSmrtZleznameni": ItemTypeClass(Graphics["svitek"], "Zle znameni", 977),
    "svitekSmrtJed": ItemTypeClass(Graphics["svitek"], "Jed", 977),
    "svitekSmrtParalyza": ItemTypeClass(Graphics["svitek"], "Paralyza", 977),
    "svitekSmrtProklejpredmet": ItemTypeClass(Graphics["svitek"], "Proklej predmet", 977),
    "svitekSmrtNeohrabanost": ItemTypeClass(Graphics["svitek"], "Neohrabanost", 977),
    "svitekSmrtMdlamysl": ItemTypeClass(Graphics["svitek"], "Mdla mysl", 977),
    "svitekSmrtSlabost": ItemTypeClass(Graphics["svitek"], "Slabost", 977),
    "svitekSmrtSlepota": ItemTypeClass(Graphics["svitek"], "Slepota", 977),
    "svitekSmrtTemnezlo": ItemTypeClass(Graphics["svitek"], "Temne zlo", 977),
    "svitekSmrtMucivabolest": ItemTypeClass(Graphics["svitek"], "Muciva bolest", 977),
    "svitekSmrtKouzlosmrti": ItemTypeClass(Graphics["svitek"], "Kouzlo smrti", 977),
    "svitekSmrtObetovani": ItemTypeClass(Graphics["svitek"], "Obetovani", 977),
    "svitekSmrtParalyzacnipole": ItemTypeClass(Graphics["svitek"], "Paralyzacni pole", 977),
    "svitekSmrtSnizochranuvuciohni": ItemTypeClass(Graphics["svitek"], "Sniz ochranu vuci ohni", 977),
    "svitekSmrtSnizochranuvucichladu": ItemTypeClass(Graphics["svitek"], "Sniz ochranu vuci chladu", 977),
    "svitekSmrtSnizochranuvucienergii": ItemTypeClass(Graphics["svitek"], "Sniz ochranu vuci energii", 977),
    "svitekSmrtSnizochranuvucikyseline": ItemTypeClass(Graphics["svitek"], "Sniz ochranu vuci kyseline", 977),
    "svitekSmrtSnizochranuvucizlu": ItemTypeClass(Graphics["svitek"], "Sniz ochranu vuci zlu", 977),
    "svitekSmrtDotykupira": ItemTypeClass(Graphics["svitek"], "Dotyk upira", 977),
    "svitekSmrtJedovepole": ItemTypeClass(Graphics["svitek"], "Jedove pole", 977),
    "svitekSmrtOvladninemrtveho": ItemTypeClass(Graphics["svitek"], "Ovladni nemrtveho", 977),
    "svitekSmrtOchromeni": ItemTypeClass(Graphics["svitek"], "Ochromeni", 977),
    "svitekSmrtMor": ItemTypeClass(Graphics["svitek"], "Mor", 977),
    "svitekSmrtPsychickyuder": ItemTypeClass(Graphics["svitek"], "Psychicky uder", 977),
    "svitekSmrtMagickapouta": ItemTypeClass(Graphics["svitek"], "Magicka pouta", 977),
    "svitekSmrtDoteksmrti": ItemTypeClass(Graphics["svitek"], "Dotek smrti", 977),
    "svitekSmrtSnizodolnostvuciparalyze": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci paralyze", 977),
    "svitekSmrtSnizodolnostvucijedu": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci jedu", 977),
    "svitekSmrtSnizodolnostvucizivotu": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci zivotu", 977),
    "svitekSmrtSnizodolnostvucismrti": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci smrti", 977),
    "svitekSmrtSnizodolnostvuciradu": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci radu", 977),
    "svitekSmrtSnizodolnostvucichaosu": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci chaosu", 977),
    "svitekSmrtSnizodolnostvuciprirode": ItemTypeClass(Graphics["svitek"], "Sniz odolnost vuci prirode", 977),
    "svitekSmrtNemotornost": ItemTypeClass(Graphics["svitek"], "Nemotornost", 977),
    "svitekSmrtKletba": ItemTypeClass(Graphics["svitek"], "Kletba", 977),
    "svitekSmrtProrazstit": ItemTypeClass(Graphics["svitek"], "Proraz stit", 977),
    "svitekSmrtPlosnesnizeniochranyvuciohni": ItemTypeClass(Graphics["svitek"], "Plosne snizeni ochrany vuci ohni", 977),
    "svitekSmrtPlosnesnizeniochranyvucichladu": ItemTypeClass(Graphics["svitek"], "Plosne snizeni ochrany vuci chladu", 977),
    "svitekSmrtPlosnesnizeniochranyvucienergii": ItemTypeClass(Graphics["svitek"], "Plosne snizeni ochrany vuci energii", 977),
    "svitekSmrtPlosnesnizeniochranyvucikyseline": ItemTypeClass(Graphics["svitek"], "Plosne snizeni ochrany vuci kyseline", 977),
    "svitekSmrtPlosnesnizeniochranyvucizlu": ItemTypeClass(Graphics["svitek"], "Plosne snizeni ochrany vuci zlu", 977),
    "svitekRadOdzbrojeni": ItemTypeClass(Graphics["svitek"], "Odzbrojeni", 2934),
    "svitekRadSeslani": ItemTypeClass(Graphics["svitek"], "Seslani", 2934),
    "svitekRadOchranapredparalyzou": ItemTypeClass(Graphics["svitek"], "Ochrana pred paralyzou", 2934),
    "svitekRadOchranapredjedem": ItemTypeClass(Graphics["svitek"], "Ochrana pred jedem", 2934),
    "svitekRadOchranapredkouzlem": ItemTypeClass(Graphics["svitek"], "Ochrana pred kouzlem", 2934),
    "svitekRadDotekledu": ItemTypeClass(Graphics["svitek"], "Dotek ledu", 2934),
    "svitekRadOchranapredmagickymoborem(zivot)": ItemTypeClass(Graphics["svitek"], "Ochrana pred magickym oborem (zivot)", 2934),
    "svitekRadOchranapredmagickymoborem(smrt)": ItemTypeClass(Graphics["svitek"], "Ochrana pred magickym oborem (smrt)", 2934),
    "svitekRadOchranapredmagickymoborem(materie)": ItemTypeClass(Graphics["svitek"], "Ochrana pred magickym oborem (materie)", 2934),
    "svitekRadOchranapredmagickymoborem(chaos)": ItemTypeClass(Graphics["svitek"], "Ochrana pred magickym oborem (chaos)", 2934),
    "svitekRadOchranapredmagickymoborem(priroda)": ItemTypeClass(Graphics["svitek"], "Ochrana pred magickym oborem (priroda)", 2934),
    "svitekRadOchranapredmagii": ItemTypeClass(Graphics["svitek"], "Ochrana pred magii", 2934),
    "svitekRadMagickazbroj": ItemTypeClass(Graphics["svitek"], "Magicka zbroj", 2934),
    "svitekRadRozptylenimagie": ItemTypeClass(Graphics["svitek"], "Rozptyleni magie", 2934),
    "svitekRadPlosnerozptylenimagie": ItemTypeClass(Graphics["svitek"], "Plosne rozptyleni magie", 2934),
    "svitekRadLedovaboure": ItemTypeClass(Graphics["svitek"], "Ledova boure", 2934),
    "svitekRadOdrazeniutoku": ItemTypeClass(Graphics["svitek"], "Odrazeni utoku", 2934),
    "svitekRadNajdikouzla": ItemTypeClass(Graphics["svitek"], "Najdi kouzla", 2934),
    "svitekRadTicho": ItemTypeClass(Graphics["svitek"], "Ticho", 2934),
    "svitekRadUmlceni": ItemTypeClass(Graphics["svitek"], "Umlceni", 2934),
    "svitekRadMagickacepel": ItemTypeClass(Graphics["svitek"], "Magicka cepel", 2934),
    "svitekRadSejmikouzlo": ItemTypeClass(Graphics["svitek"], "Sejmi kouzlo", 2934),
    "svitekRadOdrazkouzlo": ItemTypeClass(Graphics["svitek"], "Odraz kouzlo", 2934),
    "svitekRadOdhaleni": ItemTypeClass(Graphics["svitek"], "Odhaleni", 2934),
    "svitekRadPastnakouzla": ItemTypeClass(Graphics["svitek"], "Past na kouzla", 2934),
    "svitekRadMihotani": ItemTypeClass(Graphics["svitek"], "Mihotani", 2934),
    "svitekRadRozptyleniprokleti": ItemTypeClass(Graphics["svitek"], "Rozptyleni prokleti", 2934),
    "svitekChaosOhnivakoule": ItemTypeClass(Graphics["svitek"], "Ohniva koule", 2878),
    "svitekChaosOhnivepole": ItemTypeClass(Graphics["svitek"], "Ohnive pole", 2878),
    "svitekChaosOcistaohnem": ItemTypeClass(Graphics["svitek"], "Ocista ohnem", 2878),
    "svitekChaosOhniveplameny": ItemTypeClass(Graphics["svitek"], "Ohnive plameny", 2878),
    "svitekChaosChodiciplameny": ItemTypeClass(Graphics["svitek"], "Chodici plameny", 2878),
    "svitekChaosOhnivykruh": ItemTypeClass(Graphics["svitek"], "Ohnivy kruh", 2878),
    "svitekChaosEfreet": ItemTypeClass(Graphics["svitek"], "Efreet", 2878),
    "svitekChaosExploze": ItemTypeClass(Graphics["svitek"], "Exploze", 2878),
    "svitekChaosOhnivyuder": ItemTypeClass(Graphics["svitek"], "Ohnivy uder", 2878),
    "svitekChaosDechdraka": ItemTypeClass(Graphics["svitek"], "Dech draka", 2878),
    "svitekChaosEnergetickastrela": ItemTypeClass(Graphics["svitek"], "Energeticka strela", 2878),
    "svitekChaosKaskada": ItemTypeClass(Graphics["svitek"], "Kaskada", 2878),
    "svitekChaosPlanoucihul": ItemTypeClass(Graphics["svitek"], "Planouci hul", 2878),
    "svitekChaosMagickapouta": ItemTypeClass(Graphics["svitek"], "Magicka pouta", 2878),
    "svitekChaosNeznamost": ItemTypeClass(Graphics["svitek"], "Neznamost", 2878),
    "svitekChaosMeteorickyroj": ItemTypeClass(Graphics["svitek"], "Meteoricky roj", 2878),
    "svitekChaosOhnivystit": ItemTypeClass(Graphics["svitek"], "Ohnivy stit", 2878),
    "svitekChaosBranapekel": ItemTypeClass(Graphics["svitek"], "Brana pekel", 2878),
    "svitekChaosKulovyblesk": ItemTypeClass(Graphics["svitek"], "Kulovy blesk", 2878),
    "svitekChaosStrach": ItemTypeClass(Graphics["svitek"], "Strach", 2878),
    "svitekChaosMagickystit": ItemTypeClass(Graphics["svitek"], "Magicky stit", 2878),
    "svitekChaosElementalnivyboj": ItemTypeClass(Graphics["svitek"], "Elementalni vyboj", 2878),
    "svitekChaosPromenavBeholdera": ItemTypeClass(Graphics["svitek"], "Promena v Beholdera", 2878),
    "svitekPrirodaPrevodsily": ItemTypeClass(Graphics["svitek"], "Prevod sily", 1368),
    "svitekPrirodaZkameneni": ItemTypeClass(Graphics["svitek"], "Zkameneni", 1368),
    "svitekPrirodaOdkameneni": ItemTypeClass(Graphics["svitek"], "Odkameneni", 1368),
    "svitekPrirodaSvetlo": ItemTypeClass(Graphics["svitek"], "Svetlo", 1368),
    "svitekPrirodaKoreny": ItemTypeClass(Graphics["svitek"], "Koreny", 1368),
    "svitekPrirodaMlha": ItemTypeClass(Graphics["svitek"], "Mlha", 1368),
    "svitekPrirodaLvisila": ItemTypeClass(Graphics["svitek"], "Lvi sila", 1368),
    "svitekPrirodaBoure": ItemTypeClass(Graphics["svitek"], "Boure", 1368),
    "svitekPrirodaDracikuze": ItemTypeClass(Graphics["svitek"], "Draci kuze", 1368),
    "svitekPrirodaChameleon": ItemTypeClass(Graphics["svitek"], "Chameleon", 1368),
    "svitekPrirodaOchranaprotizelezu": ItemTypeClass(Graphics["svitek"], "Ochrana proti zelezu", 1368),
    "svitekPrirodaOchranaprotioceli": ItemTypeClass(Graphics["svitek"], "Ochrana proti oceli", 1368),
    "svitekPrirodaOchranaprotimedi": ItemTypeClass(Graphics["svitek"], "Ochrana proti medi", 1368),
    "svitekPrirodaOchranaprotistribru": ItemTypeClass(Graphics["svitek"], "Ochrana proti stribru", 1368),
    "svitekPrirodaOchranaprotizlatu": ItemTypeClass(Graphics["svitek"], "Ochrana proti zlatu", 1368),
    "svitekPrirodaD'ao": ItemTypeClass(Graphics["svitek"], "D'ao", 1368),
    "svitekPrirodaMarid": ItemTypeClass(Graphics["svitek"], "Marid", 1368),
    "svitekPrirodaGenie": ItemTypeClass(Graphics["svitek"], "Genie", 1368),
    "svitekPrirodaZemetreseni": ItemTypeClass(Graphics["svitek"], "Zemetreseni", 1368),
    "svitekPrirodaTelekineze": ItemTypeClass(Graphics["svitek"], "Telekineze", 1368),
    "svitekPrirodaKocicimrstnost": ItemTypeClass(Graphics["svitek"], "Kocici mrstnost", 1368),
    "svitekPrirodaDracimoudrost": ItemTypeClass(Graphics["svitek"], "Draci moudrost", 1368),
    "svitekPrirodaBlesk": ItemTypeClass(Graphics["svitek"], "Blesk", 1368),
    "svitekPrirodaOzivenizvere": ItemTypeClass(Graphics["svitek"], "Oziveni zvere", 1368),
    "svitekPrirodaRust": ItemTypeClass(Graphics["svitek"], "Rust", 1368),
    "svitekPrirodaZivyplot": ItemTypeClass(Graphics["svitek"], "Zivy plot", 1368),
    "svitekPrirodaZahradka": ItemTypeClass(Graphics["svitek"], "Zahradka", 1368),
    "svitekPrirodaKyselaslina": ItemTypeClass(Graphics["svitek"], "Kysela slina", 1368),
    "svitekPrirodaHromadnesvetlo": ItemTypeClass(Graphics["svitek"], "Hromadne svetlo", 1368),
    "svitekPrirodaKyselinovymrak": ItemTypeClass(Graphics["svitek"], "Kyselinovy mrak", 1368),
    "svitekPrirodaPromenavpostrachlesa": ItemTypeClass(Graphics["svitek"], "Promena v postrach lesa", 1368),
    "svitekPrirodaOchranapromeny": ItemTypeClass(Graphics["svitek"], "Ochrana promeny", 1368),
    "svitekPrvniStupenTeleportace": ItemTypeClass(Graphics["svitek"], "Teleportace", 0),
    "svitekPrvniStupenUbliz": ItemTypeClass(Graphics["svitek"], "Ubliz", 0),
    "svitekPrvniStupenOvazranu": ItemTypeClass(Graphics["svitek"], "Ovaz ranu", 0),
    "svitekPrvniStupenMagickasipka": ItemTypeClass(Graphics["svitek"], "Magicka sipka", 0),
    "svitekPrvniStupenPlaminek": ItemTypeClass(Graphics["svitek"], "Plaminek", 0),
    "svitekPrvniStupenPromenavbludicku": ItemTypeClass(Graphics["svitek"], "Promena v bludicku", 0),	
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
	"trophies": [Types["trophy_zmije"],Types["trophy_kobra"],Types["trophy_mamba"],Types["trophy_anakonda"],Types["trophy_obri_pavouk"],Types["trophy_desivy_pavouk"],Types["trophy_sklipkan"],Types["trophy_upiriho_pavouka"],Types["trophy_vtackar"],Types["trophy_snovac"],Types["trophy_cerna_vdova"],Types["trophy_tarantule"],Types["trophy_vrrk"],Types["trophy_skret"],Types["trophy_aligator"],Types["trophy_jesterak"],Types["trophy_gorila"],Types["trophy_mephitis"],Types["trophy_katakan"],Types["trophy_parasekt"],Types["trophy_zabi_matka"],Types["trophy_druid"],Types["trophy_dabel"],Types["trophy_strazny_golem"],Types["trophy_golem_strazce"],Types["trophy_kuresekt"],Types["trophy_kurekral"],Types["trophy_minotaur"],Types["trophy_vudce_lidozroutu"],Types["trophy_pavouci_kral"],Types["trophy_pavouci_kralovna"], ],
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
		Graphics["rostlinkaZasazenaCesnek"], Graphics["rostlinkaZasazenaBavlna"], 0x3bb8, 0xf83, 0xf79
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
		Types["jeseter"], Types["sumec"], Types["kapr"], Types["zlataryba"], Types["stika"], Types["okoun"], Types["lin"], Types["candat"], Graphics["lviryby"], Graphics["letajiciryby"], Graphics["perletoveryby"], Graphics["uhor"]
	]
}

TrophyPrices = {
	"trophy_zmije": 60,
	"trophy_kobra": 80,
	"trophy_mamba": 120,
	"trophy_anakonda": 150,
	"trophy_obri_pavouk": 16,
	"trophy_desivy_pavouk": 100,
	"trophy_sklipkan": 40,
	"trophy_upiriho_pavouka": 200,
	"trophy_vtackar": 70,
	"trophy_snovac": 220,
	"trophy_cerna_vdova": 300,
	"trophy_tarantule": 1000,
	"trophy_vrrk": 35,
	"trophy_skret": 13,
	"trophy_aligator": 25,
	"trophy_jesterak": 12,
	"trophy_gorila": 25,
	"trophy_mephitis": 4900,
	"trophy_katakan": 6500,
	"trophy_parasekt": 5500,
	"trophy_zabi_matka": 2500,
	"trophy_druid": 3500,
	"trophy_dabel": 8500,
	"trophy_strazny_golem": 7500,
	"trophy_golem_strazce": 5500,
	"trophy_kuresekt": 3000,
	"trophy_kurekral": 3000,
	"trophy_minotaur": 9000,
	"trophy_vudce_lidozroutu": 6500,
	"trophy_pavouci_kral": 11000,
	"trophy_pavouci_kralovna": 1900,
}