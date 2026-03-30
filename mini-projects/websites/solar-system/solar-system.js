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
let submitButton = document.getElementById("submit-button");

console.log(submitButton);


