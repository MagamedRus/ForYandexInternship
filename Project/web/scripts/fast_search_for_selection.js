inp_1 = $(".placeholder-1")
inp_2 = $(".placeholder-2")
inp_3 = $(".placeholder-3")
inp_4 = $(".placeholder-4")
inp_5 = $(".placeholder-5")
inp_6 = $(".placeholder-6")

d_inp_1 = document.querySelector('.placeholder-1')
d_inp_2 = document.querySelector('.placeholder-3')
d_inp_3 = document.querySelector('.placeholder-4')
d_inp_4 = document.querySelector('.placeholder-5')
d_inp_5 = document.querySelector('.placeholder-6')

d_items_1 = document.querySelectorAll('.e_items-1 option')
d_items_2 = document.querySelectorAll('.e_items-2 option')
d_items_3 = document.querySelectorAll('.e_items-3 option')
d_items_4 = document.querySelectorAll('.e_items-4 option')


c_list_1 = $(".choose-list-1")
c_list_2 = $(".choose-list-2")
c_list_3 = $(".choose-list-3")
c_list_4 = $(".choose-list-4")
c_list_5 = $(".choose-list-5")



btn_search = $(".btn-1")


function hide_all(){
    c_list_1.addClass("hide")
    c_list_2.addClass("hide")
    c_list_3.addClass("hide")
    c_list_4.addClass("hide")
    c_list_5.addClass("hide")
}


// Для первого инпута

inp_1.on("click", function(){
    if (inp_1.val() != -1){
        hide_all()
        c_list_1.removeClass("hide")
    }
})

inp_2.on("click", function(){
    hide_all()
})

inp_3.on("click", function(){
    if (inp_3.val() != -1){
        hide_all()
        c_list_2.removeClass("hide")
    }
})

inp_4.on("click", function(){
    if (inp_4.val() != -1){
        hide_all()
        c_list_3.removeClass("hide")
    }
})

inp_5.on("click", function(){
    if (inp_5.val() != -1){
        hide_all()
        c_list_4.removeClass("hide")
    }
})

inp_6.on("click", function(){
    if (inp_6.val() != -1){
        hide_all()
        c_list_5.removeClass("hide")
    }
})


btn_search.on("click", function(){
    hide_all()
})



d_inp_1.oninput = function () {
    let val = this.value.trim()
    val = val.toUpperCase()
    
    if (val != ''){
        d_items_1.forEach(function(elem){
            el = elem.innerText.toUpperCase()
            if (el.search(val) == -1) {
                elem.classList.add('hide');
                elem.innerHTML = elem.innerText;
            }else {
                elem.classList.remove('hide');
            }
        })
    }
    else {
        d_items_1.forEach(function (elem) {
            elem.classList.remove('hide');
            elem.innerHTML = elem.innerText;
        });
    }
}


//Для второго инпута


d_inp_2.oninput = function () {
    let val = this.value.trim()
    val = val.toUpperCase()
    
    if (val != ''){
        d_items_2.forEach(function(elem){
            el = elem.innerText.toUpperCase()
            if (el.search(val) == -1) {
                elem.classList.add('hide');
                elem.innerHTML = elem.innerText;
            }else {
                elem.classList.remove('hide');
            }
        })
    }
    else {
        d_items_2.forEach(function (elem) {
            elem.classList.remove('hide');
            elem.innerHTML = elem.innerText;
        });
    }
}


// Для третьего инпута


d_inp_3.oninput = function () {
    let val = this.value.trim()
    val = val.toUpperCase()
    
    if (val != ''){
        d_items_3.forEach(function(elem){
            el = elem.innerText.toUpperCase()
            if (el.search(val) == -1) {
                elem.classList.add('hide');
                elem.innerHTML = elem.innerText;
            }else {
                elem.classList.remove('hide');
            }
        })
    }
    else {
        d_items_3.forEach(function (elem) {
            elem.classList.remove('hide');
            elem.innerHTML = elem.innerText;
        });
    }
}


// Для четвертого инпута


d_inp_4.oninput = function () {
    let val = this.value.trim()
    val = val.toUpperCase()
    
    if (val != ''){
        d_items_4.forEach(function(elem){
            el = elem.innerText.toUpperCase()
            if (el.search(val) == -1) {
                elem.classList.add('hide');
                elem.innerHTML = elem.innerText;
            }else {
                elem.classList.remove('hide');
            }
        })
    }
    else {
        d_items_4.forEach(function (elem) {
            elem.classList.remove('hide');
            elem.innerHTML = elem.innerText;
        });
    }
}



// Для пятого инпута


d_inp_5.oninput = function () {
    let val = this.value.trim()
    let d_items_5 = document.querySelectorAll('.e_items-5 option')
    val = val.toUpperCase()
    if (val != ''){
        d_items_5.forEach(function(elem){
            el = elem.innerText.toUpperCase()
            if (el.search(val) == -1) {
                elem.classList.add('hide');
                elem.innerHTML = elem.innerText;
            }else {
                elem.classList.remove('hide');
            }
        })
    }
    else {
        d_items_5.forEach(function (elem) {
            elem.classList.remove('hide');
            elem.innerHTML = elem.innerText;
        });
    }
}



c_list_1.change(function(){
    d_inp_1.value = this.value
    hide_all()
})

c_list_2.change(function(){
    d_inp_2.value = this.value
    hide_all()
})

c_list_3.change(function(){
    d_inp_3.value = this.value
    hide_all()
})

c_list_4.change(function(){
    d_inp_4.value = this.value
    hide_all()
})

c_list_5.change(function(){
    d_inp_5.value = this.value
    hide_all()
})