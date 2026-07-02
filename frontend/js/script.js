window.onload = function () {

    const btn = document.getElementById("scanBtn");

    btn.addEventListener("click", async function () {

        const fileInput = document.getElementById("file");
        const height = document.getElementById("height").value;

        if (fileInput.files.length === 0) {
            alert("Please upload your photo.");
            return;
        }

        btn.disabled = true;
        btn.innerHTML = "KRVE AI SCANNING...";

        document.getElementById("viewer").innerHTML = `
            <div style="
                width:100%;
                height:720px;
                display:flex;
                justify-content:center;
                align-items:center;
                color:#d4af37;
                font-size:22px;
                font-weight:bold;
            ">
                AI Cloud Processing...
            </div>
        `;

        const formData = new FormData();
        formData.append("photo", fileInput.files[0]);
        formData.append("height", height);

        try {

            const response = await fetch("https://krve-ai-core.onrender.com/upload", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("Server Error");
            }

            const data = await response.json();

            document.getElementById("viewer").innerHTML = `
                <model-viewer
                    src="${data.modelUrl}"
                    camera-controls
                    auto-rotate
                    shadow-intensity="1"
                    exposure="1"
                    environment-image="neutral"
                    style="
                        width:100%;
                        height:720px;
                        background:#000;
                    ">
                </model-viewer>
            `;

            document.getElementById("metrics").innerHTML = `
                <h3 style="color:#d4af37;">AI RECONSTRUCTED METRICS</h3>

                <p>Chest : <b>${data.chest}</b></p>

                <p>Waist : <b>${data.waist}</b></p>

                <p>Hip : <b>${data.hip}</b></p>

                <hr>

                <h2 style="color:#00ff99;">
                    ${data.size}
                </h2>
            `;

            btn.innerHTML = "3D HUMAN DIGITAL TWIN READY";
            btn.disabled = false;

        }

        catch (error) {

            console.error(error);

            alert("Server Error");

            btn.innerHTML = "TRY AGAIN";

            btn.disabled = false;

        }

    });

};