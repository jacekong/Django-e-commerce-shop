// menu bar
function menuToggole(icon) {
    var x = document.getElementById("menu-box");
    if (x.style.display == "block") {
        icon.classList.toggle("fa-times");
        x.style.display = "none";
    } else {
        icon.classList.toggle("fa-times");
        x.style.display = "block";
    }
}

// go to top
// Get the button
let mybutton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function goTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// image slider
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("bar");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}

var slideshowContainer = document.querySelector('.slideshow-container');
// Add event listeners for keyboard navigation
document.addEventListener('keydown', function(event) {
  if (event.key === 'ArrowLeft') {
    plusSlides(-1);
  } else if (event.key === 'ArrowRight') {
    plusSlides(1);
  }
});

// Enable touch swipe gesture
var hammer = new Hammer(slideshowContainer);
hammer.on('swipeleft', function () {
  plusSlides(1);
});

hammer.on('swiperight', function () {
  plusSlides(-1);
});

// popup window
let popup = document.getElementById('popup');

function openPopup() {
  popup.classList.add("open-popup");
}
function closePopup() {
  popup.classList.remove("open-popup");
}

// open error
let openerror = document.getElementById('open-error');
function openError() {
  openerror.classList.add("open-error");
}


// share function
function shareTosocial() {
  var currentURL = window.location.href;

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(currentURL)
      .then(function() {
        console.log('URL copied to clipboard!');
        showCopiedMessage();
      })
      .catch(function(err) {
        console.error('Failed to copy URL to clipboard!', err);
        showFallbackMessage();
      });
  } else {
    showFallbackMessage();
  }

}

function showCopiedMessage() {
  // Display a message indicating that the URL has been copied
  alert('URL copied to clipboard!');
}

function showFallbackMessage() {
  // Display a fallback message with instructions for manual copying
  var fallbackMessage = 'To copy the URL, please manually select and copy it from the address bar.';
  alert(fallbackMessage);
}


// login validation
function checkStuff() {
  var email = document.adminloginform.email;
  var password = document.form1.password;
  var msg = document.getElementById('msg');
  
  if (email.value == "") {
    msg.style.display = 'block';
    msg.innerHTML = "Please enter your email";
    email.focus();
    return false;
  } else {
    msg.innerHTML = "";
  }
  
   if (password.value == "") {
    msg.innerHTML = "Please enter your password";
    password.focus();
    return false;
  } else {
    msg.innerHTML = "";
  }
   var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (!re.test(email.value)) {
    msg.innerHTML = "Please enter a valid email";
    email.focus();
    return false;
  } else {
    msg.innerHTML = "";
  }
}

// open to add category
let categoryPop = document.getElementById('categoryPop');

function openAddCategory() {
  categoryPop.classList.add("open-popup-category");
}
function closeAddCategory() {
  categoryPop.classList.remove("open-popup-category");
}
