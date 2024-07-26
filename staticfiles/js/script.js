const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");


nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        }
    })
})

function toggleOccupationType() {
    var categorySelect = document.getElementById("role");
    var occupationTypeDiv = document.getElementById("descriptionField");
    var serviceTypeOption = document.getElementById("service-type")
  
    if (categorySelect.value === "service provider") {
      occupationTypeDiv.style.display = "flex";
      serviceTypeOption.style.display = "flex";
    } else {
      serviceTypeOption.style.display = "none";
      occupationTypeDiv.style.display = "none";
    }
  }
  

backBtn.addEventListener("click", () => form.classList.remove('secActive'));




// function toggleOccupationType() {
//     var category = document.getElementById("role");
//     var descriptionField = document.getElementById("descriptionField");
//     if (category.value === "service provider") {
//         descriptionField.style.display = "block";
//     } else {
//         descriptionField.style.display = "none";
//     }
// }