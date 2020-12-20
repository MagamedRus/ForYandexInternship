const wrp_1 = $(".wrapper-1")
const wrp_2 = $(".wrapper-2")
const wrp_3 = $(".wrapper-3")
const wrp_31 = $(".wrapper-3-1")
const wrp_32 = $(".wrapper-3-2")
const wrp_4 = $(".wrapper-4")
const table = $(".tb")


// Пасспортные данные
const f_n = $(".first-name")
const s_n = $(".second-name")
const l_n = $(".last-name")

const nmb = $(".number")
const ser = $(".serial")

const dor = $(".date-of-reg")
const cor = $(".code-of-reg")

const bp = $(".birdthplace")
const bday = $(".birthdate")
const sx = $(".sex")

const btn_wr2 = $(".for-wrapper-2")

//Поиск пасспортных данных
const inp_wr32 = $(".placeholder-6")
const btn_wr31 = $(".for-wrapper-3-2-send")


// Навигация
const btn_make_report = $(".report")
const btn_new_user = $(".new_user")
const btn_another_user= $(".another_user")
const btn_nav_convert = $(".convert_to")

// Обмен валюты
const pl1 = $(".placeholder-1")
const pl2 = $(".placeholder-2")
const pl3 = $(".placeholder-3")
const pl4 = $(".placeholder-4")
const pl5 = $(".placeholder-5")

const cl_1 = $(".choose-list-1").children()
const cl_2 = $(".choose-list-2").children()
const cl_3 = $(".choose-list-3").children()
const cl_4 = $(".choose-list-4").children()

const rs = $(".res")

const btn_wr1 = $(".btn-1")


let self_code = 0


//Выполнить репорт
async function make_report_and_write(){
    const res = await eel.make_report()()    
    table.html("\t\t<table>\n" + res + "\n\t\t</table>")
}


//Добавить в базу данных пасспортные данные
async function s_l(l) {
    let res = await eel.add_passport_data(l)()
    alert("Данные записаны!")
    wrp_2.css({display: "none"})
    wrp_1.css({display: "flex"})
}


//Найти в базе данных пасспортные данные, по серии паспорта
async function f_id(code) {
    let res = await eel.find_passport(code)();
    self_code = res
    return self_code
}


//Записывает действия пользователя, и конвертирует валюту
async function calc(l){
    let res = await eel.convert_to(l)();
    console.log(res)
    rs.html("<p>Результат = " + res + "</p>")
    rs.css({display: "block"})
}


//Обработчик для добавления пасспортных данных в дб
btn_wr2.on("click", function(){
    let list_inp = [f_n, s_n, l_n,
                    sx, bday, dor,
                    cor, bp, ser, nmb]
    self_code = ser
    second_name = s_n
    for(i in list_inp){
        if (list_inp[i].val() == "") {
            alert("Заполните все пропуски!")
            return
        }
    }
    let send_l = []

    for(i in list_inp){
        send_l.push(list_inp[i].val())
    }
    s_l(send_l)
    wrp_2.css({"display": "none"})
    wrp_1.css({"display": "flex"})
})


//Обработчик для поиска пасспортных данных
btn_wr31.on("click", function(){
    let sl = $(".e_items-5 option")
    let swh = false
    if (inp_wr32.val() != ""){ 
        for(let i = 0; i < sl.length; i++){
            if(inp_wr32.val() == sl[i].innerText){
                f_id(inp_wr32.val())
                wrp_32.css({"display": "none"})
                wrp_1.css({"display": "flex"})
                swh = true
            }
            
        }
    } else alert("Строка пуста")
    if (swh == false){ 
        alert("Выберете элемент из списка")
    }
})


//Преобразует список элементов DOM, в их значения
function make_val_list(l) {
    let f_l = []
    for (var i = 0; i < l.length; i++){
        f_l.push(l[i].innerText)
    }
    return f_l
}


//Обработчик для отправки отчета
btn_wr1.on("click", function(){
    var l_exch = [pl2.val(), pl1.val(), pl3.val(),
              pl5.val(), pl4.val()]

    var l_send = [pl2.val(), pl1.val(), pl3.val(),
                  self_code, pl4.val()]

    const c_1 = make_val_list(cl_1)
    const c_2 = make_val_list(cl_2)
    const c_3 = make_val_list(cl_3)
    const c_4 = make_val_list(cl_4)

    for (var i = 0; i < l_exch.length; i++){
        if (l_exch[i] == ""){
            alert("заполните все пропуски!")
            return
        }
    }
    if (($.inArray(pl1.val(), c_1)) == -1){
        alert("Выберете элементы из списка!")
        return
    }
    if (($.isNumeric(pl2.val())) == false){
        alert("Введите число!")
        return
    }

    if (($.inArray(pl3.val(), c_2)) == -1){
        alert("Выберете элементы из списка!")
        return
    }
    if ($.inArray(pl4.val(), c_3) == -1){
        alert("Выберете элементы из списка!")
        return
    }
    if (($.inArray(pl5.val(), c_4) == -1)){
        alert("Выберете элементы из списка!")
        return
    }

    calc(l_send)
})


//Очищает все инпуты
function make_clear_all_inp(){
    pl1.val("")
    pl2.val("")
    pl3.val("")
    pl4.val("")
    pl5.val("")
    f_n.val("")
    s_n.val("")
    l_n.val("")
    cor.val("")
    dor.val("")
    bday.val("")
    bp.val("")
    sx.val("")
    nmb.val("")
    ser.val("")
    inp_wr32.val("")
    rs.html("")
    rs.css({display: "none"})
}


// Навигатор
btn_make_report.on("click", function(){
    make_clear_all_inp()
    make_report_and_write()
    wrp_1.css({display: "none"})
    wrp_2.css({display: "none"})
    wrp_3.css({display: "none"})
    wrp_4.css({display: "flex"})
})


btn_new_user.on("click", function(){
    make_clear_all_inp()
    wrp_1.css({display: "none"})
    wrp_2.css({display: "flex"})
    wrp_3.css({display: "none"})
    wrp_4.css({display: "none"})
})

btn_another_user.on("click", function(){
    make_clear_all_inp()
    wrp_1.css({display: "none"})
    wrp_2.css({display: "none"})
    wrp_3.css({display: "flex"})
    wrp_31.css({display: "none"})
    wrp_32.css({display: "flex"})
    wrp_4.css({display: "none"})
})

btn_nav_convert.on("click", function(){
    if (self_code != "") {

        make_clear_all_inp()
        wrp_1.css({display: "flex"})
        wrp_2.css({display: "none"})
        wrp_3.css({display: "none"})
        wrp_4.css({display: "none"})
    } else return alert("Сначала выберете или введите пользователя!")
})
