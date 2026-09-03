function animateCounter(id, target, speed){

    let count = 0;

    const counter = document.getElementById(id);

    const interval = setInterval(function(){

        count++;

        counter.textContent = count;

        if(count >= target){
            clearInterval(interval);
        }

    }, speed);

}

animateCounter("doctor",50,40);
animateCounter("patients",2000,1);
animateCounter("ambulance",15,100);
animateCounter("departments",20,80);

const images = [

 
    "/static/images/hero2.jpg",
    "/static/images/hero3.jpg",
    

];

let current = 0;

const slider = document.getElementById("slider");

setInterval(function(){

    current++;

    if(current >= images.length){
        current = 0;
    }

    slider.src = images[current];

},3000);