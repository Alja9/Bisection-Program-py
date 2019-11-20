Kalo mau sekalian autofill kotak sarannya 

window.els = document.querySelectorAll('input[type=radio]')

for (let i = 0; i < els.length / 5; i++) {
  let rand = Math.floor(Math.random() * 3) + 2
  window.els.item(i * 5 + rand).checked = true 
}

const katas = ['Terima Kasih telah membimbing saya', 'Sangat Memotivasi dan Membantu Belajar', 'Ramah dan Murah Senyum', 'Terima Kasih', 'Semoga Diajar lagi semester depan']
document.getElementById('saran').value = katas[Math.floor(Math.random() * 3)]
