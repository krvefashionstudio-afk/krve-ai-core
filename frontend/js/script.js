const uploadBtn = document.getElementById("uploadBtn");
const photo = document.getElementById("photo");
const result = document.getElementById("result");

uploadBtn.addEventListener("click", async () => {

    if (photo.files.length === 0) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", photo.files[0]);

    result.innerHTML = "<h2>Analyzing...</h2>";

    try {

        const response = await fetch("http://127.0.0.1:5000/api/pose", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        if (data.status === "success") {

            result.innerHTML = `

            <h2>✅ Pose Detected</h2>

            <h3>Measurements</h3>

            <p>Shoulder Width : ${data.measurements.shoulder_width.toFixed(3)}</p>

            <p>Hip Width : ${data.measurements.hip_width.toFixed(3)}</p>

            <p>Arm Length : ${data.measurements.arm_length.toFixed(3)}</p>

            <p>Leg Length : ${data.measurements.leg_length.toFixed(3)}</p>

            <hr>

            <h3>Body Analysis</h3>

            <p>Body Type : ${data.body_analysis.body_type}</p>

            <p>Ratio : ${data.body_analysis.shoulder_to_hip_ratio}</p>

            <hr>

            <h3>Height Estimation</h3>

            <p>Normalized Height : ${data.height.normalized_height}</p>

            <p>Confidence : ${data.height.confidence}</p>

            `;

        } else {

            result.innerHTML = "<h2>" + data.message + "</h2>";

        }

    } catch (err) {

        console.log(err);

        result.innerHTML = "<h2>Server Error</h2>";

    }

});