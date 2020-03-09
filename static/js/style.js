var button = document.getElementById("menu_toggle");
var menu = document.getElementById("small_screen_menu");
var counter = 1;
var wrapper = document.getElementById("wrapper");
var up_button = document.getElementById("up_button");

button.addEventListener("click", show);

function show(){
    counter += 1;
    if (counter % 2 == 0){
        menu.style.left = "0vw";
        button.style.transform = "rotate(90deg)";
        
    }
    else{
        menu.style.left = "-100vw";
        button.style.transform = "rotate(0deg)";
        
    }
     
};

window.addEventListener("scroll", up);

function up(){
    if (window.pageYOffset>650){
        up_button.style.display = "block";
    }
    else{
        up_button.style.display = "none";
    }
};
