document.addEventListener('DOMContentLoaded', () => {
	const momentumData = window.appData.momentum_data;
	const bars = Array.from(document.getElementsByClassName('bar'));
	

	// Adjust the width of given momentum bar
	function adjustBarWidth(bar, percent) {
		bar.style.width = `${percent}%`;
	}

	// Adjust the width of every momentum bar
	bars.forEach((bar) => {
		const id = bar.id;
		const percent = momentumData[id];
		adjustBarWidth(bar, percent);
	});
});
