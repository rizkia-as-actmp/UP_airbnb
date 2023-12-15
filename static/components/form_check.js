class FromCheck extends HTMLElement {
    constructor() {
        super();

        this.id = this.getAttribute('id')
        this.name = this.getAttribute('name')
        this.label = this.getAttribute('label')
        this.render()
    }
    
    render() {
        this.outerHTML = `
            <div class="form-check">
                <input class="form-check-input" type="checkbox" name="${this.name}" value="${this.label}" id="${this.id}">
                <label class="form-check-label" for="${this.id}">
                    ${this.label}
                </label>
            </div>
        `;
    }
}
    
customElements.define('form-check', FromCheck);

