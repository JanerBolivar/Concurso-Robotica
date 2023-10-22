// JavaScript para controlar la posición del menú desplegable
const navbarToggler = document.getElementById('navbarToggler');
const customDropdownMenu = document.getElementById('customDropdownMenu');

navbarToggler.addEventListener('click', function() {
  const rect = navbarToggler.getBoundingClientRect();
  const spaceRight = window.innerWidth - rect.right;
  
  if (spaceRight < customDropdownMenu.offsetWidth) {
    customDropdownMenu.style.left = 'auto';
    customDropdownMenu.style.right = '0';
  } else {
    customDropdownMenu.style.left = '0';
    customDropdownMenu.style.right = 'auto';
  }
});
