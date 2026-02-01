document.addEventListener("DOMContentLoaded", () => {
	const reveals = Array.from(document.getElementsByClassName("reveal"));

	const observer = new IntersectionObserver(
		(entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					entry.target.classList.add("active");
				}
			});
		},
		{
			threshold: 0.1,
		},
	);

	reveals.forEach((el) => observer.observe(el));
});
