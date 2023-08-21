"use strict"
for(let form_elem of document.querySelectorAll('form div'))
    {
        for(let input_elem of form_elem.childNodes)
            if(input_elem.nodeName === 'TEXTAREA' ||  input_elem.nodeName === 'INPUT')
                input_elem.classList.add('form-control')
    }
let error_lists = document.querySelectorAll('.errorlist');
for(let err_lst of error_lists){
    err_lst.style.listStyleType = 'none';
}
const tx = document.querySelectorAll("form textarea");

for (let i = 0; i < tx.length; i++) {

  tx[i].setAttribute("style", "height:" + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = 0;
  this.style.height = (this.scrollHeight) + "px";
}
let clear_button = document.getElementsByClassName('clear-button');
if(clear_button[0]) {
    clear_button[0].addEventListener('click', () => {
        let input_elements = document.getElementsByTagName('input');
        let text_elements = document.getElementsByTagName('textarea');
        for (let input of input_elements) {
            input.value = '';
        }
        for (let text of text_elements) {
            text.value = '';
        }
    });
}
let avatar = document.getElementById('id_avatar');
let avatar_img = document.getElementById('avatar-preload');
if(avatar) {
    avatar.addEventListener('change', (event) => {
        const avatar_file = avatar.files;
        if (avatar_file) {
            avatar_img.src = URL.createObjectURL(new Blob(avatar_file));
        }
    });
}

let select_menu = document.querySelectorAll('.login-form select')
if(select_menu) {
    for (let select of select_menu) {
        select.classList.add('form-select')
    }
}
