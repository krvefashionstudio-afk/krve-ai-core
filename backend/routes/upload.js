const express = require("express");
const multer = require("multer");

const router = express.Router();

const storage = multer.diskStorage({
    destination: "uploads/",
    filename: (req, file, cb) => {
        cb(null, Date.now() + "-" + file.originalname);
    }
});

const upload = multer({ storage });
router.get("/", (req, res) => {
    res.json({
        success: true,
        message: "Upload API Working ✅"
    });
});
router.post("/", upload.single("photo"), (req, res) => {

    if (!req.file) {
        return res.status(400).json({
            success: false,
            message: "No image uploaded"
        });
    }

    res.json({
        success: true,
        image: req.file.filename
    });

});

module.exports = router;