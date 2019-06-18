function addTask(){
    taskNode = document.createElement("div");
    taskNode.classList.add("task");

    checkContainerNode = document.createElement("label");
    checkContainerNode.classList.add("checkContainer");

    checkBoxNode = document.createElement("input");
    checkBoxNode.setAttribute("type","checkbox");

    checkmarkNode = document.createElement("span");
    checkmarkNode.classList.add("checkmark");

    checkContainerNode.appendChild(checkBoxNode);
    checkContainerNode.appendChild(checkmarkNode);

    courseInputNode = document.createElement("input");
    courseInputNode.classList.add("courseInput");
    courseInputNode.setAttribute("type","text");

    taskInputNode = document.createElement("input");
    taskInputNode.classList.add("taskInput");
    taskInputNode.setAttribute("type","text");

    timeInputNode = document.createElement("input");
    timeInputNode.classList.add("timeInput");
    timeInputNode.setAttribute("type","number");

    upArrowNode = document.createElement("button");
    upArrowNode.classList.add("reorderUp");
    upArrowNode.classList.add("fas");
    upArrowNode.classList.add("fa-arrow-up");
    upArrowNode.addEventListener("click", moveUp(self));

    downArrowNode = document.createElement("button");
    downArrowNode.classList.add("reorderDown");
    downArrowNode.classList.add("fas");
    downArrowNode.classList.add("fa-arrow-down");
    upArrowNode.addEventListener("click", moveDown(self));

    taskNode.appendChild(checkContainerNode);
    taskNode.appendChild(courseInputNode);
    taskNode.appendChild(taskInputNode);
    taskNode.appendChild(timeInputNode);
    taskNode.appendChild(upArrowNode);
    taskNode.appendChild(downArrowNode);

    taskContainerNode = document.getElementById("taskContainer");
    taskContainerNode.appendChild(taskNode);

    console.log("Task successfully added!");
}

function removeChecked(){
    taskContainerNode = document.getElementById("taskContainer");
    taskNodes = taskContainerNode.getElementsByClassName("task");

    for(c = 0; c < taskNodes.length; c++){
        checkContainerNode = taskNodes[c].getElementsByClassName("checkContainer");
        checkboxNode = checkContainerNode[0].getElementsByTagName("input")[0];

        if(checkboxNode.checked){
            taskContainerNode.removeChild(taskContainerNode.childNodes[c]);
            c--;
        }        
    }
}


function moveUp(){
    // console.log(self.getParent());

}

function moveDown(){

}

