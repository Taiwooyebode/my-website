// NAV: switch to solid on scroll
(function () {
  const nav = document.getElementById('siteNav');
  function toggleNav() {
    if (window.scrollY > 60) nav.classList.add('navbar-solid'), nav.classList.remove('navbar-transparent');
    else nav.classList.add('navbar-transparent'), nav.classList.remove('navbar-solid');
  }
  toggleNav();
  window.addEventListener('scroll', toggleNav);
})();

// Simple reveal on scroll
(function(){
  const observer = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  }, {threshold: 0.12});

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
})();

// Contact form client-side validation (Bootstrap style)
(function(){
  const form = document.getElementById('contactForm');
  if (!form) return;
  form.addEventListener('submit', function(e){
    if (!form.checkValidity()){
      e.preventDefault();
      e.stopPropagation();
      form.classList.add('was-validated');
      return;
    }
    // allow submit (server handles)
  }, false);
})();
