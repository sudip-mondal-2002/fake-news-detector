const express = require('express');
const app = express();
const http = require('http').Server(app);
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.set('view engine', 'ejs');

app.get("/", (req, res) => {
    res.render("index", {
        Result:"",
        color: "white",
    });
})
app.post("/", (req, res) => {
    res.render("index", {
        Result:"This is a fake news",
        color: "red"
    });
})
app.get("/teams", (req,res)=>{
    res.render("teams");
})
http.listen(PORT, () => {
    console.log(`listening on ${PORT}`);
});