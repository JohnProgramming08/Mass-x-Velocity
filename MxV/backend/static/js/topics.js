document.addEventListener("DOMContentLoaded", () => {
	const carets = Array.from(document.getElementsByClassName("caret"));
	const topicCheckboxes = Array.from(document.getElementsByClassName("topic"));
	const subtopicCheckboxes = Array.from(
		document.getElementsByClassName("subtopic"),
	);

	// Handles all logic with showing and hiding checkboxes using carets
	class CaretLogic {
		constructor(carets) {
			this.caretList = carets;
			for (const caret of this.caretList) {
				this.assignEventListener(caret);
			}
		}

		// Get the topic associated with a given caret
		getTopic(caret) {
			const parent = caret.parentElement;
			const classElement = parent.querySelector("label");
			return classElement.htmlFor;
		}

		// Change the display of all checkboxes associated with caret
		changeCheckboxesDisplay(caret, newDisplay) {
			const topic = this.getTopic(caret);
			const checkboxes = Array.from(document.getElementsByClassName(topic));

			for (const checkbox of checkboxes) {
				checkbox.parentElement.style.display = newDisplay;
			}
		}

		// Assign event listener to a caret
		assignEventListener(caret) {
			caret.addEventListener("click", () => {
				// Hide checkboxes
				if (caret.id === "down") {
					this.changeCheckboxesDisplay(caret, "none");
					caret.id = "up";
					caret.style.transform = "rotate(180deg)";
				}

				// Show checkboxes
				else {
					this.changeCheckboxesDisplay(caret, "flex");
					caret.id = "down";
					caret.style.transform = "";
				}
			});
		}
	}

	// Handles all logic of checking boxes based on the state of other boxes
	class CheckboxLogic {
		constructor(topicCheckboxes, subtopicCheckboxes) {
			this.topicCheckboxes = topicCheckboxes;
			this.subtopicCheckboxes = subtopicCheckboxes;
			this.assignTopicEventListeners(this.topicCheckboxes);
			this.assignSubtopicEventListeners(this.subtopicCheckboxes);
		}

		// Logic for when topic checkboxes are clicked
		// Return the topic associated with a checkbox
		getTopic(checkbox) {
			const parent = checkbox.parentElement;
			const classElement = parent.querySelector("label");
			return classElement.htmlFor;
		}

		// Change the check of all checkboxes with the same topic
		changeCheck(checkbox) {
			const topic = this.getTopic(checkbox);
			const checkboxes = Array.from(document.getElementsByClassName(topic));

			for (const box of checkboxes) {
				box.checked = checkbox.checked;
			}
		}

		// Assign event listeners to all topic checkboxes and labels
		assignTopicEventListeners() {
			for (const box of this.topicCheckboxes) {
				const boxLabel = box.parentElement.querySelector("label");
				box.addEventListener("click", () => {
					this.changeCheck(box);
				});

				boxLabel.addEventListener("click", () => {
					this.changeCheck(box);
				});
			}
		}

		// Logic for when subtopic checkboxes are clicked
		// Return the topic checkbox of hte clicked subtopic checkbox
		getTopicBox(checkbox) {
			const topic = checkbox.classList[1] + " " + checkbox.classList[2];
			return document.getElementById(topic);
		}

		// Return the subtopic checkboxes of the clicked checkbox
		getSubtopicBoxes(checkbox) {
			const topic = checkbox.classList[1];
			return Array.from(document.getElementsByClassName(topic));
		}

		// Change the topic boxes checked state
		changeTopicBox(checkbox) {
			const topicBox = this.getTopicBox(checkbox);
			const subtopicBoxList = this.getSubtopicBoxes(checkbox);

			for (const subtopicBox of subtopicBoxList) {
				if (!subtopicBox.checked) {
					topicBox.checked = false;
					return "";
				}
			}

			topicBox.checked = true;
		}

		assignSubtopicEventListeners() {
			for (const checkbox of this.subtopicCheckboxes) {
				checkbox.addEventListener("click", () => {
					this.changeTopicBox(checkbox);
				});
			}
		}
	}

	new CaretLogic(carets);
	new CheckboxLogic(topicCheckboxes, subtopicCheckboxes);
});
