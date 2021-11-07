$(document).ready(function(){


   
  $("#submit").click(function(){

  
    var name=$('#name').val()
    $.ajax({

      type:"GET",
      url:"/username",
      data:{
          quest:name
      },
       
      success:function(data){
            
       alert(data.done) 
        
      }


     });
     $(this).parent().addClass("d")
     $(".quiz div:first").removeClass("d")
     

  })

 


})
     





function myfunc(quizId){

$(document).ready(function(){
 
 var par =$("#"+quizId).parent();
     
     var sib=par.next();
     
     par.addClass("d");

     $.ajax({

      type:"GET",
      url:"/userquest",
      data:{
          quest:quizId
      },
      success:function(data){
              
          
          
      }
     });

     if(sib.length){
      sib.removeClass("d");
  }
  else{
    alert("No more elements")
    alert(document.cookie)
    cookie=getCookie("sessionid");
    alert(cookie)
    $(".share").removeClass("d").children().attr("href",cookie)


  }

 
   
   
  
});


    
}


function getCookie(sessionid) {
  
  let name = sessionid + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
   
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}





