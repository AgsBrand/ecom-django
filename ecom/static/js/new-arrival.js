let products = document.getElementById("products")
let productsHtml = ""
fetch("http://127.0.0.1:8000/get-products/new-arrival")
    .then(resp => {
        return resp.json()
    })
    .then(res => {
        updateDom(res)
    })

function updateDom(data) {
    let jsonData = JSON.parse(data)

    // Making the html for poducts div 
    for (let i = 0; i < jsonData.length; i++) {
        const element = jsonData[i];
        let productId = element.pk
        let title = element.fields.title
        let desc = element.fields.desc
        let product_img = element.fields.product_img
        let price = element.fields.price
        let availability = element.fields.availability

        productsHtml += `
        <div class="product">
        <a href="/product/${productId}">
        <div class="animator">
        <button>See Details</button>
        </div>
        <div class="product-top">
        <img src="/media/${product_img}" alt="">
        </div>
        <div class="product-bottom">
        <h1>${title}</h1>
                <p>${desc}</p>
                <div class="price-available">
                <p class="price">${price}$</p>
                <p class="availability">${availability}</p>
                </div>
                
                </div>
                </a>
                </div>
                `

    }
    // Sending all the html into products div
    products.innerHTML = productsHtml
}