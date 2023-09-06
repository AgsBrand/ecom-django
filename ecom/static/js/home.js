console.log("working")

// All the images links Array 
let slides = ["static/images/1.jpg", "static/images/2.jpg", "static/images/3.jpg", "static/images/4.jpg", "static/images/5.jpg"]

let slidesWithClass = document.getElementsByClassName("slide")
// Current slide variable 
let currentSlide = 0

// Function that will change the slide 


// Getting the main div in which all slide images are 
let carousel = document.getElementById("carousel")

// Rendering all the slides into the dom 
let htmlDiv = ``
for (let i = 0; i < slides.length; i++) {
    if (i == 0) {
        htmlDiv += `<img src="${slides[i]}" alt="Image" class="slide active-slide">`
    } else {
        htmlDiv += `<img src="${slides[i]}" alt="" class="slide">`
    }
}
carousel.innerHTML = htmlDiv

// Handling the next and previous buttons
const goNextSlide = () => {
    changeSlide(currentSlide + 1)
}
const goPrevSlide = () => {
    changeSlide(currentSlide - 1)
}

const changeSlide = (goTo) => {
    console.log("called")
    if (goTo >= slides.length) {
        goTo = 0
    }
    if (goTo <= -1) {
        goTo = slides.length - 1
    }
    console.log(slidesWithClass)
    console.log(currentSlide)
    console.log(goTo)
    slidesWithClass[currentSlide].classList.toggle("active-slide")
    slidesWithClass[goTo].classList.toggle("active-slide")
    currentSlide = goTo
}


setInterval(() => {
    document.body.onload(changeSlide(currentSlide+1)) 
}, 4000);


