function enlargeImg(e) {
    console.log("retard");
    var imgSRC = e.src;
    document.getElementById("largeimg").src = imgSRC;
    document.getElementById("largeimg").style.zIndex = "999";
    document.getElementById("large").style.zIndex = "900";
    document.getElementById("largeimg").style.display = "block";
}