let gamePattern = [];
let userClickedPattern = [];
let level = 0;

// Start the game on keypress
$(document).keypress(function () {
  if (level === 0) {
    nextSequence();
  }
});

// Handle button clicks
$(".btn").click(function () {
  const userChosenColor = $(this).attr("id");
  userClickedPattern.push(userChosenColor);

  playSound(userChosenColor);
  animatePress(userChosenColor);

  // Check the user's answer
  checkAnswer(userClickedPattern.length - 1);
});

// Function to check the user's answer
function checkAnswer(currentLevel) {
  if (userClickedPattern[currentLevel] === gamePattern[currentLevel]) {
    // If user completed the sequence, move to next level
    if (userClickedPattern.length === gamePattern.length) {
      setTimeout(nextSequence, 1000);
    }
  } else {
    // If user clicks the wrong color
    gameOver();
  }
}

// Function to generate the next sequence
function nextSequence() {
  userClickedPattern = []; // Reset user input for the new level
  level++;
  $("#level-title").text("Level " + level);

  // Add a new random color to the game sequence
  const randomNumber = Math.floor(Math.random() * 4);
  const randomChosenColor = ["green", "red", "yellow", "blue"][randomNumber];
  gamePattern.push(randomChosenColor);

  // Flash the chosen button and play its sound
  $("#" + randomChosenColor)
    .fadeOut(100)
    .fadeIn(100);
  playSound(randomChosenColor);
}

// Function to play sound
function playSound(name) {
  const audio = new Audio("sounds/" + name + ".mp3");
  audio.play();
}

// Function to animate button press
function animatePress(currentColor) {
  $("#" + currentColor).addClass("pressed");
  setTimeout(function () {
    $("#" + currentColor).removeClass("pressed");
  }, 100);
}

// Function to handle game over
function gameOver() {
  playSound("wrong");
  $("body").addClass("game-over");
  $("#level-title").text("Game Over, Press Any Key to Restart");

  setTimeout(function () {
    $("body").removeClass("game-over");
  }, 200);

  startOver();
}

// Function to reset game variables
function startOver() {
  level = 0;
  gamePattern = [];
  userClickedPattern = [];
}
