let lesson = document.getElementById("lesson").value;
lesson = JSON.parse(lesson);
console.log(lesson);

const tl = [];
lesson.conversation.forEach((en, i) => {
  console.log(i);
  tl.push(
    Object.assign(
      {},
      { en: en, tr: lesson.translation[i], ar: lesson.arabic[i] }
    )
  );
});
let theLesson = ``;
tl.forEach((mes, i) => {
  const en = mes.en;
  const ar = mes.ar;
  const tr = mes.tr;
  if (mes.en === undefined) {
    return (theLesson += `
  <div class="translation">
      <p>${tr}</p>
      <button onclick="playTrans('${lesson.title}','${i}')" class="playTrans">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
  <div class="arabic">
      <p>${ar}</p>
      <button onclick="playAr('${lesson.title}','${i}')" class="playMessage">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
`);
  }
  if (mes.tr === undefined) {
    return (theLesson += `
  <div class="message">
      <p>${en}</p>
      <button onclick="playMessage('${lesson.title}','${i}')" class="playMessage">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
  <div class="arabic">
      <p>${ar}</p>
      <button onclick="playAr('${lesson.title}','${i}')" class="playMessage">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
`);
  }
  if (mes.ar === undefined) {
    return (theLesson += `
  <div class="message">
      <p>${en}</p>
      <button onclick="playMessage('${lesson.title}','${i}')" class="playMessage">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
  <div class="translation">
      <p>${tr}</p>
      <button onclick="playTrans('${lesson.title}','${i}')" class="playTrans">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
`);
  }
  return (theLesson += `
  <div class="message">
      <p>${en}</p>
      <button onclick="playMessage('${lesson.title}','${i}')" class="playMessage">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
  <div class="translation">
      <p>${tr}</p>
      <button onclick="playTrans('${lesson.title}','${i}')" class="playTrans">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
  <div class="arabic">
      <p>${ar}</p>
      <button onclick="playAr('${lesson.title}','${i}')" class="playMessage">
        <i class="bx bx-volume-full"></i>
      </button>
  </div>
  `);
});

const html = document.querySelector(".theLesson");
html.innerHTML = theLesson;

console.log(tl);

/* document.addEventListener("DOMContentLoaded", () => {
        const play = document.getElementById("play");

        play.click();
      });*/
