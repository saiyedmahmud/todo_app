const message = document.querySelector('.msg');


if (message) {

   setTimeout(() => {
     message.classList.add("d-none");
   }, 3000);
   
}