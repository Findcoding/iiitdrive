

function validateSize(input) {
    const fileSize = input.files[0].size / 1024 / 1024;
    if (fileSize > 1) {
        alert('File size exceeds 1 MB');
        input.value = "";
        return;
    }
}



function clears(event) {

    var record = confirm("Do you want to clear form?");

    if(record == true) {
        $("#staticBackdrop").load(location.href + " #staticBackdrop>*", "");
        // $('#staticBackdrop').trigger("reset");

    } else {
        event.stopImmediatePropagation();
        event.preventDefault();
        return false;
    }

}



window.addEventListener("pageshow", function(event) {
    event.preventDefault();
    let historyTraversal = event.persisted || (typeof window.performance != "undefined" && window.performance.navigation.type === 2);
    if (historyTraversal) {
        window.location.reload();
    }
});


const date_url = "http://worldtimeapi.org/api/timezone/Asia/Kolkata";

async function refreshTime() {

    try {
        const response = await fetch(date_url);
        const data = await response.json();

        const dateTimeInParts = data.datetime.split("T");

        const t = new Date(dateTimeInParts);
        // console.log(t);
        // const date = dateTimeInParts[0];
        // const time = dateTimeInParts[1];

        var date = new Date(dateTimeInParts);
        // console.log(date);
        var hour = date.toLocaleString("default", { hour: "2-digit" });
        const myArray = hour.split(" ");
        var minute = date.toLocaleString("default", { minute: "2-digit" });
        var second = date.toLocaleString("default", { second: "2-digit" });

        let min = minute < 10 ? '0'+minute : minute
        let sec = second < 10 ? '0'+second : second

        document.getElementById("hour").textContent = myArray[0] + ":";
        document.getElementById("min").textContent = min + ":";
        document.getElementById("sec").textContent = sec + " ";
        document.getElementById("zone").textContent = myArray[1];

        var datetime = date.toDateString();
        const arr = datetime.split(" ");
        document.getElementById("date").textContent = arr[0] + ", " + arr[2] + " " + arr[1] + " " + arr[3];


    } catch (err) {
        alert("Something went wrong!! Please reload this page...");
        location.reload();
    }

}
    
setInterval(refreshTime, 1000);

