(function(){
   let btn = document.querySelector('#submit');
   let xls = document.querySelector('#xls');
   let sub = document.querySelector('#subject');
   let body = document.querySelector('#body');

//    $('#submit').click(function() {
//       if( 10 < 5) {
//          return true;
//       }else {
//          return false;
//       }
//    });
//    $("#btn").click(function(){
//       $.post("/ajax/",
//       {
//          name: 'Raja',
//          gender: 'do not know'
//       },
//       function(data, status){
//           demo.innerHTML = data.name + ' ' +  data.gender
//       });
//   }); 


$('#submit').click(function() {
   // console.log(xls.value);
   if(sub.value == '' || body.value == '' || xls.value == '') {
      return false;
   }
   return true;
})

}());