var epsilon = 0;

var root = new Vue({
	el: "#root",
	data: {
		coefficients: [1, 0, 1, 1],
		x: "x",
		kc: 0,
		table: [
			[
				{ id: -1, content: "Inicio", isReadOnly: true },
				{ id: 0, content: "1.00", isReadOnly: false },
				{ id: 1, content: "1.00", isReadOnly: false },
				{ id: 2, content: "0.00", isReadOnly: false },
				{ id: 3, content: "0.00", isReadOnly: false }
			],
			[
				{ id: 9, content: "Cambio", isReadOnly: true },
				{ id: 10, content: "-x", isReadOnly: false },
				{ id: 11, content: "0", isReadOnly: false },
				{ id: 12, content: "+x", isReadOnly: false },
				{ id: 13, content: "+x", isReadOnly: false }
			],
			[
				{ id: 19, content: "Equilibrio", isReadOnly: true },
				{ id: 20, content: "1.00 - x", isReadOnly: false },
				{ id: 21, content: "1.00", isReadOnly: false },
				{ id: 22, content: "x", isReadOnly: false },
				{ id: 23, content: "x", isReadOnly: false }
			]
		]
	},
	methods: {
		updateSecondRow: function (action) {
			if (action === "a") {
				// If x is a variable
				if (!String(this.x).match(/[A-DF-Za-df-z]/g)) {
					action = "f";
				} else {
					action = "s";
				}
			}

			if (action === "s") {
				for (let i = 0; i < this.coefficients.length; i++) {
					let prefix = i == 0 || i == 1 ? "-" : "+";

					if (
						this.coefficients[i] > 1 ||
						(0 < this.coefficients[i] && this.coefficients[i] < 1)
					) {
						this.table[1][i + 1].content =
							prefix + String(this.coefficients[i]) + String(this.x);
					} else if (this.coefficients[i] === 1) {
						this.table[1][i + 1].content = prefix + String(this.x);
					} else if (this.coefficients[i] === 0) {
						this.table[1][i + 1].content = 0;
					}
				}
			} else if (action === "f") {
				for (let i = 0; i < this.coefficients.length; i++) {
					let prefix = i == 0 || i == 1 ? -1 : 1;
					this.table[1][i + 1].content = prefix * this.coefficients[i] * this.x;
				}
			}
		},
		updateThirdRow: function (id, type) {
			let column = parseInt(String(id)[String(id).length - 1]);

			let beginning_id = column;
			let change_id = parseInt("1" + String(column));
			let equilibrium_id = parseInt("2" + String(column));

			let beginning_cell = this.table[0][column + 1];
			let change_cell = this.table[1][column + 1];
			let equilibrium_cell = this.table[2][column + 1];

			if (type === "a") {
				// If change does not have variables
				if (!String(change_cell.content).match(/[A-DF-Za-df-z]/g)) {
					type = "f";
				} else {
					type = "s";
				}
			}

			// If type is string
			if (type === "s") {
				console.log("Using String");
				// First two columns substract
				if (column === 0 || column === 1) {
					if (parseFloat(beginning_cell.content) === 0) {
						equilibrium_cell.content = " - " + change_cell.content.trim().slice(1).trim();
					} else {
						equilibrium_cell.content =
							String(beginning_cell.content).trim() +
							" - " +
							change_cell.content.trim().slice(1);
					}

					// Second two columns add
				} else {
					if (parseFloat(beginning_cell.content) === 0) {
						equilibrium_cell.content = " + " + change_cell.content.trim().slice(1);
					} else {
						equilibrium_cell.content =
							String(beginning_cell.content).trim() +
							" + " +
							change_cell.content.trim().slice(1);
					}
				}

				// If x is purely a number
			} else if (type === "f") {
				console.log("Using Float");

				// First two columns substract
				if (column === 0 || column === 1) {
					equilibrium_cell.content =
						parseFloat(beginning_cell.content) -
						Math.abs(parseFloat(change_cell.content));
					// Second two columns add
				} else {
					equilibrium_cell.content =
						parseFloat(beginning_cell.content) +
						Math.abs(parseFloat(change_cell.content));
				}
			}
		},
		updateCol: function (id) {
			let column = parseInt(String(id)[String(id).length - 1]);

			let beginning_id = column;
			let change_id = parseInt("1" + String(column));
			let equilibrium_id = parseInt("2" + String(column));

			let beginning_cell = this.table[0][column + 1];
			let change_cell = this.table[1][column + 1];
			let equilibrium_cell = this.table[2][column + 1];

			// First row
			if (id < 10) {
				// If it is not scientific notation, reformat
				if (beginning_cell.content.toLowerCase().search("e") == -1) {
					beginning_cell.content = String(
						parseFloat(beginning_cell.content).toFixed(2)
					);
				}

				if (String(change_cell.content).match(/[A-Za-z]/g)) {
					// If x contains variables
					this.updateThirdRow(id, "s");
				} else {
					// If x is purely a number
					this.updateThirdRow(id, "f");
				}

				// Second row
			} else if (id < 20) {
				// If the cell contains variables
				if (change_cell.content.match(/[A-Za-z]/g)) {
					change_cell.content = this.coefficients[column] * this.x;

					// Add corresponding sign if different from 0
					if (change_cell.content == 0) {
						if (column == 0 || column == 1) {
							change_cell.content = "-" + change_cell.content;
						} else {
							change_cell.content = "+" + change_cell.content;
						}
					}

					this.updateThirdRow(id, "s");

					// If the cell is purely a number
				} else {
					// this.x = parseFloat(change_cell.content) / this.coefficient;
					this.updateThirdRow(id, "f");
				}

				// Third row
			} else if (id < 30) {
				// There is only a number inside the equilibrium cell and beginning cell
				if (
					!equilibrium_cell.content.match(/[A-Za-z]/g) &&
					!beginning_cell.content.match(/[A-Za-z]/g)
				) {
					if (column == 0 || column == 1) {
						this.x =
							(parseFloat(beginning_cell.content) -
								parseFloat(equilibrium_cell.content)) /
							this.coefficients[column];
					} else {
						this.x =
							(parseFloat(equilibrium_cell.content) -
								parseFloat(beginning_cell.content)) /
							this.coefficients[column];
					}

					// change_cell.content = this.coefficients[column] * this.x;

					// There is text inside the equilibrium cell
				} else if (equilibrium_cell.content.match(/[A-Za-z]/g)) {
					this.x = "x";
					// There is a float inside the equilibrium cell
				} else {
				}
			}
		},
		formatKc: function () {
			if (this.kc === "") {
				this.kc = 0;
			} else {
				this.kc = Math.abs(parseFloat(this.kc));
			}
		},
		findX: function () {
			let url = "https://www.symbolab.com/solver/step-by-step/";
			let A = this.table[2][1].content;
			let B = this.table[2][2].content;
			let D = this.table[2][3].content;
			let E = this.table[2][4].content;
			let a = this.coefficients[0];
			let b = this.coefficients[1];
			let d = this.coefficients[2];
			let e = this.coefficients[3];


            function validate(a, A){
                if(a === "" || A === ""){
                    a = 1;
                    A = 0;
                } else if(String(A).trim().startsWith("+")){
                    A = String(A).trim().slice(1);
                }

                return [a, A]
            }

            [a, A] = validate(a, A);
            [b, B] = validate(b, B);
            [d, D] = validate(d, D);
            [e, E] = validate(e, E);

			let kc = String(this.kc).trim().toUpperCase();

			let formula = `\\frac{(${D})^${d}(${E})^${e}}{(${A})^${a}(${B})^${b}} = ${kc}`;
			url = encodeURI(url + formula);
            console.log(formula);
			// window.open(url, "_blank");
		}
	},
	watch: {
		x: function () {
			if (String(this.x).length > 0 && String(this.x).match(/[A-DF-Za-df-z]/g)) {
				// If 1 letter other than e is inserted
				this.x = "x";

				// Update
				this.updateSecondRow("s");
				for (let i = 0; i < 4; i++) {
					this.updateThirdRow(i, "s");
				}
			} else if (
				String(this.x).length > 7 &&
				String(this.x).match(/[0-9Ee\.-]/g)
			) {
				// If x is float with length greater than 7
				this.x = Math.abs(parseFloat(this.x)) + epsilon;
				for (let i = 0; i < 4; i++) {
					this.updateThirdRow(0, "f");
				}
			} else if (this.x === NaN) {
				// If x is NaN
				this.x = "x";
			} else if (String(this.x).match(/[0-9Ee\.-]/g)) {
				if (this.x < 0) {
					this.x = -this.x;
				}
				// If x is float
				this.updateSecondRow("f");
				for (let i = 0; i < 4; i++) {
					this.updateThirdRow(i, "f");
				}
			}
		},
		coefficients: function () {
			for (let i = 0; i < this.coefficients.length; i++) {
				this.coefficients[i] = Math.round(this.coefficients[i] * 10) / 10;
			}

			this.updateSecondRow("a");
			for (let i = 0; i < this.coefficients.length; i++) {
				this.updateThirdRow(i, "a");
			}
		}
	}
});
