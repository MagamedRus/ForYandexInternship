const btn_y = $(".for-wrapper-3-1-Yes")
const btn_n = $(".for-wrapper-3-1-No")
const wrapper2 = $(".wrapper-2")
const wrapper3 = $(".wrapper-3")
const wrapper31 = $(".wrapper-3-1")
const wrapper32 = $(".wrapper-3-2")
const list_numb = $(".list-of-numbers")
const inp_pass = $(".number-of-passport")


async function get_numb(){
    let res = await eel.get_numb()()
    let some_string = ""
    for (i in res) {
        some_string += "<option>" + res[i] + "</option>\n"
    }
    list_numb.html(some_string)
}



btn_n.on("click", function() {
    wrapper2.css({ "display": "flex"})
    wrapper3.css({ "display": "none"})
})


btn_y.on("click", function(){
    wrapper31.css({"display": "none"})
    wrapper32.css({"display": "flex"})
})


inp_pass.on("click", function(){
    list_numb.removeClass("hide")
    if (inp_pass.val() == "") {
        get_numb()
    }
})


