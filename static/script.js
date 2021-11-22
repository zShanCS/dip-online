console.log('hello world')
const send = document.querySelector('#send')
const form = document.querySelector('#myform')
const show = document.querySelector('#show')
const loadmore = document.querySelector('#loadmore')
let page = 0;
console.log(form);

const load_images = async ()=>{
    page = page+1
    const body = new FormData(form)
    body.append('resultLimit',page*20)
    const res = await fetch('/uploadFile', {
        method: 'POST',
        body
    })
    const images = await res.json();
    
    data = images.map(i => `<img src="/images/${i}.png" alt='images ${i}' />`)
    show.innerHTML = data.join('')
    loadmore.hidden = false
}
form.addEventListener('submit', async(e) => {
    console.log(form)
    e.preventDefault();
    console.log('someone tried to submit the form')
    load_images()
});
loadmore.addEventListener('click',load_images)
