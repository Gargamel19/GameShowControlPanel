function aufloesen(element_id){
    target = document.getElementsByClassName("aufloesen")[0]
    if(target.innerHTML === "Get Answer"){
        document.getElementById("answer_"+element_id).classList.add("right_answer")
        answers = document.getElementsByClassName("answer");
        for (let i = 0; i < answers.length; i++) {
            if (answers[i].classList.contains("selected_answer")){
                if (answers[i].classList.contains("right_answer")) {
                    answers[i].classList.remove("selected_answer")
                }else{
                    answers[i].classList.remove("selected_answer")
                    answers[i].classList.add("wrong_answer")
                }
            }else {
                if (answers[i].classList.contains("right_answer")) {
                }else {
                    answers[i].classList.remove("selected_answer")
                    answers[i].classList.remove("wrong_answer")
                    answers[i].classList.add("neutral_answer")
                }
            }
            answers[i].disabled = true
            answers[i].style.display = "block"
        }
        target.innerText = "delete"
    }else if(target.innerText === "delete"){
        answers = document.getElementsByClassName("answer");
        for (let i = 0; i < answers.length; i++) {
            answers[i].classList.remove("selected_answer")
            answers[i].classList.remove("wrong_answer")
            answers[i].classList.remove("right_answer")
            answers[i].classList.remove("neutral_answer")
            answers[i].disabled = false
        }
        target.innerText = "Get Answer"
    }

}
function antwort_auswahl(element_id){

    answers = document.getElementsByClassName("answer")
    for (let i = 0; i < answers.length; i++) {
        answers[i].classList.remove("selected_answer")
    }
    document.getElementById("answer_" + element_id).classList.add("selected_answer")

}

