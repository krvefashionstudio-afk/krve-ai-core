<script>
window.onload = function () {

  const btn = document.getElementById("scanBtn");

  if(!btn){
    console.log("Button not found");
    return;
  }

  btn.addEventListener("click", async function () {

    const file = document.getElementById('file').files[0];
    const height = document.getElementById('height').value;

    if(!file){
      alert("Upload image first");
      return;
    }

    btn.innerText = "PROCESSING...";
    btn.disabled = true;

    let formData = new FormData();
    formData.append('file', file);
    formData.append('height', height);

    try {

      const res = await fetch('https://krve-ai-core.onrender.com/upload', {
        method: 'POST',
        body: formData
      });

      const data = await res.json();

      document.getElementById('viewer').innerHTML =
        `<model-viewer src="${data.modelUrl}"
          camera-controls auto-rotate
          style="width:100%; height:700px; background:#000;">
        </model-viewer>`;

      document.getElementById('metrics').innerHTML =
        `<h3>AI METRICS</h3>
         <p>Chest: ${data.chest}</p>
         <p>Waist: ${data.waist}</p>
         <p>Hip: ${data.hip}</p>
         <p><b>${data.size}</b></p>`;

      btn.innerText = "3D MODEL READY ✔️";
      btn.disabled = false;

    } catch (e) {
      console.log(e);
      alert("Server error");
      btn.innerText = "TRY AGAIN";
      btn.disabled = false;
    }

  });

};
</script>