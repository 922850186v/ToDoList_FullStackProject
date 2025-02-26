window.onload = getTasks;

function addTask() {
	// Get the task title and description from the form inputs
	const taskTitle = document.getElementById("taskTitle").value;
	const taskDescription = document.getElementById("taskDescription").value;

	// Check if the inputs are not empty
	if (taskTitle.trim() !== "" && taskDescription.trim() !== "") {
		// Create the data to send in the request body
		const taskData = {
			task_title: taskTitle,
			task_description: taskDescription,
			created_at: Date.now(),
			updated_at: Date.now(),
		};

		// Make the API call to create the task
		fetch("http://localhost:8000/api/v1/task/add", {
			method: "POST",
			headers: {
				accept: "application/json",
				"Content-Type": "application/json",
			},
			body: JSON.stringify(taskData),
		})
			.then((response) => response.json())
			.then((data) => {
				alert("Added Successfully", data);

				window.location.reload();
			})
			.catch((error) => {
				console.error("Error adding task:", error);
				alert("Failed to add task. Please try again.");
			});
	} else {
		alert("Please fill out both task title and description.");
	}
}

function getTasks() {
	fetch("http://localhost:8000/api/v1/task/get/pending-tasks")
		.then((response) => response.json())
		.then((data) => {
			const taskListContainer = document.getElementById("taskList");
			const taskListAlert = document.getElementById("taskAlert");
			if (data.result != 0 && Array.isArray(data.result)) {
				data.result.forEach((task) => {
					if (task.is_done == false) {
						const taskItem = document.createElement("div");
						taskItem.classList.add(
							"task-item",
							"alert",
							"alert-secondary",
							"d-flex",
							"justify-content-between",
							"align-items-center"
						);
						taskItem.innerHTML = `
                            <div class="task-details align-item-center">
                                <h3 id="taskTitle">${task.task}</h3>
                                <p id="taskDescription">${task.description}</p>
                            </div>
                            <div class="task-button mt-auto d-block w-25">
                                <button class="btn btn-outline-secondary w-100 color-black" onclick="updateTask(${task.id})">Done</button>
                            </div>
                            `;
						taskListContainer.appendChild(taskItem);
					}
				});
			} else {
				const taskAlert = document.createElement("p");
				taskAlert.classList.add("h3");
				taskAlert.innerHTML = `<p class="h3 no-tasks-p">No tasks are Pending!</p>`;
				taskListAlert.appendChild(taskAlert);
			}
		})
		.catch((error) => {
			console.error("Error fetching tasks:", error);
			alert("Failed to fetch tasks. Please try again.");
		});
}

function updateTask(id) {
    const is_confirmed = confirm("Are you done with this task?");

    if (is_confirmed) {        
        const taskTitle = document.getElementById("taskTitle").value;
        const taskDescription = document.getElementById("taskDescription").value;
        
        const updatedTaskData = {
                task_title: taskTitle,
                task_description: taskDescription,
                is_done: true,
                created_at: new Date().toISOString(),
                updated_at: new Date().toISOString(),
        };
        fetch(`http://localhost:8000/api/v1/task/update/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(updatedTaskData),
            
        }).then((response) => {
            if (response.ok) {
                alert("Task is Completed!")
                window.location.reload();
            } else {
                throw new Error("Failed to update task");
            }
        });
    }
}
