/**
 * @param {number} x
 * @return {number}
 */

 var reverse = function(x){
    var reverseInteger = '';
    var endPoint = 0;
    
    if(x < 0){
        endPoint = 1;
        reverseInteger += '-';
    }

     x = x + '';
    
     for(var i = x.length - 1; i >= endPoint; i--){
         reverseInteger += x[i];
     }

     reverseInteger = Number(reverseInteger);
     return reverseInteger;
 }
