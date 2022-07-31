const express = require('express')
const app = express()
const port = 3000
const path = require("path");

app.get('/algoritmo', (req, res) => {
  const { execSync } = require('child_process');
  const output = execSync('python C:\\Users\\Eric\\Desktop\\TrabalhoIA\\trab.py', { encoding: 'utf-8' });

  res.send(output)
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname+'/main.html'));
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})