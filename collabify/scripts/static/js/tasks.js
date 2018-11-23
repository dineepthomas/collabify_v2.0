var myLowTasks = new Array();
var myMediumTasks = new Array();
var myHighTasks = new Array();

var totalLowTasksMade = 1;
var totalMedTasksMade = 1;
var totalHighTasksMade = 1;

//not really sure if this is necessary
function LowPrioTaskMachine(id){
  $( "#dragL0" ).clone()
		.attr("id", id)
		.css({"display": "block"})
		.appendTo( "#clonehere");

}

function functionName(){
  console.log("This workss.");
}

//task variables
var task ={
  name: "taskName",
  percentage: 0,
  priority: 0,
  assigned: "worker",
  id: 0,
  date: 000000,
  catagory: null
} ;

//create task
function Task(name, percent, prio, assigned){
  this.name = name;
  this.percentage = percent;
  this.priority = prio;
  this.assigned = assigned;
  this.date = Date.now();

  this.catagory = null;
  
  if(prio == 0){
    myLowTasks.push(this);
    writeLowUserTask(percent, name);
    this.id = "dragL" + totalLowTasksMade;
	totalLowTasksMade++;
  } else if (prio == 1) {
    myMediumTasks.push(this);
    //writeMedUserTask(this.percentage, this.name);
    this.id = "dragM" + totalMedTasksMade;
	totalMedTasksMade++;
  } else {
    myHighTasks.push(this);
    //writeHighUserTask(this.percentage, this.name);
    this.id = "dragH" + totalHighTasksMade;
	totalHighTasksMade++;
  }
}

//display tasks
function displayLowTask(task){
  console.log(task.id);
  var d = new Date(task.date); //reads miliseconds to dates

  $( "#" + task.id + " #lowHeader button" ).attr("id", "delete-"+task.id);
  $( "#" + task.id + " #lowHeader a" ).attr("id", "show-"+task.id);
  $( "#" + task.id + " #collapseLow0 div button" ).attr("id", "complete-"+task.id);
  $( "#" + task.id + " #collapseLow0 #Bar" ).attr("id", "Bar"+task.id);
  $( "#" + task.id + " #collapseLow0").attr("id", "collapse"+task.id);

  $( "#" + task.id + " #lowHeader h1" )
    .html("<strong>" + task.name + "</strong>");
  $( "#" + task.id + " #Bar"+task.id ).css({"width": parseInt(task.percentage) + "%"});
  $( "#" + task.id + " #Bar"+task.id )
    .html(task.percentage + "%");
  $( "#" + task.id + " #lowFooter h5" )
    .html("<strong>" + task.assigned + "</strong>  " + d.toDateString() );
 }

 function move(id) {
  var parsedID = id.slice(13); //seperates ID into usable parts
  var parsedPrio = parsedID.slice(0,1);
  var parsedIDNum = parsedID.slice(1);

  var elem = document.getElementById("Bardrag"+parsedID);
  if(elem.textContent.slice(1,2) == '%'){
    var width = elem.textContent.slice(0,1);

    var ids = setInterval(frame, 10);

    function frame() {
      if (width >= 100) { //ending width
        clearInterval(ids);
      } else {
        width++; 
        elem.style.width = width + '%'; 
        elem.innerHTML = width * 1  + '%';
      }
    }
  } else {
    if(elem.textContent != "100%" && elem.textContent != "0%"){
      var width = elem.textContent.slice(0,2); //starting width

      var ids = setInterval(frame, 10);
      function frame() {
        if (width >= 100) { //ending width
          clearInterval(ids);
        } else {
          width++; 
          elem.style.width = width + '%'; 
          elem.innerHTML = width * 1  + '%';
        }
      }
    } else if (elem.textContent == "0%"){
      var width = elem.textContent.slice(0,1); 

      var ids = setInterval(frame, 10);
      function frame() {
        if (width >= 100) { //ending width
          clearInterval(ids);
        } else {
          width++; 
          elem.style.width = width + '%'; 
          elem.innerHTML = width * 1  + '%';
        }
      }
    }
  }
}

//writes to database--need to update this
 function writeLowUserTask(LowTaskCompleted, LowTaskName) {
  
}