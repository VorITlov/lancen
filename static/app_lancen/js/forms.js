let callBtn = document.querySelector("#btnRecall");

if (callBtn){

    let form = document.querySelector("#recallForm");
    let infoBlock = document.querySelector(".recallInfo");
    let captcha  = form.querySelector(".captcha");
    captcha.onclick = function(){
        refreshCaptcha(form.id);
    }

    callBtn.onclick = function(){

        let url = '/recall/';
        let data = { 
            csrfmiddlewaretoken: form["csrfmiddlewaretoken"].value,
            phone: form["phone"].value,
            captcha_0: form["captcha_0"].value,
            captcha_1: form["captcha_1"].value,
            sogl: form['sogl'].value,
        };
    
        infoBlock.innerHTML = "Отправка данных";

        sendDataMy(url, data)
        .then(result=> {

            if(result.errors){ // валидация полей
                if(result.errors.captcha){
                    form["captcha_1"].classList.add("is-invalid");
                    refreshCaptcha(form.id);//смена каптчи
                }else{
                    form["captcha_1"].classList.add("is-valid");
                }
    
            
                if(result.errors.phone){
                    form["phone"].classList.add("is-invalid");
                }else{
                    form["phone"].classList.add("is-valid");
                }
            }else{
                console.log("Форма звонка прошла валидацию");
            }


            if(result.success){
                infoBlock.classList.add("alert-success");
                infoBlock.innerHTML = "Сообщение отпрвавлено на почту администратору";
                callBtn.style.display = "none";

            }

            if(result.error){
                console.log("res err" + result.error);
                if (freeLessonBtn.classList.contains("alert-primary")) freeLessonInfo.classList.remove("alert-primary");
                freeLessonInfo.classList.add("alert-danger");
                freeLessonInfo.innerHTML = "Ошибка отправки сообщения";
            }

        });
    }
}


let sendMailBtn = document.querySelector("#sendMailBtn");

if (sendMailBtn){
    let form = document.querySelector("#sendMailForm");
    let infoBlock = document.querySelector(".sendMaillInfo");
    let captcha  = form.querySelector(".captcha");
    captcha.onclick = function(){
        refreshCaptcha(form.id);
    }

    sendMailBtn.onclick = function(){
        let url = '/send-mail/';
        let data = { 
            csrfmiddlewaretoken: form["csrfmiddlewaretoken"].value,
            name: form["name"].value,
            email: form["email"].value,
            text: form["text"].value,
            captcha_0: form["captcha_0"].value,
            captcha_1: form["captcha_1"].value,
        };

        infoBlock.innerHTML = "Отправка данных";

        sendDataMy(url, data)
        .then(result=> {

            if(result.errors){ // валидация полей
                if(result.errors.captcha){
                    form["captcha_1"].classList.add("is-invalid");
                    refreshCaptcha(form.id);//смена каптчи
                }else{
                    form["captcha_1"].classList.add("is-valid");
                }
    
            
                if(result.errors.phone){
                    form["phone"].classList.add("is-invalid");
                }else{
                    form["phone"].classList.add("is-valid");
                }
            }else{
                console.log("Форма отправки письма  прошла валидацию");
            }


            if(result.success){
                infoBlock.classList.add("alert-success");
                infoBlock.innerHTML = "Сообщение отпрвавлено на почту администратору";
                sendMailBtn.style.display = "none";

            }

            if(result.error){
                console.log("res err" + result.error);
                if (freeLessonBtn.classList.contains("alert-primary")) freeLessonInfo.classList.remove("alert-primary");
                freeLessonInfo.classList.add("alert-danger");
                freeLessonInfo.innerHTML = "Ошибка отправки сообщения";
            }

        });

    }
}









/*###############################################*/



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


function validate_phone(evt){
    let theEvent = evt || window.event;
    let key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode( key );
    let regex = /[0-9]|\./;
    if( !regex.test(key) ) {
        theEvent.returnValue = false;
        if(theEvent.preventDefault) theEvent.preventDefault();
    }
    
}