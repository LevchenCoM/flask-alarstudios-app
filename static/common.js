function getData() {

    fetch("/data", {
        method: 'GET',
    }).then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            let root = document.getElementById("root");
            root.innerText = "No data"
        }
    }).then(function (data) {
        let root = document.getElementById("root");

            data.forEach(function (item) {
                let elem = document.createElement("p");
                elem.innerText = `ID: ${item.id}, Name: ${item.name}`;
                root.appendChild(elem);
            })

    });
}

document.addEventListener('DOMContentLoaded', function () {
    getData();
});