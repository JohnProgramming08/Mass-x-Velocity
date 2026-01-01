document.addEventListener('DOMContentLoaded', () => {
	const carets = Array.from(document.getElementsByClassName('caret'));
	const topicCheckboxes = Array.from(document.getElementsByClassName('topic'));
	const subtopicCheckboxes = Array.from(document.getElementsByClassName('subtopic'));

	// Get the class associated with each caret
	function getClass(caret) {
		const parent = caret.parentElement;
		const classElement = parent.querySelector('label');
		return classElement.htmlFor;
	}

	// Hide all associated checkboxes
	function hideCheckboxes(caret) {
		const topic = getClass(caret);
		const checkboxes = Array.from(document.getElementsByClassName(topic));
		
		for (const checkbox of checkboxes) {
			checkbox.parentElement.style.display = 'none';
		}

		caret.addEventListener('click', () => {
			showCheckboxes(caret);
		});
		caret.style.transform = 'rotate(180deg)';
	}

	// Show all associated checkboxes
	function showCheckboxes(caret) {
		const topic = getClass(caret);
		const checkboxes = Array.from(document.getElementsByClassName(topic));
		
		for (const checkbox of checkboxes) {
			checkbox.parentElement.style.display = 'flex';
		}

		caret.addEventListener('click', () => {
			hideCheckboxes(caret);
		});
		caret.style.transform = '';
	}

	// Assign event listeners to each caret
	for (const caret of carets) {
		caret.addEventListener('click', () => {
			hideCheckboxes(caret);
		});
	}

	// Change check of all checkboxes with the same topic
	function changeCheck(checkbox) {
		const topic = getClass(checkbox);
		const checkboxes = Array.from(document.getElementsByClassName(topic));

		for (const box of checkboxes) {
			box.checked = checkbox.checked;
		}
	}

	// Assign event listeners to checkboxes and labels
	for (const box of topicCheckboxes) {
		const boxLabel = box.parentElement.querySelector('label');
		box.addEventListener('click', () => {
			changeCheck(box);
		});

		boxLabel.addEventListener('click', () => {
			changeCheck(box);
		});
	}

	// Get the topic checkbox of the clicked subtopic checkbox
	function getTopicBox(box) {
		const topic = box.classList[1] + ' ' + box.classList[2];
		return document.getElementById(topic);
	}

	// Get the subtopic checkboxes of the clicked checkbox
	function getSubtopicBoxes(box) {
		const topic = box.classList[1];
		return Array.from(document.getElementsByClassName(topic));
	}

	// Change the topic boxes checked state
	function changeTopicBox(box) {
		const topicBox = getTopicBox(box);
		const boxList = getSubtopicBoxes(box);

		for (const subtopicBox of boxList) {
			if (!subtopicBox.checked) {
				topicBox.checked = false;
				return ''
			}
		}

		topicBox.checked = true;
	}

	// Assign event listeners to all subtopic checkboxes
	for (const box of subtopicCheckboxes) {
		box.addEventListener('click', () => {
			changeTopicBox(box);
		});
	}
});