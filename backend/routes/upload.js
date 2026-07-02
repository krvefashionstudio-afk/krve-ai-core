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

// Test Route
router.get("/", (req, res) => {
    res.json({
        success: true,
        message: "KRVE Upload API Running ✅"
    });
});

// Upload Route
router.post("/", upload.single("photo"), (req, res) => {

    if (!req.file) {
        return res.status(400).json({
            success: false,
            message: "Please upload an image."
        });
    }

    // Temporary AI Response
    res.json({

        success: true,

        image: req.file.filename,

        modelUrl:
        "https://modelviewer.dev/shared-assets/models/Astronaut.glb",

        chest: "38.5 IN",

        waist: "31.5 IN",

        hip: "40.2 IN",

        size: "KRVE MATCH M"

    });

});

module.exports = router;