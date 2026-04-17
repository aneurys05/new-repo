


const colors = ["blue", "green", "red", "yellow", "purple", "black", "brown", "orange"];
let count = 0; 

setInterval(changeBackground, 3000);

// function to change background color every 3 seconds
function changeBackground() {

document.body.style.backgroundColor = colors[count];

count = count == colors.length? 0 : count + 1; 


}