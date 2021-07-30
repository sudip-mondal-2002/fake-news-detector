const express = require('express');
const spawn = require("child_process").spawn;
const app = express();
const http = require('http').Server(app);
const PORT = process.env.PORT || 3000;

app.use(express.static(__dirname+'/public'));
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

app.get("/", (req, res) => {
    res.render("index", {
        Result: "Your results will appear here",
    });
})
app.post("/", (req, res) => {
    const process = spawn("py", ["./detector.py", (req.body.title+" "+req.body.description)]);
    process.stdout.on('data', (data) => {
        res.render("index", {
            Result: (data.toString()),
        });
    });
})
app.get("/teams", (req, res) => {
    res.render("teams");
})
http.listen(PORT, () => {
    console.log(`listening on ${PORT}`);
});