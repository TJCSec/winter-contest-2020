const hash = async (text) => {
    const data = new TextEncoder().encode(text);
    const hash = [...new Uint8Array(await crypto.subtle.digest('SHA-256', data))]
        .map(b => b.toString (16).padStart (2, "0"))
        .join('');
    return hash;
}

(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });
    const output = document.getElementById('output');
    const query = document.getElementById('query');
    const form = document.querySelector('form');
    form.addEventListener('submit', async e => {
        e.preventDefault();
        const data = {};
        await Promise.all(Array.from(new FormData(e.target)).map(async ([k, v]) => {
            data[k] = await hash(v)
        }))
        const result = await (await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })).json();
        query.textContent = `Query: ${result.query}`;
        output.textContent = result.success ? `Flag: ${result.flag}` : `Error: ${result.error}`;
    })
})()