let openmenu = document.getElementById("openmenu")
let mobilemenu = document.getElementById("mobile-links-side")
let closemenu = document.getElementById("closemenu")

openmenu.addEventListener("click",()=>{

    mobilemenu.style.display="block"
    mobilemenu.style.right="0px"

})

closemenu.addEventListener("click",()=>{

    mobilemenu.style.right="-300px"
    mobilemenu.style.display="none"
})

console.log(openmenu);
console.log(mobilemenu);



window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

document.addEventListener('mousemove', (event) => {
    const cursor = document.getElementById('cursor');
    cursor.style.transform = `translate(${event.clientX}px, ${event.clientY}px)`;
 });



// Get all the nav links
const navLinks = document.querySelectorAll('.navbar-link');

// Add click event listener to each link
navLinks.forEach(link => {
  link.addEventListener('click', function() {
    // Remove 'active' class from all links
    navLinks.forEach(link => link.classList.remove('active'));
    // Add 'active' class to the clicked link
    this.classList.add('active');
  });
});






