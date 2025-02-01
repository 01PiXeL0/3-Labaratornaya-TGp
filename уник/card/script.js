document.addEventListener("DOMContentLoaded", function() {
    const regions = document.querySelectorAll(".region");

    regions.forEach(region => {
        region.addEventListener("mouseover", function(e) {
            const regionName = e.target.dataset.name;
            const regionInfo = getRegionInfo(regionName);
            displayInfo(regionInfo, e.clientX, e.clientY);
        });

        region.addEventListener("mouseout", function() {
            hideInfo();
        });
    });

    function getRegionInfo(regionName) {
        // Здесь можно реализовать логику получения информации о регионе
        // Например, можно использовать объект или базу данных для хранения данных о регионах
        // Вернуть объект с информацией о регионе
    }

    function displayInfo(info, x, y) {
        const infoBox = document.getElementById("info-box");
        infoBox.innerHTML = ""; // Очищаем содержимое infoBox

        for (let key in info) {
            const p = document.createElement("p");
            p.textContent = `${key}: ${info[key]}`;
            infoBox.appendChild(p);
        }

        infoBox.style.display = "block";
        infoBox.style.top = `${y}px`;
        infoBox.style.left = `${x}px`;
    }

    function hideInfo() {
        const infoBox = document.getElementById("info-box");
        infoBox.style.display = "none";
    }
});
