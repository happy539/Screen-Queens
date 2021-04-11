//Variables
var optionA = 0;
var optionB = 0;
var optionC = 0;
var optionD = 0;
var Score = 0;

var restart = document.getElementById("restart");
var submit = document.getElementById("submit");
var result = document.getElementById("result");
var start = document.getElementById("start");
var learnMore = document.getElementById("learnMore");
var goUp = document.getElementById("goUp");

var q1a1 = document.getElementById("q1a1");
var q1a2 = document.getElementById("q1a2");
var q1a3 = document.getElementById("q1a3");
var q1a4 = document.getElementById("q1a4");

var q2a1 = document.getElementById("q2a1");
var q2a2 = document.getElementById("q2a2");
var q2a3 = document.getElementById("q2a3");
var q2a4 = document.getElementById("q2a4");

var q3a1 = document.getElementById("q3a1");
var q3a2 = document.getElementById("q3a2");
var q3a3 = document.getElementById("q3a3");
var q3a4 = document.getElementById("q3a4");

var q4a1 = document.getElementById("q4a1");
var q4a2 = document.getElementById("q4a2");
var q4a3 = document.getElementById("q4a3");
var q4a4 = document.getElementById("q4a4");

var q5a1 = document.getElementById("q5a1");
var q5a2 = document.getElementById("q5a2");
var q5a3 = document.getElementById("q5a3");
var q5a4 = document.getElementById("q5a4");

//Functions

function re_start(){
  location.reload();
  window.scrollTo(0,0);
}

function sub_mit(){
  //Scoring 
  if (q1a1.checked) {
    Score += 1;
  }
  if (q2a4.checked){
    Score +=1;
  }
  if (q3a4.checked){
    Score +=1;
  }
  if (q4a2.checked){
    Score +=1;
  }
  if (q5a3.checked){
    Score +=1;
  }
}

function re_sult(){
  if (Score == 0){
    result.innerHTML = "0/5  Try again for a better score!";
  }
  else if (Score == 1){
    result.innerHTML = "1/5  Try again for a better score!";
  }
  else if (Score == 2){
    result.innerHTML = "2/5  Keep trying for a better score!";
  }
  else if (Score == 3){
    result.innerHTML = "3/5  Keep trying for a better score!";
  }
  else if (Score == 4){
    result.innerHTML = "4/5  Keep trying for a better score!";
  }
  else if (Score == 5){
    result.innerHTML = "5/5  Wow! You are an expert about these actresses!";
  }
}

function st_art(){
  window.scrollTo(950,750);
}

function scroll_Down(){
  window.scrollTo(250,800);
}

function scroll_Up(){
  window.scrollTo(0,100);
}


//Event Listeners for buttons
restart.addEventListener("click",re_start);
submit.addEventListener("click",sub_mit);
submit.addEventListener("click",re_sult);
start.addEventListener("click",st_art);
learnMore.addEventListener("click",scroll_Down);
goUp.addEventListener("click",scroll_Up);