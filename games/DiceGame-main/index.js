//First dice
var randomNumber1 = Math.floor(Math.random()*6)+1; //random number between 1-6
var diceNumber = "images/dice" + randomNumber1 + ".png"; //sets a source to images randomly

var dice1 = document.querySelector(".img1");
dice1.setAttribute("src", diceNumber); //Changes attribute src to link to our random dice image

//Second dice
var randomNumber2 = Math.floor(Math.random()*6)+1;
var diceNumber2 = "images/dice" + randomNumber2 + ".png";

var dice2 = document.querySelector(".img2");
dice2.setAttribute("src", diceNumber2);

//Changing the heading
if (randomNumber1 > randomNumber2) {
    document.querySelector("h1").innerHTML = "Player 1 wins!";
} else {
    document.querySelector("h1").innerHTML = "Player 2 wins!";
}