//Stopwatch
function toggle_countdown_visibility(element){
    visible_countdown = document.getElementsByClassName("visible_countdown");

    for (let i = 0; i < visible_countdown.length; i++) {
        if(element.checked){
            visible_countdown[i].style.display = "block"
        }else{
            visible_countdown[i].style.display = "none"
        }
    }

}

//Countdown
function toggle_stopwatch_visibility(element){
    visible_countdown = document.getElementsByClassName("visible_stopwatch");

    for (let i = 0; i < visible_countdown.length; i++) {
        if(element.checked){
            visible_countdown[i].style.display = "block"
        }else{
            visible_countdown[i].style.display = "none"
        }
    }

}

// Frage

function toggle_show_when_question(){

    checkbox_switch_questions =  document.getElementsByClassName("checkbox_switch_questions")[0];
    show_when_question_switchs = document.getElementsByClassName("show_when_question_switch");

    for (let i = 0; i < show_when_question_switchs.length; i++) {
        if(checkbox_switch_questions.checked){
            show_when_question_switchs[i].style.display = "block"
        }else{
            show_when_question_switchs[i].style.display = "none"
        }
    }

}

//Round

function toggle_show_when_round(){

    checkbox_switch_rounds =  document.getElementsByClassName("checkbox_switch_rounds")[0];
    checkbox_switch_questions =  document.getElementsByClassName("checkbox_switch_questions")[0];
    show_when_rounds_switch = document.getElementsByClassName("show_when_rounds_switch");
    show_when_rounds_switch_block = document.getElementsByClassName("show_when_rounds_switch_block")[0];
    if (checkbox_switch_rounds.checked) {
        show_when_rounds_switch_block.style.display = "block"
    } else {
        show_when_rounds_switch_block.style.display = "none"
    }
    for (let i = 0; i < show_when_rounds_switch.length; i++) {
        if(checkbox_switch_rounds.checked){
            show_when_rounds_switch[i].style.display = "flex"
        }else{
            show_when_rounds_switch[i].style.display = "none"
        }
    }
    checkbox_switch_questions.checked = checkbox_switch_rounds.checked
    checkbox_switch_questions.disabled = !checkbox_switch_rounds.checked
    toggle_show_when_question()
}

function set_answer_cb(clicked){
    let answer_cbs = document.getElementsByClassName("answer_cb")
    for (let i = 0; i < answer_cbs.length; i++) {
        if(answer_cbs[i] === clicked){
            answer_cbs[i].disabled = true
        }else{
            answer_cbs[i].disabled = false
            answer_cbs[i].checked = false

        }
    }
}


function save_settings(target){

    let nameHome = document.getElementsByClassName("nameHome")[0].value;
    let nameGuest = document.getElementsByClassName("nameGuest")[0].value;

    // Get Title
    let title = document.getElementsByClassName("game_title")[0].children[0].value;
    // Get Game Number
    let game_number = parseInt(document.getElementsByClassName("game_number")[0].innerHTML) - 1;
    // Get amount of Games
    let amount_of_games = parseInt(document.getElementsByClassName("amount_of_games")[0].value);

    let description = document.getElementsByClassName("description")[0].value;

    let rules = document.getElementsByClassName("rules")[0].value;

    let countdown_value = -1;
    let countdown = document.getElementsByClassName("countdown_cb")[0].checked;
    if(countdown){
        countdown_value = parseInt(document.getElementsByClassName("countdown_value_input")[0].value);
    }

    let stopwatch = document.getElementsByClassName("stopwatch_cb")[0].checked;

    let output_json = {}
    output_json["nameHome"] = nameHome
    output_json["nameGuest"] = nameGuest
    output_json["title"] = title
    output_json["game_number"] = game_number
    output_json["amount_of_games"] = amount_of_games
    output_json["description"] = description
    output_json["rules"] = rules
    output_json["countdown_value"] = countdown_value
    output_json["stopwatch"] = stopwatch

    if(document.getElementsByClassName("checkbox_switch_rounds")[0].checked){
        output_json["has_rounds"] = true
        output_json["amount_of_rounds"] = parseInt(document.getElementsByClassName("amount_of_rounds")[0].value)
        if(document.getElementsByClassName("checkbox_switch_questions")[0].checked){
            output_json["has_questions"] = true
            let right_answer = 0
            let question = document.getElementsByClassName("question")[0].value;
            let answers = []
            let answer_divs = document.getElementsByClassName("answer_div");
            for (let i = 0; i < answer_divs.length; i++) {
                answers.push(answer_divs[i].children[1].value)
                console.log(answer_divs[i].children[1].value)
                console.log(answer_divs[i].children[2].checked)
                if(answer_divs[i].children[2].checked){
                    right_answer = i
                }
            }


            output_json["frage"] = [question, answers, right_answer]
        }else{
            output_json["has_questions"] = false
        }

    }else{
        output_json["has_rounds"] = false
        output_json["has_questions"] = false
    }

    console.log(document.getElementsByClassName("outer_class")[0].scrollTop)
    var input = document.createElement("input");
    input.name = "return_value"

    input.value = JSON.stringify(output_json);
    input.style.display = "none"
    document.getElementsByClassName("save_button_div")[0].appendChild(input)

}

function add_quesion(){

    index = 0

    var newDiv = document.createElement("div");
    newDiv.classList.add("answer_" + index + "_div")
    newDiv.classList.add("answer_div")
    var delete_quesion_button = document.createElement("button");
    delete_quesion_button.classList.add("remove_answer")
    delete_quesion_button.setAttribute("onclick", "delete_quesion('answer_"+index+"_div')")
    delete_quesion_button.innerText = "-"
    var quesion_input = document.createElement("input");
    quesion_input.classList.add("answer_" + index)
    quesion_input.classList.add("answer_input")
    quesion_input.type = "text"
    quesion_input.value = ""
    var quesion_cb = document.createElement("input");
    quesion_cb.classList.add("answer_cb_" + index)
    quesion_cb.classList.add("answer_cb")
    quesion_cb.type = "checkbox"
    quesion_cb.setAttribute("onclick", "set_answer_cb(this)")
    var break_element = document.createElement("br");
    newDiv.appendChild(delete_quesion_button)
    newDiv.appendChild(quesion_input)
    newDiv.appendChild(quesion_cb)
    newDiv.appendChild(break_element)
    document.getElementsByClassName("answers_section")[0].appendChild(newDiv)
    restructure_index()
}

function delete_quesion(target){
    document.getElementsByClassName(target)[0].remove();
    restructure_index()
}

function restructure_index(){
    div_list = document.getElementsByClassName("answer_div")
    for (let i = 0; i < div_list.length; i++) {
        let index = div_list[i].classList.item(1).replace("answer_", "").replace("_div", "")
        div_list[i].classList.remove("answer_" + index + "_div")
        div_list[i].classList.add("answer_" + i + "_div")
        div_list[i].children[0].setAttribute("onclick", "delete_quesion('answer_"+i+"_div')")
        div_list[i].children[1].classList.remove("answer_" + index)
        div_list[i].children[1].classList.add("answer_" + i)
        div_list[i].children[2].classList.remove("answer_cb_" + index)
        div_list[i].children[2].classList.add("answer_cb_" + i)
    }
}