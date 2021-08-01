function select_game_as_won(playerNr, gameID) {
    otherPlayer = 0
    if(playerNr === 0){
        otherPlayer = 1
    }else{
        otherPlayer = 0
    }
    playerButton = document.getElementsByClassName('button_player_' + playerNr + '_' + gameID)[0];
    opnentPlayerButton = document.getElementsByClassName('button_player_' + otherPlayer + '_' + gameID)[0];

    if(playerButton.classList.contains("selected_game_button")){
        playerButton.classList.remove("selected_game_button");
        opnentPlayerButton.classList.remove("deselected_game_button");
        get_games_score()
        return
    }

    if(!playerButton.classList.contains("selected_game_button")){
        if(playerButton.classList.contains("deselected_game_button")){
            playerButton.classList.remove("deselected_game_button");
        }
        playerButton.classList.add("selected_game_button");
    }
    if(opnentPlayerButton.classList.contains("selected_game_button")){
        opnentPlayerButton.classList.remove("selected_game_button");
    }
    opnentPlayerButton.classList.add("deselected_game_button");
    get_games_score()

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
    bonus_ammount_field = document.getElementsByClassName('bonus_ammount_' + player)[0]
    bonus_ammount_field.textContent = parseInt(bonus_ammount_field.textContent) + ammound
    get_games_score()
}