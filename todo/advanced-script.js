const todoInput = document.getElementById("todoInput");
const todoList = document.getElementById("todoList");


document.addEventListener("DOMContentLoaded", loadTodos);

function addTodo() {
  const todoText = todoInput.value.trim();

  if (todoText === "") {
    alert("Task cannot be empty!");
    return;
  }

  const todoItem = {
    text: todoText,
    completed: false,
  };

  createTodoElement(todoItem);

  saveTodoToLocalStorage(todoItem);

  todoInput.value = "";
}

function createTodoElement(todoItem) {
  const li = document.createElement("li");


  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "complete-checkbox";
  checkbox.checked = todoItem.completed;


  checkbox.addEventListener("change", () => {
    todoItem.completed = checkbox.checked;
    updateLocalStorage();
    li.classList.toggle("completed", todoItem.completed);
  });


  const span = document.createElement("span");
  span.textContent = todoItem.text;


  const removeBtn = document.createElement("button");
  removeBtn.textContent = "Remove";
  removeBtn.className = "remove-btn";
  removeBtn.onclick = function () {
    todoList.removeChild(li);
    removeTodoFromLocalStorage(todoItem);
  };

  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(removeBtn);


  li.classList.toggle("completed", todoItem.completed);

  todoList.appendChild(li);
}


function saveTodoToLocalStorage(todoItem) {
  const todos = JSON.parse(localStorage.getItem("todos")) || [];
  todos.push(todoItem);
  localStorage.setItem("todos", JSON.stringify(todos));
}

function removeTodoFromLocalStorage(todoItem) {
  const todos = JSON.parse(localStorage.getItem("todos")) || [];
  const updatedTodos = todos.filter((todo) => todo.text !== todoItem.text);
  localStorage.setItem("todos", JSON.stringify(updatedTodos));
}


function updateLocalStorage() {
  const todos = [];
  todoList.querySelectorAll("li").forEach((li) => {
    const checkbox = li.querySelector(".complete-checkbox");
    const span = li.querySelector("span");
    todos.push({
      text: span.textContent,
      completed: checkbox.checked,
    });
  });
  localStorage.setItem("todos", JSON.stringify(todos));
}


function loadTodos() {
  const todos = JSON.parse(localStorage.getItem("todos")) || [];
  todos.forEach(createTodoElement);
}
todoInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    addTodo();
  }
});
