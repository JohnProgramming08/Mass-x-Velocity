document.addEventListener("DOMContentLoaded", () => {
	const usernameEntry = document.getElementById("username");
	const bioEntry = document.getElementById("bio");
	const bio = window.appData.bio;
	const username = window.appData.user_name;

	bioEntry.value = bio;
	usernameEntry.value = username;
});