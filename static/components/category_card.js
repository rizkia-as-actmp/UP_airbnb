class CategoryCard extends HTMLElement {
    constructor() {
        super();

        this.path = this.getAttribute('path')
        this.title = this.getAttribute('title')
        this.render()
    }
    
    render() {
        this.outerHTML = `
        <div class="col g-3">
            <div class="card btn btn-outline-secondary">
                <div class="card-body d-flex gap-2">
                    <svg  xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24">
                        <path d="${this.path}"/>
                    </svg>
                    <h5 class="card-title">${this.title}</h5>
                </div>
            </div>
        </div>
        `;
    }
}
    
customElements.define('category-card', CategoryCard);

sites = {
    "owner" : "rizkia",
    "location" : "karimun, indonesia",
    "view" : "mountain and ocean view",
    "desc" : "*lorem lorem ipsum **lorem lorem ipsum",
    "price" : "1.000.000",
    "pictures" : ["link", "link", "link"],
    "facilities" : {
        "Hair dryer" : false,
        "Shampoo" : true,
        "Hot water" : false,
        "TV" : true,
        "Wifi"  : false
    },
    "reviewes" : [
        {
            "name" : "Marine",
            "date" : "October 2023",
            "star" : 4,
            "comments" : "First of all, I would like to thank you for hosting us and for providing us with friendly and helpful staff. Wonderful villa and great staff. Couldn't be more happy!w"
        }
    ]
} 