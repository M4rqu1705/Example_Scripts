var x = 0;
var kc = 0;

data = [
    ['Coeficiente', '1', '1', '1', '1'],
    ['', 'HA', 'H2O', 'H3O+', 'A-'],
    ['Inicio (M)', '1.00', '1.00', '0.00', '0.00'],
    ['Cambio (M)', '="-" + B1 + "x"', '=IFERROR(-ABS(B4), "-" + C1 + "x")', '=IFERROR(ABS(B4), "--" + D1 + "x")', '=IFERROR(ABS(B4), "--" + E1 + "x")'],
    ['Final (M)', '=B3 + B4', '=C3 + C4', '=D3 + D4', '=E3 + E4']
];

var table = jexcel(document.getElementById("table"), {
    data: data,
    colWidths: [100, 200, 200, 200, 200]
});

function updateX() {
    x = document.getElementById("x-input").value;
    if (x === "") {
        table.setValue("B4", '="-" + B1 + "x"', true);
        table.setValue("C4", '="-" + C1 + "x"', true);
        table.setValue("D4", '="--" + D1 + "x"', true);
        table.setValue("E4", '="--" + E1 + "x"', true);
    } else {
        table.setValue("B4", String(-x), true);
        table.setValue("C4", String(-x), true);
        table.setValue("D4", String(x), true);
        table.setValue("E4", String(x), true);
    }
}


function updateKc() {
    kc = document.getElementById("kc-input").value;
}


function processTable() {
  
    let url = "https://www.symbolab.com/solver/step-by-step/";
    let A = table.getLabel("B5");
    let B = table.getLabel("C5");
    let D = table.getLabel("D5");
    let E = table.getLabel("E5");
    let a = table.getLabel("B1");
    let b = table.getLabel("C1");
    let d = table.getLabel("D1");
    let e = table.getLabel("E1");
  
    if (a === "" || A === "") {
        a = 1;
        a = 1;
    }
    if (b === "" || B === "") {
        b = 1;
        B = 1;
    }
    if (d === "" || D === "") {
        d = 1;
        D = 1;
    }
    if (e === "" || E === "") {
        e = 1;
        E = 1;
    }
  
    let formula = `\\frac{(${D})^${d}(${E})^${e}}{(${A})^${a}(${B})^${b}} = ${kc}`;
    url = encodeURI(url + formula);
    window.open(url, '_blank');
}


// EVENT LISTENERS
document.getElementById("x-input").addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("find-x").click();
  }
});

document.getElementById("kc-input").addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("find-x").click();
  }
});