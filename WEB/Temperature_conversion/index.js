const tempnum = document.getElementById("text");
const ctf = document.getElementById("radio11");
const ftc = document.getElementById("radio22");
const sub = document.getElementById("submit");

sub.onclick = function(){

    if(ctf.checked){
        let conver = (tempnum.value * (9/5)) + 32;
        document.getElementById("res").textContent = `${conver.toFixed(1)}°F`;
    }
    else if(ftc.checked){
        let conver = (tempnum.value - 32) * 5/9;
        document.getElementById("res").textContent = `${conver.toFixed(1)}°C`;
    }
}