// Taken from https://www.html5rocks.com/en/tutorials/file/dndfiles/

function handleFileSelect(e){
    e.stopPropagation();
    e.preventDefault();

    var files = e.dataTransfer.files; // FileList object

    // `files` is a FileList of File objects. List some properties
    var output = [];

    // Loop through the FileList
    for(var c = 0, f; f = files[c]; c++){

        // Make sure we're dealing with image files
        if(!f.type.match('image.*')){ continue; }

        var reader = new FileReader();

        reader.onload = (function(theFile){
            return function(e){
                var container = document.createElement('div');
                var body = document.createElement('div');
                var img = document.createElement('img');
                var title = document.createElement('h5');
                var text = document.createElement('span');

                // Bootstrap
                container.classList.add("text-center");
                container.classList.add("card");
                body.classList.add("card-body");
                img.classList.add("img-fluid");
                img.classList.add("img-rounded");
                img.classList.add("card-img-top");
                title.classList.add("card-title");
                text.classList.add("card-text");

                container.classList.add("container");
                img.setAttribute("src", e.target.result);

                fileName = escape(theFile.name);
                fileType = theFile.type || 'n/a';
                fileSize = theFile.size + " bytes";
                fileModifiedDate = theFile.lastModifiedDate ? theFile.lastModifiedDate.toLocaleDateString() : 'n/a';

                title.innerHTML = fileName;
                text.innerHTML = "Type: " + fileType + "<br/>Size: " + fileSize + "<br/>Modified Date: " + fileModifiedDate;

                body.appendChild(title);
                body.appendChild(text);
                container.appendChild(img);
                container.appendChild(body);

                // Append to beginning of list
                list = document.getElementById('list'); 
                list.insertBefore(container, list.childNodes[0] || null);
            }
        })(f);
        
        // Read in the image file as data URL.
        reader.readAsDataURL(f);
    }
}

function handleDragOver(e){
    e.stopPropagation();
    e.preventDefault();
    // Explicitly show this is a copy
    e.dataTransfer.dropEffect = 'copy';
}

// Setup event listeners
var dropZone = document.getElementById('drop_zone');
dropZone.addEventListener('dragover', handleDragOver, false);
dropZone.addEventListener('drop', handleFileSelect, false);
