// Get the hamburger icon and mobile menu elements
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');

// Toggle both the mobile menu and the hamburger icon itself
hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('active');
});
