const submitButton = document.querySelector(".todo-submit");
const todoList = document.querySelector(".todo-list");

submitButton.addEventListener("click", addTask);

function addTask(event) {

    // add Task html structure
    /* <div class="task-container">
        <li class="task"></li>
        <button>delete</button>
        <button>checked</button>
    </div> */

    const divTask = document.createElement("div");
    divTask.classList.add("task-container");

    const liTask = document.createElement("li");
    liTask.innerText = "task";
    liTask.classList.add("task");
    divTask.appendChild(liTask)

    const buttonChecked = document.createElement("button");
    buttonChecked.innerHTML = '<i class="far fa-check-circle"></i>';
    buttonChecked.classList.add("button-checked");
    divTask.appendChild(buttonChecked)

    const buttonDelete = document.createElement("button");
    buttonDelete.innerHTML = '<i class="far fa-trash-alt"></i>';
    buttonDelete.classList.add("button-delete");
    divTask.appendChild(buttonDelete)

    todoList.appendChild(divTask)
}


