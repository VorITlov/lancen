let animate_blocks = document.querySelectorAll(".animate_block");
let arrow_up = document.querySelector(".arrow_up");

document.addEventListener("scroll", function(){
    arrow_up.hidden = (pageYOffset < document.documentElement.clientHeight);
})

arrow_up.onclick = function(){
    window.scrollTo(pageXOffset, 0);
}



if(animate_blocks.length > 0){

    window.onscroll = animateOnScroll;
    // window.onload = animateOnScroll;

    animateOnScroll();
}


console.log(pageYOffset  + "pageOffset");

function animateOnScroll(){
    // console.log(1);

   

    animate_blocks.forEach(element => {
        let coef = 4;
        let el_height = element.offsetHeight;
        let anim_element_point = window.innerHeight - el_height / coef;
        let anim_item_offset = offset(element).top;

        if(el_height > window.innerHeight){
            anim_element_point = window.innerHeight  - window.innerHeight / coef;
        }

        if((pageYOffset > anim_item_offset - anim_element_point) && pageYOffset < (anim_item_offset + el_height)){
            element.classList.add("active");
        }else{
            element.classList.remove("active");
        }

    });
}




function offset(el){
    let rect = el.getBoundingClientRect(),
        scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
        scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    return {top: rect.top + scrollTop, left: rect.left + scrollLeft}
        
}


let animateIcon = document.querySelectorAll(".animate_icon");

animateIcon.forEach(item =>{
    setInterval(() => {
        item.classList.toggle("confused_icon");
    }, 5000);
})



