const modal = new bootstrap.Modal(document.querySelector('#modal'));

function expose_mark(student,lesson_date,date){
    modal.show();
    console.log("Сработало открытие окнка выставления");
   
    document.addEventListener('shown.bs.modal',modalExposeMark());

    async function modalExposeMark(){
        let response = await fetch(`/journal/expose-mark/${student}/${lesson_date}/${date}`, {
            method: "GET",
        });
        let result = await response.text();
        let modalContent = await document.querySelector(".modal .modal-content");
        modalContent.innerHTML = result;
        console.log("Конец Сработало открытие окнка выставления");
    }

};


function update_mark(id_mark , id_group, year, month){
   
    modal.show();

    console.log("Сработало открытие окнка редкатирования");
    document.addEventListener('shown.bs.modal', modalEditMark());

    async function modalEditMark(){
        let response = await fetch(`/journal/update-mark/${id_mark}/${id_group}/${year}/${month}/`, {
            method: "GET",
        });

        let result = await response.text();
        let modalContent = await document.querySelector(".modal .modal-content");
        modalContent.innerHTML = result;
        console.log("конец Сработало открытие окнка редкатирования");
    
    } 

}

function delete_mark(id_mark){
    url = `/journal/delete-mark/${id_mark}`;
  
    console.log(url);
    fetch(url)
        .then(response => response.json())
        .then(res => {
            let info_square = document.querySelector(".info_square");
            info_square.innerHTML = res.result;
            
            console.log(res)})
        .then(()=>{modal.hide(); console.log("Я закрыл окно")})
       
        .then(location.reload());
}