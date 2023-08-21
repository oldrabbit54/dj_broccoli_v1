// let list_of_categories = [];
// let ul_of_categories = document.createElement('ul');
// for(let cat of categories){
//     let li = document.createElement('li');
//     li.innerHTML = `<p>${cat.name}</p>` + '<br>' + `${cat.description}`;
//     li.id = list_of_categories.length;
//     li.classList.add('features');
//    list_of_categories.push(li);
// }
// ul_of_categories.append(list_of_categories[0]);
// document.body.append(ul_of_categories);
// function illustrate_next(event){
//     let li_elem = ul_of_categories.children[0];
//     let next_id = ((+li_elem.id + 1)%list_of_categories.length);
//     li_elem.replaceWith(list_of_categories[next_id%list_of_categories.length]);
// }
// function illustrate_back(event){
//     let li_elem = ul_of_categories.children[0];
//     let back_id = +li_elem.id - 1 >= 0 ? +li_elem.id - 1 : list_of_categories.length - 1;
//     li_elem.replaceWith(list_of_categories[back_id%list_of_categories.length]);
// }
//
// let next_switcher = document.createElement('button');
// let back_switcher = document.createElement('button');
// let div_switch = document.createElement('div');
// next_switcher.addEventListener('mousedown',
//     (event) => {event.currentTarget.style.backgroundColor = 'darkred'});
// back_switcher.addEventListener('mousedown',
//     (event) => {event.currentTarget.style.backgroundColor = 'darkred'});
// next_switcher.addEventListener('mouseup',
//     (event) => {event.currentTarget.style.backgroundColor = 'limegreen'});
// back_switcher.addEventListener('mouseup',
//     (event) => {event.currentTarget.style.backgroundColor = 'limegreen'});
// next_switcher.addEventListener('mouseleave',
//     (event) => {event.currentTarget.style.backgroundColor = 'limegreen'});
// back_switcher.addEventListener('mouseleave',
//     (event) => {event.currentTarget.style.backgroundColor = 'limegreen'});
// ([next_switcher.innerHTML, back_switcher.innerHTML] = ['Next', 'Back']);
// div_switch.classList.add('switch_button_container');
// ul_of_categories.after(div_switch);
// div_switch.append(back_switcher, next_switcher);
// for(let li of list_of_categories){
//     let p_tag = li.children[0];
//     p_tag.classList.add('feature_topic');
// }
//
// back_switcher.classList.add('switch_buttons');
// next_switcher.classList.add('switch_buttons');
// back_switcher.addEventListener('click', illustrate_back);
// next_switcher.addEventListener('click', illustrate_next);
// next_switcher.addEventListener('mouseenter', button_zoom);
// next_switcher.addEventListener('mouseleave', button_unzoom);
// back_switcher.addEventListener('mouseenter', button_zoom);
// back_switcher.addEventListener('mouseleave', button_unzoom);
// function button_zoom(event){
//     event.currentTarget.style.transform = 'scaleX(1.2) scaleY(1.2)';
//     event.currentTarget.style.transition = '0.5s';
// }
// function button_unzoom(event){
//     event.currentTarget.style.transform = 'scaleX(1) scaleY(1)';
//     event.currentTarget.style.transition = '0.5s';
// }
//
// let goto_list_buttons = document.createElement('ul');
// for(let li of list_of_categories){
//     let goto_id = +li.id;
//     let goto_button = document.createElement('button');
//     goto_button.innerHTML = 'button' + goto_id;
//     goto_button.addEventListener('click', (event) =>
//     {
//         let replacent = document.getElementById(`${goto_id}`);
//         document.querySelector('li.features').replaceWith(replacent);
//         console.log(document.querySelector('li.features'), replacent);
//     })
//     goto_list_buttons.append(goto_button);
// }
// console.log(document.querySelector('.switch_button_container').firstChild);
// document.querySelector('.switch_button_container').firstChild.after(goto_list_buttons);
//
//
//
//
let list_of_categories = document.createElement('ul');
for(let cat of categories){
    let li = document.createElement('li');
    li.innerHTML = `<p>${cat.name}</p>` + '<br>' + cat.description;
    li.classList.add('features');
    list_of_categories.append(li);
    li.style.display = 'none';
}
let div_list_container = document.createElement('div');
div_list_container.classList.add('div_list_container');
div_list_container.append(list_of_categories);
document.body.append(div_list_container);


