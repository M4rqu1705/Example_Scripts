var summaryTag = document.querySelector("#summary");

/* Object blueprints */
function Item(name, price, image){
  this.name = name;
  this.price = price.toFixed(2);
  this.image = image
  this.wasSelected = false;
}

function Summary(items, onlinefee, tax){
  this.items = Object.values(items);
  this.subtotal = 0;

  for(index in items){
    this.subtotal += parseFloat(items[index].price);
  };

  this.onlinefee = onlinefee;
  this.tax = tax * this.subtotal;
  this.total = this.subtotal + this.tax + this.onlinefee;

  this.message = "";

  for(index in items){
    this.message += "\t" + items[index].name.toUpperCase() + ": $" + items[index].price.toString() + "\n";
  };

  this.message += "Subtotal: $" + this.subtotal.toFixed(2) + "\n";
  this.message += "Online Fee: $" + this.onlinefee.toFixed(2) + "\n";
  this.message += "Tax: $" + this.tax.toFixed(2) + "\n";
  this.message += "Total: $" + this.total.toFixed(2) + "\n";
}

/* Instantiation */
var items = {
  "latte": new Item("Latte", 2, null),
  "espresso": new Item("Espresso", 1.5, null),
  "mochacchino": new Item("Mochacchinno", 3, null),
  "cappuccino": new Item("Cappuccino", 2.5, null),
  "small": new Item("Pequeño 8oz", 0, "images/cup.jpg"),
  "medium": new Item("Mediano 12oz", 1.25, "images/cup.jpg"),
  "large": new Item("Grande 16oz", 2, "images/cup.jpg"),
  "whole-milk": new Item("Whole Milk", 0, "images/wholemilk.png"),
  "lactose-free": new Item("Lactose Free", 0.5, "images/lactose-free.jpeg"),
  "almond-milk": new Item("Almond Milk", 1.25, "images/almond-milk.jpg"),
  "oat-milk": new Item("Oat Milk", 2, "images/oatmilk.png"),
  "none": new Item("NO Whipped Cream", 0, "images/none.png"),
  "whipped-cream": new Item("Whipped Cream", 0.25, "images/whip-cream.jpeg"),
  "choco-whipped-cream": new Item("Chocolate Whipped Cream", 0.5, "images/choco-whip-cream.jpg")
}
var selectedItems = {}

function fill_website(){
  Object.keys(items).forEach((key) => {
    itemTag = document.getElementById(key);
    element = items[key]

    if(element.image != null){
      // Image child
      itemTag.querySelector("img").src = element.image;
    }

    // Item-title child
    itemTag.querySelector(".item-title").innerHTML = element.name;
    // Price child
    itemTag.querySelector(".price").innerHTML = "$" + element.price.toString();

    itemTag.addEventListener('click', function(){
      items[key].wasSelected = !items[key].wasSelected;

      if(items[key].wasSelected){
        document.getElementById(key).style.backgroundColor = "#2ecc71";
        selectedItems[key] = items[key];
        summary = new Summary(selectedItems, 0.25, 0.115)
        summaryTag.innerHTML = summary.message;
      } else{
        document.getElementById(key).style.backgroundColor = "#ecf0f1";
        delete selectedItems[key]
        summary = new Summary(selectedItems, 0.25, 0.115)
        summaryTag.innerHTML = summary.message;
      }
    });

  });

}

fill_website();
