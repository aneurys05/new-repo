import {mercury, venus, earth, mars, jupiter, saturn, uranus, neptune} from './planets-info.js'


const planets = [{name: "Mercury", picture: "images/fjbeeRiPRQjQNhizwy7cWX-1024-80.jpg", description: mercury}, 
                 {name: "Venus", picture: "images/venus-mariner-10-pia23791-fig2.jpg", description: venus}, 
                 {name: "Earth", picture: "images/Meteosat-12-fci-march-equinox-2025-noon.jpg", description: earth}, 
                 {name: "Mars", picture: "images/C454F5A6-536E-4C9F-AA6AF354BB85A85B_source.jpg", description: mars}, 
                 {name: "Jupiter", picture: "images/Jupiter_OPAL_2024.png", description: jupiter}, 
                 {name: "Saturn", picture: "images/saturn.png", description: saturn}, 
                 {name: "Uranus", picture: "images/71aUHserTCL.jpg", description: uranus},
                 {name: "Neptune", picture: "images/Neptune_Full.jpg", description: neptune}];


let planetPic = document.getElementById("planet-pic");
let input = document.getElementById("planet-input");
let textContainer = document.getElementById("text-container");
let submitButton = document.getElementById("submit-button");

submitButton.addEventListener("click", addContent);

function addContent() {

planetPic.style.display = "block";
let value = input.value.charAt(0).toUpperCase() + input.value.slice(1)

switch (value) {

case "Mercury":
             filterContent(0);
             break;

case "Venus":
             filterContent(1);
             break;

case "Earth":
             filterContent(2);
             break;

case "Mars":
             filterContent(3);
             break;

case "Jupiter":
             filterContent(4);
             break;

case "Saturn":
             filterContent(5);
             break;

case "Uranus":
             filterContent(6);
             break;

case "Neptune":
             filterContent(7);
             break;


default:
         planetPic.style.display = "none";
         textContainer.textContent = `${input.value} is not a planet`;
}  

}

function filterContent(position) {

planetPic.src = planets[position].picture; 
textContainer.textContent = planets[position].description


}