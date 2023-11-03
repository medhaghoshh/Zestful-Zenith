// var leafImg = document.getElementById("leaf-img-js")
// var uploadedFile = document.getElementById("upload-file-js")
// function setImage(){
//     console.log("I am alive")
//     console.log(leafImg.src)
//     console.log(uploadedFile.value)
//     var uploadFileValue = uploadedFile.value
//     var modUploadFile = uploadFileValue.replaceAll("\\","/")
//     console.log(modUploadFile)
//     leafImg.src="./image/java.jpg"
// }

var plant={
    
    Neem: {
        Description: "A large evergreen tree with compound leaves and white flowers.",
        MedicalBenefits: [
          "Natural pesticide and insect repellent",
          "Antibacterial and antifungal properties",
          "Treats skin conditions like acne and eczema"
         ]
       }

}

const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");

var plantName=document.getElementById("plant-name-js")
var plantApper=document.getElementById("plant-appear-js")
var plantBenifit=document.getElementById("plant-benifit-js")
// var plantRemedies=document.getElementById("plant-remedies-js")

inputFile.addEventListener("change", uploadImage);


function uploadImage(){
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = `url(${imgLink})`;
    imageView.textContent = "";
    imageView.style.border = 0;

}

dropArea.addEventListener("dragover", function(e){
    e.preventDefault();
}
);

dropArea.addEventListener("drop", function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
});

//Hard coded leave name , actual leave name should be coming from ML model

function plantDescription(){
	plantName.innerHTML+="Neem"
}
    
       
    

