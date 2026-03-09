// Mobile menu

const toggle = document.getElementById("menu-toggle");
const nav = document.getElementById("nav-links");

toggle.onclick = () => {

if(nav.style.display === "flex"){
nav.style.display = "none";
}
else{
nav.style.display = "flex";
}

};


// Smooth scroll

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

anchor.addEventListener("click", function(e){

e.preventDefault();

document.querySelector(this.getAttribute("href")).scrollIntoView({
behavior:"smooth"
});

});

});


// Scroll animation

const sections = document.querySelectorAll("section");

function reveal(){

const triggerBottom = window.innerHeight * 0.85;

sections.forEach(section => {

const boxTop = section.getBoundingClientRect().top;

if(boxTop < triggerBottom){
section.style.opacity = "1";
section.style.transform = "translateY(0)";
}

});

}

window.addEventListener("scroll",reveal);

reveal();