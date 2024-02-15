document.getElementById("sendButton").addEventListener("click", function() {
  var checkboxes = document.querySelectorAll('input[name="genre"]:checked');
  var selectedGenres = [];
  checkboxes.forEach(function(checkbox) {
    selectedGenres.push(checkbox.value);
  });
  document.getElementById("selectedGenresInput").value = selectedGenres.join(",");
});
