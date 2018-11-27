var myLowTasks = new Array();
var myMediumTasks = new Array();
var myHighTasks = new Array();

var totalLowTasksMade = 1;
var totalMedTasksMade = 1;
var totalHighTasksMade = 1;

//Clones and places card in clonehere
function LowPrioTaskMachine(id){
  $( "#taskCard" ).clone()
		.attr("id", id)
		.css({"display": "block"})
		.appendTo( "#clonehere");
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

//task attributes
function Task(name, percent, prio, assigned){
  this.name = name;
  this.percentage = percent;
  this.priority = prio;
  this.assigned = assigned;
  this.date = Date.now();

  this.catagory = null;
  if(prio == 0){
    myLowTasks.push(this);
    this.id = "dragL" + totalLowTasksMade;
	totalLowTasksMade++;
  } else if (prio == 1) {
    myMediumTasks.push(this);
    writeMedUserTask(this.percentage, this.name);
    this.id = "dragM" + totalMedTasksMade;
	totalMedTasksMade++;
  } else {
    myHighTasks.push(this);
    writeHighUserTask(this.percentage, this.name);
    this.id = "dragH" + totalHighTasksMade;
	totalHighTasksMade++;
  }
}

//display tasks
function displayLowTask(task){
  var d = new Date(task.date); //reads miliseconds to dates
  $( "#" + task.id + " #taskHeader button" ).attr("id", "delete-"+task.id);
  $( "#" + task.id + " #taskHeader a" ).attr("id", "show-"+task.id);
  $( "#" + task.id + " #collapseTask div button" ).attr("id", "complete-"+task.id);
  $( "#" + task.id + " #collapseTask #taskPercent" ).attr("id", "taskPercent"+task.id);
  $( "#" + task.id + " #collapseTask").attr("id", "collapse"+task.id);

  $( "#" + task.id + " #taskHeader h1" )
    .html("<strong>" + task.name + "</strong>");
  $( "#" + task.id + " #taskPercent"+task.id ).css({"width": parseInt(task.percentage) + "%"});
  $( "#" + task.id + " #taskPercent"+task.id )
    .html(task.percentage + "%");
  $( "#" + task.id + " #taskFooter h5" )
    .html("<strong>" + task.assigned + "</strong>  " + d.toDateString() );
 }

//Supposed to show the progress bar animation for finishing a task
//but it somehow doesn't work with our code
 function move(id) {
  var parsedID = id.slice(13); //seperates ID into usable parts
  var parsedPrio = parsedID.slice(0,1);
  var parsedIDNum = parsedID.slice(1);
    console.log("parsedID: " + parsedID+"");
  console.log("parsedprio: " + parsedPrio+"");
  console.log("parsedIDNum: " + parsedIDNum+"");
  var elem = document.getElementById("Bardrag"+parsedID);
  console.log("at least this works");
  console.log(elem);
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
//Shows or hides card on call
function show_hide(id) {
  var deletionCheck = id.slice(0,1);
  //redundant but possibly useful in future
  if(deletionCheck == "d"){
    var parsedShowID = id.slice(5);
    console.log(parsedShowID);
  } else {
    var parsedShowID = id.slice(5);
    console.log(parsedShowID);
  }  
    
  dv = document.getElementById("collapse" + parsedShowID);
  ele = document.getElementById(id);

  if (dv.style.display ==  '')
    { 
      dv.style.display = 'none'; 
      ele.innerHTML = "Show";
    }
    else
    {
      dv.style.display = ''; 
      ele.innerHTML = "Hide";
    }
}


//task movability functions

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
/*
  var _target = $("#" + ev.target.id);
  var data = ev.dataTransfer.getData("text");
  if ($(_target).hasClass("noDrop")) {
    console.log("no transfer");
    ev.preventDefault();
  } else {
    ev.preventDefault();
    ev.target.appendChild(document.getElementById(data));
  }*/

}

$(function() {
  var dialog, 
    form,
    name = $( "#taskName" ),
    priority = $( "#priorityLevel" ),
    percentage = $( "#percentageDone" ),
    assigned = $( "#assignedTo" ),
    allFields = $( [] ).add( name ).add( percentage ).add( priority ).add( assigned ),
    tips = $( ".validateTips" );

  var radios = document.getElementsByName('priorityLevel');
  for (var i = 0, length = radios.length; i < length; i++){
    if (radios[i].checked) {
      priority = radios[i].value;
      break;
    }
  }

  function updateTips( t ) { 
    tips.text( t ).addClass( "ui-state-highlight" );
    setTimeout(function() {
      tips.removeClass( "ui-state-highlight", 1500 );
    }, 500 );
  }
  
  function checkLength( o, n, min, max ) {
    if ( o.val().length > max || o.val().length < min ) {
      o.addClass( "ui-state-error" );
      updateTips( "Length of " + n + " must be between " +
        min + " and " + max + " characters." );
      return false;
    } else {
      return true;
    }
  }
  //Used to check the correctness of the forms in task creation form
  function checkRegexp( o, regexp, n ) {
    if ( !( regexp.test( o.val() ) ) ) {
      o.addClass( "ui-state-error" );
      updateTips( n );
      return false;
    } else {
      return true;
    }
  }
  //doesn't get called at all. Need to look into this
  function addTask() {
    console.log("called add task");
    var createdTask = new Task(name.val(), percentage.val(), priority, assigned.val());
      if(priority == 0){
        var newTask = LowPrioTaskMachine(createdTask.id);
        displayLowTask(createdTask);
        console.log("priority=0");
      } else if (priority == 1) {
        var newTask = MediumPrioTaskMachine(createdTask.id);
        displayMediumTask(createdTask);
      } else {
        var newTask = HighPrioTaskMachine(createdTask.id);
        displayHighTask(createdTask);
      }
      console.log(createdTask.id);
  }
    
  function createTask() {
    var radios = document.getElementsByName('priorityLevel');
    for (var i = 0, length = radios.length; i < length; i++){
      if (radios[i].checked) {
        priority = radios[i].value;
        break;
      }
    }
    var valid = true;
    //allFields.removeClass( "ui-state-error" );
    valid = valid && checkLength( name, "task name", 1, 30 );
    valid = valid && checkLength( percentage, "percentage", 1, 2 );
    valid = valid && checkLength( assigned, "worker's name(s)", 1, 30 );
    valid = valid && checkRegexp( name, /([0-9a-z_\s])+$/i, "Task name may consist of a-z, 0-9, underscores, spaces and must begin with a letter." );
    valid = valid && checkRegexp( percentage, /([0-9])+$/i, "Starting Perent must be an integer from 1 to 100" );
    valid = valid && checkRegexp( assigned, /([0-9a-z_\s])+$/i, "Name of worker task is assigned to. field may consist of a-z, 0-9, underscores, spaces and must begin with a letter." );
    if ( valid ) {
      var createdTask = new Task(name.val(), percentage.val(), priority, assigned.val());
      var newTask = LowPrioTaskMachine(createdTask.id);
      displayLowTask(createdTask);
    }
    return valid;
  }

  //Create Task Button Function
  $(function(){
    $('#clickme').click(function(){
         createTask();
         dialog.dialog("close");
    });
  });

  //Close Task Creation Button Function
  $(function(){
     $('#closeme').click(function(){
         dialog.dialog("close");
    });
  });

  //Get the modal
  var modal = document.getElementById('dialog-form');

  //When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
        dialog.dialog("close");
    }
  }
  //dialog form settings
  dialog = $( "#dialog-form" ).dialog({
    autoOpen: false,
    modal: true,
    close: function() {
        form[ 0 ].reset();
        allFields.removeClass( "ui-state-error" );
    }
  });
  
  form = dialog.find( "form" ).on( "submit", function( event ) {
    event.preventDefault();
  });
  //create user function call for button
  $( "#create-user" ).button().on( "click", function() {
    dialog.dialog( "open" ); 
  });
});

function remove(id) { 
  document.getElementById(id).parentElement.parentElement.outerHTML = ""; 
}
