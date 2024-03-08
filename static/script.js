const body = document.querySelector('body')
const statusBox = document.querySelector('#status-box');
const historyBox = document.querySelector('#history-box');
const topButton = document.querySelector("#top-btn");
let loaded = false;
let toggle = true;
let boxes;
let titles;
let links;
let details;


window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        topButton.style.display = "block";
    } else {
        topButton.style.display = "none";
    }
}


function goTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
};


$('body').on('click', '#status', function(e){
    e.preventDefault();
    if (!toggle) {
        toggle = true;
        statusBox.style.display = 'flex';
        statusBox.style.flexDirection = 'column';
        historyBox.style.display = 'none';
    };
});


$('body').on('click', '#history', function(e){
    e.preventDefault();
    if (toggle) {
        toggle = false;
        statusBox.style.display = 'none';
        historyBox.style.display = 'flex';
        
        // Get history if it's not loaded yet
        if (!loaded){
            $.ajax({
                url: "history",
                type: "GET",
                success: function (res) {
                    loaded = true;
                    
                    // Load title box and then the rest
                    titles = document.createElement('div');
                    titles.setAttribute('class', 'status');
                    titles.textContent = 'History of Last 5 Drops';

                    boxes = document.createElement('div');
                    boxes.setAttribute('class', 'box-small');
                    boxes.appendChild(titles);

                    historyBox.appendChild(boxes)

                    for (const drop of res.drops) {
                        titles = document.createElement('div');
                        titles.setAttribute('class', 'article');

                        links = document.createElement('a')
                        links.setAttribute('href', drop.link);
                        links.textContent = drop.title;
                        titles.appendChild(links);

                        details = document.createElement('div');
                        details.setAttribute('class', 'details');
                        details.textContent = 'From ' + drop.start_date.slice(0,10) + ' to ' + drop.end_date.slice(0,10);
                        
                        boxes = document.createElement('div');
                        boxes.setAttribute('class', 'box');
                        boxes.appendChild(titles);
                        boxes.appendChild(details);

                        historyBox.appendChild(boxes);
                    };
                },
                error: function(res){
                    alert("An error occured.")
                },
                timeout: 15000
            });
        };
    };
});