//Description

function toggle_desc(){
    description_panel_text = document.getElementsByClassName("description_panel_text")[0];
    if(description_panel_text.style.display === "none" || description_panel_text.style.display === ""){
        description_panel_text.style.display = "block"
    }else if(description_panel_text.style.display === "block"){
        description_panel_text.style.display = "none"
    }
}

function toggle_rules(){
    rules_panel_text = document.getElementsByClassName("rules_panel_text")[0];
    if(rules_panel_text.style.display === "none" || rules_panel_text.style.display === ""){
        rules_panel_text.style.display = "block"
    }else if(rules_panel_text.style.display === "block"){
        rules_panel_text.style.display = "none"
    }
}



//Frage

function show_answer(){
    answer_panel_text = document.getElementsByClassName("answer_panel_text")[0];
    if(answer_panel_text.classList.contains("panel_hidden_text")){
        answer_panel_text.classList.remove("panel_hidden_text")
    }
}

//Round

function select_round_as_won(gameID, roundID, playerID, originScore_0, originScore_1){
    var input = document.createElement("input");
    input.value = '{"method": "cahage_round_winner", "player": ' + playerID + ', "game": ' +gameID + ', "round": ' + roundID + '}';
    input.name = "return_value"
    document.getElementsByClassName("round_score")[0].appendChild(input)
}



//Scoring

function select_game_as_won(playerNr, gameID) {
    var input = document.createElement("input");
    input.value = '{"method": "cahage_game_winner", "player": ' + playerNr + ', "game": ' +gameID + '}';
    input.name = "return_value"
    document.getElementsByClassName("score")[0].appendChild(input)

}

function get_games_score(){
    //Game-points
    gamebutons = document.getElementsByClassName('selected_game_button')
    player_list = [0, 0]
    for (let i = 0; i < gamebutons.length; i++) {
        value = parseInt(gamebutons[i].textContent)
        player = ""
        for (let j = 0; j < gamebutons[i].classList.length; j++) {
            class_Name = gamebutons[i].classList[j]
            if(class_Name.startsWith("button_player_")){
                player = class_Name.replace("button_player_", "")
                player = player.replace("_" + (value-1), "")
                player = parseInt(player)
                player_list[player] += value
                break
            }
        }

    }

    //Bonus-points
    bonus_point_divs = document.getElementsByClassName('bonus_score')
    for (let i = 0; i < bonus_point_divs.length; i++) {
        value = parseInt(bonus_point_divs[i].textContent)
        for (let j = 0; j < bonus_point_divs[i].classList.length; j++) {
            class_Name = bonus_point_divs[i].classList[j]
            if (class_Name.startsWith("bonus_ammount_")) {
                player = parseInt(class_Name.replace("bonus_ammount_", ""))
                player_list[player] += value
                break
            }
        }
    }


    document.getElementsByClassName("score_sum_player0")[0].innerHTML = player_list[0]
    document.getElementsByClassName("score_sum_player1")[0].innerHTML = player_list[1]
}

function reset_gamescore(){
    gamebutons = document.getElementsByClassName('game_button')
    for (let i = 0; i < gamebutons.length; i++) {
        if(gamebutons[i].classList.contains("selected_game_button")){
            gamebutons[i].classList.remove("selected_game_button")
        }
        if(gamebutons[i].classList.contains("deselected_game_button")){
            gamebutons[i].classList.remove("deselected_game_button")
        }
    }
    bonus_point_divs = document.getElementsByClassName('bonus_score')
    for (let i = 0; i < bonus_point_divs.length; i++) {
        bonus_point_divs[i].textContent = "0"
    }

    get_games_score()
}

function inc_bonus(player, ammound){
    var input = document.createElement("input");
    input.value = '{"method": "addBonus", "player": ' + player + ', "bonus": ' +ammound + '}';
    input.name = "return_value"
    document.getElementsByClassName("score")[0].appendChild(input)
}