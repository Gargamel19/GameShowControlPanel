//Description

function toggle_desc(){
    let description_panel_text = document.getElementsByClassName("description_panel_text")[0];
    if(description_panel_text.style.display === "none" || description_panel_text.style.display === ""){
        description_panel_text.style.display = "block"
    }else if(description_panel_text.style.display === "block"){
        description_panel_text.style.display = "none"
    }
}

function toggle_rules(){
    let rules_panel_text = document.getElementsByClassName("rules_panel_text")[0];
    if(rules_panel_text.style.display === "none" || rules_panel_text.style.display === ""){
        rules_panel_text.style.display = "block"
    }else if(rules_panel_text.style.display === "block"){
        rules_panel_text.style.display = "none"
    }
}

//Frage
function show_answer(){
    let answer_panel_text = document.getElementsByClassName("right_answer")[0];
    answer_panel_text.style.color = "green"
}


//Round

function select_round_as_won(gameID, roundID, playerID){
    let input = document.createElement("input");
    input.value = '{"method": "change_round_winner", "player": ' + playerID + ', "game": ' +gameID + ', "round": ' + roundID + '}';
    input.name = "return_value"
    input.style.display = "none"
    document.getElementsByClassName("round_score")[0].appendChild(input)
}



//Scoring

function select_game_as_won(playerNr, gameID) {
    let input = document.createElement("input");
    input.value = '{"method": "change_game_winner", "player": ' + playerNr + ', "game": ' +gameID + '}';
    input.name = "return_value"
    input.style.display = "none"
    document.getElementsByClassName("score")[0].appendChild(input)

}

function inc_bonus(player, ammount){
    let input = document.createElement("input");
    input.value = '{"method": "addBonus", "player": ' + player + ', "bonus": ' +ammount + '}';
    input.name = "return_value"
    input.style.display = "none"
    document.getElementsByClassName("score")[0].appendChild(input)
}