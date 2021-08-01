function select_game_as_won(playerNr, gameID) {
    console.log(playerNr + "" + gameID)
    otherPlayer = 0
    if(playerNr === 0){
        otherPlayer = 1
    }else{
        otherPlayer = 0
    }
    console.log(otherPlayer + "" + gameID)
    classListPlayer = document.getElementsByClassName('button_player_' + playerNr + '_' + gameID)[0].classList;

    if(!classListPlayer.contains("selected_game_button")){
        document.getElementsByClassName('button_player_' + playerNr + '_' + gameID)[0].classList.add("selected_game_button");
    }
    classListOponentPlayer = document.getElementsByClassName('button_player_' + otherPlayer + '_' + gameID)[0].classList;
    if(classListPlayer.contains("selected_game_button")){
        document.getElementsByClassName('button_player_' + otherPlayer + '_' + gameID)[0].classList.remove("selected_game_button");
    }
    get_games_score()

}

function get_games_score(){
    //Home Player
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
    document.getElementsByClassName("score_sum_player0")[0].innerHTML = player_list[0]
    document.getElementsByClassName("score_sum_player1")[0].innerHTML = player_list[1]
}