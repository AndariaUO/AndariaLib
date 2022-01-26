let macros = document.querySelector("#wiki-body").querySelector(".markdown-body");

let names = macros.querySelectorAll("h3");

function getRandomInt(max) {
	return Math.floor(Math.random() * max);
}

let parsedMacros = [];
let first = true;
names.forEach((name) => {
	if (first === false) {
		return;
	}

	let macro = {
		name: name.innerText,
		description: "",
		args: [],
	}

	let isDescription = false;
	let isSameMacro = false;
	let isArgs = false;
	let isSignature = false;
	let isEnd = false;
	name.parentElement.querySelectorAll("p,h3,h4,ul,h2").forEach((p) => {
		if (isEnd) {
			return;
		}

		if (p.innerHTML.includes("Types") && p.tagName.toLowerCase() === "h2") {
			isEnd = true;
			isSameMacro = false;
			return;
		}

		if (p.innerText.includes("Description:")) {
			isDescription = true;
			return;
		}

		if (p.innerText === macro.name && !isSameMacro) {
			isSameMacro = true;
			return;
		}

		if (p.innerText.includes("Parameters")) {
			isArgs = true;
			return;
		}

		if (p.innerText.includes("Method Signature:")) {
			isSignature = true;
			return;
		}

		if (isSameMacro && isSignature) {
			let sig = p.innerText.split("(");
			if (sig.length <= 1) {
				isSignature = false;
				return;
			}

			let signature = sig[1].split(",");
			if (signature.length === 1 && signature[0] === ")") {
				isSignature = false;
				return;
			}

			signature.forEach((type, key) => {
				// console.log(type, key);
				let arg = {
					name: "",
					value: "not documented",
					type: ""
				};

				if (type.includes("Int32")) {
					arg.type = "int";
					arg.name = "int" + getRandomInt(10);
				}

				if (type.includes("System.Object")) {
					arg.type = "";
					arg.name = "obj" + getRandomInt(10);
				}

				if (type.includes("Boolean")) {
					arg.type = "bool";
					arg.name = "bool" + getRandomInt(10);
				}

				if (type.includes("System.String")) {
					arg.type = "str";
					arg.name = "str" + getRandomInt(10);
				}

				macro.args[key] = arg;
			});
			// console.log(p);
			isSignature = false;
		}

		if (isSameMacro && isArgs && p.tagName.toLowerCase() === "ul") {
			console.log(p, macro.name);
			p.querySelectorAll("li").forEach((arg, key) => {
				let argName = arg.innerText.split(":")[0];
				let argValue = arg.innerText.split(":")[1];

				// console.log(argName, argValue, macro.name);
				macro.args[key].name = argName;
				macro.args[key].value = argValue;
			});
			isArgs = false;
		}

		if (isDescription && isSameMacro) {
			macro.description = p.innerText;
			isDescription = false;
		}

		if (p.innerText.includes("Example:")) {
			isSameMacro = false;
		}
	})

	// first = false;
	parsedMacros.push(macro);
	// console.log(macro, "after push");
});

console.log(parsedMacros);


parsedMacros.forEach((macro) => {
	// return;
	let def = "def " + macro.name + "(";
	let first = true;
	macro.args.forEach((arg) => {
		def += (first ? "" : ", " ) + arg.name + (arg.type !== "" ? ": " + arg.type : "");
		first = false;
	});

	def += "):"

	// """
	//     Plays the given macro name
	//     :param name: Macro name.
	//     """
	//     pass

	console.log(def);
	console.log("    \"\"\"");
	console.log("    " + macro.description);
	macro.args.forEach((arg) => {
		console.log("    :param " + arg.name + ": " + arg.value);
	});
	console.log("    \"\"\"");
	console.log("    pass");
	console.log("");
	console.log("");
});