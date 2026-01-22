document.addEventListener('DOMContentLoaded', () => {
	const momentumData = window.appData.momentum_data;
	const bars = Array.from(document.getElementsByClassName('bar'));
	

	// Adjust the width of given momentum bar
	function adjustBarWidth(bar, percent) {
		bar.style.width = `${percent}%`;
		
		if (percent !== 100) {
			bar.style.borderTopRightRadius = '0px';
			bar.style.borderBottomRightRadius = '0px';
		}
	}

	// Adjust the width of every momentum bar
	bars.forEach((bar) => {
		const id = bar.id;
		const percent = momentumData[id];
		adjustBarWidth(bar, percent);
	});
});
