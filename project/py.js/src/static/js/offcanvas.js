
// adding contraints for admin


$(document).ready(function(){



$('#example-getting-started').multiselect();

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

$("#testbtn").click(function(e){

  $("#panel1 :input").each(function(index) {
    var FieldValue = $(this).attr("id");
    console.log(FieldValue);
  });
});

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 
     


var htmlcontents="<label id='answer-space'>Range</label><div id='answer'><div class='col-lg-12'><div class='col-lg-6'> <input autocomplete='off' class='input form-control' id='lower' name='lower' type='number' placeholder='Lower Limit'/></div><div class='col-lg-6'> <input autocomplete='off' class='input form-control' id='higher' name='higher' type='number' placeholder='Higher Limit'/></div></div></div>";
      $('.answer-space').html();
      $('.answer-space').html(htmlcontents);

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

var next = 1;
$(".add-more").click(function(){



  var constraint_name = document.getElementById('constraint_name').value;
  

  var addto = "#field" + next;
  var addRemove = "#field" + (next);
  next = next + 1;
  var newIn ='<div class=" col-lg-12 container" id="field' + next + '" name="field' + next +'"><div class=" col-lg-10 container"><label>Constraint name: </label><p>'+constraint_name+'</p></div><div class=" col-lg-2 container"><button id="remove ' + (next) + '" class="btn btn-danger remove-me" >-</button></div></div></div>';
  //var newIn = '<input autocomplete="off" class="input form-control" id="field' + next + '" name="field' + next + '" type="text">';
  var newInput = $(newIn);
  //var removeBtn = ;
  //var removeButton = $(removeBtn);

  $(addRemove).after(newInput);
  //$(addRemove).after(removeButton);

  $("#field" + next).attr('data-source',$(addto).attr('data-source'));
  $("#count").val(next);  

  $('.remove-me').click(function(e){
    e.preventDefault();

          var index = this.id.indexOf(" ");  // Gets the first index where a space occours
          var fieldNum = this.id.substr(index + 1);  // Gets the text part
          var fieldID = "#field" + fieldNum;
          $(this).remove();
          $(fieldID).remove();
        });
});



});

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



function loadNextDiv(){
    var answerType = $('#answer-type').find(":selected").text();
    console.log(answerType);
    if(answerType==='Range'){
      console.log(answerType);
      
      var htmlcontents="<label id='answer-space'>Range</label><div id='answer'><div class='col-lg-12'><div class='col-lg-6'> <input autocomplete='off' class='input form-control' id='lower' name='lower' type='number' placeholder='Lower Limit'/></div><div class='col-lg-6'> <input autocomplete='off' class='input form-control' id='higher' name='higher' type='number' placeholder='Higher Limit'/></div></div></div>";
      $('.answer-space').html('');
      $('.answer-space').html(htmlcontents);
    }
    if(answerType==='Text'){
      var htmlcontents="<label id='answer-space'>Text</label><div id='answer'><input autocomplete='off' class='input form-control' id='textans' name='textans' type='text' placeholder='Text Answer'/></div>";
      $('.answer-space').html('');
      $('.answer-space').html(htmlcontents);
    }
    if(answerType=='List Of Options'){
      var htmlcontents="<label id='answer-space'>List of Options</label><div id='answer'><label>Name of List</label><input autocomplete='off' class='input form-control' id='list-name' name='list-name' type='text' placeholder='Name of the List'/><label>Add options to the list separated by semicolons></label><input autocomplete='off' class='input form-control' id='list' name='list' type='text' placeholder='Options separated by semicolon'/></div>";
      $('.answer-space').html('');
      $('.answer-space').html(htmlcontents);
    }
    if(answerType=='Yes/No'){
      $('.answer-space').html('');
     



    }
    if(answerType=='Value'){
      var htmlcontents="<label id='answer-space'>Number</label><div id='answer'><input autocomplete='off' class='input form-control' id='numans' name='numans' type='number' placeholder='Numberical Answer'/></div>";
      $('.answer-space').html('');
      $('.answer-space').html(htmlcontents);
    }
  }

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//waste functions



