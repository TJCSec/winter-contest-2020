async function submitLogin(event) {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  const errorElement = document.getElementById('error');

  if (username.isEmpty || password.isEmpty) {
    return;
  }

  const res = await fetch('../api/login', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'same-origin',
  });

  const json = await res.json();

  if (res.status >= 400 && res.status < 500) {
    errorElement.innerText = json.error;
    errorElement.classList.remove('display-none');
    return;
  }

  if (res.status !== 200 || !json) {
    errorElement.innerText = 'Looks like an error occurred.';
    errorElement.classList.remove('display-none');
    return;
  }

  if (json.auth && json.token) {
    localStorage.setItem('jwt', json.token);
    window.location.href = '../flag';
  }
}

if (localStorage.getItem('jwt')) {
  window.location.replace('../flag');
}

const form = document.getElementById('form-login');
form.addEventListener('submit', submitLogin);
