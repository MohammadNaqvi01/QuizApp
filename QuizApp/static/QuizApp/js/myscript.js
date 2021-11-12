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
            
        $(".share").children().attr("href","quiz/"+data.link)
        

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
    $(".share").removeClass("d")
    


  }

 
   
   
  
});


    
}








