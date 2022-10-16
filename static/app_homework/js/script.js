
const modal = new bootstrap.Modal(document.querySelector('#modalDelHw'));

function delete_hw(id_hw){
    modal.show();
    console.log("Сработало открытие окнка выставления");
   
    document.addEventListener('shown.bs.modal',modalExposeMark());

    async function modalExposeMark(){
        let response = await fetch(`/homework/delete-homework/${id_hw}`, {
            method: "GET",
        });
        let result = await response.text();
        let modalContent = await document.querySelector(".modal .modal-content");
        modalContent.innerHTML = result;
        console.log("Конец Сработало открытие окнка выставления");
    }

};