var placeholderValues = {};

function clearPlaceholder(input) {
  var placeholder = input.getAttribute('placeholder');
  placeholderValues[input.id] = placeholder;
  input.placeholder = '';
}

function restorePlaceholder(input) {
  var placeholder = placeholderValues[input.id];
  input.placeholder = placeholder;
}


document.addEventListener('DOMContentLoaded', function() {
  var checkbox = document.getElementById('checkbox');
  var message = document.getElementById('message');

  if (!checkbox.checked) {
    displayErrorMessage();
  }

  checkbox.addEventListener('change', function() {
    if (!checkbox.checked) {
      displayErrorMessage();
    } else {
      hideErrorMessage();
    }
  });

  function displayErrorMessage() {
    message.textContent = 'You need to accept User Agreement';
  }

  function hideErrorMessage() {
    message.textContent = '';
  }
});

window.addEventListener("load", function() {
  var menuIcon = document.getElementById("menu-icon");
  var popupMenu = document.getElementById("popup-menu");

  menuIcon.addEventListener("click", function() {
    if (popupMenu.style.display === "none" || popupMenu.style.display === "") {
      popupMenu.style.display = "block";
    } else {
      popupMenu.style.display = "none";
    }
  });
});
