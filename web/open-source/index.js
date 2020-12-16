const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const routes = require('./routes/routes');

require('dotenv').config();

const app = express();

app.use(bodyParser.json({ extended: false }));
app.use('/api', routes);

app.use(express.static(path.join(__dirname, '/public')));
app.use('/.git', express.static(path.join(__dirname, '/git')));

app.listen(process.env.PORT || 3000, () => { console.log('Server Started!'); });
