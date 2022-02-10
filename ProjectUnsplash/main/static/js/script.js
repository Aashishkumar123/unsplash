const dropArea = document.querySelector('.drag-area');
const dragText = document.querySelector('.header');
const imgdroparea = document.querySelector('.img-drop-area'); 
const photoDetail = document.querySelector('.photo-details');

let button = dropArea.querySelector('.button');
let input = dropArea.querySelector('input');

let file;
let fileURL;

button.onclick = () => {
  input.click();
};

// when browse
input.addEventListener('change', function () {
  file = this.files[0];
  dropArea.classList.add('active');
  displayFile();
});

// when file is inside drag area
dropArea.addEventListener('dragover', (event) => {
  event.preventDefault();
  dropArea.classList.add('active');
  dragText.textContent = 'Release to Upload';
  // console.log('File is inside the drag area');
});

// when file leave the drag area
dropArea.addEventListener('dragleave', () => {
  dropArea.classList.remove('active');
  // console.log('File left the drag area');
  dragText.textContent = 'Drag & Drop';
});

// when file is dropped
dropArea.addEventListener('drop', (event) => {
  event.preventDefault();
  // console.log('File is dropped in drag area');

  file = event.dataTransfer.files[0]; // grab single file even of user selects multiple files
  // console.log(file);
  displayFile();
});

function displayFile() {
  let fileType = file.type;
  // console.log(fileType);

  let validExtensions = ['image/jpeg', 'image/jpg', 'image/png'];

  if (validExtensions.includes(fileType)) {
    // console.log('This is an image file');
    let fileReader = new FileReader();

    fileReader.onload = () => {
        fileURL = fileReader.result;
    //   console.log(fileURL);
      let imgTag = `<img src="${fileURL}" alt="">`;
      imgdroparea.innerHTML = imgTag;
      dropArea.classList = 'photo-details';
      photoDetail.classList = 'show-photo-details';

    };
    fileReader.readAsDataURL(file);
  } else {
    alert('This is not an Image File');
    imgdroparea.classList.remove('active');
  }
}



