// script.js

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

document.getElementById("sendButton").addEventListener("click", function() {
  var checkboxes = document.querySelectorAll('input[name="genre"]:checked');
  var selectedGenres = [];
  checkboxes.forEach(function(checkbox) {
    selectedGenres.push(checkbox.value);
  });
  document.getElementById("selectedGenres").innerText = "Selected genres: " + selectedGenres.join(", ");
});
