document.addEventListener("DOMContentLoaded", () => {
	const container = document.getElementById('card-div');
	const cards = Array.from(container.querySelectorAll('.card'));
	let index = 0

	// Move to display the next card
	function displayNextCard() {
		if (index < 2) { // Last card should reset
			index++;
			const nextCard = cards[index];
			container.scrollTo({
				left: nextCard.offsetLeft,
				behavior: 'smooth'
			});
		} else {
			index = 0;
			const startCard = cards[index];
			container.scrollTo({
				left: startCard.offsetLeft,
				behavior: 'smooth'
			});
		}
	}

	// Scroll the cards automatically
    function autoScroll() {
		setTimeout(() => {
			displayNextCard();
			autoScroll();
		}, 2500);
	}

	// Is the user on mobile?
	function isMobile() {
		return window.matchMedia('(max-width: 768px)').matches;
	}
	
	if (isMobile()) {
		autoScroll();
	}
});
