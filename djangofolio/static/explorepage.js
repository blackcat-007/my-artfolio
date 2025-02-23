function reveal() {
  var reveals = document.querySelectorAll(".reveal2");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;
    console.log("hello");

    if (elementTop < windowHeight-elementVisible) {
      reveals[i].classList.add("active");
      
    } 
    
  }
}

window.addEventListener("scroll", reveal);