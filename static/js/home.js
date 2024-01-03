const rightcont = document.querySelector('.rightcont')
const parent = document.querySelector('.parent')
const navbar = document.querySelector('.nav')
const about = document.querySelector('.abtimg')
const search =document.querySelector('.search')
const ham = document.querySelector('.ham')
const logohead = document.querySelector('.logohead')
const slider = document.querySelector('.slider-wrap')
const icon = document.querySelector('.icon')
const button = document.querySelector('.ctabutton')
const span1 = document.querySelector('.span1')
const span2 = document.querySelector('.span2')
const span3 = document.querySelector('.span3')
const mobilenav = document.querySelector('.mobilenav')

const jbimg1 = document.querySelector('.jbimg')
const jbimg2 = document.querySelector('.jbimg2')
rightcont.addEventListener('click', ()=>{
    jbimg1.classList.toggle('jbimg')
    jbimg1.classList.toggle('jbimg2')    

    jbimg2.classList.toggle('jbimg2')
    jbimg2.classList.toggle('jbimg')
})

ham.addEventListener('click', ()=>{
  span1.classList.toggle('mobile')
  span2.classList.toggle('mobile')
  span3.classList.toggle('mobile')

  mobilenav.classList.toggle('mobile')
})

var swiper = new Swiper(".swiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 3,
      slideShadows: true,
    },
    keyboard: {
      enabled: true,
    },
    mousewheel: {
      thresholdDelta: 70,
    },
    loop: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      640: {
        slidesPerView: 2
      },
      768: {
        slidesPerView: 2
      },
      1024: {
        slidesPerView: 3
      },
      1560: {
        slidesPerView: 3
      }
    }

  });

  button.addEventListener('mouseover', ()=>{
    console.log("sdf")
    icon.classList.toggle('active')
    setTimeout(()=>{
      icon.classList.toggle('active')
    },500)
  })
  