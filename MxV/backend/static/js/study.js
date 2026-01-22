document.addEventListener('DOMContentLoaded', () => {
	const momentum = window.appData.momentum;
	const questionInfoDisplay = document.getElementById('question-info');
	if (momentum == 0) {
		questionInfoDisplay.style.backgroundColor = '#ff0011';
	} else if (momentum > 0) {
		questionInfoDisplay.style.backgroundColor = 'green';
	}
});