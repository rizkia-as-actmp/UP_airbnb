class FromRadio extends HTMLElement {
    constructor() {
        super();

        this.name = this.getAttribute('name')
        this.id = this.getAttribute('id')
        this.label = this.getAttribute('label')
        this.render()
    }
    
    render() {
        this.outerHTML = `
            <input class="form-check-input" type="radio" name="${this.name}" id="${this.id}" value="${this.label}">
            <label class="form-check-label" for="${this.id}">
                ${this.label}
            </label>
        `;
    }
}
    
customElements.define('form-radio', FromRadio);

