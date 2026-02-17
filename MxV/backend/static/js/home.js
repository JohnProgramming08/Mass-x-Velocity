document.addEventListener("DOMContentLoaded", () => {
	const momentumData = window.appData.momentum_data;
	const userData = window.appData.user_data;
	const answerData = window.appData.answer_data;
	const bars = Array.from(document.getElementsByClassName("bar"));
	const achievementsTable = document.getElementById("achievements-table");

	// Adjust the width of given momentum bar
	function adjustBarWidth(bar, percent) {
		bar.style.width = `${percent}%`;

		if (percent !== 100) {
			bar.style.borderTopRightRadius = "0px";
			bar.style.borderBottomRightRadius = "0px";
		}
	}

	// Adjust the width of every momentum bar
	bars.forEach((bar) => {
		const id = bar.id;
		const percent = momentumData[id];
		adjustBarWidth(bar, percent);
	});

	// All of the achievements a user can get
	// Name, condition, filepath
	const achievements = [
		["Getting Started", answerData.total >= 1, "getting_started.jpg"],
		["Dedicated Student", answerData.total >= 100, "dedicated_student.jpg"],
		["Seriously?", answerData.total >= 1000, "seriously.jpg"],
		["Sigma", momentumData.total >= 67, "sigma.jpg"],
		["Exam Prepped", momentumData.exam2 >= 100, "exam_prepped.jpg"]
	];

	// Display all of the users achievements
	function displayAchievements() {
		for (const achievement of achievements) {
			if (achievement[1]) {
				const temp = `<img class="achievement-img" title="${achievement[0]}" src="/static/images/achievements/${achievement[2]}"/>`
				achievementsTable.innerHTML += temp;			
			}
		}
	}

	displayAchievements();
});
