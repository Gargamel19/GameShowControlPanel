function aufloesen(element_id){
    target = document.getElementsByClassName("aufloesen")[0]
    if(target.innerHTML === "Get Answer"){
        document.getElementById("answer_"+element_id).classList.add("right_answer_question")
        answers = document.getElementsByClassName("answer_question");
        for (let i = 0; i < answers.length; i++) {
            if (answers[i].classList.contains("selected_answer_question")){
                if (answers[i].classList.contains("right_answer_question")) {
                    answers[i].classList.remove("selected_answer_question")
                }else{
                    answers[i].classList.remove("selected_answer_question")
                    answers[i].classList.add("wrong_answer_question")
                }
            }else {
                if (answers[i].classList.contains("right_answer_question")) {
                }else {
                    answers[i].classList.remove("selected_answer_question")
                    answers[i].classList.remove("wrong_answer_question")
                    answers[i].classList.add("neutral_answer_question")
                }
            }
            answers[i].disabled = true
            answers[i].style.display = "block"
        }
        target.innerText = "delete"
    }else if(target.innerText === "delete"){
        answers = document.getElementsByClassName("answer_question");
        for (let i = 0; i < answers.length; i++) {
            answers[i].classList.remove("selected_answer_question")
            answers[i].classList.remove("wrong_answer_question")
            answers[i].classList.remove("right_answer_question")
            answers[i].classList.remove("neutral_answer_question")
            answers[i].disabled = false
        }
        target.innerText = "Get Answer"
    }

}
function antwort_auswahl(element_id){

    let answers = document.getElementsByClassName("answer_question")
    for (let i = 0; i < answers.length; i++) {
        answers[i].classList.remove("selected_answer_question")
    }
    document.getElementById("answer_" + element_id).classList.add("selected_answer_question")

}

