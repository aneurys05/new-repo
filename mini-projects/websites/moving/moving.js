let container = document.getElementById("container");
let up = 120;
let left = 80;
let speed = 5;
let selection = document.getElementById("speed-selection");
let button = document.querySelector("button");
console.log(button);



document.body.addEventListener("keydown", handleEvent)


function handleEvent(event) {

switch (event.key){

case "ArrowDown":
      up += speed;
      container.style.top = `${up}px`;
      break;

case "ArrowUp":
      up -= speed;
      container.style.top = `${up}px`;
      break;

case "ArrowRight":
      left += speed;
      container.style.left = `${left}px`;
      break;

case "ArrowLeft":
      left -= speed;
      container.style.left = `${left}px`;
      break;

}


}

button.addEventListener("click", ()=> {

switch (selection.value){

case "Fast":
      speed = 10;
      break;
case "Slow":
      speed = 1;
      break;
default:
       speed = 5;

}
})