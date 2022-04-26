//Stopwatch
function toggle_countdown_visibility(element){
    let visible_countdown = document.getElementsByClassName("visible_countdown");

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

    let checkbox_switch_questions = document.getElementsByClassName("checkbox_switch_questions")[0];
    let show_when_question_switchs = document.getElementsByClassName("show_when_question_switch");

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

    let checkbox_switch_rounds = document.getElementsByClassName("checkbox_switch_rounds")[0];
    let checkbox_switch_questions = document.getElementsByClassName("checkbox_switch_questions")[0];
    let show_when_rounds_switch = document.getElementsByClassName("show_when_rounds_switch");
    let show_when_rounds_switch_block = document.getElementsByClassName("show_when_rounds_switch_block")[0];
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


function save_settings(){

    let name_home = document.getElementsByClassName("name_home")[0].value;
    let name_guest = document.getElementsByClassName("name_guest")[0].value;

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

    let output_json = {}
    output_json["name_home"] = name_home
    output_json["name_guest"] = name_guest
    output_json["title"] = title
    output_json["game_number"] = game_number
    output_json["amount_of_games"] = amount_of_games
    output_json["description"] = description
    output_json["rules"] = rules
    output_json["countdown_value"] = countdown_value

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
    let input = document.createElement("input");
    input.name = "return_value"

    input.value = JSON.stringify(output_json);
    input.style.display = "none"
    document.getElementsByClassName("save_button_div")[0].appendChild(input)

}

function add_question(){

    let index = 0
    let newDiv = document.createElement("div");
    newDiv.classList.add("answer_" + index + "_div")
    newDiv.classList.add("answer_div")
    let delete_question_button = document.createElement("button");
    delete_question_button.classList.add("remove_answer")
    delete_question_button.setAttribute("onclick", "delete_question('answer_"+index+"_div')")
    delete_question_button.innerText = "-"
    let question_input = document.createElement("input");
    question_input.classList.add("answer_" + index)
    question_input.classList.add("answer_input")
    question_input.type = "text"
    question_input.value = ""
    let question_cb = document.createElement("input");
    question_cb.classList.add("answer_cb_" + index)
    question_cb.classList.add("answer_cb")
    question_cb.type = "checkbox"
    question_cb.setAttribute("onclick", "set_answer_cb(this)")
    let break_element = document.createElement("br");
    newDiv.appendChild(delete_question_button)
    newDiv.appendChild(question_input)
    newDiv.appendChild(question_cb)
    newDiv.appendChild(break_element)
    document.getElementsByClassName("answers_section")[0].appendChild(newDiv)
    restructure_index()
}

function delete_question(target){
    document.getElementsByClassName(target)[0].remove();
    restructure_index()
}

function restructure_index(){
    let div_list = document.getElementsByClassName("answer_div")
    for (let i = 0; i < div_list.length; i++) {
        let index = div_list[i].classList.item(1).replace("answer_", "").replace("_div", "")
        div_list[i].classList.remove("answer_" + index + "_div")
        div_list[i].classList.add("answer_" + i + "_div")
        div_list[i].children[0].setAttribute("onclick", "delete_question('answer_"+i+"_div')")
        div_list[i].children[1].classList.remove("answer_" + index)
        div_list[i].children[1].classList.add("answer_" + i)
        div_list[i].children[2].classList.remove("answer_cb_" + index)
        div_list[i].children[2].classList.add("answer_cb_" + i)
    }
}