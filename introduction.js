const form = document.getElementById("introduction")
const displayIntro = document.getElementById("display-intro")
displayIntro.style.display = 'none'

function introduceMember(){
    errorMessage = getErrors(form)

    if(errorMessage != ''){
        alert(errorMessage)
    }
    else{
        name = form.elements['name'].value
        funFact = form.elements['fun-fact'].value
        console.log("Name: "+ name)
        console.log("Fun Fact: "+ funFact)
        hideForm()
        displayIntro.children[0].innerHTML = "<strong>Name:</strong> "+ name + "</br><strong>Fun Fact:</strong> " + funFact
    }
}


function getErrors(form){
    errorMessage = ''
    fullName = form.elements['name'].value
    funFact = form.elements['fun-fact'].value
    if(fullName == ''){
        errorMessage += "Name cannot be empty!\n"
    }
    if(funFact == ''){
        errorMessage += "Fun fact cannot be empty!"
    }
    return errorMessage;
}


function showForm(){
    form.style.display = 'block'
    displayIntro.style.display = 'none'
}

function hideForm(){
    form.style.display = 'none'
    displayIntro.style.display = 'block'
}

function introduceNext(){
    form.reset()
    showForm()
}