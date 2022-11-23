function myFunction(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        x.previousElementSibling.className += " w3-theme-d1";
    } else {
        x.className = x.className.replace("w3-show", "");
        x.previousElementSibling.className =
            x.previousElementSibling.className.replace(" w3-theme-d1", "");
    }
}

// Used to toggle the menu on smaller screens when clicking on the menu button
function openNav() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}


function logout(event) {
    let val = confirm('Do you want to logout?');

    if (val == true) {
        return true;
    } else {
        event.stopImmediatePropagation();
        event.preventDefault();
        return false;
    }
}



function validateSize(input) {
    const fileSize = input.files[0].size / 1024 / 1024;
    if (fileSize > 1) {
        alert('File size exceeds 1 MB');
        input.value = "";
        return;
    }
}



function clears(event) {

    var record = confirm("Do you want to clear form??");

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



function refreshTime() {
    var date = new Date();
    var hour = date.toLocaleString("default", { hour: "2-digit" });
    const myArray = hour.split(" ");
    var minute = date.toLocaleString("default", { minute: "2-digit" });
    var second = date.toLocaleString("default", { second: "2-digit" });

    document.getElementById("hour").textContent = myArray[0] + ":";
    document.getElementById("min").textContent = minute + ":";
    document.getElementById("sec").textContent = second + " ";
    document.getElementById("zone").textContent = myArray[1];

    var datetime = date.toDateString();
    const arr = datetime.split(" ");
    document.getElementById("date").textContent = arr[0] + ", " + arr[2] + " " + arr[1] + " " + arr[3];

}
    
setInterval(refreshTime, 1000);