list_of_categories.children[0].style.display = 'block';
for(let li of list_of_categories.children){
    li.children[0].classList.add('feature_topic');
}

let [back_button, next_button] = [document.createElement('button'), document.createElement('button')];
back_button.innerHTML = 'Back';
next_button.innerHTML = 'Next';
for(let button of [back_button, next_button]){
    button.classList.add('switch_buttons');
}


let div_switch_button_container = document.createElement('div');
div_switch_button_container.classList.add('switch_button_container');
div_switch_button_container.append(back_button, next_button);
document.body.append(div_switch_button_container);


next_button.addEventListener('click', () => {
        let current_li = Array.from(list_of_categories.children).find(
            (item) => {
                return item.style.display === 'block';
            }
        );
        current_li.style.display = 'none';
        if(current_li.nextSibling){
            current_li.nextSibling.style.display = 'block';
        }
        else{
            list_of_categories.firstChild.style.display = 'block';
        }
});
back_button.addEventListener('click', () => {
        let current_li = Array.from(list_of_categories.children).find(
            (item) => {
                return item.style.display === 'block';
            }
        );
        current_li.style.display = 'none';
        if(current_li.previousSibling){
            current_li.previousSibling.style.display = 'block';
        }
        else{
            list_of_categories.lastChild.style.display = 'block';
        }
});


next_button.addEventListener('mouseenter', (event) => {
    event.currentTarget.style.transform = 'scaleX(1.2) scaleY(1.2)';
    event.currentTarget.style.transition = '0.5s';
});
back_button.addEventListener('mouseenter', (event) => {
    event.currentTarget.style.transform = 'scaleX(1.2) scaleY(1.2)';
    event.currentTarget.style.transition = '0.5s';
});


next_button.addEventListener('mouseleave', (event) => {
    event.currentTarget.style.transform = 'scaleX(1) scaleY(1)';
    event.currentTarget.style.transition = '0.5s';
    event.currentTarget.style.backgroundColor = 'limegreen';
});
back_button.addEventListener('mouseleave', (event) => {
    event.currentTarget.style.transform = 'scaleX(1) scaleY(1)';
    event.currentTarget.style.transition = '0.5s';
    event.currentTarget.style.backgroundColor = 'limegreen';
});


next_button.addEventListener('mousedown',
    (event) => {event.currentTarget.style.backgroundColor = 'darkred'});
back_button.addEventListener('mousedown',
    (event) => {event.currentTarget.style.backgroundColor = 'darkred'});
next_button.addEventListener('mouseup',
    (event) => {event.currentTarget.style.backgroundColor = 'limegreen'});
back_button.addEventListener('mouseup',
    (event) => {event.currentTarget.style.backgroundColor = 'limegreen'});

let goto_buttons = [];

for(let i = 0;i < list_of_categories.children.length;i++){
    let button = document.createElement('button');
    button.classList.add('switch_buttons');
    button.classList.add('goto_buttons');
    button.innerHTML = '<br>';
    goto_buttons.push(button);
    button.addEventListener('click', (event) => {
        let current_li = Array.from(list_of_categories.children).find(
            (item) => {
                return item.style.display === 'block';
            }
        );
        current_li.style.display = 'none';
        let to_li = list_of_categories.children[i];
        to_li.style.display = 'block';
})
    //div_switch_button_container.append(button);
    button.addEventListener('mouseenter', event => event.currentTarget.style.backgroundColor = 'darkred');
    button.addEventListener('mouseleave', event => event.currentTarget.style.backgroundColor = 'limegreen');
}
back_button.after(...goto_buttons);

