entrada = document.getElementById("entrada")

function agregar(char) {
    premisa = entrada.value + char
    console.log(premisa)
    entrada.value = premisa
    //alert(char);
}
function borrarUltimo(){
    premisa = entrada.value
    entrada.value = premisa.substr(0,premisa.length -1)
    console.log(entrada.value)
}