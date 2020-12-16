(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });
    const output = document.getElementById('output');
    const query = document.getElementById('query');
    const form = document.querySelector('form');
    form.addEventListener('submit', async e => {
        e.preventDefault();
        const result = await (await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(Object.fromEntries(new FormData(e.target)))
        })).json();
        query.textContent = `Query: ${result.query}`;
        output.textContent = result.success ? `Flag: ${result.flag}` : `Error: ${result.error}`;
    })
})()
