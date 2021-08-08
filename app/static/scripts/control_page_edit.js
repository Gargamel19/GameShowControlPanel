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


function save_settings(){

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
        let amount_of_rounds = parseInt(document.getElementsByClassName("amount_of_rounds")[0].value);
        output_json["amount_of_rounds"] = amount_of_rounds

        if(document.getElementsByClassName("checkbox_switch_questions")[0].checked){
            output_json["has_questions"] = true
            let right_answer = 0
            let question = document.getElementsByClassName("question")[0].value;
            let answer_0 = document.getElementsByClassName("answer_0")[0].value;
            if(document.getElementsByClassName("answer_cb_0")[0].checked){
                right_answer = 0
            }
            let answer_1 = document.getElementsByClassName("answer_1")[0].value;
            if(document.getElementsByClassName("answer_cb_1")[0].checked){
                right_answer = 1
            }
            let answer_2 = document.getElementsByClassName("answer_2")[0].value;
            if(document.getElementsByClassName("answer_cb_2")[0].checked){
                right_answer = 2
            }
            let answer_3 = document.getElementsByClassName("answer_3")[0].value;
            if(document.getElementsByClassName("answer_cb_3")[0].checked){
                right_answer = 3
            }
            output_json["frage"] = [question, [answer_0, answer_1, answer_2, answer_3], right_answer]
        }else{
            output_json["has_questions"] = false
        }

    }else{
        output_json["has_rounds"] = false
        output_json["has_questions"] = false
    }



    var input = document.createElement("input");
    input.name = "return_value"

    input.value = JSON.stringify(output_json);
    input.style.display = "none"
    document.getElementsByClassName("save_button_div")[0].appendChild(input)
    console.log(JSON.stringify(output_json))

}