const express = require("express");
const cors = require("cors");
require("dotenv").config();
const uploadRoute = require("./routes/upload");
const app = express();

app.use(cors());
app.use(express.json());
app.use("/upload", uploadRoute);

app.get("/", (req, res) => {
    res.json({
        success: true,
        message: "KRVE AI Core Backend Running 🚀"
    });
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});