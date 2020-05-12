var x = 0;
var kc = 0;

data = [
    ['Coeficiente', '0', '0', '0', '0'],
    ['Especies', 'HA', 'H2O', 'H3O+', 'A-'],
    ['Inicio (M)', '1.00', '1.00', '0.00', '0.00'],
    ['Cambio (M)', '="-" + B1 + "x"', '=IFERROR(-ABS(B4), "-" + C1 + "x")', '=IFERROR(ABS(B4), "+" + D1 + "x")', '=IFERROR(ABS(B4), "+" + E1 + "x")'],
    ['Final (M)', '', '', '', '']
];

var table = jexcel(document.getElementById("table"), {
    data: data,
    columns:[
        {
            type: 'text',
            title: ' ',
            width: 100,
            readOnly: true
        },
        {
            type: 'text',
            title: 'Reactivo 1',
            width: 200,
            readOnly: false
        },
        {
            type: 'text',
            title: 'Reactivo 2',
            width: 200,
            readOnly: false
        },
        {
            type: 'text',
            title: 'Producto 1',
            width: 200,
            readOnly: false
        },
        {
            type: 'text',
            title: 'Producto 2',
            width: 200,
            readOnly: false
        },
    ],
    onchange: handler
});

function handler(instance, cell, col, row, val, id){
    if(row != 4){
        let initial = table.getLabelFromCoords(col, 2);
        let change = table.getLabelFromCoords(col, 3);
        if(String(change).search("x") + 1){
            let output = String(initial) + String(change);
            if(Number(initial) == 0){
                output = String(change);
            }
            table.setValueFromCoords(col, 4, output)
        } else{
            let output = Number(initial) + Number(change);
            table.setValueFromCoords(col, 4, output)
        }
    }
}

function updateX() {
    x = document.getElementById("x-input").value;
    if (x === "") {
        table.setValue("B4", '="-" + B1 + "x"');
        table.setValue("C4", '="-" + C1 + "x"');
        table.setValue("D4", '="+" + D1 + "x"');
        table.setValue("E4", '="+" + E1 + "x"');
    } else {
        table.setValue("B4", String(-x));
        table.setValue("C4", String(-x));
        table.setValue("D4", String(x));
        table.setValue("E4", String(x));
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


for(let i = 1; i < 5; i++){
    table.setValueFromCoords(i, 0, "1");
}