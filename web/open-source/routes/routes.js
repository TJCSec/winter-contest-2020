const express = require('express');
const jwt = require('jsonwebtoken');

const router = express.Router();

require('dotenv').config();

const SECRET = process.env.SECRET_KEY;
const { FLAG } = process.env;

function verifyToken(token) {
  return jwt.verify(token, SECRET);
}

function generateToken(username) {
  return jwt.sign({
    username,
  }, SECRET, { expiresIn: '2h' });
}

router.post('/login', (req, res) => {
  const { username } = req.body;
  const { password } = req.body;

  if (!username || typeof username !== 'string') return res.status(401).send({ error: 'Please provide a username.', auth: false });
  if (!password || typeof password !== 'string') return res.status(401).send({ error: 'Please provide a password.', auth: false });

  if (username === 'admin') return res.status(401).send({ error: 'Invalid Credentials.', autH: false });

  const token = generateToken(username);
  return res.status(200).send({ token, auth: true });
});

router.get('/flag', (req, res) => {
  const token = req.headers.authorization;

  try {
    const decoded = verifyToken(token);
    if (decoded.username === 'admin') return res.status(200).send({ flag: FLAG });
    return res.status(200).send({ flag: 'No flag for you :)' });
  } catch (err) {
    return res.status(401).send({ error: 'Invalid JWT Token.' });
  }
});

module.exports = router;
