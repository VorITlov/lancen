// window.onload = function(){
//     let freeLessonFormSquare = document.querySelector(".free_lesson_form");

   
//     let url = '/free-lesson';
//     fetch(url)
//     .then(response => response.text())
//     .then(commits => freeLessonFormSquare.innerHTML =  commits);
    
// }

function mySerialize(json){
    let str = "";
    Object.entries(json).map(([key, value]) => str += `${key}=${value}&`)
    return str;
}

//console.log(mySerialize({"data1": "asd", "data2":"pde0"}));

async function sendDataMy(url, data){
    
    try {
        const response = await fetch(url, {
            method: 'POST', // или 'PUT'
            body: JSON.stringify(data), // данные могут быть 'строкой' или {объектом}!
            headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": data.csrfmiddlewaretoken,
            "X-Requested-With": "XMLHttpRequest",
            }
        });
        const json = await response.json();
        console.log('Успешно полученный JSON:', JSON.parse(JSON.stringify(json)));
        return json;
    } catch (error) {
        console.error('Ошибка:', error);
    }
}

freeLessonBtn.onclick = function(){
    let freeLessonInfo = document.querySelector(".freeLessonInfo");
    freeLessonInfo.innerHTML = "Попытка отпарвить заявку";

    console.log("Началась работа с отправкой формы");

    form = document.querySelector("#freeLessonForm");
    let url = '/free-lesson/';
    let data = { 
        csrfmiddlewaretoken: form["csrfmiddlewaretoken"].value,
        name: form["name"].value,
        email: form["email"].value,
        phone: form["phone"].value,
        captcha_0: form["captcha_0"].value,
        captcha_1: form["captcha_1"].value,
    };
    

    

    let text_errors = "";


    

    if (form["name"].value && form["email"].value && form["phone"].value && form["captcha_1"].value ){
        sendDataMy(url, data)
        .then(result=> {

            if(result.errors){ // валидация полей
                if(result.errors.captcha){
                    form["captcha_1"].classList.add("is-invalid");
                    refreshCaptcha("freeLessonForm");//смена каптчи
                }else{
                    form["captcha_1"].classList.add("is-valid");
                }
    
                if(result.errors.name){
                    form["name"].classList.add("is-invalid");
                }else{
                    form["captcha_1"].classList.add("is-valid");
                }
    
                if(result.errors.phone){
                    form["phone"].classList.add("is-invalid");
                }else{
                    form["phone"].classList.add("is-valid");
                }
    
                if(result.errors.email){
                    form["email"].classList.add("is-invalid");
                }else{
                    form["email"].classList.add("is-valid");
                }

            }else{
                console.log("Форма прошла валидацию");
            }


            if(result.success){
                //freeLessonInfo.classList.remove("alert-primary");
                freeLessonInfo.classList.add("alert-success");
                freeLessonInfo.innerHTML = "Сообщение отпрвавлено на почту";

                freeLessonBtn.style.display = "none";
            }

            if(result.error){
                console.log("res err" + result.error);
                if (freeLessonBtn.classList.contains("alert-primary")) freeLessonInfo.classList.remove("alert-primary");
                freeLessonInfo.classList.add("alert-danger");
                freeLessonInfo.innerHTML = "Ошибка отправки сообщения";
            }

            
        
        });
    }else{
        text_errors.innerHTML = "Заполните данные формы";
    }

    
}

let captcha_free_lesson = document.querySelector("#freeLessonForm .captcha");
captcha_free_lesson.addEventListener("click", ()=>{refreshCaptcha("freeLessonForm")});




let captcha_recall = document.querySelector("#recallForm .captcha");
captcha_recall.addEventListener("click", ()=>{refreshCaptcha("recallForm")});



function refreshCaptcha(id_form){
    let form = document.querySelector(`#${id_form}`);
    let url = '/captcha/refresh/';
    let captcha = form.querySelector(".captcha");

    fetch(url,{
        method: 'POST', // или 'PUT'
        headers: {
        'Content-Type': 'application/json',
        "X-CSRFToken": form["csrfmiddlewaretoken"].value,
        "X-Requested-With": "XMLHttpRequest",
        }
    })
    .then(response => response.json())
    .then(res =>{
        captcha.src = res.image_url;
        form["captcha_0"].value = res.key;
    });
}


