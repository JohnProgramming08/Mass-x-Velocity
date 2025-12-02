document.addEventListener('DOMContentLoaded', () => {
    const body = document.querySelector('body');
    const loginBtn = document.getElementById('log-in-btn');
    const signupBtn = document.getElementById('sign-up-btn');

    let state = document.querySelector('main').id === 'signup' ? 'signup' : 'login';

    // show a specific form (left = login, right = signup)
    function showForm(target) {
        const maxScrollLeft = Math.max(0, body.scrollWidth - body.clientWidth);
        if (target === 'signup') {
            body.scrollTo({ left: 0, behavior: 'smooth' });
            state = 'signup';
        } else {
            body.scrollTo({ left: maxScrollLeft, behavior: 'smooth' });
            state = 'login';
        }
    }

	// Add event listeners
    if (loginBtn) loginBtn.addEventListener('click', () => showForm('login'));
    if (signupBtn) signupBtn.addEventListener('click', () => showForm('signup'));

    showForm(state);
});