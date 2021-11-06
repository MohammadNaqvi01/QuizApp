



function myfunc(quizId){

$(document).ready(function(){
 
 var par =$("#"+quizId).parent()

 var sib= par.siblings()
 
 for(var i=0; i<=sib.length;i++){

   $.ajax({

    type:"GET",
    url:"/userquest",
    data:{
        quest:quizId
    },
    success:function(data){
            
        alert(data.category)
    }
   });
 }
  
});


    
}








