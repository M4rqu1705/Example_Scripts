const button = document.querySelector("button")! as HTMLButtonElement;
const input1 = document.getElementById("num1")! as HTMLInputElement;
const input2 = document.getElementById("num2")! as HTMLInputElement;
const output = document.getElementById("output")! as HTMLDivElement;

function add(num1: number, num2: number) {
    return num1 + num2;
}

button.addEventListener("click", () => {
    output.innerText = add(+input1.value, +input2.value).toString();
});