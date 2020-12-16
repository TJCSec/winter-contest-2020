// THIS JS FILE HAS NOTHING TO DO WITH CHALLENGE, MOVE ON
let openSourceInfo = [
    {
        title: "Linux",
        items: [
            {
                title: "Ubuntu",
                href: "https://ubuntu.com",
                img: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Ubuntu_20.10_Groovy_Gorilla_Desktop.png/1200px-Ubuntu_20.10_Groovy_Gorilla_Desktop.png"
            },
            {
                title: "Arch",
                href: "https://www.archlinux.org/",
                img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZyW8ghe2O_tuIXcKh4UUATuvsGcKR-Inqbg&usqp=CAU"
            },
            {
                title: "Fedora",
                href: "https://getfedora.org/",
                img: "https://fedoramagazine.org/wp-content/uploads/2018/04/Screenshot_fedora1_2018-10-10_115154.png"
            },
        ]
    },
    {
        title: "Web",
        items: [
            {
                title: "React",
                href: "https://reactjs.org/",
                img: "https://images.unsplash.com/photo-1593720219276-0b1eacd0aef4?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1343&q=80"
            },
            {
                title: "VueJS",
                href: "https://vuejs.org/",
                img: "https://images.unsplash.com/photo-1607435655201-1c8db5afc449?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"
            },
            {
                title: "Next.js",
                href: "https://nextjs.org/",
                img: "https://images.pexels.com/photos/952670/pexels-photo-952670.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
            },
        ]
    },
]


// there are good ways to do things, and bad ways to do things. this is a bad way, and do not write anything like this.
// this is purely for the sake of writing things quick
function getImageDiv(title, href, img) {
    return `
        <div onclick="window.location.href='${href}'" class="cursor-pointer w-64 h-64 rounded-xl overflow-hidden bg-cover bg-center text-center flex items-center mr-4 mb-4" style="background-image: url(${img})">
            <div class="font-extrabold text-4xl text-white m-auto">
                ${title}
            </div>
        </div>`;
}

function getSectionDiv(items, title) {
    return `
        <div class="font-bold text-xl">
            ${title}
        </div>
        <div class="w-full mt-4 mb-8 flex flex-wrap">
            ${items}
        </div>`;
}


let openSourceDiv = document.getElementById("opensourceitems");

openSourceInfo.forEach(obj => {
    let innerDiv = obj.items.map(item => getImageDiv(item.title, item.href, item.img)).join("");
    openSourceDiv.innerHTML += getSectionDiv(innerDiv, obj.title);
});