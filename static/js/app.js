function addFormClasses() {
    const inputs = document.querySelectorAll('input')
    inputs.forEach(input => {
        input.classList.add('form-control')   
    });
    const labels = document.querySelectorAll('label')
    labels.forEach(label => {
        label.classList.add('form-control-label')   
    });
}