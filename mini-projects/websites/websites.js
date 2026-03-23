


let items = document.querySelectorAll(".item");

let counter = {

facebook: 1,
youtube: 1,
wikipedia: 1, 
youtube: 1,
instagram: 1,
amazon: 1

}

items.forEach( element => {

element.addEventListener("click", clickedElement => {

if (counter[clickedElement.target.id] == 1) { 

let newElement = document.createElement("p");
newElement.textContent = `You visited ${clickedElement.target.id}!`
newElement.classList.add("visited");
newElement.id = `my${clickedElement.target.id}`
document.body.append(newElement);
document.body.append(newElement);
counter[clickedElement.target.id] += 1; 

}else {

let changeText = document.getElementById(`my${clickedElement.target.id}`);
changeText.textContent = `You visited ${clickedElement.target.id} ${counter[clickedElement.target.id]} times!`
counter[clickedElement.target.id] += 1; 

}

}

);

} );