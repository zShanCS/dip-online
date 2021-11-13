console.log('hello world')
const send = document.querySelector('button')[0]
const form = document.querySelector('#myform')
const show = document.querySelector('#show')
console.log(form);
form.addEventListener('submit', async(e) => {
    e.preventDefault();
    console.log('someone tried to submit the form')
    const res = await fetch('/uploadFile', {
        method: 'POST',
        body: new FormData(form)
    })
    const images = await res.json();
    data = images.map(i => `<img src="/images/${i}.png" />`)

    console.log(data)
    show.innerHTML = data.join('')
});