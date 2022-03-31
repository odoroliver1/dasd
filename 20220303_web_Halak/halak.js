function bekes(melyik){
    document.getElementById('bekesszovegkeret').style.display='none';
    document.getElementById('bekeskep').src=melyik+'.jpg';
    document.getElementById('bekeskepkeret').style.display='block';   
}
function nbekes(melyik){
    document.getElementById('nbekesszovegkeret').style.display='none';
    document.getElementById('nbekeskep').src=melyik+'.jpg';
    document.getElementById('nbekeskepkeret').style.display='block';   
}

function keprejt(melyik){
  document.getElementById('bekeskepkeret').style.display='none';
  document.getElementById('bekesszovegkeret').style.display='block';    
}