/* Important tags */ 
var teamAScoreTag = document.querySelector("#team-a-score");
var teamBScoreTag = document.querySelector("#team-b-score");
var maxScoreTag = document.querySelector("#max-score > input");
var teamABox = document.querySelector("#team-a");
var teamBBox = document.querySelector("#team-b");
var resetButtonTag = document.querySelector("button[name='reset']");

/* Variable initialization */
var maxScore = 0;
var teamAScore = 0;
var teamBScore = 0;
var winnerDetermined = false;

teamAScoreTag.innerHTML = teamAScore;
teamBScoreTag.innerHTML = teamBScore; 

/* Event Listeners */ 

// Be wary of any changes to max score input and update variable accordingly
maxScoreTag.addEventListener('change', function(){
  maxScore = maxScoreTag.value;
  maxScore = parseInt(maxScore);
});
resetButtonTag.addEventListener('click', function(){
  maxScoreTag.value = 0;
  teamAScore = 0;
  teamBScore = 0;
  teamAScoreTag.innerHTML = teamAScore;
  teamBScoreTag.innerHTML = teamBScore; 
  teamABox.style.backgroundColor = "#f39c12";
  teamBBox.style.backgroundColor = "#f39c12";
  winnerDetermined = false;
});

// Receive clicks and increment each of the team's points one by one. Also check if anybody won
teamABox.addEventListener('click', function(){
  if(winnerDetermined != true){
    teamAScore++;
    teamAScoreTag.innerHTML = teamAScore;
  }

  if(maxScore != 0 && teamAScore == maxScore){
    // alert("Team B won!");
    teamABox.style.backgroundColor = "#27ae60";
    teamBBox.style.backgroundColor = "#e74c3c";
    winnerDetermined = true;
  }

  if(maxScore != 0 && teamAScore > maxScore){
    teamAScore--;
    teamAScoreTag.innerHTML = teamAScore;
  }
});


teamBBox.addEventListener('click', function(){
  if(winnerDetermined != true){
    teamBScore++;
    teamBScoreTag.innerHTML = teamBScore;
  }

  if(maxScore != 0 && teamBScore == maxScore){
    // alert("Team B won!");
    teamBBox.style.backgroundColor = "#27ae60";
    teamABox.style.backgroundColor = "#e74c3c";
    winnerDetermined = true;
  }

});
