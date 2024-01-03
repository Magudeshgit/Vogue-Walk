const ham = document.querySelector('.ham')
const span1 = document.querySelector('.span1')
const span2 = document.querySelector('.span2')
const span3 = document.querySelector('.span3')
const mobilenav = document.querySelector('.mobilenav')

ham.addEventListener('click', ()=>{
    span1.classList.toggle('mobile')
    span2.classList.toggle('mobile')
    span3.classList.toggle('mobile')
  
    mobilenav.classList.toggle('mobile')
  })

