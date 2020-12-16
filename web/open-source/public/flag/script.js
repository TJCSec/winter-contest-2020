if (!localStorage.getItem('jwt')) {
  window.location.replace('../');
}

function logOut() {
  localStorage.removeItem('jwt');
  window.location.replace('../');
}

async function getFlag() {
  const jwt = localStorage.getItem('jwt');
  const flagTxt = document.getElementById('flag');

  const res = await fetch('../api/flag', {
    method: 'GET',
    headers: {
      authorization: jwt,
    },
    credentials: 'same-origin',
  });

  const json = await res.json();

  if (res.status !== 200 || !json) {
    flagTxt.innerText = 'Woah! Invalid JWT. Logging you out in 3 sec.';
    setTimeout(() => {
      logOut();
    }, 3000);
  }

  if (json.flag) {
    flagTxt.innerText = json.flag;
  }
}

getFlag();
document.getElementById('logout').addEventListener('click', () => logOut());
