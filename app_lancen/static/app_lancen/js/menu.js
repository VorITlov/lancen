window.onload = function(){
    let menu_links = document.querySelectorAll(".nav-link");

    menu_links.forEach(element => {
        if (element.pathname == window.location.pathname){
            element.classList.add("active");
        }
    });
}