document.getElementById("animate-btn").addEventListener("click", function() {
    let box = document.getElementById("animated-box");
    box.style.opacity = "1";
    box.style.transform = "translateY(50px)";
});

document.getElementById("disanimate-btn").addEventListener("click", function() {
    let box = document.getElementById("animated-box");
    box.style.opacity = "0";
    box.style.transform = "translateY(0px)";
});