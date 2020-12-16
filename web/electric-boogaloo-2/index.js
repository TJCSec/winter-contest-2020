const crypto = require('crypto');
const express = require('express');
const app = express();
const ajv = new require('ajv')();
const db = require('better-sqlite3')('db.sqlite3')

// generate a password for the only existing account
const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
const result = [];
for (let i = 0; i < 32; i++) {
   result.push(characters.charAt(Math.floor(Math.random() * (characters.length + 1))));
}
const randomPassword = result.join('');

// init db
db.exec(`DROP TABLE IF EXISTS users;`);
db.exec(`CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
);`);

// hash username (ginkoid) and password for security
db.exec(`INSERT INTO users (username, password) VALUES (
    'b3c705faf18090db2014e82e7447684524ae83bbf46d328e85ccdbdfe5e76c52',
    '${crypto.createHash('sha256').update(randomPassword).digest('hex')}
')`);

// parse JSON
app.use(require('body-parser').json());

// serve static files
app.use(express.static('public'));

// use ajv to validate stuff posted to /login
const schema = {
    type: 'object',
    properties: {
        username: {type: 'string'},
        password: {type: 'string'}
    },
    required: ['username', 'password'],
    additionalProperties: false
};

const validate = ajv.compile(schema);

// handle login requests
app.post('/login', (req, res) => {
    // validate request
    if (!validate(req.body)) {
        res.json({
            success: false,
            error: 'There was a problem with your request.',
            query: '',
        });
        return;
    }
    const username = req.body.username;
    const password = req.body.password;

    // query database for user
    const query = `SELECT id FROM users WHERE username = '${username}' AND password = '${password}'`;

    let id = undefined;
    try {
        id = db.prepare(query).get()?.id;
    } catch {
        res.json({
            success: false,
            error: 'There was a problem with your query.',
            query
        });
        return;
    }

    if (id) {
        // user exists
        res.json({
            success: true,
            flag: process.env.FLAG,
            query
        });
        return;
    }
    // user does not exist
    res.json({
        success: false,
        error: 'Incorrect username or password.',
        query
    });
});

app.listen(3000);
