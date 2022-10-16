function func(element, student_id, lesson_id){
    
    url = ``;
    if(element.checked){ // выставление
        console.log("Выставление")
        url = `/journal/expose-attendance/${student_id}/${lesson_id}`;

    }else{ // удаление
        console.log("Удаление")
        url = `/journal/delete-attendance/${student_id}/${lesson_id}`;
    }

    fetch(url)
        .then(response => response.json())
        .then(res => {
            let info_square = document.querySelector(".info_square");
            info_square.innerHTML = res.result;
            
            console.log(res)});
    
}